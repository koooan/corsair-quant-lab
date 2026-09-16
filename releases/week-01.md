# Week 01 — A research lab you can rerun

Target date: September 18, 2026. Prepared September 15. Version: `v0.1.0`.

## What ships

- A 16-week build schedule through December 31, with 6–8 hours per week.
- Jupyter and marimo versions of one real-data experiment.
- A shared evaluator, chronological-isolation tests, source hashes, and a locked environment.
- A project roster covering the public models and frameworks discussed, excluding traditional fixed-income models.
- A Bridgewater public-research study and capstone design.

## Experiment

Question: can both notebook interfaces reproduce the same baseline forecast evaluation?

Data: Federal Reserve Board H.15 Treasury yields via FRED, DGS2 and DGS10, 2020–2024. Evaluate 2024 targets at a one-observed-session horizon, 250 forecasts per series and baseline. Full source and snapshot hash are in `data/raw/provenance.json`.

| Series | Baseline | MAE (basis points) | RMSE (basis points) |
|---|---|---:|---:|
| 2-year Treasury | Last observed yield | 4.552 | 6.153 |
| 2-year Treasury | Trailing mean change | 4.780 | 6.263 |
| 10-year Treasury | Last observed yield | 4.480 | 5.750 |
| 10-year Treasury | Trailing mean change | 4.597 | 5.899 |

These measurements establish a reference for later experiments. No AI model ran in this release. The snapshot does not establish historical publication-time availability. No transaction-cost model, trading performance claim, confidence interval, or statistical-superiority claim is included.

## Three-minute demo

1. **0:00–0:30:** show the research question and source limitations.
2. **0:30–1:15:** open the executed Jupyter notebook and inspect the score table and chart.
3. **1:15–2:00:** run the marimo app locally; switch the horizon from 1 to 5 to 20 observed sessions and inspect the updated results.
4. **2:00–2:30:** show the test that changes future observations without changing earlier predictions.
5. **2:30–3:00:** explain what remains untested and preview FinBERT/FinGPT for next week.

The release HTML attachments are static snapshots, not live hosted apps. Use the README's marimo command for actual interactivity. A screen recording has not been made; the demo is the working notebook plus this script.

## Your first contribution

Implement median absolute error, add a hand-calculated test, and show the metric in both notebooks. Explain the difference between average and median error in two sentences.

## Verification

The local test suite passes, including marimo/evaluator agreement at horizons 1, 5 and 20. Both notebooks are executed by `scripts/build_release.py`; it refuses a Jupyter release without an embedded chart. Exported presentation and the interactive control are inspected before publishing. GitHub checks repeat tests and execution in a separate Linux environment.
