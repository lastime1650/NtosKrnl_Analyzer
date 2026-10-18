#!/usr/bin/env python3
"""Rename function reports to <symbol>_function_<RVA>.md and repair links."""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path


def load_builder(path: Path):
    spec = importlib.util.spec_from_file_location("ntk2c_builder", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load report builder: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    root = args.root.resolve()
    builder = load_builder(root / "build_reports.py")
    inventory = json.loads((root / "data" / "all_executable_functions.json").read_text(encoding="utf-8"))

    file_names: dict[int, str] = {}
    moves: list[tuple[Path, Path]] = []
    for record in inventory["functions"]:
        rva = int(record["rva"])
        section = builder.slug(str(record.get("section") or "unknown"))
        shard = f"{(rva >> 16) & 0xFF:02X}"
        directory = root / "functions" / section / shard
        old_path = directory / f"function_{rva:08X}.md"
        new_name = builder.report_filename(record)
        new_path = directory / new_name
        file_names[rva] = new_name
        if old_path.exists() and old_path != new_path:
            if new_path.exists():
                raise FileExistsError(f"Both old and new report paths exist: {old_path} ; {new_path}")
            moves.append((old_path, new_path))
        elif new_path.exists():
            continue  # Already renamed; this also makes the migration restartable.
        else:
            raise FileNotFoundError(f"Neither report path exists: {old_path} ; {new_path}")

    print(f"Renaming report files: {len(moves):,}/{len(file_names):,}", flush=True)
    for index, (old_path, new_path) in enumerate(moves, 1):
        old_path.rename(new_path)
        if index % 5000 == 0:
            print(f"Renamed {index:,}/{len(moves):,}", flush=True)

    basename_pattern = re.compile(rb"(?<![A-Za-z0-9_.-])function_([0-9A-Fa-f]{8})\.md")

    def replace_reference(match: re.Match[bytes]) -> bytes:
        rva = int(match.group(1), 16)
        new_name = file_names.get(rva)
        if new_name is None:
            return match.group(0)
        return new_name.encode("ascii")

    extensions = {".md", ".json", ".js", ".html", ".ps1", ".py", ".txt"}
    updated_files = 0
    replaced_references = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in extensions:
            continue
        original = path.read_bytes()
        if b"function_" not in original:
            continue
        updated, count = basename_pattern.subn(replace_reference, original)
        if count:
            temp_path = path.with_name(path.name + ".rename-tmp")
            temp_path.write_bytes(updated)
            temp_path.replace(path)
            updated_files += 1
            replaced_references += count

    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    filename_note = "- 파일명: 식별된 함수명 또는 `Unknown` 뒤에 `_function_RVA.md`를 붙입니다. RVA로 중복을 구분합니다."
    if filename_note not in readme:
        readme = readme.replace("- 검색: `function-index.json`을 검색하거나 보고서 파일명에서 RVA를 찾습니다.",
                                "- 검색: `function-index.json`을 검색하거나 보고서 파일명에서 RVA를 찾습니다.\n" + filename_note)
    readme_path.write_text(readme, encoding="utf-8", newline="\n")

    summary_path = root / "summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        summary["report_filename_convention"] = "<identified-symbol-or-Unknown>_function_<RVA>.md"
        summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    unknown_count = sum(1 for name in file_names.values() if name.startswith("Unknown_function_"))
    print(f"Updated {updated_files:,} text files and {replaced_references:,} report links.", flush=True)
    print(f"Complete: {len(file_names):,} reports renamed; {unknown_count:,} use the Unknown prefix.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
