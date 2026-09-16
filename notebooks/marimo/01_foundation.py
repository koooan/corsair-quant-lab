import marimo

__generated_with = "0.24.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    import sys
    _root = next(p for p in [Path.cwd(), *Path.cwd().parents] if (p / "corsair_lab").exists())
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))
    from corsair_lab.evaluation import run_benchmark, plot_benchmark, interpretation
    return interpretation, mo, plot_benchmark, run_benchmark


@app.cell
def _(mo):
    mo.md("""
    # Corsair Quant Lab · Week 01
    **One experiment, two notebook interfaces.** This first release verifies data loading,
    chronological prediction, and common evaluation code. No AI model has been evaluated yet.

    Explore how the baseline error changes with the forecast horizon. This is development
    data, not a final test set or a trading backtest.
    """)
    return


@app.cell
def _(mo):
    horizon = mo.ui.dropdown(options=[1, 5, 20], value=1, label="Forecast horizon (observed sessions)")
    horizon
    return (horizon,)


@app.cell
def _(horizon, run_benchmark):
    observations, provenance, predictions, scores = run_benchmark(horizon=int(horizon.value))
    return observations, predictions, provenance, scores


@app.cell
def _(mo, provenance):
    mo.md(f"""
    ## Context and methods
    Source: [FRED DGS2](https://fred.stlouisfed.org/series/DGS2) and
    [FRED DGS10](https://fred.stlouisfed.org/series/DGS10), originally the Federal Reserve Board.
    Snapshot: **{provenance['retrieved_at_utc']}**. Units: percent; errors reported in basis points.

    **Assumptions:** histories start in 2020; targets are in 2024. Missing observations are dropped
    per series without interpolation. Each forecast sees only history through its origin.
    A session is an observed value, not a calendar day. These are current snapshot values,
    not verified historical publication vintages. The second baseline extrapolates the mean
    of the preceding 20 observed yield changes.
    """)
    return


@app.cell
def _(mo, scores):
    mo.vstack([mo.md("## Results"), mo.ui.table(scores.round(3), selection=None)])
    return


@app.cell
def _(plot_benchmark, predictions, scores):
    figure = plot_benchmark(predictions, scores)
    figure
    return (figure,)


@app.cell
def _(interpretation, mo, scores):
    mo.md("## Takeaways\n\n" + interpretation(scores) + "\n\n**Next:** add a model adapter without changing the evaluation rules. Your coding exercise is to implement median absolute error and display it in both notebooks.")
    return


if __name__ == "__main__":
    app.run()
