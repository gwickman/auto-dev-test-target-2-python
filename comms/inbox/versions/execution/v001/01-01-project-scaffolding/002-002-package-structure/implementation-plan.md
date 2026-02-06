# Implementation Plan: 002-package-structure

## Overview

Create the src-layout package directory with __init__.py.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `src/test_target_2/__init__.py` | Create | Package init with __version__ |

## Implementation Steps

### Stage 1: Create package directory and __init__.py

Create `src/test_target_2/__init__.py`:

```python
"""test_target_2 — A minimal Python utility library."""

__version__ = "0.1.0"
```

### Stage 2: Verify

```bash
# Package is importable
uv run python -c "from test_target_2 import __version__; print(__version__)"
```

Expected output: `0.1.0`

## Quality Gates

```bash
uv run python -c "from test_target_2 import __version__; assert __version__ == '0.1.0'"
```

## Commit Message

```
feat(scaffold): create src/test_target_2 package with __init__.py

- Create src-layout package directory
- Add __init__.py with __version__ = "0.1.0"
```