#!/usr/bin/env python3
"""Small, offline environment checks; no datasets, model downloads, or training.

Run with the appropriate interpreter and --profile study|tensorflow|torch.
The optional --output path receives JSON without personal data.
"""

import argparse
import asyncio
import importlib
import importlib.metadata
import io
import json
import os
import sys
import tempfile
from pathlib import Path

STUDY_IMPORTS = {
    "numpy": "numpy",
    "pandas": "pandas",
    "scipy": "scipy",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "scikit-learn": "sklearn",
    "statsmodels": "statsmodels.api",
    "openpyxl": "openpyxl",
    "jupyterlab": "jupyterlab",
    "notebook": "notebook",
    "ipykernel": "ipykernel",
    "pillow": "PIL",
    "opencv-python": "cv2",
    "imageio": "imageio.v3",
    "fastapi": "fastapi",
    "uvicorn": "uvicorn",
    "requests": "requests",
    "httpx": "httpx",
    "pydantic": "pydantic",
    "python-dotenv": "dotenv",
    "sqlalchemy": "sqlalchemy",
    "aiosqlite": "aiosqlite",
    "pytest": "pytest",
    "ruff": "ruff",
    "black": "black",
    "dmba": "dmba",
    "pygame": "pygame",
    "ipython": "IPython",
}


def study_checks():
    """Return named checks; each assertion tests actual package behavior."""

    def numpy_array():
        import numpy as np

        a = np.arange(6).reshape(2, 3)
        assert a.sum() == 15
        assert (a @ a.T).shape == (2, 2)

    def pandas_frame():
        import pandas as pd

        frame = pd.DataFrame({"group": ["a", "a", "b"], "score": [2, 4, 6]})
        assert frame.groupby("group")["score"].mean().to_dict() == {"a": 3, "b": 6}

    def matplotlib_plot():
        import matplotlib

        matplotlib.use("Agg")
        from matplotlib import pyplot as plt

        fig, ax = plt.subplots()
        ax.plot([0, 1, 2], [0, 1, 4])
        data = io.BytesIO()
        fig.savefig(data, format="png")
        plt.close(fig)
        assert data.getvalue().startswith(b"\x89PNG")

    def sklearn_model():
        import numpy as np
        from sklearn.linear_model import LinearRegression

        model = LinearRegression().fit([[0], [1], [2]], [1, 3, 5])
        np.testing.assert_allclose(model.predict([[3]]), [7])

    def scipy_statistics():
        import statsmodels.api as sm
        from scipy.stats import norm

        assert norm.cdf(0) == 0.5
        model = sm.OLS([1, 3, 5, 7], sm.add_constant([0, 1, 2, 3])).fit()
        assert abs(model.params[1] - 2) < 1e-9

    def plotly_figure():
        import plotly.graph_objects as go

        data = json.loads(go.Figure(go.Scatter(x=[1, 2], y=[3, 4])).to_json())
        assert data["data"][0]["type"] == "scatter"

    def excel_roundtrip():
        from openpyxl import Workbook, load_workbook

        book = Workbook()
        book.active.append(["score", 42])
        stream = io.BytesIO()
        book.save(stream)
        stream.seek(0)
        assert load_workbook(stream).active["B1"].value == 42

    def vision_roundtrip():
        import cv2
        import imageio.v3 as iio
        import numpy as np
        from PIL import Image

        image = np.zeros((8, 8, 3), dtype=np.uint8)
        image[:, :, 0] = 255
        assert cv2.cvtColor(image, cv2.COLOR_RGB2GRAY).shape == (8, 8)
        encoded = iio.imwrite("<bytes>", image, extension=".png")
        assert Image.open(io.BytesIO(encoded)).size == (8, 8)
        assert iio.imread(encoded, extension=".png").shape == (8, 8, 3)

    def fastapi_endpoint():
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from pydantic import BaseModel

        app = FastAPI()

        class Item(BaseModel):
            quantity: int

        @app.post("/double")
        def double(item: Item):
            return {"result": item.quantity * 2}

        with TestClient(app) as client:
            response = client.post("/double", json={"quantity": 21})
            assert response.status_code == 200
            assert response.json() == {"result": 42}
            assert (
                client.post("/double", json={"quantity": "invalid"}).status_code == 422
            )

    def http_and_dotenv():
        import httpx
        import requests
        from dotenv import dotenv_values

        prepared = requests.Request(
            "GET", "https://example.invalid", params={"q": "test"}
        ).prepare()
        assert "q=test" in prepared.url
        with httpx.Client(
            transport=httpx.MockTransport(
                lambda request: httpx.Response(200, json={"ok": True})
            )
        ) as client:
            assert client.get("https://example.invalid").json() == {"ok": True}
        assert (
            dotenv_values(stream=io.StringIO("LEARNING_EXAMPLE=demo"))[
                "LEARNING_EXAMPLE"
            ]
            == "demo"
        )

    def sqlite_async():
        import aiosqlite
        from sqlalchemy import create_engine, text

        with create_engine("sqlite:///:memory:").begin() as connection:
            assert connection.execute(text("SELECT 6 * 7")).scalar_one() == 42

        async def query():
            async with aiosqlite.connect(":memory:") as connection:
                async with connection.execute("SELECT 42") as cursor:
                    assert await cursor.fetchone() == (42,)

        asyncio.run(query())

    return dict(
        numpy_array=numpy_array,
        pandas_frame=pandas_frame,
        matplotlib_plot=matplotlib_plot,
        sklearn_model=sklearn_model,
        scipy_statistics=scipy_statistics,
        plotly_figure=plotly_figure,
        excel_roundtrip=excel_roundtrip,
        vision_roundtrip=vision_roundtrip,
        fastapi_endpoint=fastapi_endpoint,
        http_and_dotenv=http_and_dotenv,
        sqlite_async=sqlite_async,
    )


def tensorflow_check():
    import keras
    import numpy as np
    import tensorflow as tf

    tf.random.set_seed(42)
    value = tf.matmul(tf.constant([[1.0, 2.0]]), tf.constant([[3.0], [4.0]]))
    np.testing.assert_allclose(value.numpy(), [[11.0]])
    # A tiny CNN forward/backward operation, without an expensive fit loop.
    model = keras.Sequential(
        [
            keras.Input((8, 8, 1)),
            keras.layers.Conv2D(2, 3),
            keras.layers.Flatten(),
            keras.layers.Dense(1),
        ]
    )
    x = tf.ones((1, 8, 8, 1))
    with tf.GradientTape() as tape:
        loss = tf.reduce_sum(model(x))
    gradients = tape.gradient(loss, model.trainable_weights)
    assert all(g is not None for g in gradients)
    gpus = tf.config.list_physical_devices("GPU")
    gpu_test = "not available"
    if gpus:
        with tf.device("/GPU:0"):
            z = tf.matmul(tf.ones((2, 2)), tf.ones((2, 2)))
        np.testing.assert_allclose(z.numpy(), [[2.0, 2.0], [2.0, 2.0]])
        gpu_test = z.device
    return {
        "version": tf.__version__,
        "keras": keras.__version__,
        "gpu_devices": [x.name for x in gpus],
        "gpu_operation": gpu_test,
    }


def torch_check():
    import numpy as np
    import torch
    import torchvision
    from torchvision.ops import nms

    torch.manual_seed(42)
    a = torch.tensor([[1.0, 2.0]]) @ torch.tensor([[3.0], [4.0]])
    np.testing.assert_allclose(a.numpy(), [[11.0]])
    layer = torch.nn.Conv2d(1, 2, 3)
    x = torch.ones((1, 1, 8, 8), requires_grad=True)
    layer(x).sum().backward()
    assert x.grad is not None
    boxes = torch.tensor([[0.0, 0.0, 2.0, 2.0], [0.0, 0.0, 1.0, 1.0]])
    assert len(nms(boxes, torch.tensor([0.9, 0.1]), 0.5)) == 2
    built, available = torch.backends.mps.is_built(), torch.backends.mps.is_available()
    gpu_test = "not available"
    if available:
        z = torch.ones((2, 2), device="mps") @ torch.ones((2, 2), device="mps")
        np.testing.assert_allclose(z.cpu().numpy(), [[2.0, 2.0], [2.0, 2.0]])
        gpu_test = str(z.device)
    return {
        "version": torch.__version__,
        "torchvision": torchvision.__version__,
        "mps_built": built,
        "mps_available": available,
        "gpu_operation": gpu_test,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile", choices=["study", "tensorflow", "torch"], default="study"
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
    os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
    with tempfile.TemporaryDirectory(prefix="lovam-smoke-") as temporary:
        os.environ.setdefault("MPLCONFIGDIR", temporary)
        modules = (
            STUDY_IMPORTS
            if args.profile == "study"
            else (
                {
                    "tensorflow": "tensorflow",
                    "keras": "keras",
                    "numpy": "numpy",
                    "scipy": "scipy",
                    "scikit-learn": "sklearn",
                    "ipykernel": "ipykernel",
                    "matplotlib": "matplotlib",
                    "pillow": "PIL",
                }
                if args.profile == "tensorflow"
                else {
                    "torch": "torch",
                    "torchvision": "torchvision",
                    "numpy": "numpy",
                    "sympy": "sympy",
                    "ipykernel": "ipykernel",
                    "matplotlib": "matplotlib",
                    "pillow": "PIL",
                }
            )
        )
        results = []

        def check(name, function):
            try:
                detail = function()
                results.append({"name": name, "status": "pass", "detail": detail})
            except Exception as exc:
                results.append(
                    {
                        "name": name,
                        "status": "fail",
                        "detail": type(exc).__name__ + ": " + str(exc),
                    }
                )

        for distribution, module in modules.items():

            def load(distribution=distribution, module=module):
                importlib.import_module(module)
                return importlib.metadata.version(distribution)

            check("import:" + distribution, load)
        if args.profile == "study":
            for name, function in study_checks().items():
                check(name, function)
        else:
            check(
                args.profile + ":tensor-cnn-gradient-and-gpu",
                tensorflow_check if args.profile == "tensorflow" else torch_check,
            )
    report = {
        "profile": args.profile,
        "python": sys.version.split()[0],
        "environment": Path(sys.prefix).name,
        "results": results,
    }
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    print(output)
    return int(any(result["status"] == "fail" for result in results))


if __name__ == "__main__":
    raise SystemExit(main())
