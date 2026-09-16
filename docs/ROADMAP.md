# Current project roadmap

Budget: 6–8 hours per week. Ship public code with Jupyter and marimo notebooks and a weekly demo. Week labels express the working sequence; delivery dates are not fixed here. This replaces the earlier sixteen-week project schedule.

| Week | Project | Scope and status |
|---|---|---|
| 1 | Research foundation and Curvy-CUSIPs | Notebook foundation released; complete Curvy-CUSIPs fork created at https://github.com/koooan/Curvy-CUSIPs. Explore the existing project before extending it. |
| 2 | Multi-Asset Analyst with RLHF | Train an initial analyst prototype from human feedback. Maintain a small untouched evaluation set before training; distinguish actual RLHF from other preference-training methods. |
| 2.5 | Multi-Asset Research Benchmark | [Design drafted](BENCHMARK.md): 100 final tasks across six FICC asset families and five research skills; three synthetic public development examples. Task authoring, expert review, and scorer implementation remain. Define evaluation before optimizing training. |
| 3 | Sharpe hacking project | Refer to the user's Claude context. That context is not available in this workspace; detailed scope is pending it. |
| 4 | Kalshi / CME / Polymarket FOMC arbitrage strategy | Research and test the proposed strategy. Establish comparable contract outcomes, settlement rules, executable prices, costs, and hedge exposure before claiming an arbitrage. No live trading is scheduled. |

## Analyst product direction

Eventually serve the analyst free to invited hedge-fund researchers and collect structured human feedback. Separate permission to use the product from explicit opt-in to contribute material to training. Review feedback quality and preserve an independent test set. Set an inference budget and usage limits before opening access.

Open-sourcing is under consideration, not a commitment to release private feedback or restricted model weights. Code, evaluation tools, training recipes, and adapters can be considered separately according to their rights and licenses.

Compare a trained specialist working independently with one that delegates difficult quantitative work to a frontier model while retaining task ownership and verification. Asset-class distillation remains a longer-term direction without an assigned week.

## Working rules

- Build one bounded experiment at a time; no additional future projects are scheduled.
- Keep the existing model roster as a reference catalog, not a committed release schedule.
- A proposed strategy is a research question, not an established profitable opportunity.
- Training milestones depend on reviewed examples, evaluation readiness, and an agreed compute budget.
- Preserve actual run results and label planned, unavailable, and completed work distinctly.
