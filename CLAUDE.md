# CLAUDE.md — instructions for AI assistants working in this repo

> **What is this file?** Claude Code (and similar AI tools) automatically read this file
> at the start of every session. It's like an onboarding note for a new teammate:
> what the project is, how we work, and what rules to follow.

## About the owner — TEACHING MODE IS ON

The owner of this repo is a **beginner** and is using this project to learn.
For every change, the assistant MUST:

1. **Explain what each new file is** and why it exists, in plain English.
2. **Explain code**: what each function does, its inputs and outputs, and why it's written that way.
3. **Explain new concepts the first time they appear** (e.g. "What is a Service Principal?")
   and add them to `docs/learning/glossary.md`.
4. **Explain commands before running them**: what they do and whether they change anything.
5. Prefer small steps. Don't introduce several new tools at once without explaining each.

## Project summary

- **Status:** project idea not decided yet. This is a ready-to-go starter.
- **Language:** Python 3.12, managed with `uv`
- **Cloud:** Microsoft Azure. Infrastructure written in **Bicep** (`infra/`)
- **Microsoft 365:** Outlook and Teams will be accessed through **Microsoft Graph** (later)
- **CI/CD:** GitHub Actions (`.github/workflows/`)

## Folder map

| Path | What it holds |
|---|---|
| `src/not_decided_yet/` | The Python application code |
| `tests/` | Automated tests (run with `pytest`) |
| `infra/` | Bicep files that describe Azure resources |
| `.github/workflows/` | GitHub Actions automation (CI) |
| `docs/learning/` | Beginner explanations and glossary |
| `scripts/` | Helper scripts (e.g. Mac setup) |

## Commands

```bash
uv sync                 # install dependencies
uv run pytest           # run tests
uv run ruff check .     # lint (find code problems)
uv run ruff format .    # auto-format code
uv run python -m not_decided_yet   # run the app
```

## Rules

- **Never commit secrets.** Real values go in `.env` (git-ignored); only names go in `.env.example`.
- **Never deploy to Azure production** without the owner explicitly saying so.
- Azure resource names follow: `<type>-<project>-<env>` e.g. `st-ndy-dev`, `rg-ndy-dev`.
- Every new function gets a docstring and a test.
