# Feature Flag Sweeper

> A small command-line review pass for feature flags.

![Feature Flag Sweeper cover](assets/readme-cover.svg)

Find stale and risky feature flags in config inventories. In practice it is a narrow guardrail for small developer checks: one command, a concrete report, and very little ceremony.

## Signals in plain English

- `ownerless-flag` (high): feature flag has no owner. Fix: Assign a responsible owner before rollout..
- `permanent-flag` (medium): flag has no cleanup date. Fix: Add an expiry date or removal ticket..
- `global-enabled` (low): flag appears globally enabled. Fix: Confirm whether the flag can be removed..

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/feature-flag-sweeper.git
cd feature-flag-sweeper
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
feature-flag-sweeper examples/sample.txt
feature-flag-sweeper examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m feature_flag_sweeper --help
```
