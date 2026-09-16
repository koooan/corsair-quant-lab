# Multi-Asset Research Benchmark — design v0.1

Status: design draft, not a completed or validated benchmark. The public development examples are synthetic and await independent expert review. No model scores have been produced. The 100 final tasks do not yet exist. This design evaluates the current FICC scope; it does not establish broad coverage of standalone equity or every asset class.

## Purpose and claims

Measure whether Multi-Asset Analyst completes investment-research tasks correctly, uses evidence and tools appropriately, and communicates uncertainty usefully. Evaluate fundamental reasoning and quantitative execution together, while reporting each skill separately. This is not a test of realized trading profitability.

The primary endpoint is **research task success rate** on 100 fixed final tasks. A task succeeds only when every predeclared mandatory criterion is met and no predeclared critical error occurs. Each task must have mandatory content or actions, not merely an absence of errors. Evidence-backed recognition of missing inputs can constitute success when the task explicitly calls for that behavior. Blanket refusal cannot pass answerable tasks.

Report secondary research-quality scores, calibration, numerical accuracy, critical-error rate, tool correctness, and cost separately. Do not combine calibration or user preference with accuracy into an opaque overall score.

## Coverage: 100 final tasks

Each cell is an authoring quota, not a set of completed questions. Assign one primary asset family and one primary skill to every task; additional tags are allowed. Hybrids live in their own row to avoid double counting. Each skill receives 20 tasks.

| Primary asset family | Conventions and terms | Pricing and sensitivities | Scenarios and hedging | Evidence-based research | Coding and model validation | Total |
|---|---:|---:|---:|---:|---:|---:|
| Rates and sovereigns | 5 | 5 | 5 | 5 | 5 | 25 |
| Credit | 4 | 4 | 4 | 4 | 4 | 20 |
| FX | 3 | 3 | 3 | 3 | 3 | 15 |
| Commodities | 3 | 3 | 3 | 3 | 3 | 15 |
| Hybrids, including convertibles | 3 | 3 | 3 | 3 | 3 | 15 |
| Cross-asset portfolios | 2 | 2 | 2 | 2 | 2 | 10 |
| **Total** | **20** | **20** | **20** | **20** | **20** | **100** |

Authoring examples: day-count or quotation mistakes; clean/dirty price reconciliation; hedge sizing with explicit units; scenario P&L decomposition; source-supported investment thesis and counterthesis; incomplete convertible adjustment clauses; commodity delivery mismatches; FX quote inversion; look-ahead leakage in code; and cross-asset risk aggregation. These are task ideas, not assertions about specific contracts.

Difficulty targets: 30 foundational, 50 multi-step analyst tasks, 20 specialist tasks. Apply disjoint reliability overlays to 20 of the 100 tasks: 10 missing essential inputs, 5 conflicting/stale sources, 5 unavailable or incompatible tools. Preserve at least 80 ordinary tasks so refusing everything cannot score well. Distribute overlays across asset families and skills.

## Splits and benchmark governance

- Publish the design, schemas, scoring code when implemented, and a separate development set. Start with 10–15 reviewed development tasks before training or optimizing prompts.
- Keep the 100-task final set and its answers private until the evaluation policy allows release. Store locally only under ignored `data/private/benchmark/`, not in this repository. A private file is not automatically secure: control access and provider retention when executing it.
- Group tasks by underlying document, instrument, code lineage, and derivation family. Synthetic number changes alone do not create an independent task. Keep related variants in one split; use distinct training, development, and final families.
- Curvy-CUSIPs-derived exercises are training/development material. Do not use those same workflows or near-duplicates as evidence of unseen final-test performance. Use independently authored final problems and independent numerical references.
- Freeze task manifest, rubric, evidence hashes, scorer version, model list, and budgets before final evaluation. Keep an evaluation access log. Never use final results for reward-model fitting, threshold tuning, prompt selection, or checkpoint selection.
- Final-set maintenance needs a named custodian. Refresh contaminated tasks in a new version rather than silently changing the old leaderboard. Public release increases future contamination risk; retain or author fresh private evaluation tasks.
- Rights clearance is required for actual workplace tasks. Reconstruct public/synthetic analogues when private documents or instructions cannot be shared. Current examples are explicitly not claimed to come from a hedge fund.
- Record source publication/availability time, valuation time, data vintage, and retrieval time. Historical reasoning is conditional on the supplied evidence; pretraining may contain later knowledge. Real forecasting skill requires a separate prospective, timestamped track with frozen resolution rules.

## Task package and authoring gate

Use `benchmarks/multi_asset/task_template.json` for each task. A complete package contains:

1. A realistic request, primary asset and skill, difficulty, lineage group, and whether it is answerable with the permitted resources.
2. A frozen evidence/data packet with rights, provenance, dates, and content hashes; explicit conventions, units, and required output fields.
3. Permitted tools and their versions, capabilities, input/output schemas, and frozen responses where applicable. Define access separately for each evaluation track.
4. Mandatory criteria with observable checks; numeric reference outputs with justified absolute/relative tolerances; acceptable alternative interpretations and valid abstentions.
5. Task-specific critical errors defined before model outputs are seen. Examples include inverted hedge direction, invented contract terms, unsupported numerical claims, or claiming a failed tool succeeded.
6. Fixed factual decision questions for calibration, each with a unique proposition, adjudicated label, and predeclared scoring. Avoid an undefined request for “overall confidence.”
7. Independent author and reviewer sign-off. Resolve reference-answer disagreements before final-set admission. Validate calculations using a separate derivation or implementation; do not simply trust one pricing package or another LLM.

The included examples are authoring illustrations with manually specified reference checks, not implemented automated scorers or approved final tasks.

## Fair comparisons

Keep separate leaderboards for:

- **Evidence-only:** identical self-contained packets; no external retrieval, code execution, or frontier calls. Only tasks adjudicated feasible in this track are scored; publish the denominator. Do not compare its subset score directly to a different task set.
- **Common tools:** the same frozen evidence, retrieval corpus, numerical tools, execution environment, and interface for every model. This is the primary 100-task research-system track. Tasks may deliberately require diagnosing unavailable tools.
- **Delegating systems:** frontier assistance permitted and fully logged. Compare against the same frontier model operating directly with the same tools. Treat performance as a system result, not the small model's standalone capability.

Within the primary track, compare the same student base checkpoint under domain fine-tuning only, RLHF, calibration-oriented training, and combined training. Keep training examples and compute matched where possible; report differences and use multiple training seeds when feasible. Treat a Jev router as a separate system ablation, not proof that our student was trained with Jev's RLCD. Include selected frontier baselines with dated versions and known access conditions.

Before runs, fill in token, tool-call, time, and dollar limits in the protocol config; null values mean **not ready to run**. Give identical interfaces and maximum resources within each track, record actual spending, and optionally report a separate matched-cost comparison. No paid runs are authorized by this document alone.

Model-caused invalid responses, timeouts, and tool misuse count as task failures. Independently verified service outages are run-invalid, not zero-cost successes; retain logs and rerun all affected comparisons consistently. Never drop difficult tasks after seeing scores. Report unsupported configurations as not run.

## Scoring

### Task success and critical errors

For each task, success is 1 only if all mandatory criteria pass and no critical error is present; otherwise 0. Report success count / eligible tasks and the percentage. In the primary track the denominator is 100. Critical-error rate counts tasks with at least one critical error and is reported separately, including on otherwise fluent answers.

### Research quality

Two reviewers, blinded to model identity and randomized output order, score each applicable dimension from 0–4:

- Financial/numerical correctness.
- Assumptions, conventions, and instrument fit.
- Evidence support and source attribution.
- Scenario reasoning, counterarguments, and limitations.
- Reproducibility and usefulness of the delivered work.

Common anchors: 0 absent/incorrect; 1 major defects; 2 partially correct with material gaps; 3 correct and usable with minor gaps; 4 complete and independently reproducible. Add task-specific anchors and freeze applicability before testing. Report dimension means, reviewer agreement, and adjudications. Resolve pass/fail and critical-error disagreements explicitly. An LLM judge may assist triage but cannot be the sole authority for final reported scores. Keep reward-model graders and final-test reviewers separate where practical.

### Calibration and selective answering

Attach three pre-authored binary questions to each final task: one instrument/evidence judgment, one method/tool eligibility judgment, and one evidence-sufficiency judgment. Use task-specific propositions with expert-adjudicated truth values. Return probability of the stated proposition, even when the research answer abstains. This targets 300 judgments but only 100 task clusters, not 300 independent research tasks. Report label balance and performance by question family; comparisons against constant base-rate predictions use rates fitted on development data only.

For y in {0,1} and p in [0,1], binary Brier score is mean((p-y)^2), lower is better. Also report log loss, clipping only for its calculation to [1e-6, 1-1e-6] and reporting clipping frequency. Invalid or missing probabilities are protocol violations; report their rate and withhold complete-set calibration claims rather than silently omitting them. Valid-subset scores must disclose coverage. Calibration scores do not replace accuracy or discrimination measures.

Require a separate predicted probability that the final research answer will satisfy all mandatory criteria without a critical error. Compare it with the adjudicated success label. Use this to report coverage versus failure/critical-error rates as low-confidence answers are deferred. Select operational thresholds on development data; freeze them before testing. Report abstention quality separately from research completion. A constant, uninformative probability can look calibrated, so include accuracy, task success, and useful coverage.

Reliability plots are exploratory at this size, especially within asset subgroups. Do not promise precise calibration of rare high-confidence failures from 100 tasks. Decision confidence is distinct from a financial-outcome probability; future return forecasts need realized outcomes and a separate prospective evaluation.

### Uncertainty and improvement claims

Use paired comparisons on identical tasks. Report raw paired outcomes and a 95% paired bootstrap interval for score differences, resampling whole task/lineage clusters (including all subquestions and repeated runs) with 10,000 draws and a recorded seed. These intervals describe this task sample and do not prove generalization to all investment research. Small asset-family samples warrant descriptive results, not broad superiority claims. Record all repeated runs; do not treat them as independent tasks or select the best run.

Predeclare the primary baseline and endpoint to avoid selecting the easiest comparison after testing. Secondary comparisons are exploratory unless a multiplicity policy is specified. For example, 60% to 69% success is **15% relative improvement, or 9 percentage points**. Always publish both rates and both forms of improvement. A 100-task set does not guarantee statistical power to establish a 15% effect; estimate required sample size from development discordance before making a confirmatory claim.

## First delivery and remaining work

Current deliverable: protocol, machine-readable coverage quotas, blank task template, and three synthetic development examples. Next gate: independent review of these examples, author the remaining development cases, define concrete budgets and model versions, then implement shared scoring and run it through both Jupyter and marimo. Final-task authoring and custody remain outstanding. Build this evaluation foundation before optimizing training; do not wait until after RLHF to define success.

## Methodological references

- [FinanceBench](https://arxiv.org/abs/2311.11944) provides a financial question-answering reference point. Our proposed task coverage extends into executable quantitative workflows and instrument-specific judgment; no superiority is established.
- [On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html) distinguishes prediction quality from probability calibration and motivates including a post-hoc calibration baseline. Calibration must be measured on our own held-out tasks.
- [TypeSafe's announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev) motivates the calibrated-decision experiment; the proposed protocol is our own design, not a reproduction of proprietary RLCD training.
