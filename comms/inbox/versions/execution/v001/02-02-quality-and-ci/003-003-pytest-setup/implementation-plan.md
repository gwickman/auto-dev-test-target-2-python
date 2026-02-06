# Implementation Plan: 003-pytest-setup

## Overview

Configure pytest in pyproject.toml, create tests/ directory with conftest.py, and write tests for the hello() function.

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Modify | Add [tool.pytest.ini_options] section |
| `tests/conftest.py` | Create | Empty conftest placeholder |
| `tests/test_hello.py` | Create | Unit tests for hello() function |

## Implementation Steps

### Stage 1: Add pytest configuration to pyproject.toml

Append to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--import-mode=importlib -ra -q"
```

### Stage 2: Create test directory and conftest

Create `tests/conftest.py`:

```python
"""Shared test configuration and fixtures."""
```

### Stage 3: Create test file

Create `tests/test_hello.py`:

```python
"""Tests for the hello module."""

from test_target_2.hello import hello


def test_hello_default() -> None:
    """hello() with default argument returns greeting with World."""
    assert hello() == "Hello, World!"


def test_hello_custom_name() -> None:
    """hello() with custom name returns personalized greeting."""
    assert hello("Alice") == "Hello, Alice!"


def test_hello_returns_string() -> None:
    """hello() returns a string."""
    result = hello()
    assert isinstance(result, str)


def test_hello_importable() -> None:
    """hello is importable from test_target_2.hello."""
    from test_target_2.hello import hello as h

    assert callable(h)
```

### Stage 4: Verify

```bash
uv run pytest
```

Expected: All 4 tests pass.

## Quality Gates

```bash
uv run pytest
```

## Commit Message

```
feat(quality): set up pytest with hello module tests

- Configure pytest with importlib mode and testpaths
- Create tests/conftest.py
- Add 4 passing tests for hello() function
```