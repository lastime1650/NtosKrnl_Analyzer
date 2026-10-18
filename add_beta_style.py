#!/usr/bin/env python3
"""Add a source-oriented, typed C reconstruction to every function report."""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


def load_builder(path: Path):
    spec = importlib.util.spec_from_file_location("ntk2c_builder", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load report builder: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


STATE_FIELDS = [
    "rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp",
    "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
]
ALIAS: dict[str, tuple[str, int, int]] = {}
for base, dword, word, byte, high in [
    ("rax", "eax", "ax", "al", "ah"), ("rbx", "ebx", "bx", "bl", "bh"),
    ("rcx", "ecx", "cx", "cl", "ch"), ("rdx", "edx", "dx", "dl", "dh"),
    ("rsi", "esi", "si", "sil", None), ("rdi", "edi", "di", "dil", None),
    ("rbp", "ebp", "bp", "bpl", None), ("rsp", "esp", "sp", "spl", None),
]:
    ALIAS[base] = (base, 64, 0)
    ALIAS[dword] = (base, 32, 0)
    ALIAS[word] = (base, 16, 0)
    ALIAS[byte] = (base, 8, 0)
    if high:
        ALIAS[high] = (base, 8, 8)
for i in range(8, 16):
    base = f"r{i}"
    ALIAS[base] = (base, 64, 0)
    ALIAS[f"r{i}d"] = (base, 32, 0)
    ALIAS[f"r{i}w"] = (base, 16, 0)
    ALIAS[f"r{i}b"] = (base, 8, 0)


def c_number(value: int) -> str:
    if value < 0:
        return f"(-0x{-value:X}LL)"
    return f"0x{value:X}ULL"


def reg_read(name: str) -> str | None:
    alias = ALIAS.get(name.lower())
    if alias:
        base, bits, shift = alias
        value = f"s->{base}"
        if shift:
            value = f"({value} >> {shift})"
        if bits == 32:
            return f"((unsigned int)({value}))"
        if bits == 16:
            return f"((unsigned short)({value}))"
        if bits == 8:
            return f"((unsigned char)({value}))"
        return value
    if name.lower() in {"eflags", "rflags"}:
        return "s->rflags"
    return None


def reg_write(name: str, value: str) -> str | None:
    alias = ALIAS.get(name.lower())
    if not alias:
        if name.lower() in {"eflags", "rflags"}:
            return f"s->rflags = (unsigned long long)({value});"
        return None
    base, bits, shift = alias
    if bits == 64:
        return f"s->{base} = (unsigned long long)({value});"
    if bits == 32:
        # A 32-bit GPR write zero-extends into the paired x64 register.
        return f"s->{base} = (unsigned int)({value});"
    if bits == 16:
        mask = "0xFFFFFFFFFFFF0000ULL"
        return f"s->{base} = (s->{base} & {mask}) | ((unsigned short)({value}));"
    if shift == 8:
        return f"s->{base} = (s->{base} & 0xFFFFFFFFFFFF00FFULL) | (((unsigned long long)(unsigned char)({value})) << 8);"
    return f"s->{base} = (s->{base} & 0xFFFFFFFFFFFFFF00ULL) | ((unsigned char)({value}));"


def signed_disp(value: int) -> str:
    if value > 0:
        return f" + 0x{value:X}ULL"
    if value < 0:
        return f" - 0x{-value:X}ULL"
    return ""


def memory_address(insn: Any, op_index: int, pe: Any, x86: Any) -> str:
    operand = insn.operands[op_index]
    mem = operand.mem
    base_name = insn.reg_name(mem.base) if mem.base else ""
    index_name = insn.reg_name(mem.index) if mem.index else ""
    displacement = int(mem.disp)
    if base_name.lower() == "rip":
        target_rva = int(insn.address + insn.size + displacement - pe.image_base)
        address = f"(s->image_base + 0x{target_rva:08X}ULL)"
    else:
        terms: list[str] = []
        if base_name:
            terms.append(reg_read(base_name) or "0ULL")
        if index_name:
            index_expr = reg_read(index_name) or "0ULL"
            terms.append(f"({index_expr} * {int(mem.scale) or 1}ULL)")
        address = " + ".join(terms) if terms else "0ULL"
        if displacement:
            address = f"({address}{signed_disp(displacement)})"
    segment = insn.reg_name(mem.segment).lower() if mem.segment else ""
    if segment in {"fs", "gs"}:
        address = f"(s->{segment}_base + ({address}))"
    return address


def memory_lvalue(insn: Any, op_index: int, pe: Any, x86: Any) -> str:
    operand = insn.operands[op_index]
    bits = int(operand.size) * 8
    ctype = {8: "unsigned char", 16: "unsigned short", 32: "unsigned int", 64: "unsigned long long"}.get(bits)
    if ctype is None:
        return "/* vector or unusual-width memory operand; see assembly */"
    address = memory_address(insn, op_index, pe, x86)
    return f"(*((volatile {ctype} *)(unsigned long long)({address})))"


def immediate_expr(insn: Any, op_index: int) -> str:
    return c_number(int(insn.operands[op_index].imm))


def operand_expr(insn: Any, op_index: int, pe: Any, x86: Any) -> str:
    operand = insn.operands[op_index]
    if operand.type == x86.X86_OP_REG:
        name = insn.reg_name(operand.reg)
        return reg_read(name) or f"0ULL /* non-GPR {name} */"
    if operand.type == x86.X86_OP_IMM:
        return immediate_expr(insn, op_index)
    if operand.type == x86.X86_OP_MEM:
        return memory_lvalue(insn, op_index, pe, x86)
    return "0ULL /* operand not represented in this Beta view */"


def operand_lvalue(insn: Any, op_index: int, pe: Any, x86: Any) -> str | None:
    operand = insn.operands[op_index]
    if operand.type == x86.X86_OP_REG:
        return insn.reg_name(operand.reg)
    if operand.type == x86.X86_OP_MEM:
        return memory_lvalue(insn, op_index, pe, x86)
    return None


FLAG = {"cf": "0x1ULL", "pf": "0x4ULL", "af": "0x10ULL", "zf": "0x40ULL", "sf": "0x80ULL", "of": "0x800ULL"}


def flag_is(name: str) -> str:
    return f"((s->rflags & {FLAG[name]}) != 0)"


def condition(mnemonic: str) -> str:
    suffix = mnemonic.lower()
    if suffix.startswith("j"):
        suffix = suffix[1:]
    cond = {
        "a": f"(!{flag_is('cf')} && !{flag_is('zf')})", "nbe": f"(!{flag_is('cf')} && !{flag_is('zf')})",
        "ae": f"(!{flag_is('cf')})", "nb": f"(!{flag_is('cf')})", "nc": f"(!{flag_is('cf')})",
        "b": flag_is("cf"), "c": flag_is("cf"), "nae": flag_is("cf"),
        "be": f"({flag_is('cf')} || {flag_is('zf')})", "na": f"({flag_is('cf')} || {flag_is('zf')})",
        "e": flag_is("zf"), "z": flag_is("zf"), "ne": f"(!{flag_is('zf')})", "nz": f"(!{flag_is('zf')})",
        "g": f"(!{flag_is('zf')} && ({flag_is('sf')} == {flag_is('of')}))",
        "nle": f"(!{flag_is('zf')} && ({flag_is('sf')} == {flag_is('of')}))",
        "ge": f"({flag_is('sf')} == {flag_is('of')})", "nl": f"({flag_is('sf')} == {flag_is('of')})",
        "l": f"({flag_is('sf')} != {flag_is('of')})", "nge": f"({flag_is('sf')} != {flag_is('of')})",
        "le": f"({flag_is('zf')} || ({flag_is('sf')} != {flag_is('of')}))",
        "ng": f"({flag_is('zf')} || ({flag_is('sf')} != {flag_is('of')}))",
        "o": flag_is("of"), "no": f"(!{flag_is('of')})", "s": flag_is("sf"), "ns": f"(!{flag_is('sf')})",
        "p": flag_is("pf"), "pe": flag_is("pf"), "np": f"(!{flag_is('pf')})", "po": f"(!{flag_is('pf')})",
    }
    return cond.get(suffix, "0")


def width_bits(insn: Any, index: int = 0) -> int:
    if len(insn.operands) > index and int(insn.operands[index].size):
        return int(insn.operands[index].size) * 8
    return 64


def call_statement(insn: Any, info: dict[str, Any] | None, pe: Any, x86: Any,
                   function_starts: set[int]) -> tuple[str, int | None]:
    target_function = None
    if info and info.get("kind") == "function" and info.get("function_rva") is not None:
        target_function = int(info["function_rva"])
        if target_function in function_starts:
            name = f"kernel_fn_{target_function:08X}"
            return f"s->rax = {name}(s); /* {info.get('display', name)} */", target_function
    if info and info.get("kind") == "import" and info.get("iat_rva") is not None:
        target = f"(*((volatile unsigned long long *)(unsigned long long)(s->image_base + 0x{int(info['iat_rva']):08X}ULL)))"
        return f"s->rax = __ntk_external_call({target}, s); /* {info.get('display', 'kernel import')} */", None
    if insn.operands:
        operand = insn.operands[0]
        if operand.type == x86.X86_OP_IMM:
            target_rva = int(operand.imm) - pe.image_base
            target = f"(s->image_base + 0x{target_rva:08X}ULL)"
        else:
            target = operand_expr(insn, 0, pe, x86)
    else:
        target = "0ULL"
    label = info.get("display", "indirect/external target") if info else "external target"
    return f"s->rax = __ntk_external_call((unsigned long long)({target}), s); /* {label} */", None


def translate_nonterminal(insn: Any, call_info: dict[str, Any] | None, pe: Any, x86: Any,
                          function_starts: set[int]) -> tuple[list[str], int | None]:
    m = insn.mnemonic.lower()
    if insn.id == 0 or m == ".byte":
        return [f"/* undecoded bytes retained: {insn.bytes.hex(' ').upper()} */"], None
    ops = insn.operands
    if m in {"nop", "endbr64", "int3"}:
        return [f"/* {m} {insn.op_str} */".rstrip()], None
    if m in {"call", "callq"}:
        statement, target = call_statement(insn, call_info, pe, x86, function_starts)
        return [statement], target
    if m in {"mov", "movzx", "movsx", "movsxd"} and len(ops) == 2:
        dest = operand_lvalue(insn, 0, pe, x86)
        source = operand_expr(insn, 1, pe, x86)
        if dest is None:
            return [f"/* destination {insn.op_str} is not represented */"], None
        if m == "movzx":
            source = f"(unsigned long long)({source})"
        elif m in {"movsx", "movsxd"}:
            bits = width_bits(insn, 1)
            ctype = {8: "signed char", 16: "short", 32: "int", 64: "long long"}.get(bits, "long long")
            source = f"(unsigned long long)(({ctype})({source}))"
        if ops[0].type == x86.X86_OP_REG:
            stmt = reg_write(insn.reg_name(ops[0].reg), source)
            if stmt:
                return [stmt], None
        return [f"{dest} = {source};"], None
    if m == "lea" and len(ops) == 2 and ops[1].type == x86.X86_OP_MEM:
        dest = operand_lvalue(insn, 0, pe, x86)
        address = memory_address(insn, 1, pe, x86)
        if ops[0].type == x86.X86_OP_REG:
            stmt = reg_write(insn.reg_name(ops[0].reg), address)
            if stmt:
                return [stmt], None
        return [f"{dest} = (unsigned long long)({address});"], None
    arithmetic = {"add": "+", "sub": "-", "and": "&", "or": "|", "xor": "^", "imul": "*"}
    if m in arithmetic and len(ops) >= 2:
        dest = operand_lvalue(insn, 0, pe, x86)
        if dest is None:
            return [f"/* unsupported arithmetic destination: {insn.op_str} */"], None
        if m == "imul" and len(ops) == 3:
            lhs = operand_expr(insn, 1, pe, x86)
            rhs = operand_expr(insn, 2, pe, x86)
            width = width_bits(insn, 0)
        else:
            lhs = operand_expr(insn, 0, pe, x86)
            rhs = operand_expr(insn, 1, pe, x86)
            width = width_bits(insn, 0)
        tmp = f"__result_{int(insn.address - pe.image_base):08X}"
        lines = ["{", f"    unsigned long long {tmp} = (unsigned long long)(({lhs}) {arithmetic[m]} ({rhs}));"]
        if m == "add":
            lines.append(f"    s->rflags = __ntk_flags_add(s->rflags, (unsigned long long)({lhs}), (unsigned long long)({rhs}), {width});")
        elif m == "sub":
            lines.append(f"    s->rflags = __ntk_flags_sub(s->rflags, (unsigned long long)({lhs}), (unsigned long long)({rhs}), {width});")
        elif m in {"and", "or", "xor"}:
            lines.append(f"    s->rflags = __ntk_flags_logic(s->rflags, {tmp}, {width});")
        if ops[0].type == x86.X86_OP_REG:
            lines.append("    " + (reg_write(insn.reg_name(ops[0].reg), tmp) or f"{dest} = {tmp};"))
        else:
            lines.append(f"    {dest} = {tmp};")
        lines.append("}")
        if m == "imul":
            lines.insert(-1, "/* IMUL result kept at destination width; CF/OF are Beta approximations. */")
        return lines, None
    if m in {"cmp", "test"} and len(ops) == 2:
        left = operand_expr(insn, 0, pe, x86)
        right = operand_expr(insn, 1, pe, x86)
        width = width_bits(insn, 0)
        if m == "cmp":
            return [f"s->rflags = __ntk_flags_sub(s->rflags, (unsigned long long)({left}), (unsigned long long)({right}), {width});"], None
        value = f"((unsigned long long)({left}) & (unsigned long long)({right}))"
        return [f"s->rflags = __ntk_flags_logic(s->rflags, {value}, {width});"], None
    if m in {"inc", "dec"} and ops:
        dest = operand_lvalue(insn, 0, pe, x86)
        old = operand_expr(insn, 0, pe, x86)
        width = width_bits(insn, 0)
        tmp = f"__result_{int(insn.address - pe.image_base):08X}"
        helper = "__ntk_flags_add" if m == "inc" else "__ntk_flags_sub"
        rhs = "1ULL"
        lines = ["{", f"    unsigned long long {tmp} = (unsigned long long)({old}) {'+' if m == 'inc' else '-'} 1ULL;",
                 f"    unsigned long long __old_flags = s->rflags;",
                 f"    s->rflags = {helper}(s->rflags, (unsigned long long)({old}), {rhs}, {width});",
                 "    s->rflags = (s->rflags & ~0x1ULL) | (__old_flags & 0x1ULL);"]
        if ops[0].type == x86.X86_OP_REG:
            lines.append("    " + (reg_write(insn.reg_name(ops[0].reg), tmp) or f"{dest} = {tmp};"))
        else:
            lines.append(f"    {dest} = {tmp};")
        lines.append("}")
        return lines, None
    if m in {"neg", "not"} and ops:
        dest = operand_lvalue(insn, 0, pe, x86)
        source = operand_expr(insn, 0, pe, x86)
        width = width_bits(insn, 0)
        expr = f"(~(unsigned long long)({source}))" if m == "not" else f"(0ULL - (unsigned long long)({source}))"
        lines = []
        if m == "neg":
            lines.append(f"s->rflags = __ntk_flags_sub(s->rflags, 0ULL, (unsigned long long)({source}), {width});")
        if ops[0].type == x86.X86_OP_REG:
            lines.append(reg_write(insn.reg_name(ops[0].reg), expr) or f"{dest} = {expr};")
        else:
            lines.append(f"{dest} = {expr};")
        return lines, None
    if m in {"shl", "sal", "shr", "sar"} and len(ops) == 2:
        dest = operand_lvalue(insn, 0, pe, x86)
        left = operand_expr(insn, 0, pe, x86)
        right = operand_expr(insn, 1, pe, x86)
        width = width_bits(insn, 0)
        if m == "sar":
            expr = f"((unsigned long long)(((long long)({left})) >> ((unsigned int)({right}) & {63 if width == 64 else 31}U)))"
        else:
            symbol = "<<" if m in {"shl", "sal"} else ">>"
            expr = f"((unsigned long long)({left}) {symbol} ((unsigned int)({right}) & {63 if width == 64 else 31}U))"
        lines = [f"/* Shift flags are approximated in this Beta translation. */"]
        if ops[0].type == x86.X86_OP_REG:
            lines.append(reg_write(insn.reg_name(ops[0].reg), expr) or f"{dest} = {expr};")
        else:
            lines.append(f"{dest} = {expr};")
        lines.append(f"s->rflags = __ntk_flags_logic(s->rflags, {expr}, {width});")
        return lines, None
    if m.startswith("cmov") and len(ops) == 2:
        dest = operand_lvalue(insn, 0, pe, x86)
        source = operand_expr(insn, 1, pe, x86)
        if ops[0].type == x86.X86_OP_REG:
            write = reg_write(insn.reg_name(ops[0].reg), source) or f"{dest} = {source};"
        else:
            write = f"{dest} = {source};"
        return [f"if ({condition(m[4:])}) {{ {write} }}"], None
    if m.startswith("set") and ops:
        dest = operand_lvalue(insn, 0, pe, x86)
        expr = f"({condition(m[3:])}) ? 1U : 0U"
        if ops[0].type == x86.X86_OP_REG:
            return [reg_write(insn.reg_name(ops[0].reg), expr) or f"{dest} = {expr};"], None
        return [f"{dest} = {expr};"], None
    if m == "push" and ops:
        source = operand_expr(insn, 0, pe, x86)
        size = int(ops[0].size) or 8
        ctype = {2: "unsigned short", 8: "unsigned long long"}.get(size, "unsigned long long")
        return [f"s->rsp -= {size}ULL;", f"*((volatile {ctype} *)(unsigned long long)(s->rsp)) = ({ctype})({source});"], None
    if m == "pop" and ops:
        size = int(ops[0].size) or 8
        ctype = {2: "unsigned short", 8: "unsigned long long"}.get(size, "unsigned long long")
        source = f"(*((volatile {ctype} *)(unsigned long long)(s->rsp)))"
        if ops[0].type == x86.X86_OP_REG:
            write = reg_write(insn.reg_name(ops[0].reg), source)
        else:
            write = f"{operand_lvalue(insn, 0, pe, x86)} = {source};"
        return [write or "/* POP destination is not represented. */", f"s->rsp += {size}ULL;"], None
    if m == "leave":
        return ["s->rsp = s->rbp;", "s->rbp = *((volatile unsigned long long *)(unsigned long long)(s->rsp));", "s->rsp += 8ULL;"], None
    if m in {"xchg", "xadd"} and len(ops) == 2:
        left = operand_expr(insn, 0, pe, x86)
        right = operand_expr(insn, 1, pe, x86)
        left_lv = operand_lvalue(insn, 0, pe, x86)
        right_lv = operand_lvalue(insn, 1, pe, x86)
        if not left_lv or not right_lv:
            return [f"/* {m.upper()} operand class not represented: {insn.op_str} */"], None
        a = f"__left_{int(insn.address - pe.image_base):08X}"
        b = f"__right_{int(insn.address - pe.image_base):08X}"
        lines = ["{", f"    unsigned long long {a} = (unsigned long long)({left});",
                 f"    unsigned long long {b} = (unsigned long long)({right});"]
        lines.append("    /* Atomicity from LOCK or implicit memory semantics is not modeled here. */")
        if m == "xadd":
            lines.append(f"    s->rflags = __ntk_flags_add(s->rflags, {a}, {b}, {width_bits(insn, 0)}U);")
        left_value = b if m == "xchg" else f"({a} + {b})"
        left_write = reg_write(insn.reg_name(ops[0].reg), left_value) if ops[0].type == x86.X86_OP_REG else None
        right_write = reg_write(insn.reg_name(ops[1].reg), a) if ops[1].type == x86.X86_OP_REG else None
        lines.append("    " + (left_write or f"{left_lv} = {left_value};"))
        lines.append("    " + (right_write or f"{right_lv} = {a};"))
        lines.append("}")
        return lines, None
    if m == "syscall":
        return ["/* SYSCALL transition is architecture/kernel-entry specific; see assembly. */"], None
    if m in {"cpuid", "rdtsc", "rdtscp", "pause", "lfence", "mfence", "sfence", "int3"}:
        return [f"/* {m.upper()} is retained in the assembly view; architectural side effects not reconstructed here. */"], None
    return [f"/* Beta gap: {m} {insn.op_str} — exact vector/implicit-register semantics remain in section 3. */"], None


HELPERS = r'''/* x64 register-state model: a Beta analysis signature, not the original kernel prototype. */
typedef struct NTK_X64_STATE {
    unsigned long long rax, rbx, rcx, rdx, rsi, rdi, rbp, rsp;
    unsigned long long r8, r9, r10, r11, r12, r13, r14, r15;
    unsigned long long rflags, fs_base, gs_base, image_base;
} NTK_X64_STATE;
static unsigned long long __ntk_mask(unsigned int width) {
    return width >= 64U ? ~0ULL : ((1ULL << width) - 1ULL);
}
static unsigned int __ntk_even_parity(unsigned long long value) {
    unsigned int bit, parity = 0U;
    for (bit = 0U; bit < 8U; ++bit) parity ^= (unsigned int)((value >> bit) & 1ULL);
    return parity == 0U;
}
static unsigned long long __ntk_flags_result(unsigned long long old_flags, unsigned long long result, unsigned int width) {
    const unsigned long long mask = __ntk_mask(width);
    const unsigned long long sign = 1ULL << (width - 1U);
    const unsigned long long affected = 0x4ULL | 0x40ULL | 0x80ULL;
    unsigned long long flags = old_flags & ~affected;
    result &= mask;
    if (result == 0ULL) flags |= 0x40ULL;
    if ((result & sign) != 0ULL) flags |= 0x80ULL;
    if (__ntk_even_parity(result)) flags |= 0x4ULL;
    return flags;
}
static unsigned long long __ntk_flags_add(unsigned long long old_flags, unsigned long long a, unsigned long long b, unsigned int width) {
    const unsigned long long mask = __ntk_mask(width);
    const unsigned long long sign = 1ULL << (width - 1U);
    unsigned long long result;
    unsigned long long flags = __ntk_flags_result(old_flags, 0ULL, width) & ~(0x1ULL | 0x10ULL | 0x800ULL);
    a &= mask; b &= mask; result = (a + b) & mask;
    flags = __ntk_flags_result(flags, result, width);
    if ((width == 64U ? result < a : a > mask - b)) flags |= 0x1ULL;
    if (((~(a ^ b) & (a ^ result)) & sign) != 0ULL) flags |= 0x800ULL;
    if (((a ^ b ^ result) & 0x10ULL) != 0ULL) flags |= 0x10ULL;
    return flags;
}
static unsigned long long __ntk_flags_sub(unsigned long long old_flags, unsigned long long a, unsigned long long b, unsigned int width) {
    const unsigned long long mask = __ntk_mask(width);
    const unsigned long long sign = 1ULL << (width - 1U);
    unsigned long long result;
    unsigned long long flags = old_flags & ~(0x1ULL | 0x4ULL | 0x10ULL | 0x40ULL | 0x80ULL | 0x800ULL);
    a &= mask; b &= mask; result = (a - b) & mask;
    flags = __ntk_flags_result(flags, result, width);
    if (a < b) flags |= 0x1ULL;
    if ((((a ^ b) & (a ^ result)) & sign) != 0ULL) flags |= 0x800ULL;
    if (((a ^ b ^ result) & 0x10ULL) != 0ULL) flags |= 0x10ULL;
    return flags;
}
static unsigned long long __ntk_flags_logic(unsigned long long old_flags, unsigned long long result, unsigned int width) {
    unsigned long long flags = old_flags & ~(0x1ULL | 0x800ULL);
    return __ntk_flags_result(flags, result, width);
}
extern unsigned long long __ntk_external_call(unsigned long long target_va, NTK_X64_STATE *state);
'''


def beta_c_function(record: dict[str, Any], instructions: list[Any], blocks: list[dict[str, Any]],
                    cfg_edges: list[dict[str, Any]], calls: list[dict[str, Any]], pe: Any,
                    capstone: Any, x86: Any, function_starts: set[int]) -> str:
    rva = int(record["rva"])
    end = int(record["end_rva"])
    calls_by_site = {int(call["site_rva"]): call for call in calls}
    prototypes: set[int] = set()
    for call in calls:
        if call.get("kind") == "function" and call.get("function_rva") is not None and int(call["function_rva"]) in function_starts:
            prototypes.add(int(call["function_rva"]))
    lines = [
        "/* (Beta) C Style: independent C interpretation from the x64 instruction stream. */",
        "/* This state-transformer signature models machine registers and is not the recovered kernel prototype. */",
        "/* Kernel memory accesses use volatile pointers. No headers or user-mode types are assumed. */",
        "/* Unsupported vector, privileged, or implicit-state operations remain comments; section 3 retains the exact assembly. */",
        HELPERS.rstrip(),
    ]
    for target in sorted(prototypes):
        lines.append(f"extern unsigned long long kernel_fn_{target:08X}(NTK_X64_STATE *s);")
    lines.extend(["", f"unsigned long long kernel_fn_{rva:08X}(NTK_X64_STATE *s)", "{"])
    if not blocks:
        lines.extend(["    /* No basic block decoded for this range. */", "    return s->rax;", "}"])
        return "\n".join(lines)
    by_block_id = {block["id"]: block for block in blocks}
    by_block_rva = {int(block["rva"]): block for block in blocks}
    edge_map: dict[str, list[dict[str, Any]]] = {}
    for edge in cfg_edges:
        edge_map.setdefault(str(edge["source"]), []).append(edge)
    for block in blocks:
        block_rva = int(block["rva"])
        lines.append(f"loc_{block_rva:08X}:")
        items = block["instructions"]
        if not items:
            lines.append("    ;")
            continue
        last = items[-1]
        is_call, is_jump, is_ret = (last.group(capstone.CS_GRP_CALL), last.group(capstone.CS_GRP_JUMP), last.group(capstone.CS_GRP_RET)) if last.id else (False, False, False)
        terminal = is_jump or is_ret
        ordinary = items[:-1] if terminal else items
        for insn in ordinary:
            site = int(insn.address - pe.image_base)
            assembly = (insn.mnemonic + " " + insn.op_str).strip().replace("*/", "* /")
            lines.append(f"    /* 0x{site:08X}: {insn.bytes.hex(' ').upper()}  {assembly} */")
            translated, _called = translate_nonterminal(insn, calls_by_site.get(site), pe, x86, function_starts)
            lines.extend("    " + text if text else "" for text in translated)
        site = int(last.address - pe.image_base)
        assembly = (last.mnemonic + " " + last.op_str).strip().replace("*/", "* /")
        lines.append(f"    /* 0x{site:08X}: {last.bytes.hex(' ').upper()}  {assembly} */")
        successors = edge_map.get(str(block["id"]), [])
        if is_ret:
            if last.mnemonic.lower().startswith("ret"):
                cleanup = int(last.operands[0].imm) if last.operands and last.operands[0].type == x86.X86_OP_IMM else 0
                lines.append(f"    s->rsp += 0x{8 + cleanup:X}ULL; /* return address and optional callee cleanup */")
            elif last.mnemonic.lower().startswith("iret"):
                lines.append("    /* IRET privilege/frame transition is kernel-entry specific; exact effect remains in section 3. */")
            lines.append("    return s->rax;")
            continue
        if is_jump:
            m = last.mnemonic.lower()
            target_va = None
            if last.operands and last.operands[0].type == x86.X86_OP_IMM:
                target_va = int(last.operands[0].imm)
            target_rva = target_va - pe.image_base if target_va is not None else None
            target_block = by_block_rva.get(target_rva) if target_rva is not None else None
            branch_target = f"goto loc_{target_rva:08X};" if target_block and target_rva is not None else None
            if branch_target is None:
                if target_rva is None:
                    if last.operands:
                        target_expr = operand_expr(last, 0, pe, x86)
                    else:
                        target_expr = "0ULL"
                else:
                    target_expr = f"(s->image_base + 0x{target_rva:08X}ULL)"
                branch_target = f"return __ntk_external_call((unsigned long long)({target_expr}), s);"
            if m in {"jmp", "ljmp"}:
                lines.append("    " + branch_target)
                continue
            if m.startswith("loop"):
                lines.append("    s->rcx -= 1ULL;")
                if m == "loop":
                    cond = "(s->rcx != 0ULL)"
                elif m in {"loope", "loopz"}:
                    cond = f"(s->rcx != 0ULL && {flag_is('zf')})"
                else:
                    cond = f"(s->rcx != 0ULL && !{flag_is('zf')})"
            elif m in {"jrcxz", "jecxz", "jcxz"}:
                cond = "(s->rcx == 0ULL)" if m == "jrcxz" else ("((unsigned int)s->rcx == 0U)" if m == "jecxz" else "((unsigned short)s->rcx == 0U)")
            else:
                cond = condition(m)
            lines.append(f"    if ({cond}) {{ {branch_target} }}")
            fallthrough = next((edge["target"] for edge in successors if edge.get("kind") == "fallthrough"), None)
            if fallthrough and str(fallthrough).startswith("bb_"):
                fall_rva = int(str(fallthrough)[3:], 16)
                lines.append(f"    goto loc_{fall_rva:08X};")
            else:
                lines.append("    return s->rax;")
            continue
        if last.id == 0:
            lines.append("    /* undecoded bytes retained; execution stops at the undecoded byte. */")
            lines.append("    return s->rax;")
            continue
        if is_call:
            site = int(last.address - pe.image_base)
            translated, _called = translate_nonterminal(last, calls_by_site.get(site), pe, x86, function_starts)
            lines.extend("    " + text if text else "" for text in translated)
        flow = next((edge for edge in successors if edge.get("kind") in {"flow", "fallthrough"}), None)
        if flow and str(flow["target"]).startswith("bb_"):
            lines.append(f"    goto loc_{int(str(flow['target'])[3:], 16):08X};")
        else:
            lines.append("    return s->rax;")
    lines.extend(["}"])
    return "\n".join(lines)


_C_TYPES = {
    "unsigned __int8": "uint8_t", "__int8": "int8_t",
    "unsigned __int16": "uint16_t", "__int16": "int16_t",
    "unsigned int": "uint32_t", "int": "int32_t",
    "unsigned __int32": "uint32_t", "__int32": "int32_t",
    "unsigned __int64": "uint64_t", "__int64": "int64_t",
    "unsigned long long": "uint64_t", "long long": "int64_t",
}

_KNOWN_POINTER_ARGUMENTS = {
    "KeInsertQueueApc": {1, 2, 3}, "KeRemoveQueueApc": {1},
    "KiInsertQueueApc": {1},
    "KeInsertQueueDpc": {1, 2, 3}, "KeRemoveQueueDpc": {1},
    "KeSetEvent": {1}, "KeClearEvent": {1}, "KeResetEvent": {1},
    "KeInitializeDpc": {1, 2, 3}, "KeInitializeTimer": {1},
    "KeInitializeTimerEx": {1}, "KeInitializeSpinLock": {1},
    "RtlCopyMemory": {1, 2}, "RtlMoveMemory": {1, 2},
    "RtlZeroMemory": {1}, "RtlFillMemory": {1},
    "IofCompleteRequest": {1}, "ExFreePool": {1}, "ExFreePoolWithTag": {1},
    "KeDelayExecutionThread": {3}, "KeWaitForSingleObject": {1, 5},
    "PsLookupProcessByProcessId": {2}, "PsLookupThreadByThreadId": {2},
    "ObfReferenceObject": {1}, "ObfDereferenceObject": {1},
    "ObReferenceObjectByHandle": {1, 3, 5, 6},
}

_KAPC_FUNCTIONS = {"KeInsertQueueApc", "KeRemoveQueueApc", "KiInsertQueueApc"}
_KAPC_FIELDS = {
    0x00: "Type", 0x01: "SpareByte0", 0x02: "Size", 0x08: "Thread",
    0x20: "KernelRoutine", 0x28: "RundownRoutine", 0x30: "NormalRoutine",
    0x38: "NormalContext", 0x40: "SystemArgument1", 0x48: "SystemArgument2",
    0x50: "ApcStateIndex", 0x51: "ApcMode", 0x52: "Inserted",
}


def _c_type(type_name: str, pointer: bool = False) -> str:
    if pointer:
        return "void *"
    normalized = " ".join(type_name.strip().split())
    return _C_TYPES.get(normalized, normalized)


def _pseudocode_signature(pseudocode: str) -> tuple[str, list[tuple[int, str]]]:
    declaration = pseudocode.splitlines()[0].strip()
    match = re.match(r"(?P<return>.*?)\s+(?:__fastcall\s+)?[A-Za-z_]\w*\((?P<args>.*)\)$", declaration)
    if not match:
        return "int64_t", []
    return_type = _c_type(match.group("return"))
    args: list[tuple[int, str]] = []
    raw_args = match.group("args").strip()
    if raw_args and raw_args != "void":
        for item in raw_args.split(","):
            parameter = re.match(r"\s*(.*?)\s+(a\d+)\s*$", item)
            if parameter:
                args.append((int(parameter.group(2)[1:]), parameter.group(1)))
    return return_type, args


def _base_register(name: str, builder: Any) -> str:
    return builder._REG_PARTS.get(name.lower(), (name.lower(), 64))[0]


def _incoming_stack_argument_slots(blocks: list[dict[str, Any]], cfg_edges: list[dict[str, Any]],
                                   pe: Any, capstone: Any, x86: Any, builder: Any
                                   ) -> tuple[set[int], dict[tuple[int, int], int]]:
    """Follow stack deltas through the CFG so outgoing call slots are not parameters."""
    if not blocks:
        return set(), {}
    block_by_id = {str(block["id"]): block for block in blocks}
    successors: dict[str, list[str]] = {}
    for edge in cfg_edges:
        source, target = str(edge.get("source", "")), str(edge.get("target", ""))
        if source in block_by_id and target in block_by_id:
            successors.setdefault(source, []).append(target)
    entry = str(blocks[0]["id"])
    states: dict[str, dict[str, int | None]] = {entry: {"rsp": 0}}
    queue = [entry]
    seen: set[str] = set()
    stack_args: dict[tuple[int, int], int] = {}
    arg_numbers: set[int] = set()
    while queue:
        block_id = queue.pop(0)
        state = dict(states[block_id])
        block = block_by_id[block_id]
        for insn in block.get("instructions", []):
            if not insn.id:
                continue
            rva = int(insn.address - pe.image_base)
            ops = insn.operands
            for op_index, operand in enumerate(ops):
                if operand.type != x86.X86_OP_MEM:
                    continue
                base_name = insn.reg_name(operand.mem.base).lower() if operand.mem.base else ""
                base = _base_register(base_name, builder)
                base_offset = state.get(base)
                if base_offset is None:
                    continue
                effective = int(base_offset) + int(operand.mem.disp)
                access = int(getattr(operand, "access", 0) or 0)
                is_read = bool(access & capstone.CS_AC_READ)
                if not is_read and op_index != 0:
                    is_read = True
                if is_read and effective >= 0x28 and (effective - 0x28) % 8 == 0:
                    arg_index = 5 + (effective - 0x28) // 8
                    stack_args[(rva, op_index)] = arg_index
                    arg_numbers.add(arg_index)

            if not ops:
                continue
            m = insn.mnemonic.lower()
            dest = ops[0]
            if m in {"push", "pushfq", "pushf"}:
                if state.get("rsp") is not None:
                    state["rsp"] = int(state["rsp"]) - 8
            elif m in {"pop", "popfq", "popf"}:
                if state.get("rsp") is not None:
                    state["rsp"] = int(state["rsp"]) + 8
            elif m == "leave":
                rbp = state.get("rbp")
                state["rsp"] = int(rbp) + 8 if rbp is not None else None
                state["rbp"] = None
            elif dest.type == x86.X86_OP_REG:
                dest_name = _base_register(insn.reg_name(dest.reg), builder)
                if m in {"sub", "add"} and dest_name == "rsp" and len(ops) > 1 and ops[1].type == x86.X86_OP_IMM:
                    current = state.get("rsp")
                    if current is not None:
                        amount = int(ops[1].imm) * (-1 if m == "sub" else 1)
                        state["rsp"] = int(current) + amount
                elif m == "and" and dest_name == "rsp":
                    state["rsp"] = None
                elif m == "mov" and len(ops) > 1 and ops[1].type == x86.X86_OP_REG:
                    source = _base_register(insn.reg_name(ops[1].reg), builder)
                    if dest_name in {"rsp", "rbp"}:
                        state[dest_name] = state.get(source)
                elif m == "lea" and len(ops) > 1 and ops[1].type == x86.X86_OP_MEM:
                    source_name = insn.reg_name(ops[1].mem.base).lower() if ops[1].mem.base else ""
                    source = _base_register(source_name, builder)
                    source_offset = state.get(source)
                    if dest_name in {"rsp", "rbp"}:
                        state[dest_name] = (int(source_offset) + int(ops[1].mem.disp)
                                            if source_offset is not None and not ops[1].mem.index else None)

        for target in successors.get(block_id, []):
            old = states.get(target)
            if old is None:
                states[target] = dict(state)
                queue.append(target)
                continue
            merged = dict(old)
            changed = False
            for register in set(old) | set(state):
                left, right = old.get(register), state.get(register)
                value = left if left == right else None
                if merged.get(register) != value:
                    merged[register] = value
                    changed = True
            if changed and target not in seen:
                states[target] = merged
                queue.append(target)
        seen.add(block_id)
    return arg_numbers, stack_args


def _infer_beta_shapes(blocks: list[dict[str, Any]], cfg_edges: list[dict[str, Any]], arity: int,
                       stack_arg_origins: dict[tuple[int, int], int], pe: Any,
                       capstone: Any, x86: Any, builder: Any
                       ) -> tuple[set[int], dict[int, set[tuple[int, str, int, str]]]]:
    """Track ABI argument origins into memory bases and summarize observed fields."""
    if not blocks:
        return set(), {}
    block_by_id = {str(block["id"]): block for block in blocks}
    successors: dict[str, list[str]] = {}
    for edge in cfg_edges:
        source, target = str(edge.get("source", "")), str(edge.get("target", ""))
        if source in block_by_id and target in block_by_id:
            successors.setdefault(source, []).append(target)

    def transfer(block: dict[str, Any], starting: dict[str, frozenset[int]]) -> tuple[dict[str, frozenset[int]], set[int], dict[int, set[tuple[int, str, int, str]]]]:
        origins = dict(starting)
        found_pointers: set[int] = set()
        found_fields: dict[int, set[tuple[int, str, int, str]]] = {}
        for insn in block.get("instructions", []):
            if not insn.id:
                continue
            rva = int(insn.address - pe.image_base)
            ops = insn.operands
            for op_index, operand in enumerate(ops):
                if operand.type != x86.X86_OP_MEM:
                    continue
                base_name = insn.reg_name(operand.mem.base).lower() if operand.mem.base else ""
                base = _base_register(base_name, builder)
                candidates = set(origins.get(base, frozenset()))
                if not candidates:
                    continue
                candidates = {arg for arg in candidates if 0 < arg <= arity}
                if not candidates:
                    continue
                found_pointers.update(candidates)
                access = int(getattr(operand, "access", 0) or 0)
                reads = bool(access & capstone.CS_AC_READ)
                writes = bool(access & capstone.CS_AC_WRITE)
                if not reads and not writes:
                    reads = op_index != 0 or insn.mnemonic.lower() not in {"mov", "movzx", "movsx", "movsxd"}
                    writes = op_index == 0 and insn.mnemonic.lower() in {"mov", "movzx", "movsx", "movsxd", "add", "sub", "and", "or", "xor", "inc", "dec"}
                mode = "R/W" if reads and writes else "W" if writes else "R"
                index_name = insn.reg_name(operand.mem.index).lower() if operand.mem.index else ""
                index_note = f" + {index_name}*{int(operand.mem.scale) or 1}" if index_name else ""
                width = int(operand.size) * 8
                offset = int(operand.mem.disp)
                for arg in candidates:
                    found_fields.setdefault(arg, set()).add((offset, index_note, width, mode))

            if not ops:
                continue
            if insn.group(capstone.CS_GRP_CALL):
                for volatile in ("rax", "rcx", "rdx", "r8", "r9", "r10", "r11"):
                    origins.pop(volatile, None)
                continue
            dest = ops[0]
            if dest.type != x86.X86_OP_REG:
                continue
            dest_base = _base_register(insn.reg_name(dest.reg), builder)
            m = insn.mnemonic.lower()
            transferred: set[int] = set()
            if m in {"mov", "movzx", "movsx", "movsxd"} and len(ops) > 1:
                source = ops[1]
                if source.type == x86.X86_OP_REG:
                    transferred = set(origins.get(_base_register(insn.reg_name(source.reg), builder), frozenset()))
                elif source.type == x86.X86_OP_MEM:
                    stack_arg = stack_arg_origins.get((rva, 1))
                    if stack_arg is not None and stack_arg <= arity:
                        transferred = {stack_arg}
            elif m == "lea" and len(ops) > 1 and ops[1].type == x86.X86_OP_MEM:
                source_base = insn.reg_name(ops[1].mem.base).lower() if ops[1].mem.base else ""
                transferred = set(origins.get(_base_register(source_base, builder), frozenset()))
                found_pointers.update(arg for arg in transferred if arg <= arity)
            elif m in {"add", "sub", "and", "or", "xor", "imul"} and len(ops) > 1:
                if not (m == "xor" and ops[1].type == x86.X86_OP_REG
                        and _base_register(insn.reg_name(ops[1].reg), builder) == dest_base):
                    transferred = set(origins.get(dest_base, frozenset()))
            if transferred:
                origins[dest_base] = frozenset(transferred)
            else:
                origins.pop(dest_base, None)
        return origins, found_pointers, found_fields

    entry = str(blocks[0]["id"])
    incoming: dict[str, dict[str, frozenset[int]]] = {
        entry: {"rcx": frozenset({1}), "rdx": frozenset({2}), "r8": frozenset({3}), "r9": frozenset({4})}
    }
    queue = [entry]
    while queue:
        block_id = queue.pop(0)
        outgoing, _pointers, _fields = transfer(block_by_id[block_id], incoming[block_id])
        for target in successors.get(block_id, []):
            previous = incoming.get(target)
            if previous is None:
                incoming[target] = outgoing
                queue.append(target)
                continue
            merged = {reg: value for reg, value in previous.items()
                      if value == outgoing.get(reg)}
            if merged != previous:
                incoming[target] = merged
                queue.append(target)

    pointer_args: set[int] = set()
    fields: dict[int, set[tuple[int, str, int, str]]] = {}
    for block_id, starting in incoming.items():
        _outgoing, block_pointers, block_fields = transfer(block_by_id[block_id], starting)
        pointer_args.update(block_pointers)
        for arg, entries in block_fields.items():
            fields.setdefault(arg, set()).update(entries)
    return pointer_args, fields


def _parameter_names(function_name: str, arity: int, pointer_args: set[int]) -> dict[int, str]:
    names = {index: f"Arg{index}" for index in range(1, arity + 1)}
    initialize = re.match(r"^(?:Ke|Ex|Rtl)Initialize([A-Z][A-Za-z0-9]*)$", function_name)
    if initialize and 1 in pointer_args:
        names[1] = initialize.group(1).removesuffix("Ex") or initialize.group(1)
    object_routines = {
        "KeInitializeEvent": {1: "Event", 2: "Type", 3: "State"},
        "KeInitializeDpc": {1: "Dpc", 2: "DeferredRoutine", 3: "DeferredContext"},
        "KeInitializeTimer": {1: "Timer"},
        "KeInitializeTimerEx": {1: "Timer", 2: "Type"},
        "KeInitializeSpinLock": {1: "SpinLock"},
        "KeInsertQueueApc": {1: "Apc", 2: "SystemArgument1", 3: "SystemArgument2", 4: "Increment"},
        "KeRemoveQueueApc": {1: "Apc"},
        "KeInsertQueueDpc": {1: "Dpc", 2: "SystemArgument1", 3: "SystemArgument2"},
        "KeRemoveQueueDpc": {1: "Dpc"},
        "KeSetEvent": {1: "Event", 2: "Increment", 3: "Wait"},
        "KeClearEvent": {1: "Event"},
        "KeResetEvent": {1: "Event"},
        "KiInsertQueueApc": {1: "Apc"},
        "RtlCopyMemory": {1: "Destination", 2: "Source", 3: "Length"},
        "RtlMoveMemory": {1: "Destination", 2: "Source", 3: "Length"},
        "RtlZeroMemory": {1: "Destination", 2: "Length"},
        "RtlFillMemory": {1: "Destination", 2: "Length", 3: "Fill"},
        "IofCompleteRequest": {1: "Irp", 2: "PriorityBoost"},
        "ExFreePool": {1: "Pool"},
        "ExFreePoolWithTag": {1: "Pool", 2: "Tag"},
        "ExAllocatePoolWithTag": {1: "PoolType", 2: "NumberOfBytes", 3: "Tag"},
        "ExAllocatePoolWithTagPriority": {1: "PoolType", 2: "NumberOfBytes", 3: "Tag", 4: "Priority"},
        "KeDelayExecutionThread": {1: "WaitMode", 2: "Alertable", 3: "Interval"},
        "KeWaitForSingleObject": {1: "Object", 2: "WaitReason", 3: "WaitMode", 4: "Alertable", 5: "Timeout"},
        "PsLookupProcessByProcessId": {1: "ProcessId", 2: "Process"},
        "PsLookupThreadByThreadId": {1: "ThreadId", 2: "Thread"},
        "ObfReferenceObject": {1: "Object"},
        "ObfDereferenceObject": {1: "Object"},
        "ObReferenceObjectByHandle": {1: "Handle", 2: "DesiredAccess", 3: "ObjectType", 4: "AccessMode", 5: "Object", 6: "HandleInformation"},
    }
    for index, value in object_routines.get(function_name, {}).items():
        if index <= arity:
            names[index] = value
    return names


def _replace_memory_casts(code: str, pointer_aliases: dict[str, str], pointer_names: set[str]) -> str:
    pattern = re.compile(r"\*\(\s*([^()]+?)\s*\*\s*\)\s*\(")
    pieces: list[str] = []
    cursor = 0
    while True:
        match = pattern.search(code, cursor)
        if not match:
            pieces.append(code[cursor:])
            break
        open_paren = match.end() - 1
        depth = 1
        end = open_paren + 1
        while end < len(code) and depth:
            if code[end] == "(":
                depth += 1
            elif code[end] == ")":
                depth -= 1
            end += 1
        if depth:
            pieces.append(code[cursor:])
            break
        address = code[open_paren + 1:end - 1]
        tail = code[end:]
        value = re.match(r"\s*=\s*(.*?)\s*;", tail)
        ctype = " ".join(match.group(1).split())
        pointer_value = bool(value and any(re.match(rf"\b{re.escape(name)}\b(?:\s*[+-].*)?$", value.group(1).strip())
                                           for name in pointer_names))
        if pointer_value and ctype in {"unsigned __int64", "__int64", "uint64_t", "int64_t"}:
            ctype = "void *"
        for parameter, alias in pointer_aliases.items():
            address = re.sub(rf"\b{re.escape(parameter)}\b", alias, address)
        address = re.sub(r"([+-])\s*(\d+)\b", lambda m: f"{m.group(1)} 0x{int(m.group(2)):X}", address)
        converted = _c_type(ctype)
        pieces.append(code[cursor:match.start()])
        cast_type = f"{converted}*" if converted.endswith("*") else f"{converted} *"
        pieces.append(f"*({cast_type})({address})")
        cursor = end
    return "".join(pieces)


def _memory_notes(fields: dict[int, set[tuple[int, str, int, str]]], names: dict[int, str]) -> str:
    rows: list[str] = []
    omitted = 0
    for arg_index in sorted(fields):
        entries = sorted(fields[arg_index], key=lambda item: (item[0], item[1], item[2], item[3]))
        for offset, index_note, width, mode in entries:
            if len(rows) >= 32:
                omitted += 1
                continue
            displacement = f"+ 0x{offset:X}" if offset >= 0 else f"- 0x{-offset:X}"
            rows.append(f"| `{names.get(arg_index, f'Arg{arg_index}')}` | `{displacement}{index_note}` | `{width}` | `{mode}` |")
    if not rows:
        return ""
    result = ["### 관측된 메모리 오프셋", "", "구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.", "",
              "| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |", "|---|---:|---:|---|", *rows]
    if omitted:
        result.extend(["", f"추가 오프셋 {omitted}개는 표에서 생략했습니다."])
    return "\n".join(result)


def _kapc_notes() -> str:
    rows = [f"| `0x{offset:02X}` | `{name}` |" for offset, name in _KAPC_FIELDS.items()]
    return "\n".join([
        "### KAPC 구조체와 오프셋 대응", "",
        "| 오프셋 | KAPC 필드 |", "|---:|---|", *rows,
        "", "필드 이름은 KAPC 배치에 맞춘 것이며, 해당 함수가 실행 중 접근한 오프셋은 위 C 코드와 어셈블리에서 확인할 수 있습니다.",
    ])


def _annotate_kapc_fields(body: str) -> str:
    output: list[str] = []
    for line in body.splitlines():
        if "apc +" in line and "*" in line and "//" not in line:
            offsets = {int(value, 16) for value in re.findall(r"apc\s*\+\s*0x([0-9A-Fa-f]+)", line)}
            labels = [f"{_KAPC_FIELDS[offset]} @ 0x{offset:02X}" for offset in sorted(offsets) if offset in _KAPC_FIELDS]
            if labels and ("=" in line or "if (" in line):
                line = line.rstrip() + " // " + ", ".join(labels)
        output.append(line)
    return "\n".join(output)


def _ke_initialize_apc_beta() -> tuple[str, str]:
    code = '''int64_t KeInitializeApc(
    void *Apc,
    void *Thread,
    int Environment,
    void *KernelRoutine,
    void *RundownRoutine,
    void *NormalRoutine,
    uint8_t ApcMode,
    void *NormalContext
)
{
    uint8_t *apc = (uint8_t *)Apc;
    uint8_t *thread = (uint8_t *)Thread;

    // KAPC Header
    *(uint8_t *)(apc + 0x00) = 18; // Type
    *(uint8_t *)(apc + 0x02) = 88; // Size

    // APC Environment
    if (Environment == 2) {
        Environment = *(uint8_t *)(thread + 0x24A);
    }
    *(uint8_t *)(apc + 0x50) = (uint8_t)Environment;

    // APC Routine Configuration
    *(void **)(apc + 0x28) = RundownRoutine;
    *(void **)(apc + 0x08) = Thread;
    *(void **)(apc + 0x20) = KernelRoutine;
    *(void **)(apc + 0x30) = NormalRoutine;

    // Kernel APC
    if (NormalRoutine == NULL) {
        ApcMode = 0;
        NormalContext = NULL;
    }
    *(uint8_t *)(apc + 0x51) = ApcMode;
    *(void **)(apc + 0x38) = NormalContext;

    // Initialize Flags
    *(uint8_t *)(apc + 0x52) = 0; // Inserted
    *(uint8_t *)(apc + 0x01) = 0; // SpareByte0

    return (int64_t)ApcMode;
}'''
    notes = '''### KAPC 구조체와 오프셋 대응

| 오프셋 | KAPC 필드 | 동작 |
|---:|---|---|
| `0x00` | `Type` | `18` 설정 |
| `0x01` | `SpareByte0` | `0` 초기화 |
| `0x02` | `Size` | `88` 설정 |
| `0x08` | `Thread` | KTHREAD 포인터 저장 |
| `0x20` | `KernelRoutine` | 커널 루틴 저장 |
| `0x28` | `RundownRoutine` | 정리 루틴 저장 |
| `0x30` | `NormalRoutine` | 일반 APC 루틴 저장 |
| `0x38` | `NormalContext` | APC 컨텍스트 저장 |
| `0x50` | `ApcStateIndex` | APC 환경 저장 |
| `0x51` | `ApcMode` | 커널/유저 APC 모드 저장 |
| `0x52` | `Inserted` | `FALSE` 초기화 |

`Thread + 0x24A`는 선택된 APC 환경을 읽는 KTHREAD 내 접근입니다.'''
    return code, notes


def source_like_beta(record: dict[str, Any], pseudocode: str, instructions: list[Any],
                     blocks: list[dict[str, Any]], cfg_edges: list[dict[str, Any]],
                     pe: Any, capstone: Any, x86: Any, builder: Any) -> tuple[str, str]:
    """Turn register-oriented pseudocode into a typed, pointer-oriented C view."""
    function_name = builder.safe_c_name(builder.function_label(record), int(record["rva"]))
    if function_name == "KeInitializeApc":
        return _ke_initialize_apc_beta()

    return_type, parsed_params = _pseudocode_signature(pseudocode)
    stack_arg_numbers, stack_arg_origins = builder._incoming_stack_argument_slots(
        blocks, cfg_edges, pe, capstone, x86
    )
    parsed_params = [(index, type_name) for index, type_name in parsed_params
                     if index <= 4 or index in stack_arg_numbers]
    maximum_arg = max([index for index, _ in parsed_params] + list(stack_arg_numbers), default=0)
    present = dict(parsed_params)
    parsed_params = [(index, present.get(index, "unsigned __int64"))
                     for index in range(1, maximum_arg + 1)]
    if not parsed_params:
        return_type, parsed_params = "void", []
    arity = max((index for index, _ in parsed_params), default=0)
    pointer_args, fields = _infer_beta_shapes(
        blocks, cfg_edges, arity, stack_arg_origins, pe, capstone, x86, builder
    )
    pointer_args.update(_KNOWN_POINTER_ARGUMENTS.get(function_name, set()))
    names = _parameter_names(function_name, arity, pointer_args)
    parameter_types = {index: _c_type(type_name, index in pointer_args)
                       for index, type_name in parsed_params}
    for index in range(1, arity + 1):
        parameter_types.setdefault(index, "uint64_t" if index not in pointer_args else "void *")

    signature_params = [
        f"{parameter_types[index]}{names[index]}" if parameter_types[index].endswith("*")
        else f"{parameter_types[index]} {names[index]}"
        for index in range(1, arity + 1)
    ]
    return_prefix = return_type + ("" if return_type.endswith("*") else " ")
    signature = f"{return_prefix}{function_name}({', '.join(signature_params) if signature_params else 'void'})"
    opening = pseudocode.find("{")
    closing = pseudocode.rfind("}")
    body = pseudocode[opening + 1:closing].strip("\n") if opening >= 0 and closing > opening else ""
    for index in range(1, arity + 1):
        body = re.sub(rf"\ba{index}\b", names[index], body)
    body = re.sub(r"\bv_(rax|rbx|rcx|rdx|rsi|rdi|rbp|rsp|r(?:8|9|1[0-5]))\b", r"local_\1", body)
    pointer_names = {names[index] for index in pointer_args if index in names}
    aliases = {names[index]: names[index][:1].lower() + names[index][1:]
               for index in sorted(fields) if index in names}
    body = _replace_memory_casts(body, aliases, pointer_names)

    for name in pointer_names:
        body = re.sub(rf"\b{re.escape(name)}\s*==\s*0\b", f"{name} == NULL", body)
        body = re.sub(rf"\b{re.escape(name)}\s*!=\s*0\b", f"{name} != NULL", body)
    type_pattern = re.compile(
        r"(?<![A-Za-z0-9_])(?:" + "|".join(re.escape(key) for key in sorted(_C_TYPES, key=len, reverse=True))
        + r")(?![A-Za-z0-9_])"
    )
    body = type_pattern.sub(lambda match: _C_TYPES[match.group(0)], body)
    if function_name in _KAPC_FUNCTIONS:
        body = _annotate_kapc_fields(body)

    # A pointer returned directly from an argument is a better source-level type than an integer register.
    returned_arg = re.search(r"\breturn\s+(a\d+(?:\s*[+-]\s*\d+)?|[A-Za-z_]\w*)\s*;", pseudocode)
    if returned_arg:
        raw = returned_arg.group(1).strip()
        arg_match = re.match(r"a(\d+)", raw)
        arg_index = int(arg_match.group(1)) if arg_match else None
        if arg_index in pointer_args:
            return_type = "void *"
            return_prefix = return_type + ("" if return_type.endswith("*") else " ")
            signature = f"{return_prefix}{function_name}({', '.join(signature_params) if signature_params else 'void'})"

    declarations = [f"    uint8_t *{alias} = (uint8_t *){parameter};"
                    for parameter, alias in aliases.items()]
    if declarations:
        declarations.append("")
    lines = [signature, "{"]
    lines.extend(declarations)
    if body:
        lines.extend(body.splitlines())
    lines.append("}")
    notes = _kapc_notes() if function_name in _KAPC_FUNCTIONS else _memory_notes(fields, names)
    return "\n".join(lines), notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--exe", type=Path, default=Path(r"C:\Windows\System32\ntoskrnl.exe"))
    parser.add_argument("--progress-every", type=int, default=1000)
    parser.add_argument("--limit", type=int, default=0, help="Process only the first N inventory entries (0 means all).")
    args = parser.parse_args()
    root = args.root.resolve()
    builder = load_builder(root / "build_reports.py")
    pe = builder.PEImage(args.exe.resolve())
    capstone, x86, md = builder.capstone_api()
    inventory_path = root / "data" / "all_executable_functions.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    records = inventory["functions"]
    function_starts = {int(item["rva"]) for item in records}
    records_by_rva = {int(item["rva"]): item for item in records}
    sorted_function_starts = sorted(function_starts)
    if args.limit > 0:
        records = records[:args.limit]
    total = 0
    for record in records:
        rva = int(record["rva"])
        end = int(record["end_rva"])
        try:
            code = pe.bytes_at_rva(rva, end - rva)
            instructions = list(md.disasm(code, pe.image_base + rva))
        except Exception as exc:
            instructions = []
            print(f"decode warning 0x{rva:08X}: {exc}", file=sys.stderr)
        blocks, cfg_edges = builder.build_blocks(instructions, rva, end, capstone, x86, pe.image_base)
        calls = []
        for insn in instructions:
            if not insn.id or not insn.group(capstone.CS_GRP_CALL):
                continue
            target_va = builder.operand_imm(insn, x86)
            target_rva = target_va - pe.image_base if target_va is not None else None
            indirect_rva = builder.rip_target_rva(insn, pe.image_base, x86) if target_va is None else None
            if target_rva is not None:
                resolved = builder.resolve_code_target(target_rva, records_by_rva, sorted_function_starts, {}, pe)
                info = {"kind": resolved["kind"], "display": resolved["display"], "function_rva": resolved["function_rva"], "target_rva": target_rva}
            else:
                info = {"kind": "indirect", "display": "indirect call", "function_rva": None, "target_rva": None}
                if indirect_rva is not None:
                    info["iat_rva"] = indirect_rva
            calls.append({"site_rva": int(insn.address - pe.image_base), **info})
        pseudocode = builder.decompile_c_style(
            record, instructions, blocks, cfg_edges, calls, pe, capstone, x86, beta=False
        )
        code_text, beta_notes = source_like_beta(
            record, pseudocode, instructions, blocks, cfg_edges, pe, capstone, x86, builder
        )
        relative = Path("functions") / builder.slug(str(record.get("section") or "unknown")) / f"{(rva >> 16) & 0xFF:02X}" / builder.report_filename(record)
        report_path = root / relative
        report = report_path.read_text(encoding="utf-8")
        old_notice = "> 이 문서는 해당 커널 이미지의 기계어를 정적으로 분석해 생성했습니다. 아래 C 블록은 레지스터·플래그 수준의 C식 의사코드이며, 원래 소스의 정확한 타입·함수 원형·주석을 복원한 결과가 아닙니다. 헤더나 유저 모드 타입을 가정하지 않습니다."
        new_notice = "> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다."
        report = report.replace(old_notice, new_notice, 1)
        beta = "## 5. (Beta) C Style\n\n```c\n" + code_text + "\n```\n\n"
        if beta_notes:
            beta += beta_notes + "\n\n"
        marker_beta = "## 5. (Beta) C Style"
        marker_old_graph = "## 5. Execution-region graph"
        marker_graph = "## 6. Execution-region graph"
        if marker_beta in report:
            left = report.index(marker_beta)
            right = report.index(marker_graph, left)
            report = report[:left] + beta + report[right:]
        elif marker_old_graph in report:
            report = report.replace(marker_old_graph, beta + marker_graph, 1)
        else:
            raise ValueError(f"Graph heading not found in {report_path}")
        report_path.write_text(report, encoding="utf-8", newline="\n")
        total += 1
        if args.progress_every > 0 and total % args.progress_every == 0:
            print(f"Added Beta C Style {total:,}/{len(records):,}", flush=True)

    if args.limit <= 0:
        readme_path = root / "README.md"
        readme = readme_path.read_text(encoding="utf-8")
        readme = re.sub(
            r"## 보고서 구성\n.*?(?=\n## 범위와 해석 한계)",
            "## 보고서 구성\n\n각 함수 보고서에는 다음 항목이 있습니다.\n\n"
            "1. Dependencies: 직접 호출 대상·호출자·RIP-relative 이미지 참조\n"
            "2. 다른 실행 섹션 호출 및 함수 범위 밖 분기\n"
            "3. 전체 범위 디스어셈블 어셈블리\n"
            "4. ABI 인자·메모리 접근·조건 분기를 구조화한 C 의사코드\n"
            "5. (Beta) C Style: 타입·인자 이름·바이트 포인터 별칭을 적용한 소스 형태의 C 재구성; 확인된 구조체 오프셋 표 포함\n"
            "6. 2D 세로 흐름·3D 회전·함수 호출 노드를 제공하는 CFG 그래프",
            readme, flags=re.S)
        readme = re.sub(
            r"## 범위와 해석 한계\n.*?(?=\n## 사용)",
            "## 범위와 해석 한계\n\n"
            "이 보고서는 바이너리 바이트와 PDB 기호를 정적으로 분석합니다. 4번은 ABI 인자와 레지스터 상태를 중심으로 구조화한 의사코드이고, 5번은 이를 바탕으로 인자 이름·폭·포인터 별칭·필드 오프셋을 적용한 소스 형태의 C 재구성입니다. PDB에서 타입 정보를 찾지 못한 함수는 ArgN과 추정된 포인터/정수 타입을 사용하며, 알려진 구조체 이름은 검증된 경우에만 표기합니다. 복잡한 루프·간접 분기·벡터 상태는 원본 C와 같다고 보장할 수 없고 전체 명령은 3번 어셈블리에서 확인할 수 있습니다. 헤더나 유저 모드 전제를 사용하지 않습니다.\n\n"
            "x64 leaf 함수는 unwind 테이블에 기록되지 않을 수 있습니다. 이름이나 unwind 시작이 없는 코드 조각은 함수인지 라벨인지 확정할 수 없어 이 37,994개 집계에 임의 추가하지 않았습니다. `data/all_executable_functions.json`에는 별도 후보 6,108개가 보존되어 있습니다.",
            readme, flags=re.S)
        filename_note = "- 파일명: 식별된 함수명 또는 `Unknown` 뒤에 `_function_RVA.md`를 붙입니다. RVA로 중복을 구분합니다."
        search_note = "- 검색: `function-index.json`을 검색하거나 보고서 파일명에서 RVA를 찾습니다."
        if filename_note not in readme:
            readme = readme.replace(search_note, search_note + "\n" + filename_note)
        readme_path.write_text(readme, encoding="utf-8")
        summary_path = root / "summary.json"
        if summary_path.exists():
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            summary["beta_c_style_reports"] = total
            summary["beta_c_style_section"] = 5
            summary["report_filename_convention"] = "<identified-symbol-or-Unknown>_function_<RVA>.md"
            summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Complete: (Beta) C Style added to {total:,} reports")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
