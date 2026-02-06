# External Research — v001

All research conducted via DeepWiki MCP queries against official repositories.

## 1. uv Project Configuration (astral-sh/uv)

**Source**: DeepWiki query on astral-sh/uv

### pyproject.toml with src Layout

```toml
[project]
name = "test-target-2"
version = "0.1.0"
description = "A minimal Python utility library for auto-dev-mcp integration testing"
requires-python = ">=3.11"

[build-system]
requires = ["uv_build>=0.9.21,<0.10.0"]
build-backend = "uv_build"

[dependency-groups]
dev = ["pytest", "ruff", "mypy"]
```

Key findings:
- `[dependency-groups]` dev is the modern way (replaces deprecated `tool.uv.dev-dependencies`)
- `uv_build` is uv's native build backend for src layout
- `uv sync` installs all deps including dev group by default
- `uv.lock` is auto-generated; do not edit manually

## 2. ruff Configuration (astral-sh/ruff)

**Source**: DeepWiki query on astral-sh/ruff

### Recommended Configuration

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

Key findings:
- `E501` (line too long) should be ignored when using formatter — formatter handles wrapping
- `line-length = 88` matches Black convention, applies to both lint and format
- Rule sets: E (pycodestyle), F (pyflakes), I (isort), UP (pyupgrade), B (bugbear), SIM (simplify)

## 3. mypy Strict Mode (python/mypy)

**Source**: DeepWiki query on python/mypy

### Configuration

```toml
[tool.mypy]
python_version = "3.11"
strict = true
```

`strict = true` enables these 14 flags:
- `warn_unused_configs`, `warn_redundant_casts`, `warn_unused_ignores`
- `strict_equality`, `check_untyped_defs`
- `disallow_subclassing_any`, `disallow_untyped_decorators`
- `disallow_any_generics`, `disallow_untyped_calls`
- `disallow_incomplete_defs`, `disallow_untyped_defs`
- `no_implicit_reexport`, `warn_return_any`, `extra_checks`

## 4. pytest Configuration (pytest-dev/pytest)

**Source**: DeepWiki query on pytest-dev/pytest

### Configuration

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--import-mode=importlib -ra -q"
```

Key findings:
- `--import-mode=importlib` is recommended for src layout (avoids sys.path hacks)
- `testpaths = ["tests"]` restricts discovery to tests/ directory
- `-ra` shows summary of all non-passing tests; `-q` for quiet output
- conftest.py can be minimal or empty for initial setup

## 5. GitHub Actions with uv (astral-sh/uv)

**Source**: DeepWiki query on astral-sh/uv

### Recommended Workflow Structure

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

Key findings:
- `astral-sh/setup-uv@v7` is the official action
- `enable-cache: true` persists uv cache between runs
- `uv sync --locked` ensures lockfile matches (fails if out of sync)
- `uv run` executes in project environment with all deps available
- No need for `actions/setup-python` — uv handles Python installation
