# Evaluation contract

## Separate scorecards

| Track | Primary evidence | Useful metrics |
|---|---|---|
| Text classification | Expert-reviewed labels; disagreement recorded | Macro-F1, class recall, confusion matrix |
| Quant reasoning/code | Verified answer, executed code, unit checks | Pass rate, numeric tolerance, critical error rate |
| Numerical forecasting | Chronological origins and identical target windows | MAE/RMSE in native units; quantile loss/coverage when supported |
| Judgmental forecasting | Timestamped probability and explicit resolution rule | Brier score, log loss, calibration, coverage of resolved events |
| Research agents | Frozen task, evidence, tools and budget | Completion, citation support, reproducibility, cost, time |
| Trading/RL | Executable strategy with point-in-time inputs | Net returns, turnover, drawdown, cost sensitivity; uncertainty |

No single combined leaderboard ranks unrelated tasks. A good sentiment F1 is not a forecasting result. A low yield-level error is not demonstrated return predictability.

## Timing and leakage

- Preserve observation date, publication/availability timestamp, ingestion timestamp and vintage where applicable. Never infer historical availability from the observation date alone.
- Split chronologically for predictive tasks. Fit preprocessing only on training data. Group related documents, issuers and near-duplicate tasks to prevent cross-split contamination.
- For multi-step targets, prevent training labels from overlapping validation/test windows. Define horizons in calendar days or observed sessions explicitly.
- Keep final test sets sealed until the release gate; log repeated tuning and model selection. Reserve prospective examples for models whose pretraining may include the historical period.
- Revised data and pretrained-model knowledge can contaminate historical tests. Report known/unknown pretraining coverage; do not call a chronological split proof of a clean foundation-model test.
- Model inputs at each origin must exclude later observations. Test this by changing future data and confirming that earlier forecasts are unchanged.

## Reproducible run record

Record experiment ID, task, model/checkpoint/revision, source URLs and hashes, time coverage, split rules, horizon, target units, transformations, seed, hardware, dependency lock, inference settings, runtime, cost (unknown is not zero), metrics and run status. Save predictions as well as aggregates. A run that fails or lacks credentials is `not_run` or `failed`, never an inferred score.

## Week 01 scope

The first experiment uses a current downloaded snapshot of DGS2/DGS10 for 2020–2024. It evaluates last-value and trailing-average-change baselines on 2024, using only preceding observations for each prediction. It drops missing values per series without filling them and defines horizons as **observed sessions**, not calendar days. The snapshot is not historical-vintage data and cannot establish point-in-time trading performance. The held-out rows are development observations, not a final test set. No confidence intervals or statistical superiority claim is made.

## Before any public release

Both notebooks execute from a clean environment; results agree; titles/units/sources match; no credentials or private/licensed corpus are included; model/data terms are recorded; failed tests and unavailable access are visible. Do not ship generated plots or sample predictions as if a model actually ran.
