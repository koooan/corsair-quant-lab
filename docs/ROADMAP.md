# Sixteen weekly releases

Planning date: September 15, 2026. Budget: 6–8 hours per week, roughly 96–128 hours in total. Friday releases, with the final release moved to Thursday December 31. Prepare holiday releases early. Dates are targets, not automatic jobs.

The realistic year-end outcome is a reproducible research prototype and a small trained adapter with measured strengths and weaknesses. Broad expert-level competence or profitable forecasting is not promised. Advanced training experiments depend on data readiness and a separately agreed compute budget.

| Week | Ship by | Bounded deliverable | Skill you practice |
|---|---|---|---|
| 01 | Sep 18 | Shared evaluation core; real-data baseline experiment in Jupyter and marimo; source registry | Python functions, environments, tables, tests |
| 02 | Sep 25 | FinBERT + one FinGPT checkpoint on financial sentiment; separate relevance task shows transfer limits | Text cleaning, labels, confusion matrices |
| 03 | Oct 02 | Fin-R1 vs general-model baseline on a small verified quant task set; BloombergGPT paper/access review | Structured outputs, numerical checks, model cards |
| 04 | Oct 09 | Chronos-2 and TimeGPT on a common numerical forecasting task; hosted run only if access/budget exists | Model adapters, forecast horizons, API boundaries |
| 05 | Oct 16 | TimesFM, Moirai, TTM through the same evaluation core; use small runnable versions | Batching, dependency isolation, profiling |
| 06 | Oct 23 | Kronos on liquid-instrument bars; TabPFN on structured observations; distinct scorecards | Feature design, different dataset shapes |
| 07 | Oct 30 | N-HiTS, TFT, PatchTST with fixed small training budgets | Training/validation splits, optimization, checkpoints |
| 08 | Nov 06 | Qlib + RD-Agent: one bounded factor-research loop and an audit of repeated-test overfitting | Backtests, experiment logs, failure handling |
| 09 | Nov 13 | FinRobot issuer memo with citation checks; FinRL tiny paper-only policy experiment with costs | Tool calling, source checks, simulated environments |
| 10 | Nov 20 | Bridgewater-inspired forecaster: retrieve, forecast, reconcile, calibrate; ablations | Probabilities, Brier score, calibration |
| 11 | Nov 27 | Small expert-labeled relevance set and error review; training-data release with rights/provenance | Annotation, disagreement resolution, data versioning |
| 12 | Dec 04 | Fixed-income specialist v0: small adapter fine-tune; base-vs-tuned evaluation | Supervised fine-tuning, held-out evaluation |
| 13 | Dec 11 | Specialist supervisor with frontier delegation; compare specialist-only and frontier-only | Routing, acceptance checks, cost/quality tradeoffs |
| 14 | Dec 18 | Cross-asset v0: additional training on mixed tasks; retention checks on fixed income | Multi-task training, transfer, regression testing |
| 15 | Dec 25 | Asset-class distillation pilot: separate rates and credit students/adapters; prepare by Dec 23 | Verified teacher data, student evaluation |
| 16 | Dec 31 | Frozen final evaluation, prospective forecast readout, public capstone demo/model cards | Release engineering, honest performance reporting |

## How a 7-hour week works

- 45 minutes: read the primary source and define one falsifiable question.
- 3 hours: implement the smallest runnable experiment, including one part you code yourself.
- 90 minutes: inspect errors, compare the baseline, and record limitations.
- 60 minutes: make both notebooks readable and record a short demo.
- 45 minutes: tests, release notes, tag, publish.

Multi-model weeks share a task and adapter interface. Limit each model to one version, one main task, a fixed number of origins/examples, and one small parameter sweep. Add second use cases only when the core comparison is complete. Keep heavier packages in per-experiment environments to prevent incompatible dependencies from breaking the whole lab.

## Access and scope rules

BloombergGPT and Bridgewater AIA are research-study tracks unless usable weights/code are actually released. Do not silently substitute another model and call it a reproduction. TimeGPT/frontier APIs need credentials and spending limits. If access is unavailable, ship a documented access review and reusable adapter contract; keep status `not_run`, not `evaluated`.

Begin timestamped prospective forecasts as soon as an eligible model adapter exists (target: week 04); week 10 adds judgmental event forecasts. Only score outcomes that have resolved. This gives a small genuinely forward-looking year-end sample, not a claim of statistical power.

## Week 01: your first coding exercise

Open `corsair_lab/evaluation.py`, follow the conversion from percentage points to basis points, and explain why it is multiplied by 100. Then add median absolute error, test it against a hand-calculated example, and display it in both notebooks. Keep the existing experiment configuration fixed so the change is easy to review.

## Definition of capstone readiness

Training starts only when labels are reviewed, train/validation/test families are separated, data rights are recorded, and a compute cap exists. If these conditions slip, keep shipping the benchmark and dataset improvements. Report the training milestone as incomplete rather than replacing it with a prompted model and calling it trained.
