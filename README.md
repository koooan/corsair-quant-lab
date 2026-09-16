# Corsair Quant Lab

Learn to build software by shipping one financial-AI experiment every week.

**Cadence:** weekly releases, with the current scope in the roadmap. **Time budget:** 6–8 hours a week. **Format:** public GitHub release, executed Jupyter notebook, interactive marimo notebook, and a short demo/readout.

The capstone is a trained fixed-income research specialist, then a cross-asset research prototype, with asset-class distillation experiments. We will compare a specialist that delegates difficult work with a specialist that completes the same tasks without a frontier model. Neither path is presumed to win.

## Start here

- [Weekly roadmap](docs/ROADMAP.md)
- [Bridgewater: public evidence and experiments](docs/BRIDGEWATER.md)
- [Capstone design and promotion gates](docs/CAPSTONE.md)
- [Evaluation rules](docs/EVALUATION.md)
- [Project roster and access limits](docs/ROSTER.md)
- [First release](releases/week-01.md)

## Run the first experiment

Install [uv](https://docs.astral.sh/uv/), then run from this project directory:

```sh
uv sync --locked
uv run python scripts/build_release.py
uv run jupyter lab notebooks/jupyter/01_foundation.ipynb
```

For the interactive version:

```sh
uv run marimo edit notebooks/marimo/01_foundation.py
```

For a read-only local demo:

```sh
uv run marimo run notebooks/marimo/01_foundation.py
```

The first experiment uses a checked-in public FRED snapshot of US Treasury yields. It compares two simple numerical baselines on **development data**, exercises chronological evaluation, and validates both notebook interfaces. No AI model is trained or evaluated in this first release. It establishes the common measurement machinery for subsequent experiments.

## One experiment, two notebook interfaces

Shared calculations live in `corsair_lab/`. Jupyter provides a linear research record; marimo provides reactive exploration. Neither notebook contains a separate implementation of the metrics. Every future experiment must pass both execution paths before release.

```text
corsair_lab/       Shared data loading, model adapters, evaluation, plotting
config/           Project registry and dated release schedule
data/raw/         Redistributable source snapshots plus provenance
docs/             Scope, research notes, methodology, architecture
notebooks/        Jupyter and marimo interfaces
scripts/          Reproducible release commands
tests/            Temporal isolation, metrics, data-integrity checks
artifacts/        Generated results, provenance and HTML previews
releases/         Weekly findings and demo scripts
```

## What counts as shipping

A bounded question; working code in both notebook formats; source/weight/version records; an appropriate baseline; measured results or an explicitly documented access failure; limitations; and a 3-minute demo. A negative result is a valid release. Merely installing a package is not a completed experiment.

Traditional fixed-income models (Diebold–Li, ACM, and the excess bond premium model) are excluded from the project roster, as requested. Fixed-income *use cases* remain central. Simple no-change and statistical baselines remain necessary to evaluate the AI projects.

Training weights, private data, credentials, and proprietary documents do not belong in this repository. Model and data licenses are independent of this project's code. Paid APIs and GPU training require a defined budget before their scheduled experiment; the starter makes no paid calls.

## Learning by building

Each week, make one meaningful change yourself: implement a metric, write a loader, add a model adapter, inspect an error, or build a notebook control. Explain it in your own words in the release note. AI assistance should support this learning rather than turn the project into a sequence of opaque generated demos.

No recurring job or automatic publishing schedule is installed. The roadmap is a working schedule; releases are deliberate, reviewed artifacts.
