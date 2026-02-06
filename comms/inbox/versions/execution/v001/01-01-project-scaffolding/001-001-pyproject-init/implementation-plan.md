# Implementation Plan: 001-pyproject-init

## Overview

Create the project's pyproject.toml with uv build backend, metadata, and dev dependencies. Run `uv sync` to generate the lock file.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Create | Project manifest with metadata, build system, dev deps |

## Files Generated (by tooling)

| File | Action | Description |
|------|--------|-------------|
| `uv.lock` | Auto-generated | Lock file created by `uv sync` |

## Implementation Steps

### Stage 1: Create pyproject.toml

Create `pyproject.toml` with the following content:

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

### Stage 2: Generate lock file

```bash
uv sync
```

**Verify:**
```bash
# Lock file exists
ls uv.lock

# No errors from sync
uv sync 2>&1 | tail -1
```

## Quality Gates

```bash
uv sync  # Must complete without error
```

## Commit Message

```
feat(scaffold): initialize pyproject.toml with uv build backend

- Add project metadata (name, version, requires-python >= 3.11)
- Configure uv_build as build backend
- Add dev dependencies (pytest, ruff, mypy)
- Generate uv.lock
```