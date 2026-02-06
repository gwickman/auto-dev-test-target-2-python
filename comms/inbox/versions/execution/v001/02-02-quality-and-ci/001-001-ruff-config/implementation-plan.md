# Implementation Plan: 001-ruff-config

## Overview

Add ruff linting and formatting configuration to pyproject.toml.

## Files to Modify

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Modify | Add [tool.ruff], [tool.ruff.lint], [tool.ruff.format] sections |

## Implementation Steps

### Stage 1: Add ruff configuration to pyproject.toml

Append to `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```

### Stage 2: Run ruff and fix any issues

```bash
# Check linting
uv run ruff check src/

# Check formatting
uv run ruff format --check src/
```

If formatting issues exist:
```bash
uv run ruff format src/
```

### Stage 3: Verify

```bash
uv run ruff check src/
uv run ruff format --check src/
```

Both must pass with exit code 0.

## Quality Gates

```bash
uv run ruff check src/
uv run ruff format --check src/
```

## Commit Message

```
feat(quality): configure ruff linting and formatting

- Add [tool.ruff] with line-length 88, target Python 3.11
- Select rules: E, F, I, UP, B, SIM (ignore E501)
- Configure format: double quotes, space indent, auto line-ending
```