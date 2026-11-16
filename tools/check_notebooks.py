#!/usr/bin/env python3
"""Execute tiny notebooks in each registered local kernel, never old exercises."""

import argparse
import json
import os
import tempfile
from pathlib import Path


def main():
    import nbformat
    from nbclient import NotebookClient

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    results = []
    with tempfile.TemporaryDirectory(prefix="lovam-notebooks-") as temp:
        os.environ.setdefault("JUPYTER_RUNTIME_DIR", temp)
        os.environ.setdefault("MPLCONFIGDIR", temp)
        os.environ.setdefault("IPYTHONDIR", temp)
        for profile, code in {
            "study": 'import numpy as np, pandas as pd\nassert np.arange(3).sum() == 3\nassert pd.DataFrame({"x": [42]}).iloc[0, 0] == 42',
            "tensorflow": "import tensorflow as tf\nassert float(tf.reduce_sum(tf.constant([1., 2.]))) == 3.",
            "torch": "import torch\nassert torch.tensor([1, 2]).sum().item() == 3",
        }.items():
            prefix = f'import sys\nfrom pathlib import Path\nassert Path(sys.prefix).name == ".venv-{profile}"\n'
            notebook = nbformat.v4.new_notebook(
                cells=[nbformat.v4.new_code_cell(prefix + code)]
            )
            try:
                executed = NotebookClient(
                    notebook,
                    kernel_name="lovam-" + profile,
                    timeout=60,
                    resources={"metadata": {"path": str(root)}},
                ).execute()
                assert executed.cells[0].execution_count is not None
                results.append(
                    {"profile": profile, "kernel": "lovam-" + profile, "status": "pass"}
                )
            except Exception as exc:
                results.append(
                    {
                        "profile": profile,
                        "kernel": "lovam-" + profile,
                        "status": "fail",
                        "detail": type(exc).__name__ + ": " + str(exc),
                    }
                )
    text = json.dumps(results, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)
    return int(any(result["status"] == "fail" for result in results))


if __name__ == "__main__":
    raise SystemExit(main())
