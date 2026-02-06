# Handoff: 001-001-ruff-config -> next feature

## What Was Done

Ruff linting and formatting is now configured in pyproject.toml with:
- Line length 88, target Python 3.11
- Lint rules: E, F, I, UP, B, SIM (E501 ignored — formatter handles line length)
- Format: double quotes, space indent, auto line-ending

## For Next Feature

- Ruff is ready to use as a quality gate
- Run `uv run ruff check src/` and `uv run ruff format --check src/` to validate
- Run `uv run ruff format src/` to auto-fix formatting issues
- Run `uv run ruff check --fix src/` to auto-fix lint issues
