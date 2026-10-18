#!/usr/bin/env python3
"""Build the offline all-in-one browser for reports and per-function CFGs."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


PREFIX = b"window.NTOSKRNL_GRAPHS="


def skip_space(data: bytes, position: int) -> int:
    while position < len(data) and data[position] in b" \t\r\n":
        position += 1
    return position


def object_end(data: bytes, start: int) -> int:
    if start >= len(data) or data[start] != ord("{"):
        raise ValueError(f"Graph value at byte {start} is not an object")
    depth = 0
    in_string = False
    escaped = False
    for position in range(start, len(data)):
        char = data[position]
        if in_string:
            if escaped:
                escaped = False
            elif char == ord("\\"):
                escaped = True
            elif char == ord('"'):
                in_string = False
            continue
        if char == ord('"'):
            in_string = True
        elif char == ord("{"):
            depth += 1
        elif char == ord("}"):
            depth -= 1
            if depth == 0:
                return position + 1
    raise ValueError(f"Unclosed graph object beginning at byte {start}")


def graph_offsets(path: Path) -> list[list[Any]]:
    data = path.read_bytes()
    if not data.startswith(PREFIX):
        raise ValueError(f"Unexpected graph data format in {path}")
    position = skip_space(data, len(PREFIX))
    if data[position] != ord("{"):
        raise ValueError(f"Missing graph bundle object in {path}")
    position += 1
    result: list[list[Any]] = []
    relative_file = f"graphs/{path.name}"
    while True:
        position = skip_space(data, position)
        if position >= len(data):
            raise ValueError(f"Unexpected end of graph data in {path}")
        if data[position] == ord("}"):
            break
        if data[position] == ord(","):
            position = skip_space(data, position + 1)
        if data[position] != ord('"'):
            raise ValueError(f"Expected graph RVA key at byte {position} in {path}")
        key_end = data.find(b'"', position + 1)
        if key_end < 0:
            raise ValueError(f"Unclosed graph RVA key in {path}")
        key = data[position + 1:key_end].decode("ascii").upper()
        position = skip_space(data, key_end + 1)
        if data[position] != ord(":"):
            raise ValueError(f"Missing colon after {key} in {path}")
        value_start = skip_space(data, position + 1)
        value_end = object_end(data, value_start)
        result.append([key, relative_file, value_start, value_end - value_start])
        position = value_end
    return result


def safe_script_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, separators=(",", ":")).replace("</", "<\\/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    root = args.root.resolve()
    template_path = root / "control-panel.template.html"
    template = template_path.read_text(encoding="utf-8")

    index = json.loads((root / "function-index.json").read_text(encoding="utf-8"))
    rows = [[
        row["rva_hex"], row["name"], row["section"], row["report"], row["end_rva"],
        row["blocks"], row["instructions"], row["has_pdb_name"],
    ] for row in index]

    offsets: list[list[Any]] = []
    for graph_path in sorted((root / "graphs").glob("*.js")):
        offsets.extend(graph_offsets(graph_path))
    if len(rows) != len(offsets):
        raise ValueError(f"Index has {len(rows)} reports but graph data has {len(offsets)} entries")
    graph_keys = {item[0] for item in offsets}
    missing = [row[0] for row in rows if row[0].upper() not in graph_keys]
    if missing:
        raise ValueError(f"No graph bundle for {len(missing)} function RVAs; first is {missing[0]}")

    html = template.replace("__FUNCTION_ROWS__", safe_script_json(rows))
    html = html.replace("__GRAPH_OFFSETS__", safe_script_json(offsets))
    if "__FUNCTION_ROWS__" in html or "__GRAPH_OFFSETS__" in html:
        raise ValueError("A data placeholder was not expanded")
    target = root / "control-panel.html"
    target.write_text(html, encoding="utf-8", newline="\n")
    simulator_builder = root / "build_simulator.py"
    if simulator_builder.is_file():
        image = json.loads((root / "summary.json").read_text(encoding="utf-8")).get("image", "C:/Windows/System32/ntoskrnl.exe")
        subprocess.run([sys.executable, str(simulator_builder), "--root", str(root), "--exe", image], check=True)
    print(f"Built {target} with {len(rows):,} functions and {len(offsets):,} graph offsets ({target.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
