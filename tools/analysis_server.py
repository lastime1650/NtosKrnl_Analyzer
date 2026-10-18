#!/usr/bin/env python3
"""Loopback-only HTTP bridge for the dynamic ntoskrnl analysis control panel."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
import subprocess
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote, urlsplit


JOBS: dict[str, dict[str, Any]] = {}
JOBS_LOCK = threading.Lock()
FOLDER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._ -]{0,79}$")
RESERVED_NAMES = {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}


def is_child(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


class Server(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address: tuple[str, int], root: Path):
        self.root = root.resolve()
        super().__init__(address, Handler)


class Handler(BaseHTTPRequestHandler):
    server: Server
    protocol_version = "HTTP/1.1"

    def log_message(self, format: str, *args: object) -> None:
        sys.stdout.write("[%s] %s\n" % (self.log_date_time_string(), format % args))
        sys.stdout.flush()

    def _loopback_request(self) -> bool:
        allowed_hosts = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        if self.client_address[0] != "127.0.0.1" or self.headers.get("Host", "").lower() not in allowed_hosts:
            self.send_error(403, "Loopback requests only")
            return False
        origin = self.headers.get("Origin")
        if origin and origin not in {f"http://127.0.0.1:{self.server.server_port}", f"http://localhost:{self.server.server_port}"}:
            self.send_error(403, "Cross-origin requests are not accepted")
            return False
        return True

    def _json(self, status: int, value: dict[str, Any]) -> None:
        data = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def _job_data(self, job: dict[str, Any]) -> dict[str, Any]:
        state_path = job["out"] / ".analysis-state.json"
        state: dict[str, Any] = {}
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
        process: subprocess.Popen[bytes] | None = job.get("process")
        if process is not None and process.poll() is not None and state.get("status") not in {"completed", "failed"}:
            status = "completed" if process.returncode == 0 else "failed"
            state.update({"status": status, "phase": status, "message": "분석 완료" if status == "completed" else f"분석 실패 · exit code {process.returncode}"})
            state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        try:
            log = job["log"].read_text(encoding="utf-8", errors="replace")[-14000:]
        except OSError:
            log = ""
        folder = job["out"].name
        result_url = "/analyses/" + quote(folder, safe="") + "/control-panel.html"
        return {
            "job_id": job["id"],
            "status": state.get("status", "running"),
            "phase": state.get("phase", "starting"),
            "message": state.get("message", "분석 작업을 시작하는 중"),
            "destination": str(job["out"]),
            "log_tail": log,
            "result_url": result_url if state.get("status") == "completed" else None,
            "error_type": state.get("error_type"),
        }

    def do_GET(self) -> None:
        if not self._loopback_request():
            return
        request_path = unquote(urlsplit(self.path).path)
        if request_path == "/api/health":
            root = self.server.root
            self._json(200, {"ok": True, "project_root": str(root), "default_folder": root.name, "analysis_root": str(root / "analyses"), "port": self.server.server_port})
            return
        if request_path.startswith("/api/jobs/"):
            job_id = request_path.rsplit("/", 1)[-1]
            with JOBS_LOCK:
                job = JOBS.get(job_id)
            if not job:
                self._json(404, {"error": "Analysis job not found"})
                return
            self._json(200, self._job_data(job))
            return
        if request_path in {"/", "/control-panel.html"}:
            target = self.server.root / "control-panel.html"
        elif request_path.startswith(("/analyses/", "/simulator/", "/functions/")):
            relative = request_path.lstrip("/")
            target = (self.server.root / Path(relative)).resolve()
            if not is_child(target, self.server.root) or any(part.startswith(".") for part in Path(relative).parts):
                self.send_error(404)
                return
        else:
            self.send_error(404)
            return
        if not target.is_file():
            self.send_error(404, "File not found")
            return
        content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", content_type + ("; charset=utf-8" if content_type.startswith("text/") or content_type in {"application/json", "application/javascript"} else ""))
        self.send_header("Content-Length", str(target.stat().st_size))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        with target.open("rb") as source:
            while chunk := source.read(256 * 1024):
                self.wfile.write(chunk)

    def do_POST(self) -> None:
        if not self._loopback_request():
            return
        if urlsplit(self.path).path != "/api/analyze":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 16_384:
                raise ValueError("Invalid request size")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            folder_name = str(payload.get("folder_name", "")).strip()
            exe_text = str(payload.get("exe_path", "")).strip().strip('"')
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            self._json(400, {"error": "요청 형식이 올바르지 않습니다: " + str(exc)})
            return
        if not FOLDER_RE.fullmatch(folder_name) or folder_name in {".", ".."} or folder_name.endswith((".", " ")) or folder_name.split(".")[0].upper() in RESERVED_NAMES:
            self._json(400, {"error": "폴더명은 영문·숫자로 시작하고, 끝에 공백이나 점이 올 수 없습니다. Windows 예약 이름도 사용할 수 없습니다."})
            return
        exe = Path(exe_text).expanduser()
        if exe.name.casefold() != "ntoskrnl.exe" or not exe.is_file():
            self._json(400, {"error": "존재하는 ntoskrnl.exe 파일 경로를 입력하세요."})
            return
        root = self.server.root
        analyses = root / "analyses"
        analyses.mkdir(exist_ok=True)
        if not is_child(analyses, root):
            self._json(400, {"error": "분석 출력 폴더 경로가 프로젝트 폴더를 벗어납니다."})
            return
        out = analyses / folder_name
        with JOBS_LOCK:
            active = [j for j in JOBS.values() if j["process"] is not None and j["process"].poll() is None]
            if active:
                self._json(409, {"error": "이미 동적 분석 작업이 실행 중입니다. 진행이 끝난 뒤 다시 요청하세요."})
                return
            try:
                out.mkdir(exist_ok=False)
            except FileExistsError:
                self._json(409, {"error": "같은 이름의 분석 폴더가 이미 있습니다. 다른 이름을 입력하세요."})
                return
            job_id = uuid.uuid4().hex
            log_path = out / "analysis.log"
            state_path = out / ".analysis-state.json"
            state_path.write_text(json.dumps({"status": "running", "phase": "starting", "message": "분석 프로세스 시작"}, ensure_ascii=False), encoding="utf-8")
            command = [sys.executable, str(root / "tools" / "analysis_runner.py"), "--root", str(root), "--exe", str(exe.resolve()), "--out", str(out)]
            env = os.environ.copy()
            env["PYTHONUNBUFFERED"] = "1"
            env["PYTHONIOENCODING"] = "utf-8:replace"
            env["PYTHONUTF8"] = "1"
            creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
            with log_path.open("ab") as log_file:
                process = subprocess.Popen(
                    command,
                    cwd=str(root),
                    stdin=subprocess.DEVNULL,
                    stdout=log_file,
                    stderr=subprocess.STDOUT,
                    env=env,
                    creationflags=creationflags,
                )
            job = {"id": job_id, "out": out, "log": log_path, "process": process, "created": time.time(), "exe": str(exe.resolve())}
            JOBS[job_id] = job
        self._json(202, self._job_data(job))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    root = args.root.resolve()
    if not (root / "control-panel.html").is_file() or not (root / "tools" / "analysis_runner.py").is_file():
        raise SystemExit(f"Incomplete project root: {root}")
    server = Server(("127.0.0.1", args.port), root)
    print(f"Dynamic analysis service listening at http://127.0.0.1:{args.port}/", flush=True)
    print(f"Project root: {root}", flush=True)
    try:
        server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
