# Feature Flag Sweeper

![Feature Flag Sweeper cover](assets/readme-cover.svg)

> Find stale and risky feature flags in config inventories

![stack](https://img.shields.io/badge/stack-Python-b45309?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-be185d?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-4b5563?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-2563eb?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | feature flags |
| Command | `feature-flag-sweeper` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `ownerless-flag` | high | feature flag has no owner |
| `permanent-flag` | medium | flag has no cleanup date |
| `global-enabled` | low | flag appears globally enabled |

## Try it locally

```bash
python -m pip install -e ".[dev]"
feature-flag-sweeper examples/sample.txt
feature-flag-sweeper examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m feature_flag_sweeper --help
```
