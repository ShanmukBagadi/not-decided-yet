# not-decided-yet

An AI-native Python + Azure starter repo. The project idea isn't decided yet, but the setup is ready.

**New here? Read [docs/learning/00-start-here.md](docs/learning/00-start-here.md)**, then the
[glossary](docs/learning/glossary.md).

## Quick start (MacBook)

```bash
git clone https://github.com/ShanmukBagadi/not-decided-yet.git
cd not-decided-yet
bash scripts/setup-mac.sh
uv run pytest
uv run python -m not_decided_yet
```

## Stack

- **Python 3.12** with [uv](https://docs.astral.sh/uv/), pytest, ruff
- **Azure** infrastructure in **Bicep** (`infra/`)
- **GitHub Actions** CI (`.github/workflows/ci.yml`)
- AI-assistant instructions in [CLAUDE.md](CLAUDE.md)
