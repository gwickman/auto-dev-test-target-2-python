# Requirements: 002-mypy-config

## Goal

Configure mypy with strict mode and Python 3.11 target in pyproject.toml.

## Background

mypy provides static type checking. Strict mode enables 14 checking flags via a single `strict = true` setting. The project's code surface (hello.py) uses only primitive types, so strict mode poses no risk.

- **Backlog:** BL-004 (mypy configuration with strict mode)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: mypy configuration**
- `[tool.mypy]` section in pyproject.toml with:
  - `python_version = "3.11"`
  - `strict = true`
- Acceptance: Configuration is present and valid

**FR-002: Type checking passes**
- `uv run mypy src/` passes with exit code 0
- Acceptance: No type errors reported

## Non-Functional Requirements

**NFR-001: Dev dependency**
- mypy is listed in `[dependency-groups]` dev (already added in 001-pyproject-init)

**NFR-002: Strict mode coverage**
- All public functions must have type annotations
- `strict = true` enables: warn_unused_configs, warn_redundant_casts, warn_unused_ignores, strict_equality, check_untyped_defs, disallow_subclassing_any, disallow_untyped_decorators, disallow_any_generics, disallow_untyped_calls, disallow_incomplete_defs, disallow_untyped_defs, no_implicit_reexport, warn_return_any, extra_checks

## Out of Scope

- Per-module mypy overrides
- Third-party type stubs

## Test Requirements

- Quality gate verification: `uv run mypy src/` passes with exit code 0
- No test file — mypy is a quality gate, not a testable feature

## Reference

Design artifacts: `comms/outbox/versions/design/v001/003-research/evidence-log.md` (mypy strict mode flags)