# Start here: a tour of this repo, file by file

Read this first. Each section answers: **What is it? Why do we have it?**

---

## The big picture

```
You (on Mac) ──write code──▶ Git (local history) ──push──▶ GitHub (online copy)
                                                              │
                                                              ▼
                                                   GitHub Actions (auto checks)
                                                              │
                                                     (later) deploy ▼
                                                       Azure (cloud resources)
```

- **Git** saves snapshots ("commits") of your code on your computer.
- **GitHub** stores those snapshots online, so they're backed up and shareable.
- **GitHub Actions** are robots on GitHub that test your code each time you push.
- **Azure** is Microsoft's cloud, where your app and its resources will run.

---

## Files for AI assistants ("AI-native" part)

| File | What it does |
|---|---|
| `CLAUDE.md` | Instructions Claude reads automatically: project summary, rules, and **teaching mode** (always explain things to you). |
| `AGENTS.md` | Same idea for other AI tools; it just points to `CLAUDE.md`. |

"AI-native" means the repo is written so an AI assistant can understand it quickly
and safely: clear instructions, clear folder layout, automated tests to check its work,
and guardrails (secret scanning) so mistakes get caught.

---

## Python project files

| File | What it does |
|---|---|
| `pyproject.toml` | The project's ID card: name, Python version, libraries needed, tool settings. |
| `.python-version` | Tells `uv` which Python version to use (3.12). |
| `uv.lock` | Exact versions of every library installed, so every machine gets identical versions. Auto-generated; don't edit by hand. |
| `src/not_decided_yet/__init__.py` | Makes the folder a Python *package* (importable code). |
| `src/not_decided_yet/config.py` | Loads settings (Azure IDs, environment name) from environment variables. |
| `src/not_decided_yet/__main__.py` | The program's starting point. Run it with `uv run python -m not_decided_yet`. |
| `tests/test_config.py` | Automated tests that check `config.py` works. |

**Why `src/` layout?** Putting code in `src/` forces tests to use the *installed* package,
which catches packaging mistakes early. It's the modern recommended layout.

---

## Settings & secrets

| File | What it does |
|---|---|
| `.env.example` | A template listing setting *names* only. Safe to commit. |
| `.env` | Your real values. **Git-ignored and never uploaded.** You create it from the example. |
| `.gitignore` | List of files git must never track (secrets, caches, junk). |

---

## Code-quality tools

| File | What it does |
|---|---|
| `.editorconfig` | Basic formatting rules (spaces, line endings) every editor follows. |
| `.pre-commit-config.yaml` | Checks that run *before each commit*: blocks secrets, fixes formatting. |

---

## Automation

| File | What it does |
|---|---|
| `.github/workflows/ci.yml` | GitHub Actions workflow: on every push, lints + tests Python and validates Bicep. |

---

## Azure infrastructure

| File | What it does |
|---|---|
| `infra/main.bicep` | Describes Azure resources as code (one storage account for now). |
| `infra/README.md` | How to preview, deploy, and delete those resources. |

---

## Helpers

| File | What it does |
|---|---|
| `scripts/setup-mac.sh` | One script that installs everything on your MacBook. |
| `docs/learning/glossary.md` | Every term explained in plain English. **Keep growing this.** |
