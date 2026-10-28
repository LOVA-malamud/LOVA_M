#!/usr/bin/env python3
"""Register available project kernels inside .venv-study, never globally."""

import os
import subprocess
import tempfile
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    study = root / ".venv-study"
    if not (study / "bin/python").exists():
        raise SystemExit("Create .venv-study first; see PYTHON_ENVIRONMENT.md")
    with tempfile.TemporaryDirectory(prefix="lovam-register-") as temp:
        env = dict(os.environ, IPYTHONDIR=temp)
        for profile in ["study", "tensorflow", "torch"]:
            python = root / (".venv-" + profile) / "bin/python"
            if not python.exists():
                print("Skipped missing optional environment:", profile)
                continue
            subprocess.run(
                [
                    str(python),
                    "-m",
                    "ipykernel",
                    "install",
                    "--prefix",
                    str(study),
                    "--name",
                    "lovam-" + profile,
                    "--display-name",
                    "LOVA_M · " + profile + " (Python 3.12)",
                ],
                env=env,
                check=True,
            )


if __name__ == "__main__":
    main()
