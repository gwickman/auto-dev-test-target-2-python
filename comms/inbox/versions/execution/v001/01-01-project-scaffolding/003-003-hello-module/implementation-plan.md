# Implementation Plan: 003-hello-module

## Overview

Create the hello module with a typed hello() function.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `src/test_target_2/hello.py` | Create | Hello module with typed hello() function |

## Implementation Steps

### Stage 1: Create hello.py

Create `src/test_target_2/hello.py`:

```python
"""Hello module — minimal utility for quality gate validation."""


def hello(name: str = "World") -> str:
    """Return a greeting string.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
```

### Stage 2: Verify

```bash
# Function works
uv run python -c "from test_target_2.hello import hello; print(hello()); print(hello('Alice'))"
```

Expected output:
```
Hello, World!
Hello, Alice!
```

## Quality Gates

```bash
uv run python -c "from test_target_2.hello import hello; assert hello() == 'Hello, World!'; assert hello('Alice') == 'Hello, Alice!'"
```

## Commit Message

```
feat(scaffold): add hello module with typed hello() function

- Create src/test_target_2/hello.py
- Implement hello(name: str = "World") -> str
- Full type annotations for mypy strict compliance
```