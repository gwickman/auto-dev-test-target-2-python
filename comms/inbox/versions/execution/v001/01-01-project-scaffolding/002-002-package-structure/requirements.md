# Requirements: 002-package-structure

## Goal

Create the `src/test_target_2/` package directory with `__init__.py` containing version info.

## Background

With pyproject.toml established (feature 001), this feature creates the source package that all quality gates will target. The src-layout pattern is standard for modern Python projects and avoids import ambiguity.

- **Backlog:** BL-001 (Python project scaffolding)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: Package directory**
- `src/test_target_2/` directory exists
- Acceptance: Directory is present

**FR-002: Init module**
- `src/test_target_2/__init__.py` exists with `__version__ = "0.1.0"`
- Acceptance: `from test_target_2 import __version__` returns `"0.1.0"`

## Non-Functional Requirements

**NFR-001: Version consistency**
- `__version__` in `__init__.py` must match `version` in pyproject.toml (`"0.1.0"`)

## Out of Scope

- hello.py module — added in feature 003
- Any utility functions — deferred to v002

## Test Requirements

- Verification only: Package is importable
- Importability is implicitly tested by feature 003's test file

## Reference

Design artifacts: `comms/outbox/versions/design/v001/004-logical-design/logical-design.md` (Theme 01 features)