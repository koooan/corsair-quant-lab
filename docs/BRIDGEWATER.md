# What we can learn from Bridgewater

Reviewed September 15, 2026. This is a public-source design study, not access to Bridgewater's models, data, portfolio, or infrastructure.

## Public evidence

Bridgewater describes AIA as an artificial-investor research effort supported by proprietary economic data, investment reasoning, and expert feedback. Its claimed live-investment results are company statements, not results independently reproduced here. [AIA Labs](https://www.bridgewater.com/aia-labs)

The AIA Forecaster report describes news research, a supervisor that reconciles forecasts, and statistical calibration. The authors report matching superforecasters on ForecastBench. On their prediction-market benchmark, the system alone lagged market consensus, while combining the two improved on consensus. These are event-probability results, not evidence of a universal asset-return predictor. [Technical report, November 2025](https://arxiv.org/abs/2511.07678)

A June 2026 study with Thinking Machines targets six document-filtering tasks using expert-reviewed labels and Qwen3-235B training. It reports average accuracy of 84.7%, versus 78.2% for its best tested frontier comparator. The scope is information processing, not full investment research. [Expert judgment study](https://thinkingmachines.ai/news/learning-to-replicate-expert-judgment-in-financial-tasks/)

## Our independent experiments

1. **Relevance:** label whether public central-bank passages help answer a specific rates question. Separate financial relevance from decision usefulness. Compare a prompt baseline, a small fine-tune, and human agreement.
2. **Judgmental forecasting:** freeze a public evidence packet at a timestamp. Generate probabilities, reconcile disagreements, and calibrate only on earlier resolved examples. Compare with a base-rate forecast and timestamp-matched public consensus where available.
3. **Supervision:** deliberately insert wrong units, mismatched dates, and unsupported causal conclusions into tool outputs. Measure how often the specialist detects them before accepting a delegated result.
4. **Learning from errors:** use reviewed failures to improve the training set, without recycling final-test examples into training.

These are our proposals, not claims about Bridgewater's unpublished implementation. Begin with inexpensive supervised fine-tuning; reproduce complex reinforcement-learning recipes only if simpler methods and the budget justify it.

## What remains unknown

The full private corpus, current production architecture, proprietary model weights, complete evaluation sets, investment constraints, and attribution of live returns are not available through these sources. We cannot reproduce AIA as a whole or verify its reported investment performance.
