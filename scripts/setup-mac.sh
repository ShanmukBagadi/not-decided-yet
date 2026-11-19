#!/usr/bin/env bash
# setup-mac.sh — installs everything you need on your MacBook to work on this repo.
# Run from the repo folder:  bash scripts/setup-mac.sh
# Safe to run more than once: it skips anything already installed.

set -euo pipefail   # stop immediately if any command fails

echo "==> 1/6 Homebrew (the Mac package manager: installs other tools)"
if ! command -v brew >/dev/null; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "==> 2/6 Core tools: git, uv (Python manager), Azure CLI, GitHub CLI"
brew install git uv azure-cli gh

echo "==> 3/6 Bicep (Azure infrastructure language)"
az bicep install || az bicep upgrade

echo "==> 4/6 Python + project dependencies (creates .venv/)"
uv sync

echo "==> 5/6 Git pre-commit hooks (secret scanning, formatting)"
uv run pre-commit install

echo "==> 6/6 Local settings file"
[ -f .env ] || cp .env.example .env

cat <<'EOF'

Done! Next steps:
  1. az login                 # sign in to Azure (opens browser)
  2. az account show          # copy "id" and "tenantId" into .env
  3. uv run pytest            # tests should pass
  4. uv run python -m not_decided_yet
Optional: install VS Code (brew install --cask visual-studio-code)
          and Claude Code (see https://code.claude.com)
EOF
