#!/usr/bin/env python3
"""Build a version-specific ntoskrnl analysis project from a PE image and its matching PDB."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import traceback
from pathlib import Path
from typing import Any


def write_state(out: Path, status: str, phase: str, message: str, **extra: Any) -> None:
    state = {"status": status, "phase": phase, "message": message, **extra}
    (out / ".analysis-state.json").write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def run_step(command: list[str], cwd: Path, out: Path, phase: str, label: str) -> None:
    write_state(out, "running", phase, label)
    print("\n== " + label + " ==", flush=True)
    print("$ " + subprocess.list2cmdline(command), flush=True)
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8:replace"
    env["PYTHONUTF8"] = "1"
    process = subprocess.Popen(
        command,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
        env=env,
    )
    assert process.stdout is not None
    for line in process.stdout:
        print(line.rstrip("\r\n"), flush=True)
    code = process.wait()
    if code:
        raise RuntimeError(f"{label} exited with code {code}")


def update_pdb_path(json_path: Path, relative_path: str) -> None:
    if not json_path.exists():
        return
    value = json.loads(json_path.read_text(encoding="utf-8"))
    if isinstance(value.get("pdb"), dict):
        value["pdb"]["path"] = relative_path
    json_path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="NtKrnl2C tool root")
    parser.add_argument("--exe", required=True, type=Path, help="ntoskrnl.exe to analyze")
    parser.add_argument("--out", required=True, type=Path, help="new analysis project directory")
    args = parser.parse_args()

    root = args.root.resolve()
    exe = args.exe.resolve()
    out = args.out.resolve()
    if not exe.is_file() or exe.name.casefold() != "ntoskrnl.exe":
        raise FileNotFoundError(f"Expected an existing ntoskrnl.exe: {exe}")
    if os.name != "nt":
        raise RuntimeError("The PDB symbol enumerator requires Windows DbgHelp")
    try:
        import capstone  # noqa: F401
    except ImportError as exc:
        raise RuntimeError("Capstone is required. Install it with: python -m pip install capstone") from exc
    if not out.is_dir():
        raise FileNotFoundError(f"Reserved output directory is missing: {out}")

    tools_dir = root / "tools"
    analyzer = tools_dir / "ntoskrnl_disassembler.py"
    if not analyzer.is_file():
        raise FileNotFoundError(f"Inventory analyzer is missing: {analyzer}")

    (out / "source-analysis").mkdir(exist_ok=True)
    (out / "tools").mkdir(exist_ok=True)
    source_inventory = out / "source-analysis" / "all_executable_functions.json"
    write_state(out, "running", "inventory", "PE/PDB 인벤토리를 만드는 중")
    run_step(
        [sys.executable, str(analyzer), "--exe", str(exe), "--out-dir", str(out / "source-analysis")],
        root,
        out,
        "inventory",
        "PE, exports/imports, matching Microsoft PDB, and executable symbol inventory",
    )
    if not source_inventory.is_file():
        raise RuntimeError("The analyzer did not produce all_executable_functions.json")

    inventory = json.loads(source_inventory.read_text(encoding="utf-8"))
    function_count = int(inventory.get("function_count", 0))
    if function_count <= 0 or len(inventory.get("functions", [])) != function_count:
        raise RuntimeError("The generated runtime-function inventory is empty or inconsistent")

    pdb = inventory.get("pdb") or {}
    original_pdb = Path(str(pdb.get("path", "")))
    if not original_pdb.is_file():
        raise FileNotFoundError(f"Matching PDB was not found at the recorded path: {original_pdb}")
    symbols_dir = out / "symbols"
    symbols_dir.mkdir(exist_ok=True)
    pdb_target = symbols_dir / original_pdb.name
    shutil.copy2(original_pdb, pdb_target)
    pdb_relative = "symbols/" + pdb_target.name
    update_pdb_path(source_inventory, pdb_relative)
    update_pdb_path(out / "source-analysis" / "pdb_functions.json", pdb_relative)
    summary_path = out / "source-analysis" / "README.md"
    if summary_path.exists():
        summary_text = summary_path.read_text(encoding="utf-8")
        summary_text = re.sub(r"(?m)^- PDB: `[^`]*`$", "- PDB: `" + pdb_relative + "`", summary_text)
        summary_path.write_text(summary_text, encoding="utf-8", newline="\n")

    for name in ("build_reports.py", "add_beta_style.py", "build_control_panel.py", "control-panel.template.html", "build_simulator.py", "build_internal_graphs.py"):
        shutil.copy2(root / name, out / name)
    shutil.copytree(root / "simulator", out / "simulator", ignore=shutil.ignore_patterns("catalog.js", "internal-graphs", "internal-index.json", "__pycache__", "screenshots", "test-results", "release"))
    shutil.copy2(Path(__file__).resolve(), out / "tools" / "analysis_runner.py")
    shutil.copy2(analyzer, out / "tools" / analyzer.name)

    run_step(
        [sys.executable, str(out / "build_reports.py"), "--exe", str(exe), "--index", str(source_inventory), "--out", str(out)],
        out,
        out,
        "reports",
        f"Generate {function_count:,} function reports, disassembly, pseudocode, and control-flow graphs",
    )
    run_step(
        [sys.executable, str(out / "add_beta_style.py"), "--exe", str(exe), "--root", str(out)],
        out,
        out,
        "beta-c",
        "Generate the source-oriented C Style interpretation",
    )
    run_step(
        [sys.executable, str(out / "build_control_panel.py"), "--root", str(out)],
        out,
        out,
        "control-panel",
        "Build the all-in-one interactive control panel",
    )

    final_inventory = json.loads((out / "data" / "all_executable_functions.json").read_text(encoding="utf-8"))
    manifest = {
        "schema_version": 1,
        "analysis_status": "complete",
        "image": str(exe),
        "image_sha256": hashlib.sha256(exe.read_bytes()).hexdigest(),
        "image_size_bytes": exe.stat().st_size,
        "architecture": final_inventory.get("architecture"),
        "image_base": final_inventory.get("image_base_hex"),
        "pdb": {
            "name": pdb.get("name"),
            "guid": pdb.get("guid"),
            "age": pdb.get("age"),
            "symbol_key": pdb.get("symbol_key"),
            "stored_at": pdb_relative,
        },
        "runtime_function_count": function_count,
        "counts": final_inventory.get("counts", {}),
        "analysis_basis": "PE executable sections, x64 RUNTIME_FUNCTION entries, exports/imports, and the exact RSDS-matched Microsoft PDB.",
        "limitations": final_inventory.get("completeness_note", ""),
        "interpretation_note": "Markdown C-style output is an analysis reconstruction from machine code and symbols, not recovered original source code. Stripped leaf routines without metadata cannot all be distinguished from labels.",
        "artifacts": ["function-index.json", "data/all_executable_functions.json", "source-analysis/", "symbols/", "functions/", "graphs/", "control-panel.html", "simulator/"],
    }
    (out / "analysis-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_state(out, "completed", "complete", f"분석 완료 · {function_count:,}개 실행 함수 범위", manifest="analysis-manifest.json")
    print("\nAnalysis complete: " + str(out), flush=True)
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    try:
        exit_code = main()
    except Exception as exc:
        if len(sys.argv) >= 2:
            try:
                parsed = argparse.ArgumentParser(add_help=False)
                parsed.add_argument("--out", type=Path)
                known, _ = parsed.parse_known_args()
                if known.out:
                    write_state(known.out.resolve(), "failed", "failed", str(exc), error_type=type(exc).__name__)
            except Exception:
                pass
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        traceback.print_exc()
        raise
    raise SystemExit(exit_code)
