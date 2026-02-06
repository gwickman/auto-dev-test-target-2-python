# Requirements: 003-hello-module

## Goal

Create hello.py with a typed hello() function returning a greeting string.

## Background

This feature provides the minimal code surface for all quality gates to run against. The function must be fully typed for mypy strict compliance.

- **Backlog:** BL-006 (Hello world utility function)
- **Also satisfies:** BL-001 acceptance criterion 3 (hello.py exists with hello() function)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: hello function**
- `src/test_target_2/hello.py` contains `def hello(name: str = "World") -> str`
- Function returns a greeting string (e.g., `"Hello, World!"`)
- Acceptance: `hello()` returns `"Hello, World!"`; `hello("Alice")` returns `"Hello, Alice!"`

**FR-002: Importability**
- Function is importable: `from test_target_2.hello import hello`
- Acceptance: Import succeeds without error

**FR-003: Type annotations**
- All parameters and return type are annotated
- Acceptance: `uv run mypy src/` passes (verified in Theme 02)

## Non-Functional Requirements

**NFR-001: mypy strict compliance**
- Function must pass mypy strict mode (all 14 flags)
- Uses only primitive types (str) — no generics or complex patterns needed

## Out of Scope

- Unit tests — created in Theme 02, Feature 003 (pytest-setup)
- Re-exporting hello from __init__.py — not required by backlog

## Test Requirements

- Unit tests created in Theme 02 (003-pytest-setup):
  1. `hello()` returns string containing "World"
  2. `hello("Alice")` returns string containing "Alice"
  3. Return type is `str`
  4. Function is importable from `test_target_2.hello`

## Reference

Design artifacts: `comms/outbox/versions/design/v001/003-research/evidence-log.md` (hello() typing)