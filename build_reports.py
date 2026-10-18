#!/usr/bin/env python3
"""Generate per-function Markdown and interactive CFGs from a PE/PDB inventory.

This creates a register-level, C-style interpretation. It does not claim to
recover the original kernel C source or unavailable type/signature metadata.
"""

from __future__ import annotations

import argparse
import bisect
import collections
import csv
import hashlib
import html
import json
import os
import re
import shutil
import struct
import sys
from pathlib import Path
from typing import Any


DEFAULT_EXE = Path(r"C:\Windows\System32\ntoskrnl.exe")
DEFAULT_OUT = Path(__file__).resolve().parent


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "section"


def function_label(record: dict[str, Any]) -> str:
    if record.get("name"):
        return str(record["name"])
    if record.get("export_names"):
        return str(record["export_names"][0])
    return f"sub_{int(record['rva']):08X}"


def report_filename(record: dict[str, Any]) -> str:
    """Create a readable, RVA-unique report filename from a known symbol."""
    rva = int(record["rva"])
    raw_name = record.get("name") or next(iter(record.get("export_names", [])), None)
    if not raw_name:
        prefix = "Unknown"
    else:
        prefix = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(raw_name)).strip(" .")
        prefix = prefix[:100].rstrip(" .") or "Unknown"
    return f"{prefix}_function_{rva:08X}.md"


def safe_c_name(name: str, rva: int) -> str:
    normalized = re.sub(r"[^A-Za-z0-9_]", "_", name)
    if not normalized or normalized[0].isdigit():
        normalized = "kernel_fn_" + normalized
    return (normalized[:100] or f"kernel_fn_{rva:08X}")


class PEImage:
    def __init__(self, path: Path):
        self.path = path
        self.data = path.read_bytes()
        if self.data[:2] != b"MZ":
            raise ValueError(f"Not a PE image: {path}")
        peoff = struct.unpack_from("<I", self.data, 0x3C)[0]
        if self.data[peoff:peoff + 4] != b"PE\0\0":
            raise ValueError("Missing PE signature")
        coff = peoff + 4
        self.machine, nsections, _, _, _, opt_size, _ = struct.unpack_from(
            "<HHIIIHH", self.data, coff
        )
        opt = coff + 20
        magic = struct.unpack_from("<H", self.data, opt)[0]
        if magic != 0x20B or self.machine != 0x8664:
            raise ValueError("This report builder currently expects an x64 PE image")
        self.image_base = struct.unpack_from("<Q", self.data, opt + 24)[0]
        self.size_of_image = struct.unpack_from("<I", self.data, opt + 56)[0]
        self.number_dirs = struct.unpack_from("<I", self.data, opt + 108)[0]
        self.directories = opt + 112
        section_table = opt + opt_size
        self.sections: list[dict[str, Any]] = []
        for i in range(nsections):
            off = section_table + 40 * i
            name = self.data[off:off + 8].split(b"\0", 1)[0].decode("ascii", "replace")
            vsize, va, raw_size, raw_ptr = struct.unpack_from("<IIII", self.data, off + 8)
            characteristics = struct.unpack_from("<I", self.data, off + 36)[0]
            self.sections.append({
                "name": name, "va": va, "vsize": vsize, "raw_size": raw_size,
                "raw_ptr": raw_ptr, "extent": max(vsize, raw_size),
                "executable": bool(characteristics & 0x20000000),
            })

    def section_for_rva(self, rva: int) -> dict[str, Any] | None:
        for section in self.sections:
            if section["va"] <= rva < section["va"] + section["extent"]:
                return section
        return None

    def rva_to_offset(self, rva: int) -> int:
        for section in self.sections:
            if section["va"] <= rva < section["va"] + section["extent"]:
                delta = rva - section["va"]
                if delta >= section["raw_size"]:
                    raise ValueError(f"RVA 0x{rva:08X} has no raw bytes")
                return section["raw_ptr"] + delta
        if 0 <= rva < len(self.data):
            return rva
        raise ValueError(f"RVA 0x{rva:08X} is outside the image")

    def bytes_at_rva(self, rva: int, size: int) -> bytes:
        off = self.rva_to_offset(rva)
        if size < 0 or off + size > len(self.data):
            raise ValueError(f"Function range at 0x{rva:08X} exceeds file bytes")
        return self.data[off:off + size]

    def c_string(self, rva: int) -> str:
        off = self.rva_to_offset(rva)
        end = self.data.find(b"\0", off, min(len(self.data), off + 65536))
        if end < 0:
            end = min(len(self.data), off + 65536)
        return self.data[off:end].decode("ascii", "replace")

    def imports(self) -> dict[int, dict[str, str]]:
        if self.number_dirs < 2:
            return {}
        rva, size = struct.unpack_from("<II", self.data, self.directories + 8)
        if not rva or not size:
            return {}
        offset = self.rva_to_offset(rva)
        result: dict[int, dict[str, str]] = {}
        max_descriptors = min(size // 20 + 1, 65536)
        for i in range(max_descriptors):
            pos = offset + i * 20
            if pos + 20 > len(self.data):
                break
            original, timestamp, forwarder, name_rva, first_thunk = struct.unpack_from(
                "<IIIII", self.data, pos
            )
            if not any((original, timestamp, forwarder, name_rva, first_thunk)):
                break
            dll = self.c_string(name_rva)
            lookup_rva = original or first_thunk
            for index in range(1_000_000):
                thunk_rva = lookup_rva + index * 8
                thunk_off = self.rva_to_offset(thunk_rva)
                value = struct.unpack_from("<Q", self.data, thunk_off)[0]
                if not value:
                    break
                iat_rva = first_thunk + index * 8
                if value & (1 << 63):
                    symbol = f"ordinal_{value & 0xFFFF}"
                else:
                    hint_name_rva = value & 0x7FFFFFFFFFFFFFFF
                    symbol = self.c_string(hint_name_rva + 2)
                result[iat_rva] = {"dll": dll, "name": symbol}
        return result


def capstone_api():
    try:
        import capstone
        from capstone import x86_const
    except ImportError as exc:
        raise RuntimeError("Capstone is required. Install with: python -m pip install capstone") from exc
    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
    md.detail = True
    md.skipdata = True
    md.syntax = capstone.CS_OPT_SYNTAX_INTEL
    return capstone, x86_const, md


def operand_imm(insn: Any, x86: Any) -> int | None:
    if insn.id == 0:
        return None
    if insn.operands and insn.operands[0].type == x86.X86_OP_IMM:
        return int(insn.operands[0].imm)
    return None


def instruction_groups(insn: Any, capstone: Any) -> tuple[bool, bool, bool]:
    if insn.id == 0:
        return False, False, False
    return (
        insn.group(capstone.CS_GRP_CALL),
        insn.group(capstone.CS_GRP_JUMP),
        insn.group(capstone.CS_GRP_RET),
    )


def rip_target_rva(insn: Any, image_base: int, x86: Any) -> int | None:
    if insn.id == 0:
        return None
    for operand in insn.operands:
        if operand.type == x86.X86_OP_MEM and operand.mem.base == x86.X86_REG_RIP:
            return insn.address + insn.size + int(operand.mem.disp) - image_base
    return None


def resolve_code_target(
    target_rva: int | None,
    starts: dict[int, dict[str, Any]],
    sorted_starts: list[int],
    symbols_by_rva: dict[int, list[str]],
    pe: PEImage,
) -> dict[str, Any]:
    if target_rva is None:
        return {"kind": "indirect", "display": "indirect target", "function_rva": None, "section": None}
    if target_rva in starts:
        record = starts[target_rva]
        return {
            "kind": "function", "display": function_label(record),
            "function_rva": target_rva, "section": record.get("section"),
        }
    index = bisect.bisect_right(sorted_starts, target_rva) - 1
    if index >= 0:
        owner = starts[sorted_starts[index]]
        if target_rva < int(owner["end_rva"]):
            return {
                "kind": "inside-function", "display": f"{function_label(owner)} + 0x{target_rva - int(owner['rva']):X}",
                "function_rva": int(owner["rva"]), "section": owner.get("section"),
            }
    names = symbols_by_rva.get(target_rva, [])
    section = pe.section_for_rva(target_rva)
    return {
        "kind": "code-address" if section and section["executable"] else "external-address",
        "display": names[0] if names else f"0x{target_rva:08X}",
        "function_rva": None,
        "section": section["name"] if section else None,
    }


def build_blocks(instructions: list[Any], start: int, end: int, capstone: Any,
                 x86: Any, image_base: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if not instructions:
        return [], []
    by_addr = {insn.address - image_base: i for i, insn in enumerate(instructions)}
    leaders = {int(instructions[0].address - image_base)}
    for index, insn in enumerate(instructions):
        _, is_jump, is_ret = instruction_groups(insn, capstone)
        target = operand_imm(insn, x86) if is_jump else None
        if target is not None:
            target_rva = target - image_base
            if start <= target_rva < end and target_rva in by_addr:
                leaders.add(target_rva)
        if (is_jump or is_ret) and index + 1 < len(instructions):
            next_rva = int(instructions[index + 1].address - image_base)
            if start <= next_rva < end:
                leaders.add(next_rva)

    leader_list = sorted(leaders)
    blocks: list[dict[str, Any]] = []
    insn_block: dict[int, int] = {}
    for i, leader in enumerate(leader_list):
        first_index = by_addr.get(leader)
        if first_index is None:
            continue
        limit = leader_list[i + 1] if i + 1 < len(leader_list) else end
        items = [x for x in instructions[first_index:] if leader <= x.address - image_base < limit]
        if not items:
            continue
        block_id = f"bb_{leader:08X}"
        block = {
            "id": block_id, "rva": leader,
            "end_rva": int(items[-1].address + items[-1].size - image_base),
            "instructions": items,
        }
        blocks.append(block)
        for insn in items:
            insn_block[int(insn.address - image_base)] = leader

    block_by_rva = {int(block["rva"]): block for block in blocks}
    edges: list[dict[str, Any]] = []
    for i, block in enumerate(blocks):
        insn = block["instructions"][-1]
        is_call, is_jump, is_ret = instruction_groups(insn, capstone)
        del is_call
        from_id = block["id"]
        next_block = blocks[i + 1] if i + 1 < len(blocks) else None
        target = operand_imm(insn, x86) if is_jump else None
        target_rva = target - image_base if target is not None else None
        is_unconditional = insn.mnemonic.lower() in {"jmp", "ljmp"}
        if is_jump:
            if target_rva in block_by_rva:
                edges.append({"source": from_id, "target": block_by_rva[target_rva]["id"], "kind": "branch"})
            elif target_rva is not None:
                edges.append({"source": from_id, "target": f"outside_{target_rva:08X}", "kind": "branch-out", "target_rva": target_rva})
            else:
                edges.append({"source": from_id, "target": f"indirect_jump_{int(insn.address - image_base):08X}", "kind": "indirect"})
            if not is_unconditional and next_block is not None:
                edges.append({"source": from_id, "target": next_block["id"], "kind": "fallthrough"})
        elif not is_ret and next_block is not None:
            edges.append({"source": from_id, "target": next_block["id"], "kind": "flow"})
    return blocks, edges


CONDITIONS = {
    "a": "CF == 0 && ZF == 0", "ae": "CF == 0", "b": "CF == 1", "be": "CF == 1 || ZF == 1",
    "c": "CF == 1", "e": "ZF == 1", "z": "ZF == 1", "g": "ZF == 0 && SF == OF",
    "ge": "SF == OF", "l": "SF != OF", "le": "ZF == 1 || SF != OF", "na": "CF == 1 || ZF == 1",
    "nae": "CF == 1", "nb": "CF == 0", "nbe": "CF == 0 && ZF == 0", "nc": "CF == 0",
    "ne": "ZF == 0", "ng": "ZF == 1 || SF != OF", "nge": "SF != OF", "nl": "SF == OF",
    "nle": "ZF == 0 && SF == OF", "no": "OF == 0", "np": "PF == 0", "ns": "SF == 0",
    "nz": "ZF == 0", "o": "OF == 1", "p": "PF == 1", "pe": "PF == 1", "po": "PF == 0",
    "s": "SF == 1",
}


def jump_condition(mnemonic: str) -> str:
    name = mnemonic.lower()
    for prefix in ("j", "cmov", "set"):
        if name.startswith(prefix):
            suffix = name[len(prefix):]
            if suffix in CONDITIONS:
                return CONDITIONS[suffix]
    if name in {"jcxz", "jecxz"}:
        return "ECX == 0"
    if name == "jrcxz":
        return "RCX == 0"
    if name.startswith("loop"):
        return "RCX decremented and nonzero"
    return "condition flags indicate true"


def c_operand_text(text: str) -> str:
    return text.replace(" qword ptr ", " ").replace(" dword ptr ", " ").replace(
        " word ptr ", " ").replace(" byte ptr ", " ").replace(" xmmword ptr ", " ")


def memory_info(text: str) -> tuple[int, str] | None:
    width = {"byte": 8, "word": 16, "dword": 32, "qword": 64,
             "xmmword": 128, "ymmword": 256, "zmmword": 512}
    width_match = re.search(r"\b(byte|word|dword|qword|xmmword|ymmword|zmmword)\s+ptr\b", text)
    bits = width.get(width_match.group(1).lower(), 0) if width_match else 0
    segment_match = re.search(r"\b(cs|ds|es|fs|gs|ss):\s*\[([^\]]+)\]", text, re.I)
    if segment_match:
        segment = segment_match.group(1).upper()
        address = f"{segment}_BASE + {segment_match.group(2)}"
    else:
        match = re.search(r"\[([^\]]+)\]", text)
        if not match:
            return None
        address = match.group(1)
    return bits, address


def c_value(text: str) -> str:
    """Render a register/immediate or a width-explicit memory read."""
    memory = memory_info(text)
    if memory is None:
        return c_operand_text(text).strip()
    bits, address = memory
    return f"LOAD{bits}({address})" if bits else f"LOAD({address})"


def c_write(destination: str, value: str) -> str:
    """Render a register assignment or a width-explicit memory write."""
    memory = memory_info(destination)
    if memory is None:
        return f"{c_operand_text(destination).strip()} = {value};"
    bits, address = memory
    op = f"STORE{bits}" if bits else "STORE"
    return f"{op}({address}, {value});"


def pseudo_for_instruction(insn: Any, call_info: dict[str, Any] | None, image_base: int,
                           start: int, end: int) -> str:
    mnemonic = insn.mnemonic.lower()
    op = c_operand_text(insn.op_str)
    # Keep the original width qualifier for LOADn/STOREn in C pseudocode.
    operands = [x.strip() for x in insn.op_str.split(",")] if insn.op_str else []
    location = int(insn.address - image_base)
    if insn.id == 0 or mnemonic == ".byte":
        return f"/* undecoded bytes: {insn.bytes.hex(' ')} */"
    if mnemonic in {"nop", "endbr64", "int3"}:
        return f"/* {mnemonic} {op} */".rstrip()
    if mnemonic == "mov" and len(operands) == 2:
        return c_write(operands[0], c_value(operands[1]))
    if mnemonic.startswith("movzx") and len(operands) == 2:
        return c_write(operands[0], f"zero_extend({c_value(operands[1])})")
    if mnemonic.startswith("movsx") or mnemonic.startswith("movsxd"):
        if len(operands) == 2:
            return c_write(operands[0], f"sign_extend({c_value(operands[1])})")
    if mnemonic == "lea" and len(operands) == 2:
        # LEA computes the bracketed effective-address arithmetic; it does not
        # read memory and does not take a source-language address-of expression.
        return c_write(operands[0], operands[1].strip("[]"))
    if mnemonic in {"add", "sub", "and", "or", "xor", "imul", "shl", "sal", "shr", "sar", "rol", "ror"}:
        if len(operands) == 2:
            opmap = {"add": "+", "sub": "-", "and": "&", "or": "|", "xor": "^",
                     "imul": "*", "shl": "<<", "sal": "<<", "shr": ">>",
                     "sar": "arithmetic_shift_right", "rol": "rotate_left", "ror": "rotate_right"}
            operator = opmap.get(mnemonic, mnemonic)
            old = c_value(operands[0])
            rhs = c_value(operands[1])
            return c_write(operands[0], f"({old}) {operator} ({rhs})")
        if mnemonic == "imul" and len(operands) == 3:
            return c_write(operands[0], f"({c_value(operands[1])}) * ({c_value(operands[2])})")
    if mnemonic in {"inc", "dec", "neg", "not"} and operands:
        old = c_value(operands[0])
        if mnemonic == "inc":
            return c_write(operands[0], f"({old}) + 1")
        if mnemonic == "dec":
            return c_write(operands[0], f"({old}) - 1")
        opmap = {"neg": "negate", "not": "bitwise_not"}
        return c_write(operands[0], f"{opmap[mnemonic]}({old})")
    if mnemonic in {"cmp", "test"} and len(operands) == 2:
        if mnemonic == "cmp":
            return f"FLAGS = compare({c_value(operands[0])}, {c_value(operands[1])});"
        return f"FLAGS = test_bits({c_value(operands[0])}, {c_value(operands[1])});"
    if mnemonic.startswith("cmov") and len(operands) == 2:
        return f"if ({jump_condition(mnemonic)}) {{ {c_write(operands[0], c_value(operands[1]))} }}"
    if mnemonic.startswith("set") and operands:
        return c_write(operands[0], f"({jump_condition(mnemonic)}) ? 1 : 0")
    if mnemonic == "push" and operands:
        return f"stack_push({c_value(operands[0])});"
    if mnemonic == "pop" and operands:
        return c_write(operands[0], "stack_pop()")
    if mnemonic == "leave":
        return "RSP = RBP; RBP = stack_pop();"
    if mnemonic in {"call", "callq"}:
        if call_info:
            return f"RAX = CALL({safe_c_name(str(call_info['display']), int(call_info.get('target_rva') or location))}); /* {call_info['display']} */"
        return f"RAX = CALL({op or 'indirect_target'});"
    if mnemonic in {"jmp", "ljmp"}:
        if operands:
            try:
                dest = int(operands[0], 0) - image_base
            except ValueError:
                dest = None
            if dest is not None and start <= dest < end:
                return f"goto loc_{dest:08X};"
            return f"TAIL_TRANSFER({operands[0]}); /* control leaves this function range */"
        return "TAIL_TRANSFER(indirect_target);"
    if mnemonic.startswith("j") and mnemonic not in {"jmp", "jmpl"}:
        target = None
        if operands:
            try:
                target = int(operands[0], 0) - image_base
            except ValueError:
                pass
        label = f"loc_{target:08X}" if target is not None and start <= target < end else (operands[0] if operands else "target")
        return f"if ({jump_condition(mnemonic)}) goto {label};"
    if mnemonic.startswith("loop") or mnemonic in {"jcxz", "jecxz", "jrcxz"}:
        target = None
        if operands:
            try:
                target = int(operands[0], 0) - image_base
            except ValueError:
                pass
        label = f"loc_{target:08X}" if target is not None and start <= target < end else (operands[0] if operands else "target")
        return f"if ({jump_condition(mnemonic)}) goto {label};"
    if mnemonic.startswith("ret"):
        return "return; /* RAX carries a return value when the ABI contract uses one */"
    if mnemonic in {"xchg", "xadd"} and len(operands) == 2:
        return f"exchange({operands[0]}, {operands[1]});"
    if mnemonic == "syscall":
        return "SYSCALL();"
    if mnemonic.startswith("int"):
        return f"INTERRUPT({op});"
    if mnemonic in {"bt", "bts", "btr", "btc"}:
        return f"bit_operation_{mnemonic}({op}); /* updates flags */"
    if mnemonic in {"mul", "div", "idiv", "imul"}:
        return f"arithmetic_{mnemonic}({op});"
    if mnemonic in {"cpuid", "rdtsc", "rdtscp", "pause", "lfence", "mfence", "sfence"}:
        return f"{mnemonic.upper()}({op});".rstrip("()") + ";"
    # Preserve every instruction that does not have a reliable generic mapping.
    return f"/* semantics not simplified: {mnemonic} {op} */".rstrip()


_REG_PARTS = {
    "rax": ("rax", 64), "eax": ("rax", 32), "ax": ("rax", 16), "al": ("rax", 8), "ah": ("rax", 8),
    "rbx": ("rbx", 64), "ebx": ("rbx", 32), "bx": ("rbx", 16), "bl": ("rbx", 8), "bh": ("rbx", 8),
    "rcx": ("rcx", 64), "ecx": ("rcx", 32), "cx": ("rcx", 16), "cl": ("rcx", 8), "ch": ("rcx", 8),
    "rdx": ("rdx", 64), "edx": ("rdx", 32), "dx": ("rdx", 16), "dl": ("rdx", 8), "dh": ("rdx", 8),
    "rsi": ("rsi", 64), "esi": ("rsi", 32), "si": ("rsi", 16), "sil": ("rsi", 8),
    "rdi": ("rdi", 64), "edi": ("rdi", 32), "di": ("rdi", 16), "dil": ("rdi", 8),
    "rbp": ("rbp", 64), "ebp": ("rbp", 32), "bp": ("rbp", 16), "bpl": ("rbp", 8),
    "rsp": ("rsp", 64), "esp": ("rsp", 32), "sp": ("rsp", 16), "spl": ("rsp", 8),
}
for _register_number in range(8, 16):
    _register_base = f"r{_register_number}"
    _REG_PARTS[_register_base] = (_register_base, 64)
    _REG_PARTS[f"{_register_base}d"] = (_register_base, 32)
    _REG_PARTS[f"{_register_base}w"] = (_register_base, 16)
    _REG_PARTS[f"{_register_base}b"] = (_register_base, 8)


def c_width_type(bits: int, signed: bool = False, beta: bool = False) -> str:
    if bits <= 8:
        return "unsigned __int8" if not signed else "__int8"
    if bits <= 16:
        return "unsigned __int16" if not signed else "__int16"
    if bits <= 32:
        return "unsigned int" if not signed or beta else "int"
    return "unsigned __int64" if beta else "__int64"


def _stack_model(instructions: list[Any], pe: PEImage, x86: Any) -> tuple[dict[tuple[int, int], int], dict[int, int]]:
    """Map stack operands to offsets from function-entry RSP, including common prologues."""
    operand_offsets: dict[tuple[int, int], int] = {}
    rsp_offset_at: dict[int, int] = {}
    rsp_offset = 0
    stack_registers: dict[str, int] = {"rsp": 0}
    for insn in instructions:
        if not insn.id:
            continue
        address = int(insn.address - pe.image_base)
        rsp_offset_at[address] = rsp_offset
        for index, operand in enumerate(insn.operands):
            if operand.type != x86.X86_OP_MEM:
                continue
            base = insn.reg_name(operand.mem.base).lower() if operand.mem.base else ""
            if base in stack_registers and not operand.mem.index:
                operand_offsets[(address, index)] = stack_registers[base] + int(operand.mem.disp)

        m = insn.mnemonic.lower()
        ops = insn.operands
        if m in {"push", "pushfq", "pushf"}:
            rsp_offset -= 8
            stack_registers["rsp"] = rsp_offset
        elif m in {"pop", "popfq", "popf"}:
            rsp_offset += 8
            stack_registers["rsp"] = rsp_offset
        elif m in {"sub", "add"} and len(ops) == 2 and ops[0].type == x86.X86_OP_REG:
            dest = insn.reg_name(ops[0].reg).lower()
            if dest in {"rsp", "esp"} and ops[1].type == x86.X86_OP_IMM:
                amount = int(ops[1].imm) * (-1 if m == "sub" else 1)
                rsp_offset += amount
                stack_registers["rsp"] = rsp_offset
        elif m == "mov" and len(ops) == 2 and ops[0].type == x86.X86_OP_REG and ops[1].type == x86.X86_OP_REG:
            dest = insn.reg_name(ops[0].reg).lower()
            source = insn.reg_name(ops[1].reg).lower()
            dest_base = _REG_PARTS.get(dest, (dest, 64))[0]
            source_base = _REG_PARTS.get(source, (source, 64))[0]
            if source_base in stack_registers and dest_base in {"rbp", "rsp"}:
                stack_registers[dest_base] = stack_registers[source_base]
                if dest_base == "rsp":
                    rsp_offset = stack_registers[dest_base]
        elif m == "lea" and len(ops) == 2 and ops[0].type == x86.X86_OP_REG and ops[1].type == x86.X86_OP_MEM:
            dest = _REG_PARTS.get(insn.reg_name(ops[0].reg).lower(), ("", 0))[0]
            base = insn.reg_name(ops[1].mem.base).lower() if ops[1].mem.base else ""
            source_base = _REG_PARTS.get(base, (base, 64))[0]
            if dest in {"rbp", "rsp"} and source_base in stack_registers and not ops[1].mem.index:
                stack_registers[dest] = stack_registers[source_base] + int(ops[1].mem.disp)
                if dest == "rsp":
                    rsp_offset = stack_registers[dest]
    return operand_offsets, rsp_offset_at


def _incoming_stack_argument_slots(blocks: list[dict[str, Any]], cfg_edges: list[dict[str, Any]],
                                   pe: PEImage, capstone: Any, x86: Any
                                   ) -> tuple[set[int], dict[tuple[int, int], int]]:
    """Resolve incoming x64 stack arguments without treating locals as parameters."""
    if not blocks:
        return set(), {}
    block_by_id = {str(block["id"]): block for block in blocks}
    successors: dict[str, list[str]] = collections.defaultdict(list)
    for edge in cfg_edges:
        source, target = str(edge.get("source", "")), str(edge.get("target", ""))
        if source in block_by_id and target in block_by_id:
            successors[source].append(target)

    def transfer(block: dict[str, Any], start: dict[str, int | None], collect: bool = False
                  ) -> tuple[dict[str, int | None], list[tuple[int, int, int]]]:
        state = dict(start)
        found: list[tuple[int, int, int]] = []
        for insn in block.get("instructions", []):
            if not insn.id:
                continue
            rva = int(insn.address - pe.image_base)
            ops = insn.operands
            if collect:
                for op_index, operand in enumerate(ops):
                    if operand.type != x86.X86_OP_MEM:
                        continue
                    base_name = insn.reg_name(operand.mem.base).lower() if operand.mem.base else ""
                    base = _REG_PARTS.get(base_name, (base_name, 64))[0]
                    base_offset = state.get(base)
                    if base_offset is None:
                        continue
                    effective = int(base_offset) + int(operand.mem.disp)
                    access = int(getattr(operand, "access", 0) or 0)
                    reads = bool(access & capstone.CS_AC_READ) if access else op_index > 0
                    if reads and effective >= 0x28 and (effective - 0x28) % 8 == 0:
                        found.append((rva, op_index, 5 + (effective - 0x28) // 8))
            if not ops:
                continue
            m = insn.mnemonic.lower()
            dest = ops[0]
            if m in {"push", "pushfq", "pushf"}:
                current = state.get("rsp")
                state["rsp"] = int(current) - 8 if current is not None else None
            elif m in {"pop", "popfq", "popf"}:
                current = state.get("rsp")
                state["rsp"] = int(current) + 8 if current is not None else None
            elif m == "leave":
                rbp = state.get("rbp")
                state["rsp"] = int(rbp) + 8 if rbp is not None else None
                state["rbp"] = None
            elif dest.type == x86.X86_OP_REG:
                dest_name = _REG_PARTS.get(insn.reg_name(dest.reg).lower(), (insn.reg_name(dest.reg).lower(), 64))[0]
                if m in {"sub", "add"} and dest_name == "rsp" and len(ops) > 1 and ops[1].type == x86.X86_OP_IMM:
                    current = state.get("rsp")
                    if current is not None:
                        amount = int(ops[1].imm) * (-1 if m == "sub" else 1)
                        state["rsp"] = int(current) + amount
                elif m == "and" and dest_name == "rsp":
                    state["rsp"] = None
                elif m == "mov" and len(ops) > 1 and ops[1].type == x86.X86_OP_REG:
                    source_name = _REG_PARTS.get(insn.reg_name(ops[1].reg).lower(), (insn.reg_name(ops[1].reg).lower(), 64))[0]
                    if dest_name in {"rsp", "rbp"}:
                        state[dest_name] = state.get(source_name)
                elif m == "lea" and len(ops) > 1 and ops[1].type == x86.X86_OP_MEM:
                    source_name = insn.reg_name(ops[1].mem.base).lower() if ops[1].mem.base else ""
                    source = _REG_PARTS.get(source_name, (source_name, 64))[0]
                    source_offset = state.get(source)
                    if dest_name in {"rsp", "rbp"}:
                        state[dest_name] = (int(source_offset) + int(ops[1].mem.disp)
                                            if source_offset is not None and not ops[1].mem.index else None)
        return state, found

    entry = str(blocks[0]["id"])
    states: dict[str, dict[str, int | None]] = {entry: {"rsp": 0, "rbp": None}}
    queue = [entry]
    while queue:
        block_id = queue.pop(0)
        outgoing, _ = transfer(block_by_id[block_id], states[block_id])
        for target in successors.get(block_id, []):
            previous = states.get(target)
            if previous is None:
                states[target] = outgoing
                queue.append(target)
                continue
            merged = {}
            for register in set(previous) | set(outgoing):
                left, right = previous.get(register), outgoing.get(register)
                merged[register] = left if left == right else None
            if merged != previous:
                states[target] = merged
                queue.append(target)

    slots: dict[tuple[int, int], int] = {}
    for block_id, start in states.items():
        _end, found = transfer(block_by_id[block_id], start, collect=True)
        for rva, operand_index, arg_index in found:
            slots[(rva, operand_index)] = arg_index
    return set(slots.values()), slots


def _format_c_add(base: str, displacement: int) -> str:
    if not displacement:
        return base
    return f"{base} {'+' if displacement > 0 else '-'} {abs(displacement)}"


def decompile_c_style(record: dict[str, Any], instructions: list[Any], blocks: list[dict[str, Any]],
                      cfg_edges: list[dict[str, Any]], calls: list[dict[str, Any]], pe: PEImage,
                      capstone: Any, x86: Any, beta: bool = False) -> str:
    """Produce structured, symbol-aware C-like output from decoded x64 instructions.

    This is a lightweight static decompiler: it recovers ABI arguments, stack slots,
    register values, simple if/then diamonds, memory widths, and common arithmetic.
    It deliberately leaves irreducible control flow as explicit labels and gotos.
    """
    rva = int(record["rva"])
    function_name = safe_c_name(function_label(record), rva)
    stack_offsets, _rsp_at = _stack_model(instructions, pe, x86)
    _stack_argument_numbers, incoming_stack_args = _incoming_stack_argument_slots(
        blocks, cfg_edges, pe, capstone, x86
    )
    arguments: dict[int, dict[str, Any]] = {}
    arg_registers = {"rcx": 1, "rdx": 2, "r8": 3, "r9": 4}
    max_argument = 0
    live_arguments = set(arg_registers)
    for instruction in instructions:
        if not instruction.id or not live_arguments:
            continue
        reads: dict[str, int] = {}
        writes: set[str] = set()
        for operand in instruction.operands:
            if operand.type == x86.X86_OP_REG:
                reg = instruction.reg_name(operand.reg).lower()
                base, bits = _REG_PARTS.get(reg, (reg, 64))
                if base in arg_registers:
                    if operand.access & capstone.CS_AC_READ:
                        reads[base] = max(reads.get(base, 0), bits)
                    if operand.access & capstone.CS_AC_WRITE:
                        writes.add(base)
            elif operand.type == x86.X86_OP_MEM:
                for register_id in (operand.mem.base, operand.mem.index):
                    if register_id:
                        reg = instruction.reg_name(register_id).lower()
                        base, _bits = _REG_PARTS.get(reg, (reg, 64))
                        if base in arg_registers:
                            reads[base] = max(reads.get(base, 0), 64)
        for base in tuple(live_arguments):
            if base in reads:
                arg_index = arg_registers[base]
                max_argument = max(max_argument, arg_index)
                info = arguments.setdefault(arg_index, {"bits": 0, "stack": False})
                info["bits"] = max(int(info["bits"]), reads[base])
            if base in writes:
                live_arguments.discard(base)
    for instruction in instructions:
        if not instruction.id:
            continue
        address = int(instruction.address - pe.image_base)
        for index, operand in enumerate(instruction.operands):
            if operand.type == x86.X86_OP_MEM:
                base = instruction.reg_name(operand.mem.base).lower() if operand.mem.base else ""
                base = _REG_PARTS.get(base, (base, 64))[0]
                arg_index = incoming_stack_args.get((address, index))
                if arg_index is not None:
                    max_argument = max(max_argument, arg_index)
                    info = arguments.setdefault(arg_index, {"bits": 64, "stack": True})
                    info["bits"] = min(int(info["bits"]), int(operand.size) * 8)
    for arg_index in range(1, max_argument + 1):
        arguments.setdefault(arg_index, {"bits": 64, "stack": arg_index > 4})

    argument_types: dict[int, str] = {}
    for arg_index, info in arguments.items():
        bits = int(info["bits"])
        if bits == 32 and arg_index <= 4:
            argument_types[arg_index] = "int" if not beta else "unsigned int"
        else:
            argument_types[arg_index] = c_width_type(bits, beta=beta)

    locals_: dict[str, str] = {}
    constants: dict[str, str] = {}
    stack_locals: dict[int, str] = {}
    regs: dict[str, str] = {base: f"v_{base}" for base in (
        "rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp",
        "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
    )}
    for base, number in arg_registers.items():
        regs[base] = f"a{number}"
    regs["rax"] = "result"
    rax_written = any(
        insn.id and (
            insn.group(capstone.CS_GRP_CALL)
            or (insn.operands and insn.operands[0].type == x86.X86_OP_REG
                and _REG_PARTS.get(insn.reg_name(insn.operands[0].reg).lower(), ("", 0))[0] == "rax"
                and insn.mnemonic.lower() not in {"cmp", "test", "jmp", "ljmp"})
        )
        for insn in instructions
    )
    for address, instruction in ((int(ins.address - pe.image_base), ins) for ins in instructions):
        if not instruction.id:
            continue
        for index, operand in enumerate(instruction.operands):
            if operand.type != x86.X86_OP_MEM:
                continue
            effective = stack_offsets.get((address, index))
            if effective is None or (address, index) in incoming_stack_args:
                continue
            if effective not in stack_locals:
                sign = f"m{-effective:X}" if effective < 0 else f"p{effective:X}"
                name = f"v_stack_{sign}"
                stack_locals[effective] = name
                locals_[name] = c_width_type(int(operand.size) * 8, beta=True)

    def stack_arg(insn: Any, operand_index: int) -> str | None:
        rva = int(insn.address - pe.image_base)
        arg_index = incoming_stack_args.get((rva, operand_index))
        return f"a{arg_index}" if arg_index is not None else None

    def register_expr(insn: Any, operand_index: int) -> str:
        operand = insn.operands[operand_index]
        name = insn.reg_name(operand.reg).lower()
        base, bits = _REG_PARTS.get(name, (name, 64))
        expr = regs.get(base, f"v_{base}")
        if expr in constants:
            expr = constants[expr]
        arg_match = re.fullmatch(r"a(\d+)", expr)
        if bits == 64:
            return expr
        if re.fullmatch(r"-?\d+", expr):
            return expr
        if arg_match:
            argument_info = arguments.get(int(arg_match.group(1)))
            if argument_info and int(argument_info["bits"]) <= bits:
                return expr
        return f"({c_width_type(bits, beta=beta)})({expr})"

    def address_expr(insn: Any, operand_index: int) -> str:
        operand = insn.operands[operand_index]
        mem = operand.mem
        base_name = insn.reg_name(mem.base).lower() if mem.base else ""
        base, _ = _REG_PARTS.get(base_name, (base_name, 64))
        effective = stack_offsets.get((int(insn.address - pe.image_base), operand_index))
        if effective is not None:
            argument = stack_arg(insn, operand_index)
            if argument:
                return argument
            return stack_locals.get(effective, "v_stack_unknown")
        terms: list[str] = []
        if base_name:
            terms.append(regs.get(base, f"v_{base}"))
        if mem.index:
            index_name = insn.reg_name(mem.index).lower()
            index_base, _ = _REG_PARTS.get(index_name, (index_name, 64))
            index_expr = regs.get(index_base, f"v_{index_base}")
            terms.append(f"{index_expr} * {int(mem.scale) or 1}")
        address = " + ".join(terms) if terms else "0"
        address = _format_c_add(address, int(mem.disp))
        segment = insn.reg_name(mem.segment).lower() if mem.segment else ""
        if segment in {"fs", "gs"}:
            address = f"{segment}_base + ({address})"
        return address

    def operand_value(insn: Any, index: int) -> str:
        operand = insn.operands[index]
        if operand.type == x86.X86_OP_REG:
            return register_expr(insn, index)
        if operand.type == x86.X86_OP_IMM:
            value = int(operand.imm)
            return str(value) if -1000 <= value <= 1000 else f"0x{value & 0xFFFFFFFFFFFFFFFF:X}ULL"
        if operand.type == x86.X86_OP_MEM:
            effective = stack_offsets.get((int(insn.address - pe.image_base), index))
            if effective is not None:
                argument = stack_arg(insn, index)
                if argument:
                    return argument
                return stack_locals.get(effective, "v_stack_unknown")
            bits = int(operand.size) * 8
            typ = c_width_type(bits, beta=True)
            return f"*({typ} *)({address_expr(insn, index)})"
        return "0"

    def lvalue(insn: Any, index: int) -> str | None:
        operand = insn.operands[index]
        if operand.type == x86.X86_OP_REG:
            return register_expr(insn, index)
        if operand.type == x86.X86_OP_MEM:
            effective = stack_offsets.get((int(insn.address - pe.image_base), index))
            if effective is not None:
                return stack_arg(insn, index) or stack_locals.get(effective, "v_stack_unknown")
            typ = c_width_type(int(operand.size) * 8, beta=True)
            return f"*({typ} *)({address_expr(insn, index)})"
        return None

    def write_target(base: str) -> str:
        if base == "rax":
            locals_["result"] = c_width_type(64, beta=beta)
            return "result"
        if base in arg_registers:
            return f"a{arg_registers[base]}"
        name = f"v_{base}"
        locals_.setdefault(name, c_width_type(64, beta=beta))
        return name

    flag_context: dict[str, Any] = {"kind": "unknown"}

    def condition_for(mnemonic: str, context: dict[str, Any] | None = None) -> str:
        ctx = context or flag_context
        suffix = mnemonic.lower()
        if suffix.startswith("cmov") or suffix.startswith("set"):
            suffix = suffix[4:] if suffix.startswith("cmov") else suffix[3:]
        elif suffix.startswith("j"):
            suffix = suffix[1:]
        left, right = ctx.get("left", "flags"), ctx.get("right", "0")
        if ctx.get("kind") == "test":
            if left == right and suffix in {"e", "z"}:
                return f"{left} == 0"
            if left == right and suffix in {"ne", "nz"}:
                return f"{left} != 0"
            test_expr = f"(({left}) & ({right}))"
            if suffix in {"e", "z", "cxz", "rcxz"}:
                return f"{test_expr} == 0"
            if suffix in {"ne", "nz"}:
                return f"{test_expr} != 0"
        operators = {
            "e": "==", "z": "==", "ne": "!=", "nz": "!=",
            "b": "<", "c": "<", "nae": "<", "ae": ">=", "nb": ">=", "nc": ">=",
            "be": "<=", "na": "<=", "a": ">", "nbe": ">",
            "l": "<", "nge": "<", "ge": ">=", "nl": ">=", "le": "<=", "ng": "<=", "g": ">", "nle": ">",
        }
        if ctx.get("kind") == "cmp" and suffix in operators:
            atom = re.compile(r"^(?:[A-Za-z_]\w*|-?\d+|0x[0-9A-Fa-f]+ULL)$")
            left_text = left if atom.fullmatch(left) else f"({left})"
            right_text = right if atom.fullmatch(right) else f"({right})"
            return f"{left_text} {operators[suffix]} {right_text}"
        if ctx.get("kind") == "test" and suffix in {"e", "z", "ne", "nz"}:
            op = "==" if suffix in {"e", "z"} else "!="
            return f"{left} {op} 0"
        return {
            "e": "condition_is_equal", "z": "condition_is_equal", "ne": "condition_is_not_equal", "nz": "condition_is_not_equal",
            "a": "condition_is_above", "nbe": "condition_is_above", "ae": "condition_is_above_or_equal", "nb": "condition_is_above_or_equal",
            "b": "condition_is_below", "c": "condition_is_below", "nae": "condition_is_below", "be": "condition_is_below_or_equal", "na": "condition_is_below_or_equal",
            "g": "condition_is_greater", "nle": "condition_is_greater", "ge": "condition_is_greater_or_equal", "nl": "condition_is_greater_or_equal",
            "l": "condition_is_less", "nge": "condition_is_less", "le": "condition_is_less_or_equal", "ng": "condition_is_less_or_equal",
            "o": "overflow_flag", "no": "!overflow_flag", "s": "sign_flag", "ns": "!sign_flag",
            "p": "parity_flag", "pe": "parity_flag", "np": "!parity_flag", "po": "!parity_flag",
        }.get(suffix, "condition_is_true")

    def invert_condition(expression: str) -> str:
        pairs = {"==": "!=", "!=": "==", "<": ">=", ">=": "<", ">": "<=", "<=": ">"}
        for operator, inverse in pairs.items():
            if operator in expression:
                left, right = expression.split(operator, 1)
                return f"{left.strip()} {inverse} {right.strip()}"
        if expression.startswith("!"):
            return expression[1:]
        return f"!({expression})"

    def translate_instruction(insn: Any, call_info: dict[str, Any] | None,
                              output: list[str], indent: str = "    ",
                              conditional: bool = False) -> None:
        nonlocal flag_context
        if not insn.id:
            return
        m = insn.mnemonic.lower()
        ops = insn.operands
        if m in {"nop", "endbr64", "int3"}:
            return
        if m in {"cmp", "test"} and len(ops) == 2:
            left, right = operand_value(insn, 0), operand_value(insn, 1)
            flag_context = {"kind": "cmp" if m == "cmp" else "test", "left": left, "right": right}
            if m == "test" and left == right:
                flag_context["right"] = left
            return
        if m in {"mov", "movzx", "movsx", "movsxd", "lea"} and len(ops) == 2:
            source = address_expr(insn, 1) if m == "lea" and ops[1].type == x86.X86_OP_MEM else operand_value(insn, 1)
            if m in {"movsx", "movsxd"}:
                source = f"({c_width_type(int(ops[1].size) * 8, signed=True)})({source})"
            if ops[0].type == x86.X86_OP_REG:
                name = insn.reg_name(ops[0].reg).lower()
                base, bits = _REG_PARTS.get(name, (name, 64))
                if conditional:
                    target = write_target(base)
                    output.append(f"{indent}{target} = {source};")
                    regs[base] = target
                    constants.pop(target, None)
                else:
                    if bits < 64 and m == "mov" and bits == 32 and not re.fullmatch(r"-?\d+", source):
                        source = f"(unsigned int)({source})"
                    regs[base] = source
            else:
                destination = lvalue(insn, 0)
                if destination:
                    output.append(f"{indent}{destination} = {source};")
            return
        if m in {"add", "sub", "and", "or", "xor", "imul", "shl", "sal", "shr", "sar"} and len(ops) >= 2:
            if ops[0].type == x86.X86_OP_REG:
                base, bits = _REG_PARTS.get(insn.reg_name(ops[0].reg).lower(), (insn.reg_name(ops[0].reg).lower(), 64))
                target = write_target(base)
                old = regs.get(base, target)
                rhs = operand_value(insn, 1)
                if m == "xor" and ops[1].type == x86.X86_OP_REG and _REG_PARTS.get(insn.reg_name(ops[1].reg).lower(), ("", 0))[0] == base:
                    expression = "0"
                else:
                    operator = {"add": "+", "sub": "-", "and": "&", "or": "|", "xor": "^", "imul": "*", "shl": "<<", "sal": "<<", "shr": ">>", "sar": ">>"}[m]
                    expression = f"({old}) {operator} ({rhs})"
                if bits < 64 and not re.fullmatch(r"-?\d+", expression):
                    expression = f"({c_width_type(bits, beta=beta)})({expression})"
                output.append(f"{indent}{target} = {expression};")
                regs[base] = target
                if expression == "0":
                    constants[target] = "0"
                else:
                    constants.pop(target, None)
                flag_context = {"kind": "unknown"}
            return
        if m in {"inc", "dec", "neg", "not"} and ops and ops[0].type == x86.X86_OP_REG:
            base, bits = _REG_PARTS.get(insn.reg_name(ops[0].reg).lower(), (insn.reg_name(ops[0].reg).lower(), 64))
            target = write_target(base)
            old = regs.get(base, target)
            expression = {"inc": f"({old}) + 1", "dec": f"({old}) - 1", "neg": f"-({old})", "not": f"~({old})"}[m]
            if bits < 64:
                expression = f"({c_width_type(bits, beta=beta)})({expression})"
            output.append(f"{indent}{target} = {expression};")
            regs[base] = target
            constants.pop(target, None)
            return
        if m.startswith("cmov") and len(ops) == 2 and ops[0].type == x86.X86_OP_REG:
            name = insn.reg_name(ops[0].reg).lower()
            base, bits = _REG_PARTS.get(name, (name, 64))
            current = regs.get(base, f"v_{base}")
            target = current if re.fullmatch(r"a\d+", current) else write_target(base)
            if target not in locals_ and not re.fullmatch(r"a\d+", target):
                locals_[target] = c_width_type(64, beta=beta)
            if current != target:
                output.append(f"{indent}{target} = {current};")
            source = operand_value(insn, 1)
            output.append(f"{indent}if ({condition_for(m)}) {{ {target} = {source}; }}")
            regs[base] = target
            constants.pop(target, None)
            return
        if m.startswith("set") and ops and ops[0].type == x86.X86_OP_REG:
            base, _bits = _REG_PARTS.get(insn.reg_name(ops[0].reg).lower(), (insn.reg_name(ops[0].reg).lower(), 64))
            target = write_target(base)
            output.append(f"{indent}{target} = ({condition_for(m)}) ? 1 : 0;")
            regs[base] = target
            constants.pop(target, None)
            return
        if m in {"call", "callq"}:
            locals_["result"] = c_width_type(64, beta=beta)
            target_name = safe_c_name(str((call_info or {}).get("display", "kernel_call")), int((call_info or {}).get("target_rva") or rva))
            arguments_text = ", ".join(regs.get(base, f"v_{base}") for base in ("rcx", "rdx", "r8", "r9"))
            target_rva = (call_info or {}).get("function_rva")
            if call_info and call_info.get("kind") == "import":
                target_name = safe_c_name(str(call_info.get("display", "kernel_import")), rva)
            if target_rva is None and (not call_info or call_info.get("kind") != "import"):
                target_name = "kernel_indirect_call"
            output.append(f"{indent}result = {target_name}({arguments_text});")
            regs["rax"] = "result"
            constants.pop("result", None)
            return
        if m.startswith("j") and m not in {"jmp", "jmpl"}:
            return
        if m in {"push", "pop", "leave", "xchg", "xadd"}:
            return
        if m.startswith("ret"):
            return
        if m in {"syscall", "sysret", "iret", "iretd", "iretq", "ud2"}:
            return
        if m in {"movaps", "movups", "movdqa", "movdqu", "movss", "movsd", "movd", "movq", "movntdq"}:
            if len(ops) == 2 and ops[0].type == x86.X86_OP_MEM:
                destination = lvalue(insn, 0)
                if destination:
                    output.append(f"{indent}{destination} = {operand_value(insn, 1)};")

    block_by_id = {str(block["id"]): block for block in blocks}
    block_order_all = [str(block["id"]) for block in blocks]
    reachable = {block_order_all[0]} if block_order_all else set()
    work = list(reachable)
    while work:
        source = work.pop()
        for edge in cfg_edges:
            target = str(edge.get("target", ""))
            if str(edge.get("source")) == source and target in block_by_id and target not in reachable:
                reachable.add(target)
                work.append(target)
    block_order = [block_id for block_id in block_order_all if block_id in reachable]
    order_index = {block_id: index for index, block_id in enumerate(block_order)}
    edges_by_source: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for edge in cfg_edges:
        edges_by_source[str(edge["source"])].append(edge)
    call_by_site = {int(call["site_rva"]): call for call in calls}
    output: list[str] = []
    skipped: set[str] = set()
    label_targets = {str(edge["target"]) for edge in cfg_edges if edge.get("kind") in {"branch", "branch-out"} and str(edge.get("target", "")).startswith("bb_")}
    for i, block_id in enumerate(block_order):
        if block_id in skipped:
            continue
        block = block_by_id[block_id]
        items = list(block["instructions"])
        if not items:
            continue
        if block_id in label_targets and block_id != block_order[0]:
            output.append(f"loc_{int(block['rva']):08X}:")
        last = items[-1]
        is_jump = bool(last.id and last.group(capstone.CS_GRP_JUMP))
        is_ret = bool(last.id and last.group(capstone.CS_GRP_RET))
        terminal_jump = is_jump and last.mnemonic.lower() not in {"jmp", "ljmp"}
        ordinary = items[:-1] if is_jump or is_ret else items
        for insn in ordinary:
            address = int(insn.address - pe.image_base)
            translate_instruction(insn, call_by_site.get(address), output)
        successors = edges_by_source.get(block_id, [])
        if terminal_jump:
            branch_edge = next((edge for edge in successors if edge.get("kind") == "branch"), None)
            fall_edge = next((edge for edge in successors if edge.get("kind") == "fallthrough"), None)
            branch_target = str(branch_edge.get("target")) if branch_edge else ""
            fall_target = str(fall_edge.get("target")) if fall_edge else ""
            branch_condition = condition_for(last.mnemonic)
            structured = None
            if branch_target in block_by_id and fall_target in block_by_id:
                # Collapse the common one-block if/then diamond into an ordinary C if.
                fall_edges = edges_by_source.get(fall_target, [])
                fall_merge = next((str(edge["target"]) for edge in fall_edges if edge.get("kind") in {"flow", "fallthrough"}), None)
                target_edges = edges_by_source.get(branch_target, [])
                target_merge = next((str(edge["target"]) for edge in target_edges if edge.get("kind") in {"flow", "fallthrough"}), None)
                fall_last = block_by_id[fall_target]["instructions"][-1]
                target_last = block_by_id[branch_target]["instructions"][-1]
                fall_has_jump = bool(fall_last.id and fall_last.group(capstone.CS_GRP_JUMP))
                target_has_jump = bool(target_last.id and target_last.group(capstone.CS_GRP_JUMP))
                if fall_merge == branch_target and len(fall_edges) == 1 and not fall_has_jump:
                    structured = (fall_target, branch_target, invert_condition(branch_condition))
                elif target_merge == fall_target and len(target_edges) == 1 and not target_has_jump:
                    structured = (branch_target, fall_target, branch_condition)
            if structured:
                body_id, merge_id, body_condition = structured
                previous_regs = dict(regs)
                arm_lines: list[str] = []
                arm_items = list(block_by_id[body_id]["instructions"])
                for insn in arm_items:
                    translate_instruction(insn, call_by_site.get(int(insn.address - pe.image_base)), arm_lines, "        ", conditional=True)
                changed_locals = []
                for base, expression in regs.items():
                    old_expression = previous_regs.get(base)
                    if expression != old_expression and expression in locals_ and not re.fullmatch(r"a\d+", expression):
                        if old_expression and old_expression != expression:
                            changed_locals.append((expression, old_expression))
                for target, initial in changed_locals:
                    output.append(f"    {target} = {initial};")
                output.append(f"    if ({body_condition}) {{")
                output.extend(arm_lines)
                output.append("    }")
                skipped.add(body_id)
                label_targets.discard(merge_id)
                if merge_id != body_id and merge_id in block_order:
                    # Keep the merge block in normal RVA order; the skipped arm already rejoins it.
                    pass
                continue
            if branch_target.startswith("bb_"):
                target_rva = int(branch_target[3:], 16)
                output.append(f"    if ({branch_condition}) goto loc_{target_rva:08X};")
            elif branch_target:
                output.append(f"    if ({branch_condition}) return result;")
            if fall_target.startswith("bb_") and (i + 1 >= len(block_order) or fall_target != block_order[i + 1]):
                output.append(f"    goto loc_{int(fall_target[3:], 16):08X};")
            continue
        if is_jump:
            target = next((str(edge["target"]) for edge in successors if edge.get("kind") in {"branch", "branch-out"}), "")
            if target.startswith("bb_"):
                output.append(f"    goto loc_{int(target[3:], 16):08X};")
            continue
        if is_ret:
            output.append(f"    return {regs.get('rax', 'result')};" if rax_written else "    return;")
            continue
        flow_target = next((str(edge["target"]) for edge in successors if edge.get("kind") in {"flow", "fallthrough"}), None)
        if flow_target and flow_target.startswith("bb_") and (i + 1 >= len(block_order) or flow_target != block_order[i + 1]):
            output.append(f"    goto loc_{int(flow_target[3:], 16):08X};")
        elif not flow_target and i == len(block_order) - 1:
            output.append(f"    return {regs.get('rax', 'result')};" if rax_written else "    return;")

    merged_output: list[str] = []
    conditional_pattern = re.compile(r"^(\s*)if \((.*)\) \{ (.+?) = (.*); \}$")
    cursor = 0
    while cursor < len(output):
        first = conditional_pattern.match(output[cursor])
        if not first:
            merged_output.append(output[cursor])
            cursor += 1
            continue
        indent, condition_text = first.group(1), first.group(2)
        assignments = [f"{first.group(3)} = {first.group(4)};"]
        cursor += 1
        while cursor < len(output):
            following = conditional_pattern.match(output[cursor])
            if not following or following.group(1) != indent or following.group(2) != condition_text:
                break
            assignments.append(f"{following.group(3)} = {following.group(4)};")
            cursor += 1
        if len(assignments) == 1:
            merged_output.append(f"{indent}if ({condition_text}) {{ {assignments[0]} }}")
        else:
            merged_output.append(f"{indent}if ({condition_text}) {{")
            merged_output.extend(f"{indent}    {assignment}" for assignment in assignments)
            merged_output.append(f"{indent}}}")
    output = merged_output

    parameters = []
    for arg_index in range(1, max_argument + 1):
        parameters.append(f"{argument_types[arg_index]} a{arg_index}")
    if not parameters:
        parameters_text = "void"
    else:
        parameters_text = ", ".join(parameters)
    return_type = c_width_type(64, beta=beta) if rax_written else "void"
    declaration = [f"{return_type} __fastcall {function_name}({parameters_text})", "{"]
    for variable, typ in sorted(locals_.items()):
        declaration.append(f"    {typ} {variable};")
    if locals_ and output:
        declaration.append("")
    declaration.extend(output)
    declaration.append("}")
    return "\n".join(declaration)


def asm_line(insn: Any, image_base: int) -> str:
    rva = int(insn.address - image_base)
    raw = insn.bytes.hex(" ").upper()
    return f"{rva:08X}  {raw:<30}  {insn.mnemonic} {insn.op_str}".rstrip()


def markdown_call_target(call: dict[str, Any], index: dict[int, dict[str, Any]],
                         report_dir: Path) -> str:
    target = call.get("function_rva")
    display = str(call.get("display", "unknown"))
    if target is not None and int(target) in index:
        rel = Path(os.path.relpath(index[int(target)]["path"], str(report_dir))).as_posix()
        return f"[{display}]({rel})"
    return f"`{display}`"


def make_report(
    record: dict[str, Any], instructions: list[Any], blocks: list[dict[str, Any]],
    cfg_edges: list[dict[str, Any]], calls: list[dict[str, Any]], transfers: list[dict[str, Any]],
    data_refs: list[dict[str, Any]], callers: list[dict[str, Any]], pe: PEImage,
    capstone: Any, x86: Any,
    function_index: dict[int, dict[str, Any]], function_names: dict[int, str],
    imports_by_iat: dict[int, dict[str, str]], report_dir: Path, viewer_link: str,
    graph_link: str,
) -> str:
    rva = int(record["rva"])
    end = int(record["end_rva"])
    name = function_label(record)
    va = pe.image_base + rva
    decoded_bytes = sum(int(insn.size) for insn in instructions)
    skipdata_bytes = sum(int(insn.size) for insn in instructions if insn.id == 0)
    lines = [
        f"# {html.escape(name)}",
        "",
        f"- RVA: `0x{rva:08X}`–`0x{end:08X}` (길이 `{end-rva:,}` bytes)",
        f"- VA: `0x{va:016X}`",
        f"- 실행 섹션: `{record.get('section', 'unknown')}`",
        f"- PDB 이름 있음: `{ '예' if record.get('has_pdb_name') else '아니요' }`; PDB Function 태그: `{ '예' if record.get('has_pdb_function_record') else '아니요' }`",
        f"- unwind 정보 RVA: `0x{int(record.get('unwind_info_rva', 0)):08X}`",
        f"- 디코드: `{len(instructions):,}`개 명령, `{decoded_bytes:,}/{end-rva:,}` bytes 표시",
        f"- 미해석 바이트: `{skipdata_bytes}` (있으면 어셈블리에 `.byte`로 보존)",
        "",
        "> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.",
        "",
        "## 1. Dependencies",
        "",
        f"- 직접 호출 지점: **{len(calls)}**; 고유 호출 대상: **{len({(c.get('kind'), c.get('target_rva'), c.get('display')) for c in calls})}**",
        f"- 직접 호출자로 확인된 함수: **{len({int(c['caller_rva']) for c in callers})}**",
        f"- RIP 상대 이미지 참조: **{len(data_refs)}**",
        "",
        "### Outgoing calls",
    ]
    if calls:
        for call in calls:
            site = int(call["site_rva"])
            where = markdown_call_target(call, function_index, report_dir)
            extra = f"; import `{call['dll']}!{call['import_name']}`" if call.get("dll") else ""
            target_text = f"`0x{int(call['target_rva']):08X}`" if call.get("target_rva") is not None else "간접 대상"
            lines.append(f"- `0x{site:08X}` → {where} ({call.get('kind', 'unknown')}, {target_text}{extra})")
    else:
        lines.append("- 직접 디코드된 call 명령이 없습니다.")
    lines.extend(["", "### Direct callers"])
    if callers:
        for caller in callers:
            crva = int(caller["caller_rva"])
            site = int(caller["site_rva"])
            if crva in function_index:
                rel = Path(os.path.relpath(function_index[crva]["path"], str(report_dir))).as_posix()
                caller_label = f"[{function_names.get(crva, f'sub_{crva:08X}')}]({rel})"
            else:
                caller_label = f"`0x{crva:08X}`"
            lines.append(f"- `{caller_label}` at `0x{site:08X}`")
    else:
        lines.append("- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.")
    lines.extend(["", "### Static image references"])
    if data_refs:
        for ref in data_refs:
            target = int(ref["rva"])
            section = ref.get("section") or "image boundary/outside"
            import_info = ref.get("import")
            label = f"{import_info['dll']}!{import_info['name']} (IAT)" if import_info else (ref.get("symbol") or section)
            lines.append(f"- `0x{int(ref['site_rva']):08X}` → RVA `0x{target:08X}` (`{label}`; {ref.get('access', 'reference')})")
    else:
        lines.append("- 디코드된 RIP-relative 메모리 참조가 없습니다.")
    lines.extend(["", "## 2. Other-region calls and transfers", ""])
    cross_section = [c for c in calls if c.get("target_section") and c.get("target_section") != record.get("section")]
    lines.append(f"- 다른 실행 섹션으로 향하는 call: **{len(cross_section)}**")
    if cross_section:
        lines.extend(f"  - `0x{int(c['site_rva']):08X}` → {markdown_call_target(c, function_index, report_dir)} (`{record.get('section')}` → `{c['target_section']}`)" for c in cross_section)
    if transfers:
        lines.append(f"- call이 아닌 외부 분기/꼬리 이동: **{len(transfers)}**")
        for transfer in transfers:
            lines.append(f"  - `0x{int(transfer['site_rva']):08X}` → {markdown_call_target(transfer, function_index, report_dir)} (`{transfer.get('kind')}`)")
    else:
        lines.append("- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.")
    lines.extend(["", "## 3. Assembly (complete function range)", "", "```asm"])
    if instructions:
        lines.extend(asm_line(insn, pe.image_base) for insn in instructions)
    else:
        lines.append("; no bytes decoded")
    lines.extend(["```", "", "## 4. C-style interpretation (structured pseudocode)", "", "```c"])
    lines.append(decompile_c_style(record, instructions, blocks, cfg_edges, calls, pe, capstone, x86, beta=False))
    lines.extend(["```", "", "## 5. Execution-region graph", ""])
    lines.append(f"[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널]({graph_link})")
    lines.append("")
    lines.append("- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.")
    if len(blocks) <= 60:
        lines.extend(["", "### Static fallback", "", "```mermaid", "flowchart TD"])
        for block in blocks:
            label = f"BB_{int(block['rva']):08X}"
            lines.append(f"  {block['id']}[{label}]")
        for edge in cfg_edges:
            if edge["target"].startswith("bb_"):
                lines.append(f"  {edge['source']} -->|{edge['kind']}| {edge['target']}")
        lines.extend(["```"])
    lines.append("")
    return "\n".join(lines)


VIEWER_HTML = r'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ntoskrnl 실행 흐름 그래프</title>
<style>
:root{color-scheme:dark;--bg:#10141b;--panel:#171e28;--text:#e6edf5;--muted:#9aa9ba;--line:#344455;--blue:#4ea1ff;--green:#46c98b;--orange:#ffb454}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 Segoe UI,Arial,sans-serif}header{height:58px;display:flex;align-items:center;gap:9px;padding:9px 14px;background:var(--panel);border-bottom:1px solid var(--line)}h1{font-size:15px;margin:0 14px 0 0;max-width:48vw;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}button,a{background:#263344;color:var(--text);border:1px solid #41566b;border-radius:6px;padding:7px 10px;text-decoration:none;cursor:pointer}button:hover,a:hover{background:#32465c}#meta{color:var(--muted);margin-left:auto;white-space:nowrap}main{height:calc(100vh - 58px);display:grid;grid-template-columns:minmax(0,1fr) 290px}.canvas{position:relative;overflow:hidden}svg{width:100%;height:100%;background-image:radial-gradient(#273342 1px,transparent 1px);background-size:22px 22px;cursor:grab;touch-action:none}svg.dragging{cursor:grabbing}.side{background:var(--panel);border-left:1px solid var(--line);padding:14px;overflow:auto}.side h2{font-size:13px;margin:0 0 8px}.side p{color:var(--muted);white-space:pre-wrap;overflow-wrap:anywhere}.node rect{fill:#1d2a39;stroke:var(--blue);stroke-width:2}.node.call rect{fill:#342b1e;stroke:var(--orange)}.node.outside rect{fill:#30252b;stroke:#e77982}.node text{fill:var(--text);font-size:12px;pointer-events:none}.node{cursor:pointer}.edge{fill:none;stroke:#718399;stroke-width:1.5;opacity:.8}.edge.branch{stroke:var(--green)}.edge.call{stroke:var(--orange);stroke-dasharray:6 4}.edge.branch-out,.edge.indirect{stroke:#e77982;stroke-dasharray:5 4}.legend{color:var(--muted);font-size:12px}.error{padding:24px;color:#ff9292}@media(max-width:760px){main{grid-template-columns:minmax(0,1fr)}.side{display:none}h1{max-width:32vw}#meta{display:none}}
</style></head><body>
<header><h1 id="title">ntoskrnl graph</h1><button id="fit">전체 보기</button><button id="minus">−</button><button id="plus">+</button><a id="report" href="#" target="_blank">Markdown 보고서</a><span id="meta"></span></header>
<main><div class="canvas"><svg id="svg" xmlns="http://www.w3.org/2000/svg"><defs><marker id="arrow" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#718399"/></marker></defs><g id="world"></g></svg></div><aside class="side"><h2>선택한 노드</h2><p id="details">노드를 선택하면 블록 정보가 표시됩니다.</p><h2>조작</h2><p class="legend">휠: 확대·축소<br>드래그: 화면 이동<br>함수 호출 노드 클릭: 대상 보고서 열기<br>전체 보기: 그래프 범위에 맞추기</p><h2>그래프</h2><p id="summary"></p></aside></main>
<script>
const params=new URLSearchParams(location.search);const section=params.get('section')||'';const rva=(params.get('rva')||'').toUpperCase();
const safe=/^[a-z0-9-]+$/.test(section);const title=document.getElementById('title');const svg=document.getElementById('svg');const world=document.getElementById('world');const meta=document.getElementById('meta');let current={x:30,y:30,s:1};let dragging=null;
function fail(message){document.querySelector('main').innerHTML='<div class="error">'+message+'</div>';}
if(!safe||!/^0X[0-9A-F]{8}$/.test(rva)){fail('URL에 올바른 section과 RVA가 필요합니다.');}
else{const script=document.createElement('script');script.src='../graphs/'+section+'.js';script.onload=()=>{const graph=(window.NTOSKRNL_GRAPHS||{})[rva];if(!graph){fail('그래프 데이터를 찾지 못했습니다: '+rva);return;}render(graph);};script.onerror=()=>fail('그래프 파일을 읽지 못했습니다: '+section);document.head.appendChild(script);}
function render(g){title.textContent=g.name+' — '+g.rva;meta.textContent=g.section+' · '+g.blocks+' blocks · '+g.calls+' calls';const report=document.getElementById('report');if(g.report)report.href=g.report;document.getElementById('summary').textContent='범위 '+g.rva+'–'+g.end+'\nCFG block '+g.blocks+'개\ncall site '+g.calls+'개\n외부 호출 노드는 주황색입니다.';
 const nodes=g.nodes;const blocks=nodes.filter(n=>n.kind==='block');const externals=nodes.filter(n=>n.kind!=='block');const byId=new Map(nodes.map(n=>[n.id,n]));
 const adjacency=new Map(blocks.map(n=>[n.id,[]]));for(const e of g.edges)if(adjacency.has(e.source)&&adjacency.has(e.target))adjacency.get(e.source).push(e.target);
 const depth=new Map();if(blocks.length)depth.set(blocks[0].id,0);const queue=blocks.length?[blocks[0].id]:[];while(queue.length){const id=queue.shift();for(const next of adjacency.get(id)||[])if(!depth.has(next)){depth.set(next,depth.get(id)+1);queue.push(next);}}
 let max=0;for(const n of blocks)if(!depth.has(n.id)){max++;depth.set(n.id,max);}const layers=new Map();for(const n of blocks){const d=depth.get(n.id);if(!layers.has(d))layers.set(d,[]);layers.get(d).push(n);}for(const list of layers.values())list.sort((a,b)=>a.rva-b.rva);
 const pos=new Map();const W=210,H=66,GX=100,GY=45;let maxY=0;for(const [d,list] of layers){list.forEach((n,i)=>{const p={x:40+d*(W+GX),y:35+i*(H+GY),w:W,h:H};pos.set(n.id,p);maxY=Math.max(maxY,p.y+H);});}
 const callX=40+(Math.max(0,...layers.keys())+1)*(W+GX);externals.forEach((n,i)=>{const p={x:callX,y:35+i*(H+GY),w:W,h:H};pos.set(n.id,p);maxY=Math.max(maxY,p.y+H);});
 const width=callX+W+40,height=Math.max(180,maxY+40);svg.setAttribute('viewBox','0 0 '+width+' '+height);
 const ns='http://www.w3.org/2000/svg';const make=(tag,attrs,parent)=>{const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs||{}))e.setAttribute(k,v);if(parent)parent.appendChild(e);return e;};
 for(const e of g.edges){const a=pos.get(e.source),b=pos.get(e.target);if(!a||!b)continue;const x1=a.x+a.w,y1=a.y+a.h/2,x2=b.x,y2=b.y+b.h/2;const bend=Math.max(35,Math.abs(x2-x1)*.45);const path=make('path',{d:`M ${x1} ${y1} C ${x1+bend} ${y1}, ${x2-bend} ${y2}, ${x2} ${y2}`,class:'edge '+e.kind,'marker-end':'url(#arrow)'},world);}
 for(const n of nodes){const p=pos.get(n.id);if(!p)continue;const group=make('g',{class:'node '+(n.kind==='block'?'block':n.kind==='call'?'call':'outside'),transform:`translate(${p.x} ${p.y})`},world);make('rect',{width:p.w,height:p.h,rx:8},group);const lines=(n.label||n.id).split('\n').slice(0,3);lines.forEach((line,i)=>{const t=make('text',{x:10,y:21+i*17},group);t.textContent=line.length>28?line.slice(0,27)+'…':line;});group.addEventListener('click',()=>{document.getElementById('details').textContent=(n.label||n.id)+'\n\n'+(n.detail||'');if(n.url)location.href=new URL(n.url,location.href).href;});group.addEventListener('dblclick',()=>{if(n.url)window.open(new URL(n.url,location.href).href,'_blank');});}
 fit(width,height);document.getElementById('fit').onclick=()=>fit(width,height);document.getElementById('plus').onclick=()=>zoomAt(.8);document.getElementById('minus').onclick=()=>zoomAt(1.25);svg.addEventListener('wheel',e=>{e.preventDefault();zoomAt(e.deltaY<0?.88:1.14,e.clientX,e.clientY);},{passive:false});svg.addEventListener('pointerdown',e=>{dragging={x:e.clientX,y:e.clientY,tx:current.x,ty:current.y};svg.classList.add('dragging');svg.setPointerCapture(e.pointerId);});svg.addEventListener('pointermove',e=>{if(!dragging)return;const scale=svg.clientWidth/Math.max(1,width*current.s);current.x=dragging.tx+(e.clientX-dragging.x)/scale;current.y=dragging.ty+(e.clientY-dragging.y)/scale;apply();});svg.addEventListener('pointerup',()=>{dragging=null;svg.classList.remove('dragging');});
 function apply(){world.setAttribute('transform',`translate(${current.x} ${current.y}) scale(${current.s})`);}function fit(w,h){const box=svg.getBoundingClientRect();current.s=Math.min((box.width-40)/w,(box.height-40)/h,1);current.x=(box.width/current.s-w)/2;current.y=(box.height/current.s-h)/2;apply();}function zoomAt(factor,cx,cy){const box=svg.getBoundingClientRect();const px=cx==null?box.width/2:cx-box.left,py=cy==null?box.height/2:cy-box.top;const scale=box.width/Math.max(1,width*current.s);const wx=px*scale-current.x,wy=py*scale-current.y;const next=Math.max(.08,Math.min(4,current.s/factor));current.x=px*scale-wx*next;current.y=py*scale-wy*next;current.s=next;apply();}
}
</script></body></html>'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exe", type=Path, default=DEFAULT_EXE)
    parser.add_argument("--index", type=Path, default=DEFAULT_OUT / "data" / "all_executable_functions.json")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--progress-every", type=int, default=1000)
    args = parser.parse_args()
    out = args.out.resolve()
    args.exe = args.exe.resolve()
    args.index = args.index.resolve()
    if not args.exe.is_file():
        raise FileNotFoundError(f"Kernel image not found: {args.exe}")
    if not args.index.is_file():
        raise FileNotFoundError(f"Function inventory not found: {args.index}")
    index_data = json.loads(args.index.read_text(encoding="utf-8"))
    records = index_data["functions"]
    if len(records) != int(index_data["function_count"]):
        raise ValueError("Function inventory count does not match its records")
    if len({int(item["rva"]) for item in records}) != len(records):
        raise ValueError("Duplicate function start RVAs in inventory")
    pe = PEImage(args.exe)
    capstone, x86, md = capstone_api()
    imports_by_iat = pe.imports()
    starts = {int(item["rva"]): item for item in records}
    sorted_starts = sorted(starts)
    symbols_by_rva: dict[int, list[str]] = collections.defaultdict(list)
    for item in records:
        rva = int(item["rva"])
        for sym in item.get("pdb_symbols", []):
            if sym.get("name"):
                symbols_by_rva[rva].append(str(sym["name"]))
        symbols_by_rva[rva].extend(str(x) for x in item.get("export_names", []) if x)
    for item in index_data.get("additional_code_symbol_candidates", []):
        rva = int(item["rva"])
        for sym in item.get("pdb_symbols", []):
            if sym.get("name"):
                symbols_by_rva[rva].append(str(sym["name"]))
        symbols_by_rva[rva].extend(str(x) for x in item.get("export_names", []) if x)
    function_names = {rva: function_label(item) for rva, item in starts.items()}

    report_paths: dict[int, dict[str, Any]] = {}
    section_slugs = sorted({slug(str(item.get("section") or "unknown")) for item in records})
    for item in records:
        rva = int(item["rva"])
        section_slug = slug(str(item.get("section") or "unknown"))
        shard = f"{(rva >> 16) & 0xFF:02X}"
        relpath = Path("functions") / section_slug / shard / report_filename(item)
        report_paths[rva] = {
            "path": str((out / relpath).resolve()),
            "relative_path": relpath.as_posix(),
            "section_slug": section_slug,
        }

    graph_bundles: dict[str, dict[str, Any]] = collections.defaultdict(dict)
    index_rows: list[dict[str, Any]] = []
    caller_map: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    generated = 0
    decode_failures: list[dict[str, Any]] = []
    total_instructions = 0
    total_cfg_blocks = 0
    total_skipdata_bytes = 0
    functions_with_skipdata = 0
    for record in records:
        rva = int(record["rva"])
        end = int(record["end_rva"])
        section_slug = report_paths[rva]["section_slug"]
        report_file = Path(report_paths[rva]["path"])
        try:
            code = pe.bytes_at_rva(rva, end - rva)
            instructions = list(md.disasm(code, pe.image_base + rva))
        except Exception as exc:
            instructions = []
            decode_failures.append({"rva": f"0x{rva:08X}", "error": str(exc)})
        blocks, cfg_edges = build_blocks(instructions, rva, end, capstone, x86, pe.image_base)
        total_instructions += len(instructions)
        total_cfg_blocks += len(blocks)
        function_skipdata_bytes = sum(int(insn.size) for insn in instructions if insn.id == 0)
        total_skipdata_bytes += function_skipdata_bytes
        functions_with_skipdata += int(function_skipdata_bytes > 0)
        call_by_site: dict[int, dict[str, Any]] = {}
        calls: list[dict[str, Any]] = []
        transfers: list[dict[str, Any]] = []
        data_ref_map: dict[tuple[int, str], dict[str, Any]] = {}
        call_sites_in_block: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
        for insn in instructions:
            site = int(insn.address - pe.image_base)
            call_flag, jump_flag, _ret_flag = instruction_groups(insn, capstone)
            if call_flag:
                direct_va = operand_imm(insn, x86)
                indirect_rva = rip_target_rva(insn, pe.image_base, x86) if direct_va is None else None
                import_info = imports_by_iat.get(indirect_rva) if indirect_rva is not None else None
                target_rva = direct_va - pe.image_base if direct_va is not None else None
                if import_info:
                    resolved = {"kind": "import", "display": f"{import_info['dll']}!{import_info['name']}", "function_rva": None, "section": None}
                else:
                    resolved = resolve_code_target(target_rva, starts, sorted_starts, symbols_by_rva, pe)
                call = {
                    "site_rva": site,
                    "target_rva": target_rva,
                    "iat_rva": indirect_rva,
                    "kind": resolved["kind"],
                    "display": resolved["display"],
                    "function_rva": resolved["function_rva"],
                    "target_section": resolved["section"],
                    "instruction": (insn.mnemonic + " " + insn.op_str).strip(),
                }
                if import_info:
                    call.update({"dll": import_info["dll"], "import_name": import_info["name"]})
                calls.append(call)
                call_by_site[site] = call
                call_sites_in_block[site].append(call)
                if call.get("function_rva") is not None:
                    caller_map[int(call["function_rva"])].append({
                        "caller_rva": rva, "site_rva": site,
                    })
            elif jump_flag:
                target_va = operand_imm(insn, x86)
                if target_va is not None:
                    target_rva = target_va - pe.image_base
                    if not (rva <= target_rva < end):
                        resolved = resolve_code_target(target_rva, starts, sorted_starts, symbols_by_rva, pe)
                        transfers.append({
                            "site_rva": site, "target_rva": target_rva,
                            "kind": "tail-transfer", "display": resolved["display"],
                            "function_rva": resolved["function_rva"], "target_section": resolved["section"],
                        })
            ref_rva = rip_target_rva(insn, pe.image_base, x86)
            if ref_rva is not None:
                section = pe.section_for_rva(ref_rva)
                imp = imports_by_iat.get(ref_rva)
                access = []
                for operand in insn.operands:
                    if operand.type == x86.X86_OP_MEM and operand.mem.base == x86.X86_REG_RIP:
                        if operand.access & capstone.CS_AC_READ:
                            access.append("read")
                        if operand.access & capstone.CS_AC_WRITE:
                            access.append("write")
                key = (ref_rva, "/".join(access) or "reference")
                data_ref_map.setdefault(key, {
                    "site_rva": site, "rva": ref_rva,
                    "section": section["name"] if section else None,
                    "symbol": (symbols_by_rva.get(ref_rva) or [None])[0],
                    "import": imp, "access": "/".join(access) or "reference",
                })

        block_start_for_insn = {}
        for block in blocks:
            for insn in block["instructions"]:
                block_start_for_insn[int(insn.address - pe.image_base)] = int(block["rva"])
        graph_nodes: list[dict[str, Any]] = []
        for block in blocks:
            first = block["instructions"][0]
            short = (first.mnemonic + " " + first.op_str).strip()
            detail = "\n".join(asm_line(insn, pe.image_base) for insn in block["instructions"][:8])
            graph_nodes.append({
                "id": block["id"], "rva": int(block["rva"]), "kind": "block",
                "label": f"BB 0x{int(block['rva']):08X}\n{short}", "detail": detail,
            })
        graph_edges = list(cfg_edges)
        external_graph_nodes: dict[str, dict[str, Any]] = {}
        block_ids = {block["id"] for block in blocks}
        for edge in cfg_edges:
            target_id = str(edge["target"])
            if target_id in block_ids or target_id in external_graph_nodes:
                continue
            target_rva = edge.get("target_rva")
            if target_rva is None:
                external_graph_nodes[target_id] = {
                    "id": target_id, "kind": "outside", "label": "INDIRECT JUMP",
                    "detail": "Control leaves this function through an indirect jump; the runtime target cannot be determined statically.",
                }
                continue
            target_rva = int(target_rva)
            resolved = resolve_code_target(target_rva, starts, sorted_starts, symbols_by_rva, pe)
            target_function = resolved.get("function_rva")
            target_rel = None
            if target_function is not None and int(target_function) in report_paths:
                target_rel = Path(os.path.relpath(report_paths[int(target_function)]["path"], str(out / "viewer"))).as_posix()
            external_graph_nodes[target_id] = {
                "id": target_id, "kind": "outside",
                "label": f"BRANCH OUT {resolved['display']}\n0x{target_rva:08X}",
                "detail": f"Control-flow target RVA 0x{target_rva:08X}\nResolution: {resolved['kind']}\nSection: {resolved.get('section') or 'outside image'}",
                "url": target_rel,
            }
        for call in calls:
            source_rva = block_start_for_insn.get(int(call["site_rva"]))
            if source_rva is None:
                continue
            if call.get("function_rva") is not None:
                target_key = int(call["function_rva"])
                node_id = f"call_fn_{target_key:08X}"
                target_record = starts.get(target_key)
                target_section_slug = report_paths[target_key]["section_slug"] if target_key in report_paths else None
                target_rel = None
                if target_key in report_paths:
                    target_rel = Path(os.path.relpath(report_paths[target_key]["path"], str(out / "viewer"))).as_posix()
                external_graph_nodes[node_id] = {
                    "id": node_id, "kind": "call", "label": f"CALL {call['display']}\n0x{target_key:08X}",
                    "detail": f"Call target RVA 0x{target_key:08X}\nSection: {target_record.get('section') if target_record else 'unknown'}",
                    "url": target_rel,
                }
            elif call.get("kind") == "import":
                node_id = "call_import_" + re.sub(r"[^A-Za-z0-9]", "_", str(call["display"]))[:80]
                external_graph_nodes[node_id] = {
                    "id": node_id, "kind": "call", "label": f"IMPORT\n{call['display']}",
                    "detail": f"Imported kernel dependency: {call['display']}",
                }
            elif call.get("target_rva") is not None:
                target_key = int(call["target_rva"])
                node_id = f"call_addr_{target_key:08X}"
                target_rel = None
                if target_key in report_paths:
                    target_rel = Path(os.path.relpath(report_paths[target_key]["path"], str(out / "viewer"))).as_posix()
                external_graph_nodes[node_id] = {
                    "id": node_id, "kind": "call", "label": f"CALL {call['display']}\n0x{target_key:08X}",
                    "detail": f"Resolved address: RVA 0x{target_key:08X}\nResolution: {call['kind']}",
                    "url": target_rel,
                }
            else:
                node_id = "call_indirect"
                external_graph_nodes[node_id] = {"id": node_id, "kind": "call", "label": "INDIRECT CALL", "detail": "Target depends on runtime register or memory state."}
            graph_edges.append({"source": f"bb_{source_rva:08X}", "target": node_id, "kind": "call"})
        graph_nodes.extend(external_graph_nodes.values())
        graph_bundle = {
            "name": function_label(record), "rva": f"0x{rva:08X}", "end": f"0x{end:08X}",
            "section": str(record.get("section", "unknown")), "blocks": len(blocks), "calls": len(calls),
            "report": Path(os.path.relpath(report_file, str(out / "viewer"))).as_posix(),
            "nodes": graph_nodes, "edges": graph_edges,
        }
        graph_bundles[section_slug][f"0x{rva:08X}"] = graph_bundle
        data_refs = sorted(data_ref_map.values(), key=lambda item: (int(item["site_rva"]), int(item["rva"])))
        viewer_link = f"../../../control-panel.html?section={section_slug}&rva=0x{rva:08X}&view=graph"
        graph_link = viewer_link
        report = make_report(
            record, instructions, blocks, cfg_edges, calls, transfers, data_refs,
            caller_map.get(rva, []), pe, capstone, x86, report_paths, function_names,
            imports_by_iat, report_file.parent, viewer_link, graph_link,
        )
        report_file.parent.mkdir(parents=True, exist_ok=True)
        legacy_report_file = report_file.with_name(f"function_{rva:08X}.md")
        if legacy_report_file != report_file and legacy_report_file.exists():
            legacy_report_file.unlink()
        report_file.write_text(report, encoding="utf-8", newline="\n")
        index_rows.append({
            "rva": rva, "rva_hex": f"0x{rva:08X}", "end_rva": end,
            "name": function_label(record), "section": record.get("section"),
            "report": report_paths[rva]["relative_path"], "blocks": len(blocks),
            "instructions": len(instructions), "has_pdb_name": bool(record.get("has_pdb_name")),
        })
        generated += 1
        if args.progress_every > 0 and generated % args.progress_every == 0:
            print(f"Generated {generated:,}/{len(records):,} reports", flush=True)

    # Build the reverse call edges once all functions have been analyzed, then
    # update reports so early RVA entries include callers discovered later.
    for rva, path_info in report_paths.items():
        report_file = Path(path_info["path"])
        report_text = report_file.read_text(encoding="utf-8")
        unique_callers = sorted({
            (int(item["caller_rva"]), int(item["site_rva"]))
            for item in caller_map.get(rva, [])
        })
        start_marker = "### Direct callers\n"
        end_marker = "\n### Static image references"
        start_at = report_text.find(start_marker)
        end_at = report_text.find(end_marker, start_at + len(start_marker)) if start_at >= 0 else -1
        if start_at < 0 or end_at < 0:
            continue
        replacement = [start_marker.rstrip("\n")]
        if unique_callers:
            for caller_rva, site_rva in unique_callers:
                if caller_rva in report_paths:
                    rel = Path(os.path.relpath(report_paths[caller_rva]["path"], str(report_file.parent))).as_posix()
                    label = html.escape(function_names.get(caller_rva, f"sub_{caller_rva:08X}"))
                    replacement.append(f"- [{label}]({rel}) at `0x{site_rva:08X}`")
                else:
                    replacement.append(f"- `0x{caller_rva:08X}` at `0x{site_rva:08X}`")
        else:
            replacement.append("- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.")
        report_text = report_text[:start_at] + "\n".join(replacement) + "\n" + report_text[end_at:]
        report_text = re.sub(
            r"(- 직접 호출자로 확인된 함수: \*\*)\d+(\*\*)",
            lambda match: match.group(1) + str(len({caller for caller, _site in unique_callers})) + match.group(2),
            report_text,
            count=1,
        )
        report_file.write_text(report_text, encoding="utf-8", newline="\n")

    graph_dir = out / "graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)
    for section_slug, graph_data in graph_bundles.items():
        target = graph_dir / f"{section_slug}.js"
        target.write_text(
            "window.NTOSKRNL_GRAPHS=" + json.dumps(graph_data, ensure_ascii=False, separators=(",", ":")) + ";\n",
            encoding="utf-8", newline="\n",
        )
    viewer_dir = out / "viewer"
    viewer_dir.mkdir(parents=True, exist_ok=True)
    (viewer_dir / "index.html").write_text(VIEWER_HTML, encoding="utf-8", newline="\n")

    for target_rva, items in caller_map.items():
        unique = {(int(item["caller_rva"]), int(item["site_rva"])) for item in items}
        caller_map[target_rva] = [
            {"caller_rva": crva, "site_rva": site} for crva, site in sorted(unique)
        ]

    (out / "function-index.json").write_text(
        json.dumps(index_rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    (out / "data").mkdir(parents=True, exist_ok=True)
    bundled_index = out / "data" / "all_executable_functions.json"
    if args.index != bundled_index.resolve():
        shutil.copy2(args.index, bundled_index)
    if Path(__file__).resolve() != (out / "build_reports.py").resolve():
        shutil.copy2(Path(__file__).resolve(), out / "build_reports.py")
    (out / "viewer" / "README.md").write_text(
        "# Interactive graph viewer\n\nOpen a function report and follow its graph link. The viewer supports mouse-wheel zoom, drag-to-pan, fit-to-view, node selection, and links from function-call nodes to reports. The graph data is bundled as local JavaScript by executable section, so no network or server is required.\n",
        encoding="utf-8", newline="\n",
    )
    (out / "generate_all.ps1").write_text(
        "$ErrorActionPreference = 'Stop'\n"
        "$exe = 'C:\\Windows\\System32\\ntoskrnl.exe'\n"
        "python (Join-Path $PSScriptRoot 'build_reports.py') --exe $exe\n"
        "if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }\n"
        "python (Join-Path $PSScriptRoot 'add_beta_style.py') --exe $exe\n"
        "if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }\n"
        "python (Join-Path $PSScriptRoot 'build_control_panel.py')\n"
        "exit $LASTEXITCODE\n",
        encoding="utf-8", newline="\n",
    )
    sha256 = hashlib.sha256(args.exe.read_bytes()).hexdigest()
    summary = {
        "image": str(args.exe), "image_sha256": sha256,
        "pdb": index_data.get("pdb"), "function_reports_generated": generated,
        "inventory_functions": len(records), "total_instructions_decoded": total_instructions,
        "total_cfg_blocks": total_cfg_blocks,
        "functions_with_skipdata_bytes": functions_with_skipdata,
        "skipdata_bytes": total_skipdata_bytes,
        "functions_without_pdb_names": int(index_data.get("counts", {}).get("runtime_function_records_without_pdb_symbol_name", 0)),
        "additional_code_symbol_candidates_not_promoted_to_functions": int(index_data.get("counts", {}).get("additional_code_symbol_candidates_without_unwind_start", 0)),
        "decode_failures": decode_failures,
        "leaf_and_stripped_function_limit": index_data.get("completeness_note", ""),
    }
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    section_counts = collections.Counter(str(row["section"]) for row in index_rows)
    readme = [
        "# ntoskrnl.exe → C-style analysis reports", "",
        f"이 프로젝트는 `{args.exe}`에서 추출한 x64 `RUNTIME_FUNCTION` 실행 범위 **{generated:,}개**를 각각 Markdown 보고서로 정리합니다.",
        "", "## 보고서 구성", "",
        "각 함수 보고서에는 다음 항목이 있습니다.",
        "", "1. Dependencies: 직접 호출 대상·호출자·RIP-relative 이미지 참조",
        "2. 다른 실행 섹션 호출 및 함수 범위 밖 분기",
        "3. 전체 범위 디스어셈블 어셈블리",
        "4. 레지스터와 플래그를 보존한 C식 의사코드",
        "5. (Beta) C Style: 폭이 명시된 두 번째 C 해석",
        "6. 2D 세로 흐름·3D 회전·함수 호출 노드를 제공하는 CFG 그래프", "",
        "## 범위와 해석 한계", "",
        "이 보고서는 바이너리와 PDB 기호를 정적으로 분석합니다. 디컴파일은 ABI 인자, 스택 인자, 메모리 접근 폭, 단순 조건 분기를 추정하며 단순 if/then 흐름을 구조화합니다. 복잡한 루프, 간접 분기, 벡터 상태는 원본 C와 동일하다고 보장할 수 없고 모든 명령은 어셈블리에서 확인할 수 있습니다. 헤더나 유저 모드 전제를 사용하지 않습니다.",
        "", "x64 leaf 함수는 unwind 테이블에 기록되지 않을 수 있습니다. 이름이나 unwind 시작이 없는 코드 조각은 함수인지 라벨인지 확정할 수 없어 이 37,994개 집계에 임의 추가하지 않았습니다. `data/all_executable_functions.json`에는 별도 후보 6,108개가 보존되어 있습니다.",
        "", "## 사용", "",
        "- 시작: `index.md`에서 실행 섹션별 목록을 연 뒤 RVA를 선택합니다.",
        "- 검색: `function-index.json`을 검색하거나 보고서 파일명에서 RVA를 찾습니다.",
        "- 그래프: 컨트롤 패널에서 2D 세로 흐름 또는 3D 회전 화면을 선택합니다. 2D는 드래그 이동, 3D는 드래그 회전과 Shift+드래그 이동을 지원합니다.",
        "- 전체 재생성: `generate_all.ps1` 실행. Python과 Capstone이 필요합니다 (`python -m pip install capstone`).", "",
        "## 실행 섹션별 보고서 수", "", "| PE 실행 섹션 | 보고서 |", "|---|---:|",
    ]
    for section, count in sorted(section_counts.items()):
        readme.append(f"| `{section}` | {count:,} |")
    readme.extend(["", f"디코드 항목: **{total_instructions:,}** · CFG basic blocks: **{total_cfg_blocks:,}** · 미해석 바이트: **{total_skipdata_bytes:,} bytes / {functions_with_skipdata:,} 함수**", ""])
    (out / "README.md").write_text("\n".join(readme), encoding="utf-8", newline="\n")
    index_md = ["# Function report index", "", f"Total: **{generated:,}**", ""]
    for section, _count in sorted(section_counts.items()):
        section_slug = slug(section)
        index_md.extend([f"## `{section}`", ""])
        for row in index_rows:
            if row["section"] == section:
                shard = f"{(int(row['rva']) >> 16) & 0xFF:02X}"
                rel = row["report"]
                label = html.escape(str(row["name"]).replace("|", "\\|"))
                index_md.append(f"- [`{row['rva_hex']}` — {label}]({rel})")
        index_md.append("")
    (out / "index.md").write_text("\n".join(index_md), encoding="utf-8", newline="\n")
    print(f"Complete: {generated:,} Markdown function reports")
    print(f"Instructions: {total_instructions:,}; CFG blocks: {total_cfg_blocks:,}; decode failures: {len(decode_failures):,}")
    print(f"Output: {out}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
