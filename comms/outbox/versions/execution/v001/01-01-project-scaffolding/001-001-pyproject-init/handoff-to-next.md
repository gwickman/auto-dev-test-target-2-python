# Handoff: 001-001-pyproject-init -> Next Feature

## What Was Done

- `pyproject.toml` created with project metadata, uv_build backend, and dev dependencies
- `src/test_target_2/__init__.py` created as empty placeholder for src-layout
- `tests/__init__.py` created as empty placeholder
- `uv.lock` generated with all dev dependencies resolved

## What the Next Feature Needs to Know

- The package is named `test-target-2` (import as `test_target_2`)
- Build backend is `uv_build` with src-layout convention
- Dev dependencies installed: pytest, ruff, mypy
- Tool configuration sections (ruff, mypy, pytest) are NOT yet in pyproject.toml — those are planned for Theme 02
- `uv sync` must continue to pass after any changes to pyproject.toml
