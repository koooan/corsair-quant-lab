from pathlib import Path
import runpy
from types import SimpleNamespace
import pandas as pd
import pytest
from corsair_lab.evaluation import run_benchmark


@pytest.mark.parametrize("horizon", [1, 5, 20])
def test_marimo_matches_shared_evaluator(horizon, monkeypatch):
    root = Path(__file__).resolve().parents[1]
    monkeypatch.chdir(root)
    namespace = runpy.run_path(str(root / "notebooks/marimo/01_foundation.py"))
    _, definitions = namespace["app"].run(defs={"horizon": SimpleNamespace(value=horizon)})
    expected = run_benchmark(horizon)[3]
    pd.testing.assert_frame_equal(definitions["scores"], expected)
