#!/usr/bin/env python3
"""Small PE/PDB inspection helper for ntoskrnl.exe (Windows, x64).

The tool reads PE exports/imports, obtains public symbol names through the
Windows DbgHelp API, and disassembles selected symbol entries with Capstone.
It is intentionally an inspection aid, not a source-code decompiler.
"""

from __future__ import annotations

import argparse
import csv
import ctypes
import json
import os
import struct
import sys
import urllib.request
import uuid
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_EXE = Path(r"C:\Windows\System32\ntoskrnl.exe")
WORKSPACE = Path(__file__).resolve().parents[1]
DEFAULT_PDB_CACHE = WORKSPACE / "work"
DEFAULT_OUT = WORKSPACE / "outputs" / "ntoskrnl-analysis"
SYMBOL_SERVER = "https://msdl.microsoft.com/download/symbols"
PDB_MAGIC = b"Microsoft C/C++ MSF 7.00"


class AnalysisError(RuntimeError):
    pass


@dataclass
class Section:
    name: str
    virtual_address: int
    virtual_size: int
    raw_pointer: int
    raw_size: int
    characteristics: int

    @property
    def extent(self) -> int:
        return max(self.virtual_size, self.raw_size)

    @property
    def executable(self) -> bool:
        return bool(self.characteristics & 0x20000000)


class PEImage:
    def __init__(self, path: Path):
        self.path = path
        self.data = path.read_bytes()
        if self.data[:2] != b"MZ":
            raise AnalysisError(f"Not a PE image: {path}")
        self.pe_offset = self._u32(0x3C)
        if self.data[self.pe_offset : self.pe_offset + 4] != b"PE\0\0":
            raise AnalysisError("Missing PE signature")
        coff = self.pe_offset + 4
        self.machine, nsections, self.timestamp, _, _, opt_size, _ = struct.unpack_from(
            "<HHIIIHH", self.data, coff
        )
        self.optional_offset = coff + 20
        magic = self._u16(self.optional_offset)
        if magic == 0x20B:
            self.is_64 = True
            self.image_base = self._u64(self.optional_offset + 24)
            self.size_of_image = self._u32(self.optional_offset + 56)
            self.number_of_dirs_offset = self.optional_offset + 108
            self.directories_offset = self.optional_offset + 112
            self.thunk_size = 8
            self.ordinal_flag = 1 << 63
        elif magic == 0x10B:
            self.is_64 = False
            self.image_base = self._u32(self.optional_offset + 28)
            self.size_of_image = self._u32(self.optional_offset + 56)
            self.number_of_dirs_offset = self.optional_offset + 92
            self.directories_offset = self.optional_offset + 96
            self.thunk_size = 4
            self.ordinal_flag = 1 << 31
        else:
            raise AnalysisError(f"Unsupported optional-header magic {magic:#x}")
        self.directory_count = self._u32(self.number_of_dirs_offset)
        self.sections: list[Section] = []
        section_table = self.optional_offset + opt_size
        for i in range(nsections):
            off = section_table + 40 * i
            name = self.data[off : off + 8].split(b"\0", 1)[0].decode("ascii", "replace")
            vsize, va, raw_size, raw_pointer = struct.unpack_from("<IIII", self.data, off + 8)
            characteristics = self._u32(off + 36)
            self.sections.append(
                Section(name, va, vsize, raw_pointer, raw_size, characteristics)
            )

    def _u16(self, offset: int) -> int:
        return struct.unpack_from("<H", self.data, offset)[0]

    def _u32(self, offset: int) -> int:
        return struct.unpack_from("<I", self.data, offset)[0]

    def _u64(self, offset: int) -> int:
        return struct.unpack_from("<Q", self.data, offset)[0]

    def directory(self, index: int) -> tuple[int, int]:
        if index >= self.directory_count:
            return 0, 0
        return struct.unpack_from("<II", self.data, self.directories_offset + 8 * index)

    def rva_to_offset(self, rva: int) -> int:
        if rva < self.size_of_image:
            for section in self.sections:
                if section.virtual_address <= rva < section.virtual_address + section.extent:
                    delta = rva - section.virtual_address
                    if delta >= section.raw_size:
                        raise AnalysisError(f"RVA {rva:#x} points to uninitialized section data")
                    return section.raw_pointer + delta
        if rva < len(self.data):
            # Header RVAs are also file offsets.
            return rva
        raise AnalysisError(f"RVA {rva:#x} is outside the image")

    def read_c_string(self, rva: int, limit: int = 65536) -> str:
        offset = self.rva_to_offset(rva)
        end = self.data.find(b"\0", offset, min(len(self.data), offset + limit))
        if end < 0:
            end = min(len(self.data), offset + limit)
        return self.data[offset:end].decode("ascii", "replace")

    def debug_pdb_identity(self) -> tuple[str, str, int, str] | None:
        rva, size = self.directory(6)
        if not rva or not size:
            return None
        offset = self.rva_to_offset(rva)
        for off in range(offset, min(offset + size, len(self.data)), 28):
            if off + 28 > len(self.data):
                break
            debug_entry = struct.unpack_from("<IIHHIIII", self.data, off)
            dtype, data_size, data_ptr = debug_entry[4], debug_entry[5], debug_entry[7]
            # IMAGE_DEBUG_TYPE_CODEVIEW = 2; RSDS record has GUID, age, PDB path.
            if dtype != 2 or data_size < 25 or data_ptr + data_size > len(self.data):
                continue
            record = self.data[data_ptr : data_ptr + data_size]
            if record[:4] != b"RSDS":
                continue
            guid = uuid.UUID(bytes_le=record[4:20])
            age = struct.unpack_from("<I", record, 20)[0]
            pdb_name = record[24:].split(b"\0", 1)[0].decode("utf-8", "replace")
            symbol_key = guid.hex.upper() + str(age)
            return str(guid), symbol_key, age, Path(pdb_name).name
        return None

    def exports(self) -> list[dict[str, object]]:
        rva, size = self.directory(0)
        if not rva or not size:
            return []
        off = self.rva_to_offset(rva)
        (_characteristics, _timestamp, _major, _minor, _name_rva, ordinal_base,
         nfuncs, nnames, funcs_rva, names_rva, ords_rva) = struct.unpack_from(
            "<IIHHIIIIIII", self.data, off
        )
        names: dict[int, list[str]] = defaultdict(list)
        for i in range(nnames):
            name_rva = self._u32(self.rva_to_offset(names_rva) + i * 4)
            ordinal_index = self._u16(self.rva_to_offset(ords_rva) + i * 2)
            names[ordinal_index].append(self.read_c_string(name_rva))
        result = []
        for i in range(nfuncs):
            function_rva = self._u32(self.rva_to_offset(funcs_rva) + i * 4)
            if not function_rva:
                continue
            is_forwarder = rva <= function_rva < rva + size
            result.append(
                {
                    "ordinal": ordinal_base + i,
                    "name": ";".join(names.get(i, [])),
                    "rva": f"0x{function_rva:08X}",
                    "forwarder": self.read_c_string(function_rva) if is_forwarder else "",
                    "kind": "forwarder" if is_forwarder else "export",
                }
            )
        return result

    def imports(self) -> list[dict[str, object]]:
        rva, size = self.directory(1)
        if not rva or not size:
            return []
        descriptor_off = self.rva_to_offset(rva)
        result = []
        for descriptor_index in range(size // 20 + 1):
            off = descriptor_off + descriptor_index * 20
            if off + 20 > len(self.data):
                break
            original_thunk, _timestamp, _forwarder, name_rva, first_thunk = struct.unpack_from(
                "<IIIII", self.data, off
            )
            if not any((original_thunk, _timestamp, _forwarder, name_rva, first_thunk)):
                break
            dll = self.read_c_string(name_rva)
            lookup_rva = original_thunk or first_thunk
            n = 0
            while True:
                thunk_rva = lookup_rva + n * self.thunk_size
                thunk_off = self.rva_to_offset(thunk_rva)
                value = int.from_bytes(self.data[thunk_off : thunk_off + self.thunk_size], "little")
                if value == 0:
                    break
                if value & self.ordinal_flag:
                    symbol = f"ordinal_{value & 0xFFFF}"
                    hint = ""
                    ordinal = value & 0xFFFF
                else:
                    import_name_rva = value & (0x7FFFFFFF if self.is_64 else 0x7FFFFFFF)
                    import_off = self.rva_to_offset(import_name_rva)
                    hint = self._u16(import_off)
                    symbol = self.read_c_string(import_name_rva + 2)
                    ordinal = ""
                iat_rva = first_thunk + n * self.thunk_size
                result.append(
                    {
                        "dll": dll,
                        "name": symbol,
                        "hint": hint,
                        "ordinal": ordinal,
                        "lookup_rva": f"0x{thunk_rva:08X}",
                        "iat_rva": f"0x{iat_rva:08X}",
                    }
                )
                n += 1
        return result

    def section_for_rva(self, rva: int) -> Section | None:
        return next(
            (s for s in self.sections if s.virtual_address <= rva < s.virtual_address + s.extent),
            None,
        )

    def bytes_at_rva(self, rva: int, limit: int) -> bytes:
        offset = self.rva_to_offset(rva)
        return self.data[offset : min(offset + limit, len(self.data))]

    def x64_runtime_functions(self) -> list[dict[str, object]]:
        """Read IMAGE_RUNTIME_FUNCTION_ENTRY records from the PE exception directory."""
        if not self.is_64 or self.machine != 0x8664:
            return []
        rva, size = self.directory(3)  # IMAGE_DIRECTORY_ENTRY_EXCEPTION
        if not rva or size < 12:
            return []
        offset = self.rva_to_offset(rva)
        entries = []
        for index in range(size // 12):
            begin, end, unwind = struct.unpack_from("<III", self.data, offset + index * 12)
            section = self.section_for_rva(begin) if begin else None
            if not begin or end <= begin or end > self.size_of_image:
                continue
            if section is None or not section.executable:
                continue
            entries.append(
                {
                    "begin_rva": begin,
                    "end_rva": end,
                    "unwind_info_rva": unwind,
                    "section": section.name,
                }
            )
        return entries


def download_pdb(pe: PEImage, cache_dir: Path) -> tuple[Path, tuple[str, str, int, str]]:
    identity = pe.debug_pdb_identity()
    if not identity:
        raise AnalysisError("The executable has no RSDS PDB identity")
    _, key, _, pdb_name = identity
    path = cache_dir / "pdb" / pdb_name / key / pdb_name
    path.parent.mkdir(parents=True, exist_ok=True)
    cached_ok = False
    if path.is_file():
        with path.open("rb") as cached:
            cached_ok = cached.read(64).startswith(PDB_MAGIC)
        if not cached_ok:
            print(f"Ignoring invalid cached PDB: {path}")
    if not cached_ok:
        url = f"{SYMBOL_SERVER}/{pdb_name}/{key}/{pdb_name}"
        print(f"Downloading matching PDB from Microsoft Symbol Server: {url}")
        request = urllib.request.Request(url, headers={"User-Agent": "ntoskrnl-disassembler/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                data = response.read()
                content_length = response.headers.get("Content-Length")
                content_type = response.headers.get("Content-Type", "unknown")
        except Exception as exc:
            raise AnalysisError(f"PDB download failed: {exc}") from exc
        if content_length and len(data) != int(content_length):
            raise AnalysisError(f"PDB download was incomplete: received {len(data)} of {content_length} bytes")
        if len(data) < 64 or not data.startswith(PDB_MAGIC):
            raise AnalysisError(
                f"Symbol server response is not an MSF 7.0 PDB: {len(data)} bytes, "
                f"Content-Type={content_type!r}, prefix={data[:48]!r}"
            )
        temporary = path.with_name(path.name + ".download-" + uuid.uuid4().hex)
        try:
            temporary.write_bytes(data)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)
    return path, identity


class DbgHelpSymbols:
    """Loads the matching PDB using the Windows symbol handler (DbgHelp)."""

    class SymbolInfo(ctypes.Structure):
        _fields_ = [
            ("SizeOfStruct", ctypes.c_ulong),
            ("TypeIndex", ctypes.c_ulong),
            ("Reserved", ctypes.c_ulonglong * 2),
            ("Index", ctypes.c_ulong),
            ("Size", ctypes.c_ulong),
            ("ModBase", ctypes.c_ulonglong),
            ("Flags", ctypes.c_ulong),
            ("Value", ctypes.c_ulonglong),
            ("Address", ctypes.c_ulonglong),
            ("Register", ctypes.c_ulong),
            ("Scope", ctypes.c_ulong),
            ("Tag", ctypes.c_ulong),
            ("NameLen", ctypes.c_ulong),
            ("MaxNameLen", ctypes.c_ulong),
            ("Name", ctypes.c_char * 1),
        ]

    def __init__(self, image: PEImage, pdb_path: Path):
        if os.name != "nt":
            raise AnalysisError("PDB symbol enumeration through DbgHelp requires Windows")
        self.image = image
        self.pdb_path = pdb_path
        self.dbghelp = ctypes.WinDLL("dbghelp.dll", use_last_error=True)
        self.process = ctypes.c_void_p(-1).value
        self._setup_api()
        self.dbghelp.SymSetOptions(0x00000002 | 0x00000004 | 0x00000200)  # undecorate, defer, fail critical
        if not self.dbghelp.SymInitializeW(self.process, None, False):
            raise AnalysisError(f"SymInitializeW failed: {ctypes.get_last_error()}")
        search = str(pdb_path.parent) + ";" + str(DEFAULT_PDB_CACHE)
        if not self.dbghelp.SymSetSearchPathW(self.process, search):
            self.dbghelp.SymCleanup(self.process)
            raise AnalysisError(f"SymSetSearchPathW failed: {ctypes.get_last_error()}")
        base = self.dbghelp.SymLoadModuleExW(
            self.process,
            None,
            str(image.path),
            "ntoskrnl",
            image.image_base,
            image.size_of_image,
            None,
            0,
        )
        if not base:
            error = ctypes.get_last_error()
            self.dbghelp.SymCleanup(self.process)
            raise AnalysisError(f"SymLoadModuleExW failed: {error}")
        self.module_base = int(base)
        self.symbols = self._enumerate()
        if not self.symbols:
            self.close()
            raise AnalysisError(
                "DbgHelp loaded the image but enumerated no PDB symbols; check that the PDB matches the image"
            )

    def _setup_api(self) -> None:
        h = self.dbghelp
        h.SymSetOptions.argtypes = [ctypes.c_ulong]
        h.SymSetOptions.restype = ctypes.c_ulong
        h.SymInitializeW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_bool]
        h.SymInitializeW.restype = ctypes.c_bool
        h.SymSetSearchPathW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p]
        h.SymSetSearchPathW.restype = ctypes.c_bool
        h.SymLoadModuleExW.argtypes = [
            ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p,
            ctypes.c_ulonglong, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong,
        ]
        h.SymLoadModuleExW.restype = ctypes.c_ulonglong
        h.SymEnumSymbols.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_char_p,
                                     ctypes.c_void_p, ctypes.c_void_p]
        h.SymEnumSymbols.restype = ctypes.c_bool
        h.SymCleanup.argtypes = [ctypes.c_void_p]
        h.SymCleanup.restype = ctypes.c_bool

    def _enumerate(self) -> list[dict[str, object]]:
        callback_type = ctypes.WINFUNCTYPE(
            ctypes.c_bool, ctypes.POINTER(self.SymbolInfo), ctypes.c_ulong, ctypes.c_void_p
        )
        rows: list[dict[str, object]] = []

        @callback_type
        def callback(info_ptr, _size, _context):
            info = info_ptr.contents
            name_addr = ctypes.addressof(info) + self.SymbolInfo.Name.offset
            raw_name = ctypes.string_at(name_addr, int(info.NameLen))
            name = raw_name.decode("utf-8", "replace")
            address = int(info.Address)
            if address >= self.module_base:
                rva = address - self.module_base
                rows.append(
                    {
                        "name": name,
                        "rva": rva,
                        "size": int(info.Size),
                        "tag": int(info.Tag),
                        "flags": int(info.Flags),
                        "type_index": int(info.TypeIndex),
                    }
                )
            return True

        ok = self.dbghelp.SymEnumSymbols(
            self.process, self.module_base, b"*", callback, None
        )
        if not ok and not rows:
            raise AnalysisError(f"SymEnumSymbols failed: {ctypes.get_last_error()}")
        # Collapse exact duplicate records and sort in image order.
        unique = {(row["name"], row["rva"], row["size"], row["tag"]): row for row in rows}
        return sorted(unique.values(), key=lambda row: (int(row["rva"]), str(row["name"])))

    def close(self) -> None:
        if getattr(self, "process", None):
            self.dbghelp.SymCleanup(self.process)
            self.process = None

    def __enter__(self) -> "DbgHelpSymbols":
        return self

    def __exit__(self, *_exc) -> None:
        self.close()


def write_csv(path: Path, rows: Iterable[dict[str, object]], columns: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def disassemble(pe: PEImage, symbols: list[dict[str, object]], selected_name: str | None,
                output: Path, max_bytes: int) -> int:
    try:
        from capstone import Cs, CS_ARCH_X86, CS_MODE_64, CS_MODE_32
    except ImportError as exc:
        raise AnalysisError("Install Capstone first: python -m pip install capstone") from exc
    mode = CS_MODE_64 if pe.is_64 else CS_MODE_32
    md = Cs(CS_ARCH_X86, mode)
    md.detail = False
    wanted = selected_name.casefold() if selected_name else None
    if wanted:
        candidates = [
            symbol for symbol in symbols
            if str(symbol["name"]).casefold() == wanted
            and (section := pe.section_for_rva(int(symbol["rva"]))) is not None
            and section.executable
        ]
    else:
        export_names = {
            name for entry in pe.exports() if entry["name"] and not entry["forwarder"]
            for name in str(entry["name"]).split(";")
        }
        candidates = [
            symbol for symbol in symbols
            if str(symbol["name"]) in export_names
            and (section := pe.section_for_rva(int(symbol["rva"]))) is not None
            and section.executable
        ][:25]
    if wanted and not candidates:
        near = [str(s["name"]) for s in symbols if wanted in str(s["name"]).casefold()][:20]
        raise AnalysisError(f"No executable PDB symbol named {selected_name!r}. Similar: {near}")
    if not candidates:
        raise AnalysisError("No named executable exports found to disassemble")

    by_rva: dict[int, list[str]] = defaultdict(list)
    for symbol in symbols:
        if (section := pe.section_for_rva(int(symbol["rva"]))) is not None and section.executable:
            by_rva[int(symbol["rva"])].append(str(symbol["name"]))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        f.write("; Capstone x86-64 disassembly with PDB public symbols\n")
        f.write("; This output is annotated assembly, not recovered original C source.\n\n")
        for symbol in candidates:
            start = int(symbol["rva"])
            section = pe.section_for_rva(start)
            assert section is not None
            sec_end = section.virtual_address + section.extent
            later = [r for r in by_rva if r > start]
            limit_end = min([start + max_bytes, sec_end] + later) if later else min(start + max_bytes, sec_end)
            code = pe.bytes_at_rva(start, max(0, limit_end - start))
            f.write(f"; {symbol['name']}  RVA=0x{start:08X}  size={symbol['size']}\n")
            for insn in md.disasm(code, pe.image_base + start):
                rva = insn.address - pe.image_base
                labels = by_rva.get(rva)
                if labels:
                    f.write(f"\nloc_{rva:08X}: ; {' | '.join(labels)}\n")
                f.write(f"  {rva:08X}  {insn.mnemonic:<8} {insn.op_str}\n")
                if insn.mnemonic.lower().startswith("ret") or insn.mnemonic.lower() == "int3":
                    break
            f.write("\n")
    return len(candidates)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exe", type=Path, default=DEFAULT_EXE, help="PE image path")
    parser.add_argument("--pdb", type=Path, help="matching PDB path (downloaded automatically if omitted)")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT, help="analysis output directory")
    parser.add_argument("--disassemble", help="PDB function name; omit to disassemble up to 25 exported symbols")
    parser.add_argument("--max-bytes", type=int, default=512, help="maximum bytes per function")
    args = parser.parse_args()

    try:
        pe = PEImage(args.exe)
        identity = pe.debug_pdb_identity()
        if not identity:
            raise AnalysisError("No CodeView RSDS PDB identity found in the executable")
        pdb_path = args.pdb
        if pdb_path is None:
            pdb_path, identity = download_pdb(pe, DEFAULT_PDB_CACHE)
        elif not pdb_path.is_file():
            raise AnalysisError(f"PDB file does not exist: {pdb_path}")
        args.out_dir.mkdir(parents=True, exist_ok=True)

        exports = pe.exports()
        imports = pe.imports()
        write_csv(args.out_dir / "exports.csv", exports,
                  ["ordinal", "name", "rva", "forwarder", "kind"])
        write_csv(args.out_dir / "imports.csv", imports,
                  ["dll", "name", "hint", "ordinal", "lookup_rva", "iat_rva"])

        symbols = []
        function_records: list[dict[str, object]] = []
        runtime_function_count = 0
        unnamed_runtime_function_count = 0
        additional_code_candidate_count = 0
        pdb_error = None
        try:
            with DbgHelpSymbols(pe, pdb_path) as handler:
                symbols = handler.symbols
                write_csv(args.out_dir / "pdb_symbols.csv", [
                    {**s, "rva": f"0x{int(s['rva']):08X}"} for s in symbols
                ], ["name", "rva", "size", "tag", "flags", "type_index"])
                disasm_count = disassemble(
                    pe, symbols, args.disassemble,
                    args.out_dir / "disassembly.asm", args.max_bytes
                )
                symbols_by_rva: dict[int, list[str]] = defaultdict(list)
                executable_symbol_details: dict[int, list[dict[str, object]]] = defaultdict(list)
                for symbol in symbols:
                    rva = int(symbol["rva"])
                    symbols_by_rva[rva].append(str(symbol["name"]))
                    section = pe.section_for_rva(rva)
                    if section is not None and section.executable:
                        executable_symbol_details[rva].append(
                            {
                                "name": str(symbol["name"]),
                                "tag": int(symbol["tag"]),
                                "size_bytes": int(symbol["size"]),
                                "type_index": int(symbol["type_index"]),
                            }
                        )
                write_csv(
                    args.out_dir / "exports_with_symbols.csv",
                    [
                        {**entry, "pdb_symbols": ";".join(
                            symbols_by_rva.get(int(str(entry["rva"]), 16), [])
                        )}
                        for entry in exports
                    ],
                    ["ordinal", "name", "rva", "forwarder", "kind", "pdb_symbols"],
                )
                exports_by_rva: dict[int, list[str]] = defaultdict(list)
                for entry in exports:
                    if entry["forwarder"]:
                        continue
                    export_rva = int(str(entry["rva"]), 16)
                    export_names = [n for n in str(entry["name"]).split(";") if n]
                    if export_names:
                        exports_by_rva[export_rva].extend(export_names)
                for symbol in symbols:
                    rva = int(symbol["rva"])
                    section = pe.section_for_rva(rva)
                    # DbgHelp's SymTagFunction value is 5. Restrict these records
                    # to executable PE sections to avoid non-code records.
                    if int(symbol["tag"]) != 5 or section is None or not section.executable:
                        continue
                    function_records.append(
                        {
                            "name": str(symbol["name"]),
                            "rva": rva,
                            "rva_hex": f"0x{rva:08X}",
                            "va": pe.image_base + rva,
                            "va_hex": f"0x{pe.image_base + rva:016X}",
                            "size_bytes": int(symbol["size"]),
                            "section": section.name,
                            "export_names": sorted(set(exports_by_rva.get(rva, []))),
                            "pdb_tag": int(symbol["tag"]),
                            "pdb_type_index": int(symbol["type_index"]),
                            "flags": int(symbol["flags"]),
                        }
                    )
                function_records.sort(key=lambda f: (f["rva"], f["name"]))
                (args.out_dir / "pdb_functions.json").write_text(
                    json.dumps(
                        {
                            "schema_version": 1,
                            "image": str(args.exe),
                            "image_base": pe.image_base,
                            "image_base_hex": f"0x{pe.image_base:016X}",
                            "pdb": {
                                "path": str(pdb_path),
                                "name": identity[3],
                                "guid": identity[0],
                                "age": identity[2],
                                "symbol_key": identity[1],
                            },
                            "symbol_kind": "DbgHelp SymTagFunction (5), executable-section entries",
                            "function_count": len(function_records),
                            "functions": function_records,
                        },
                        ensure_ascii=False,
                        indent=2,
                    )
                    + "\n",
                    encoding="utf-8",
                )

                runtime_entries = pe.x64_runtime_functions()
                runtime_by_rva = {int(entry["begin_rva"]): entry for entry in runtime_entries}
                executable_exports_by_rva: dict[int, list[str]] = defaultdict(list)
                for entry in exports:
                    if entry["forwarder"]:
                        continue
                    export_rva = int(str(entry["rva"]), 16)
                    section = pe.section_for_rva(export_rva)
                    if section is not None and section.executable and entry["name"]:
                        executable_exports_by_rva[export_rva].extend(
                            name for name in str(entry["name"]).split(";") if name
                        )

                all_executable_functions = []
                for entry in runtime_entries:
                    begin = int(entry["begin_rva"])
                    end = int(entry["end_rva"])
                    pdb_records = executable_symbol_details.get(begin, [])
                    pdb_names = sorted({str(record["name"]) for record in pdb_records})
                    all_executable_functions.append(
                        {
                            "rva": begin,
                            "rva_hex": f"0x{begin:08X}",
                            "end_rva": end,
                            "end_rva_hex": f"0x{end:08X}",
                            "size_bytes": end - begin,
                            "unwind_info_rva": int(entry["unwind_info_rva"]),
                            "unwind_info_rva_hex": f"0x{int(entry['unwind_info_rva']):08X}",
                            "section": str(entry["section"]),
                            "name": pdb_names[0] if pdb_names else None,
                            "pdb_symbols": pdb_records,
                            "export_names": sorted(set(executable_exports_by_rva.get(begin, []))),
                            "has_pdb_name": bool(pdb_names),
                            "has_pdb_function_record": any(int(record["tag"]) == 5 for record in pdb_records),
                            "discovery": "x64 PE exception directory RUNTIME_FUNCTION entry",
                        }
                    )

                candidate_rvas = set(executable_symbol_details) - set(runtime_by_rva)
                candidate_rvas.update(set(executable_exports_by_rva) - set(runtime_by_rva))
                additional_code_candidates = []
                for candidate_rva in sorted(candidate_rvas):
                    section = pe.section_for_rva(candidate_rva)
                    if section is None or not section.executable:
                        continue
                    additional_code_candidates.append(
                        {
                            "rva": candidate_rva,
                            "rva_hex": f"0x{candidate_rva:08X}",
                            "section": section.name,
                            "pdb_symbols": executable_symbol_details.get(candidate_rva, []),
                            "export_names": sorted(set(executable_exports_by_rva.get(candidate_rva, []))),
                            "classification": "possible leaf function, alternate entry, stub, or code label; no unwind-table start",
                        }
                    )

                exception_rva, exception_size = pe.directory(3)
                unnamed_runtime_functions = sum(
                    not executable_symbol_details.get(int(entry["begin_rva"]))
                    for entry in runtime_entries
                )
                runtime_function_count = len(all_executable_functions)
                unnamed_runtime_function_count = unnamed_runtime_functions
                additional_code_candidate_count = len(additional_code_candidates)
                (args.out_dir / "all_executable_functions.json").write_text(
                    json.dumps(
                        {
                            "schema_version": 1,
                            "image": str(args.exe),
                            "architecture": "x64" if pe.is_64 else "x86",
                            "image_base": pe.image_base,
                            "image_base_hex": f"0x{pe.image_base:016X}",
                            "pdb": {
                                "path": str(pdb_path),
                                "name": identity[3],
                                "guid": identity[0],
                                "age": identity[2],
                                "symbol_key": identity[1],
                            },
                            "executable_sections": [
                                {
                                    "name": section.name,
                                    "start_rva": section.virtual_address,
                                    "start_rva_hex": f"0x{section.virtual_address:08X}",
                                    "end_rva": section.virtual_address + section.extent,
                                    "end_rva_hex": f"0x{section.virtual_address + section.extent:08X}",
                                }
                                for section in pe.sections if section.executable
                            ],
                            "counts": {
                                "runtime_function_table_records_in_executable_sections": len(all_executable_functions),
                                "runtime_function_records_without_pdb_symbol_name": unnamed_runtime_functions,
                                "pdb_symtag_function_records": len(function_records),
                                "additional_code_symbol_candidates_without_unwind_start": len(additional_code_candidates),
                            },
                            "exception_directory": {
                                "rva": exception_rva,
                                "rva_hex": f"0x{exception_rva:08X}",
                                "size_bytes": exception_size,
                                "raw_record_count": exception_size // 12,
                            },
                            "function_boundary_basis": "Each item in functions is an x64 RUNTIME_FUNCTION range from the PE exception directory. Unnamed entries are retained.",
                            "additional_candidate_note": "additional_code_symbol_candidates lists executable PDB symbols or exports that are not starts in the unwind table; entries can be leaf routines, alternate entries, stubs, or labels.",
                            "completeness_note": "The unwind table gives explicit ranges for functions with unwind metadata. x64 leaf routines may omit unwind entries; candidates are included separately. A stripped unnamed leaf routine with no metadata cannot be distinguished with certainty from code bytes alone.",
                            "function_count": len(all_executable_functions),
                            "functions": all_executable_functions,
                            "additional_code_symbol_candidates": additional_code_candidates,
                        },
                        ensure_ascii=False,
                        indent=2,
                    )
                    + "\n",
                    encoding="utf-8",
                )
        except (AnalysisError, OSError) as exc:
            pdb_error = str(exc)
            disasm_count = 0

        version = "unknown"
        try:
            import ctypes.wintypes as wt
            version_dll = ctypes.WinDLL("version", use_last_error=True)
            size = version_dll.GetFileVersionInfoSizeW(str(args.exe), None)
            if size:
                buffer = ctypes.create_string_buffer(size)
                if version_dll.GetFileVersionInfoW(str(args.exe), 0, size, buffer):
                    value_ptr = ctypes.c_void_p()
                    value_len = wt.UINT()
                    if version_dll.VerQueryValueW(buffer, "\\", ctypes.byref(value_ptr), ctypes.byref(value_len)):
                        class VS_FIXEDFILEINFO(ctypes.Structure):
                            _fields_ = [("dwSignature", wt.DWORD), ("dwStrucVersion", wt.DWORD),
                                        ("dwFileVersionMS", wt.DWORD), ("dwFileVersionLS", wt.DWORD),
                                        ("dwProductVersionMS", wt.DWORD), ("dwProductVersionLS", wt.DWORD),
                                        ("dwFileFlagsMask", wt.DWORD), ("dwFileFlags", wt.DWORD),
                                        ("dwFileOS", wt.DWORD), ("dwFileType", wt.DWORD),
                                        ("dwFileSubtype", wt.DWORD), ("dwFileDateMS", wt.DWORD),
                                        ("dwFileDateLS", wt.DWORD)]
                        info = ctypes.cast(value_ptr, ctypes.POINTER(VS_FIXEDFILEINFO)).contents
                        version = ".".join(str(v) for v in [info.dwFileVersionMS >> 16,
                                                           info.dwFileVersionMS & 0xFFFF,
                                                           info.dwFileVersionLS >> 16,
                                                           info.dwFileVersionLS & 0xFFFF])
        except Exception:
            pass

        guid, key, age, pdb_name = identity
        summary = [
            "# ntoskrnl.exe analysis summary",
            "",
            f"- Executable: `{args.exe}`",
            f"- File version: `{version}`",
            f"- Architecture: `{ 'x64' if pe.is_64 else 'x86' }`",
            f"- PDB: `{pdb_path}`",
            f"- PDB identity: `{guid}` age `{age}` (symbol key `{key}`)",
            f"- Exports: **{len(exports)}** entries (`exports.csv`)",
            f"- Imports: **{len(imports)}** entries (`imports.csv`)",
            f"- PDB public symbols: **{len(symbols)}** (`pdb_symbols.csv`)",
            f"- PDB Function records: **{len(function_records)}** (`pdb_functions.json`)",
            f"- Executable-section runtime functions: **{runtime_function_count}** (`all_executable_functions.json`)",
            f"- Runtime functions without a PDB name: **{unnamed_runtime_function_count}**",
            f"- Additional code-symbol candidates outside unwind starts: **{additional_code_candidate_count}**",
            f"- Exports joined to PDB names: `exports_with_symbols.csv`",
            f"- Disassembled functions: **{disasm_count}** (`disassembly.asm`)",
            "",
            "## 사용 방법",
            "",
            f"- 전체 분석/목록 재생성: `python \"{Path(__file__).resolve()}\"`",
            f"- 함수 하나 디스어셈블: `python \"{Path(__file__).resolve()}\" --disassemble KeInsertQueueApc`",
            "- 실행 파일이나 PDB 경로 변경: `--exe <경로> --pdb <경로>`",
            "- Capstone이 없으면 `python -m pip install capstone`으로 설치합니다.",
            "",
            "Import entries do not have implementation RVAs in this image. The CSV records each import's lookup-table RVA and IAT slot RVA.",
            "`pdb_functions.json` contains PDB entries classified by DbgHelp as SymTagFunction (5), limited to executable sections.",
            "`all_executable_functions.json` lists every executable x64 unwind-table function range, including entries without PDB names; possible leaf functions or labels outside that table are listed separately.",
            "PDB public symbols provide names and addresses, not the original private C source. The assembly listing is not source recovery.",
        ]
        if pdb_error:
            summary.extend(["", f"PDB/disassembly warning: `{pdb_error}`"])
        (args.out_dir / "README.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
        print("\n".join(summary))
        return 0 if not pdb_error else 2
    except (AnalysisError, OSError, struct.error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
