# Multi-Asset Analyst

Status: proposed product and research targets. No analyst model has been trained, deployed, or benchmarked in this repository. The existing release evaluates numerical forecasting baselines only. The proposed January–July 2026 résumé dates are not a verified development history; use actual dates for eventual reporting.

## Ambition

Build a reliability-first assistant for fundamental and quantitative investment research across fixed income, currencies, and commodities. Support instrument conventions, pricing-tool use, and explicit upside/downside scenarios, including complex instruments such as convertible bonds with dividend protection.

| Target | Evidence required before claiming achievement |
|---|---|
| Approximately 4B-parameter analyst trained with human feedback | Identify base checkpoint, license, training recipe, expert feedback provenance, and held-out gains. Record whether training is RLHF, DPO, or another method. |
| Strong niche instrument coverage | Rights-cleared domain corpus and asset-specific tests of conventions, tool selection, calculations, and evidence use. |
| 100-task research benchmark | Independently reviewed reference answers and scoring rubrics; separate development data; sealed final tasks; breakdowns by asset and skill. |
| 15% improvement over frontier baselines | Predeclare relative improvement versus percentage-point improvement, primary metric, model versions, equal evidence/tool access, and uncertainty. |
| 20× smaller | Name a baseline with documented parameter count and compare like-for-like total and active parameters. A 4B model is 20× smaller than an 80B model; do not infer proprietary frontier model sizes. |
| 10,000+ users, including professional researchers | Define active usage and report measured adoption. Do not imply firm endorsement from individual usage. |
| Free access through MCP and possible Hugging Face release | Running hosted service, inference budget, access limits, MCP interface, and separately licensed code/weights/data. MCP alone does not host inference. |
| Custom pricing plugins and uploaded documentation | Versioned tool schemas, units, dates, input validation, isolated execution, and retrieval with attributable sources. Document upload need not retrain weights. |

These are capstone goals, not a one-week delivery commitment at 6–8 hours per week. The week-two milestone remains a bounded prototype.

## Training corpus: Curvy-CUSIPs

The user has selected [our Curvy-CUSIPs fork](https://github.com/koooan/Curvy-CUSIPs) as a source for the Multi-Asset Analyst training corpus. It is not yet ingested or converted into training examples. GitHub identifies the repository license as [MIT](https://github.com/koooan/Curvy-CUSIPs/blob/main/LICENSE); preserve attribution and license notices in redistributed source material and check any separately sourced data or documents before inclusion.

Curate relevant code, documentation, and notebook workflows into explanatory examples, tool-use demonstrations, and executable quantitative exercises. Record each example's source commit and path, transformations, and validation results. Validate numerical answers independently; code appearing in a repository is not automatically a correct reference answer. Keep changing market observations in dated retrieval sources rather than presenting them as timeless model knowledge.

Split related notebooks, code variants, and derived questions together to prevent near-duplicate training/test leakage. The final research benchmark must remain independent of training examples.

## Training direction: human feedback and calibrated decisions

Explore both human-feedback learning and calibration-oriented decision training. The TypeSafe article calls Jev's method **RLCD: Reinforcement Learning for Calibrated Decisions**, not RLCI. The announcement does not provide a complete reproducible training recipe, so our proposed experiment should be described as RLCD-inspired until an exact implementation and evidence justify a stronger claim. Calling the Jev API is distinct from training our own model this way.

For the initial calibration experiment, use labeled instrument-feature and tool-eligibility questions, require probability outputs, and evaluate with proper scoring rules such as Brier score or log loss on held-out examples. Compare the supervised baseline, any subsequent reinforcement-learning variant, and a post-hoc calibration baseline. Proper scoring rules alone do not establish that an experiment reproduces Jev's RLCD. Assess both accuracy and calibration, including critical errors versus abstention coverage. Human preferences continue to inform research usefulness, explanations, and corrections; executable checks assess numerical correctness.

## Model versus system

Keep three configurations measurable: the small analyst alone, the analyst with numerical tools/retrieval, and the analyst that can also delegate to a frontier model. Report all external dependencies, call rates, latency, and total cost. An assisted system's score is not the standalone student's score.

The exact “Kimi K” checkpoint is unresolved. If this means Kimi K2, its official card reports 1T total and 32B activated parameters. It could be evaluated as a teacher; obtaining a 4B student requires a separate smaller architecture and a suitable training/distillation process. Quantization or adapter tuning does not change that parameter count. Check teacher and student licenses before releasing derivatives. [Official Kimi K2 model card](https://huggingface.co/moonshotai/Kimi-K2-Instruct).

## Proposed TypeSafe experiment

TypeSafe introduces Jev as an early-access model for typed probabilistic decisions, with RLCD as its training approach. Its schema guarantee does not establish financial correctness. The published workflow evaluation uses large-model reference probabilities, which are not independently verified financial answers. Availability of trainable Jev weights is not established by the announcement. [Announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev).

Use an optional decision provider around the analyst, then test whether it improves outcomes:

| Decision | Candidate use | Independent check |
|---|---|---|
| Instrument features | Identify likely dividend protection, callable features, or missing terms | Expert labels and cited contract passages |
| Tool eligibility | Choose among approved pricing engines or abstain | Deterministic capability/input checks |
| Evidence sufficiency | Flag unsupported claims for review | Source verification and expert assessment |
| Escalation | Route difficult or incomplete cases to a human or frontier model | Critical-error rate at each automation coverage level |
| Feedback selection | Prioritize disagreements and uncertain cases | Include random audits to avoid sampling bias |

TypeSafe offers Choice, Score, and Noul primitives. Questions within a call are independent; dependent decisions should be separate workflow stages. [API introduction](https://docs.typesafe.ai/introduction).

The public MIT-licensed adapter supports the same decision interface using LLM APIs and custom compatible endpoints. It enables a baseline before Jev access, subject to provider access and an agreed budget. It does not supply Jev weights or Jev's performance guarantees. [Adapter repository](https://github.com/typesafe-ai/system-one-adapter-python).

### First bounded experiment

Build paired Jupyter/marimo notebooks sharing one evaluator. Use a small rights-cleared development set of convertible-bond terms, including dividend protection, absent clauses, and deliberately incomplete examples. Compare deterministic rules, an LLM-backed decision adapter, and Jev if available, using identical inputs and approved tools. This experiment has not yet been implemented.

The workflow retrieves attributable terms, proposes instrument features, validates required inputs, selects a compatible pricing engine, calculates scenario values, and drafts an explanation. Deterministic checks verify units, valuation dates, model support, and numerical consistency; expert review assesses interpretation. A plain convertible pricer must not silently stand in for one supporting the relevant contractual dividend adjustment.

Measure critical false acceptances, abstention/coverage, classification accuracy, Brier score or log loss on labeled decisions, latency, and cost per completed task. Tune thresholds on development data only. Decision confidence is not the probability of a market return or proof that a valuation is correct.

## Human feedback and evaluation

Collect expert comparisons, corrections, and reasons with explicit permission for training use. Keep private uploads separate from opt-in contributions. Use numerical reference checks where correctness can be verified; distinguish verifiable rewards from human preferences. Jev may prioritize review or propose labels, but its judgments alone are AI feedback, not RLHF.

Build training and development examples separately from the final 100 research tasks. Use only material with appropriate rights; private employer tasks and documents must not be copied into a public benchmark without permission. Freeze the final set before optimization, and report per-asset/task performance and uncertainty rather than only one overall score.

The same optional decision interface could later help flag ambiguous claims in the Sharpe-hacking project or propose contract matches for FOMC research. Statistical leakage checks, contract-equivalence verification, payoff calculations, and execution-cost analysis remain independently testable code or expert-reviewed work. No profitability or arbitrage is presumed.
