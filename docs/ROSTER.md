# Reference project roster

This catalog is retained for reference. The current roadmap supersedes its original week assignments.

No project below has been executed in release 01. `reference_only` denotes a public-methods study, not a runnable reproduction. This roster excludes Diebold–Li, ACM, and excess bond premium models.

| Project | Track | Schedule | Planned use case | Access/constraint |
|---|---|---|---|---|
| [FinBERT](https://huggingface.co/ProsusAI/finbert) | text | Unscheduled | Financial sentiment; issuer-news transfer | Weights available; inspect checkpoint terms |
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | text | Unscheduled | Sentiment and relevance-transfer experiment | Select one adapter; base-model terms also apply |
| [Fin-R1](https://huggingface.co/SUFE-AIFLM-Lab/Fin-R1) | reasoning | Unscheduled | Verified numerical QA and code tasks | Open checkpoint; GPU feasibility check |
| [BloombergGPT](https://arxiv.org/abs/2303.17564) | reference | Unscheduled | Pretraining design and evaluation critique | No downloadable checkpoint identified; study only |
| [Chronos-2](https://github.com/amazon-science/chronos-forecasting) | forecasting | Unscheduled | Yield changes and macro series | Public code/weights; pin revision |
| [TimeGPT](https://github.com/Nixtla/nixtla) | forecasting | Unscheduled | Same target windows as Chronos | Hosted API; credentials and spend cap required |
| [TimesFM](https://github.com/google-research/timesfm) | forecasting | Unscheduled | Univariate and related-series forecasting | 3.0 weights noncommercial/nonproduction; 2.5 Apache-2.0 |
| [Moirai](https://github.com/SalesforceAIResearch/uni2ts) | forecasting | Unscheduled | Same numerical benchmark | Pin checkpoint and inspect version capabilities |
| [Granite TTM](https://github.com/ibm-granite/granite-tsfm) | forecasting | Unscheduled | Lightweight numerical forecasting | Select daily-frequency-compatible checkpoint |
| [Kronos](https://github.com/shiyu-coder/Kronos) | forecasting | Unscheduled | Liquid-instrument OHLCV forecast | Not a bond convention or cash-flow model |
| [TabPFN](https://github.com/PriorLabs/TabPFN) | tabular | Unscheduled | Structured macro/issuer observations | Check chosen version license and data limits |
| [N-HiTS](https://github.com/Nixtla/neuralforecast) | trainable | Unscheduled | Small-budget supervised forecast | Architecture to train, not a financial checkpoint |
| [Temporal Fusion Transformer](https://github.com/Nixtla/neuralforecast) | trainable | Unscheduled | Covariate-informed forecast | Architecture to train; fixed tuning budget |
| [PatchTST](https://github.com/Nixtla/neuralforecast) | trainable | Unscheduled | Patch-based sequence forecast | Architecture to train; fixed tuning budget |
| [Qlib](https://github.com/microsoft/qlib) | research_system | Unscheduled | One reproducible research/backtest pipeline | Equity-oriented examples; adapt assumptions explicitly |
| [RD-Agent](https://github.com/microsoft/RD-Agent) | research_system | Unscheduled | One factor proposal/test loop | LLM/API access; isolated execution and fixed budget |
| [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | research_system | Unscheduled | Issuer memo and citation support | External providers may require credentials |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | policy | Unscheduled | Tiny simulated allocation task after costs | Training framework; no live trading |
| [Bridgewater AIA](https://arxiv.org/abs/2511.07678) | reference | Unscheduled | Independent supervision/calibration and relevance experiments | Public methods only; private system unavailable |

Version and license checks are repeated when each experiment is implemented. No pretrained model is assumed to have clean historical holdouts.
