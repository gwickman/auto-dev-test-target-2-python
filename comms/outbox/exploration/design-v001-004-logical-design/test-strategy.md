# Test Strategy — v001 Foundation

## Overview

v001 has minimal test surface — one module (`hello.py`) with one function (`hello()`). The test strategy focuses on validating that all quality gates work end-to-end rather than extensive unit testing.

## Test Requirements by Feature

### Theme 01: `01-project-scaffolding`

#### Feature `001-pyproject-init`

**Test type:** Verification (not unit test)
- `uv sync` completes without error
- `uv.lock` is generated
- No automated test file needed — verified by successful command execution

#### Feature `002-package-structure`

**Test type:** Verification (not unit test)
- `src/test_target_2/__init__.py` exists and is importable
- `from test_target_2 import __version__` works
- No dedicated test file — importability is implicitly tested by Feature 003's tests

#### Feature `003-hello-module`

**Test type:** Unit test
- **Test file:** `tests/test_hello.py` (created in Theme 02, Feature 003)
- Tests:
  1. `hello()` returns a string
  2. `hello()` with default argument returns expected greeting
  3. `hello("Alice")` returns greeting with name
  4. `hello` is importable from `test_target_2.hello`

**Note:** The test file is created in Theme 02 Feature 003 (pytest-setup), but the function being tested is from this feature. This is by design — Theme 01 creates the code, Theme 02 creates the test infrastructure.

---

### Theme 02: `02-quality-and-ci`

#### Feature `001-ruff-config`

**Test type:** Quality gate verification
- `uv run ruff check src/` passes with exit code 0
- `uv run ruff format --check src/` passes with exit code 0
- No test file — ruff is a quality gate, not a testable feature

#### Feature `002-mypy-config`

**Test type:** Quality gate verification
- `uv run mypy src/` passes with exit code 0
- All functions in `hello.py` have type annotations
- No test file — mypy is a quality gate, not a testable feature

#### Feature `003-pytest-setup`

**Test type:** Unit test + infrastructure verification
- **Test file:** `tests/test_hello.py`
- **Fixture file:** `tests/conftest.py` (empty or minimal)
- Tests for `hello()` function (see Feature 003 above)
- `uv run pytest` passes with green output
- Importlib mode works correctly with src layout

#### Feature `004-github-actions`

**Test type:** Integration verification
- CI workflow triggers on push to main
- All four steps pass: ruff check, ruff format --check, mypy, pytest
- Verified by `gh pr checks --watch` during PR workflow
- No test file — CI is verified by successful workflow run

---

## Test File Summary

| File | Contents | Created By |
|------|----------|------------|
| `tests/conftest.py` | Empty (no shared fixtures needed for v001) | Theme 02, Feature 003 |
| `tests/test_hello.py` | Unit tests for `hello()` function | Theme 02, Feature 003 |

## Quality Gate Verification Order

After all features are implemented, the full quality gate suite should pass:

```bash
uv run ruff check src/           # Linting
uv run ruff format --check src/  # Formatting
uv run mypy src/                 # Type checking
uv run pytest                    # Tests
```

This matches the order defined in AGENTS.md and the CI workflow.

## Test Coverage Expectations

- **v001 target:** 100% of `hello.py` (single function)
- **Coverage tooling:** Not configured in v001 (no backlog item for it)
- **Future:** Coverage configuration can be added in v002 when more modules exist
