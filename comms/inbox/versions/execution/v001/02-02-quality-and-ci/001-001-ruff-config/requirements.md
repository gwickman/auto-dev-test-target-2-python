# Requirements: 001-ruff-config

## Goal

Configure ruff linting and formatting rules in pyproject.toml.

## Background

Ruff provides both linting and formatting for the project. Configuration uses `[tool.ruff]` sections in pyproject.toml. The E501 rule is ignored because the formatter handles line length.

- **Backlog:** BL-003 (ruff configuration)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: Ruff base configuration**
- `[tool.ruff]` section in pyproject.toml with:
  - `line-length = 88`
  - `target-version = "py311"`
- Acceptance: Configuration is present and valid

**FR-002: Lint rules**
- `[tool.ruff.lint]` section with:
  - `select = ["E", "F", "I", "UP", "B", "SIM"]`
  - `ignore = ["E501"]`
- Acceptance: `uv run ruff check src/` passes

**FR-003: Format configuration**
- `[tool.ruff.format]` section with:
  - `quote-style = "double"`
  - `indent-style = "space"`
  - `skip-magic-trailing-comma = false`
  - `line-ending = "auto"`
- Acceptance: `uv run ruff format --check src/` passes

## Non-Functional Requirements

**NFR-001: Dev dependency**
- ruff is listed in `[dependency-groups]` dev (already added in 001-pyproject-init)

## Out of Scope

- Per-file rule overrides
- Custom rule plugins

## Test Requirements

- Quality gate verification: `uv run ruff check src/` and `uv run ruff format --check src/` both pass with exit code 0
- No test file — ruff is a quality gate, not a testable feature

## Reference

Design artifacts: `comms/outbox/versions/design/v001/003-research/evidence-log.md` (ruff rule sets, formatting settings)