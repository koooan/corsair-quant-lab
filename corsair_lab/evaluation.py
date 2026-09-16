"""Small, auditable development benchmark. No trained AI models in release 01."""

from pathlib import Path
import hashlib
import json
import math
import platform
from datetime import datetime, timezone

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def load_yields():
    """Read the frozen snapshot and refuse silent modification."""
    path = ROOT / "data/raw/treasury_yields.csv"
    meta = json.loads((ROOT / "data/raw/provenance.json").read_text())
    if hashlib.sha256(path.read_bytes()).hexdigest() != meta["sha256"]:
        raise ValueError("Snapshot hash mismatch: review and version the data change.")
    frame = pd.read_csv(path, na_values=[".", ""], parse_dates=["observation_date"])
    if frame.observation_date.duplicated().any():
        raise ValueError("Duplicate observation dates")
    if not frame.observation_date.is_monotonic_increasing:
        raise ValueError("Dates must be increasing")
    return frame, meta


def forecast_records(series, horizon=1, window=20, evaluation_start="2024-01-01"):
    """Predict from history through each origin; horizon counts observed sessions."""
    if not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    if not isinstance(window, int) or window < 2:
        raise ValueError("window must be at least two observations")
    series = series.dropna().astype(float)
    if not isinstance(series.index, pd.DatetimeIndex):
        raise ValueError("A DatetimeIndex is required")
    if series.index.has_duplicates or not series.index.is_monotonic_increasing:
        raise ValueError("Dates must be unique and increasing")
    if not all(math.isfinite(x) for x in series):
        raise ValueError("Values must be finite")
    rows = []
    for i in range(window, len(series) - horizon):
        target_date = series.index[i + horizon]
        if target_date < pd.Timestamp(evaluation_start):
            continue
        history = series.iloc[i - window:i + 1]
        forecasts = {
            "Last observed yield": float(history.iloc[-1]),
            "Trailing mean change": float(history.iloc[-1] + horizon * history.diff().dropna().mean()),
        }
        for model, prediction in forecasts.items():
            rows.append({"series": series.name, "model": model,
                         "origin_date": series.index[i], "target_date": target_date,
                         "horizon_sessions": horizon, "last_yield_pct": float(history.iloc[-1]),
                         "actual_pct": float(series.iloc[i + horizon]), "prediction_pct": prediction})
    if not rows:
        raise ValueError("Insufficient data for this evaluation configuration")
    return pd.DataFrame(rows)


def score_forecasts(records):
    """Percentage-point yield errors become basis points by multiplying by 100."""
    if records.empty:
        raise ValueError("Cannot score empty predictions")
    rows = []
    for (series, model), group in records.groupby(["series", "model"], sort=False):
        errors = (group.prediction_pct - group.actual_pct) * 100
        if not all(math.isfinite(x) for x in errors):
            raise ValueError("Non-finite prediction or target")
        rows.append({"Series": series, "Model": model, "Forecasts": len(group),
                     "MAE (bp)": float(errors.abs().mean()),
                     "RMSE (bp)": float((errors.pow(2).mean()) ** 0.5)})
    return pd.DataFrame(rows)


def run_benchmark(horizon=1):
    frame, meta = load_yields()
    indexed = frame.set_index("observation_date")
    predictions = pd.concat([forecast_records(indexed[name], horizon=horizon)
                             for name in ["DGS2", "DGS10"]], ignore_index=True)
    scores = score_forecasts(predictions)
    return frame, meta, predictions, scores


def plot_benchmark(predictions, scores):
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), layout="constrained")
    one = predictions[predictions["model"] == "Last observed yield"]
    for series, color, style in [("DGS2", "#265DAB", "-"), ("DGS10", "#A36313", "--")]:
        subset = one[one.series == series]
        axes[0].plot(subset.target_date, subset.actual_pct, color=color, linestyle=style,
                     label=series, linewidth=1.6)
    axes[0].set(title="Development observations · 2024", ylabel="Treasury yield (%)", xlabel="Observation date")
    start, end = one.target_date.min(), one.target_date.max()
    axes[0].set_xticks([start, pd.Timestamp("2024-04-01"), pd.Timestamp("2024-07-01"), pd.Timestamp("2024-10-01"), end])
    axes[0].xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    axes[0].legend(frameon=False)
    labels = [f"{row['Series']} · {row['Model']}" for _, row in scores.iterrows()]
    bars = axes[1].barh(labels, scores["MAE (bp)"], color="#265DAB")
    axes[1].bar_label(bars, fmt="%.2f", padding=4)
    axes[1].set_xlim(0, scores["MAE (bp)"].max() * 1.22)
    axes[1].invert_yaxis()
    horizon = int(predictions.horizon_sessions.iloc[0])
    axes[1].set(title=f"Baseline error · {horizon} observed-session horizon", xlabel="Mean absolute error (basis points)")
    for ax in axes:
        ax.grid(axis="y" if ax is axes[0] else "x", alpha=.15)
        ax.set_axisbelow(True)
    fig.suptitle("Corsair Quant Lab · evaluation foundation", fontsize=15, fontweight="bold")
    return fig


def interpretation(scores):
    lines = []
    for name, group in scores.groupby("Series"):
        values = "; ".join(f"{r['Model']}: {r['MAE (bp)']:.2f} bp MAE" for _, r in group.iterrows())
        lines.append(f"**{name}:** {values} ({int(group.Forecasts.iloc[0])} forecasts per baseline).")
    lines.append("These are development-period baseline measurements, not AI-model results or evidence of a profitable strategy. Differences have not been tested for statistical significance.")
    return "\n\n".join(lines)


def write_artifacts(horizon=1):
    frame, meta, predictions, scores = run_benchmark(horizon)
    destination = ROOT / "artifacts"
    destination.mkdir(exist_ok=True)
    predictions.to_csv(destination / "week01_predictions.csv", index=False)
    scores.to_csv(destination / "week01_scores.csv", index=False)
    plot_benchmark(predictions, scores).savefig(destination / "week01.png", dpi=160)
    manifest = {"experiment_id": "week01_foundation", "status": "completed_baselines_only",
                "created_at_utc": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
                "dataset_sha256": meta["sha256"], "horizon_observed_sessions": horizon,
                "evaluation_start": "2024-01-01", "evaluation_end": "2024-12-31",
                "window": 20, "models": ["last_observed_yield", "trailing_mean_change"],
                "seed": None, "seed_note": "Deterministic; no stochastic training",
                "paid_api_cost_usd": 0, "hardware": platform.machine(),
                "limitations": ["Current snapshot, not historical vintages", "Development only", "No AI model runs"]}
    (destination / "week01_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return scores
