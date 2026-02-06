# Implementation Plan: 004-github-actions

## Overview

Create the GitHub Actions CI workflow file that runs all quality gates.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `.github/workflows/ci.yml` | Create | CI workflow with all quality gates |

## Implementation Steps

### Stage 1: Create workflow directory and file

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v7
        with:
          enable-cache: true
      - run: uv sync --locked --dev
      - run: uv run ruff check src/
      - run: uv run ruff format --check src/
      - run: uv run mypy src/
      - run: uv run pytest
```

### Stage 2: Verify locally

```bash
# Validate YAML syntax (basic check)
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))" 2>/dev/null || echo "Note: yaml module not available, will verify via CI"
```

### Stage 3: Verify via PR

The CI workflow is ultimately verified by creating a PR and watching checks:

```bash
gh pr create --fill --base main
gh pr checks --watch
```

If CI fails, follow AGENTS.md workflow: `gh run view --log-failed`, fix, push (max 3 iterations).

## Quality Gates

CI verification happens during the PR workflow for Theme 02. All four quality gate steps must pass:
1. `uv run ruff check src/`
2. `uv run ruff format --check src/`
3. `uv run mypy src/`
4. `uv run pytest`

## Commit Message

```
feat(ci): add GitHub Actions CI workflow

- Trigger on push and PR to main
- Use astral-sh/setup-uv@v7 with caching
- Run ruff check, ruff format --check, mypy, and pytest
```