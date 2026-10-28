#!/usr/bin/env python3
"""Start a temporary authenticated localhost JupyterLab and fetch a notebook."""

import argparse
import json
import os
import secrets
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="lovam-jupyter-") as temp:
        directory = Path(temp)
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            port = listener.getsockname()[1]
        token = secrets.token_urlsafe(32)
        config = directory / "jupyter_config.json"
        config.write_text(
            json.dumps(
                {
                    "IdentityProvider": {"token": token},
                    "ServerApp": {
                        "root_dir": str(root),
                        "ip": "127.0.0.1",
                        "port": port,
                        "port_retries": 0,
                        "open_browser": False,
                    },
                }
            )
        )
        config.chmod(0o600)
        env = os.environ.copy()
        env.update(JUPYTER_RUNTIME_DIR=temp, IPYTHONDIR=temp, MPLCONFIGDIR=temp)
        with (directory / "server.log").open("w") as log:
            process = subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "jupyterlab",
                    "--no-browser",
                    "--config=" + str(config),
                    "--ServerApp.root_dir=" + str(root),
                ],
                cwd=root,
                env=env,
                stdout=log,
                stderr=log,
            )
            try:
                base = f"http://127.0.0.1:{port}"

                def request(path):
                    req = urllib.request.Request(
                        base + path, headers={"Authorization": "token " + token}
                    )
                    with urllib.request.urlopen(req, timeout=3) as response:
                        return response.status, response.read()

                deadline = time.monotonic() + 60
                while True:
                    try:
                        status, _ = request("/api/status")
                        break
                    except (OSError, ValueError):
                        if process.poll() is not None or time.monotonic() > deadline:
                            raise RuntimeError(
                                "Jupyter server did not become ready; see local execution log"
                            )
                        time.sleep(0.5)
                assert status == 200
                status, data = request(
                    "/api/contents/experiments/environment-checks/environment-smoke.ipynb"
                )
                notebook = json.loads(data)
                assert status == 200 and notebook["type"] == "notebook"
                assert (
                    notebook["content"]["metadata"]["kernelspec"]["name"]
                    == "lovam-study"
                )
                assert request("/lab")[0] == 200
                result = {
                    "status": "pass",
                    "interface": "127.0.0.1",
                    "lab_http": 200,
                    "notebook_http": 200,
                    "notebook_kernel": "lovam-study",
                    "authentication": "temporary token",
                }
            except Exception:
                diagnostic = root / ".local/environment/jupyter-server-debug.log"
                diagnostic.parent.mkdir(parents=True, exist_ok=True)
                log.flush()
                diagnostic.write_text(
                    (directory / "server.log").read_text().replace(token, "[redacted]")
                )
                try:
                    _, listing = request("/api/contents")
                    summary = json.loads(listing)
                    print(
                        "Server root entries:",
                        [x["name"] for x in summary.get("content", [])],
                    )
                except OSError:
                    pass
                raise
            finally:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)


if __name__ == "__main__":
    main()
