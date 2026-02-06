# Requirements: 003-pytest-setup

## Goal

Set up pytest with importlib import mode, create the tests/ directory, and write a basic passing test for the hello() function.

## Background

pytest is the project's test framework. It needs importlib import mode to work correctly with the src-layout package structure. This feature creates the first test file, validating the full test pipeline end-to-end.

- **Backlog:** BL-002 (pytest setup with basic passing test)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: pytest configuration**
- `[tool.pytest.ini_options]` section in pyproject.toml with:
  - `testpaths = ["tests"]`
  - `addopts = "--import-mode=importlib -ra -q"`
- Acceptance: Configuration is present and valid

**FR-002: Test directory structure**
- `tests/conftest.py` exists (empty or minimal)
- Acceptance: File is present

**FR-003: Test file**
- `tests/test_hello.py` exists with passing tests for hello():
  1. `hello()` returns `"Hello, World!"`
  2. `hello("Alice")` returns `"Hello, Alice!"`
  3. Return type is `str`
  4. Function is importable from `test_target_2.hello`
- Acceptance: `uv run pytest` passes with all tests green

## Non-Functional Requirements

**NFR-001: Dev dependency**
- pytest is listed in `[dependency-groups]` dev (already added in 001-pyproject-init)

**NFR-002: Import mode**
- importlib mode avoids sys.path manipulation; recommended for src layout

## Out of Scope

- Coverage configuration — no backlog item for v001
- Fixtures beyond conftest.py placeholder
- Integration tests

## Test Requirements

- `uv run pytest` passes with green output
- All 4 test cases pass
- importlib mode works correctly with src layout

## Reference

Design artifacts: `comms/outbox/versions/design/v001/003-research/evidence-log.md` (pytest settings)