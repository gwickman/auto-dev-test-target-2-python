# Task 004: Logical Design Proposal — v001 Foundation

The v001 Foundation version is structured as 2 themes with 7 features total. Theme 01 (`01-project-scaffolding`, 3 features) establishes the Python project structure using uv, and Theme 02 (`02-quality-and-ci`, 4 features) configures all quality gates and CI. All 6 backlog items (BL-001 through BL-006) are mapped to specific features with no deferrals.

## Theme Overview

### Theme 01: `01-project-scaffolding` (BL-001, BL-006)

Establish the complete Python project structure using uv as the package manager, with a src-layout package containing a minimal hello module. Three features execute sequentially: pyproject.toml initialization, package structure creation, and hello module implementation.

### Theme 02: `02-quality-and-ci` (BL-002, BL-003, BL-004, BL-005)

Configure all quality gate tooling (ruff, mypy, pytest) and a GitHub Actions CI workflow. Three tool-configuration features can execute in any order, followed by the CI workflow feature which depends on all three.

## Key Decisions

1. **BL-001/BL-006 overlap resolved:** BL-001 maps to structural features (pyproject-init, package-structure); BL-006 maps to function implementation (hello-module). Both are completed when 003-hello-module passes. This avoids duplicate work while preserving clear feature boundaries.

2. **All config in pyproject.toml:** ruff, mypy, and pytest are all configured in pyproject.toml sections rather than separate config files. This follows Task 003 research recommendations and keeps the project clean.

3. **Theme 02 features are partially parallelizable:** ruff, mypy, and pytest configuration are independent of each other and could execute in any order. Only the GitHub Actions feature depends on all three.

4. **uv_build as build backend:** Following Task 003 research, using uv's native build backend rather than hatchling or setuptools.

## Dependencies

Theme 01 must complete before Theme 02 begins — quality gates need source files to operate on. Within Theme 01, features are strictly sequential (pyproject.toml → package → module). Within Theme 02, features 001-003 are independent; feature 004 (GitHub Actions) depends on all three.

## Risks and Unknowns

| Risk | Severity | Notes |
|------|----------|-------|
| CI first-run failure | Medium | Covered by AGENTS.md 3-iteration limit |
| uv_build version pinning | Low | Verify at implementation time |
| BL-001/BL-006 overlap | Low | Resolved in design — features clearly separated |
| mypy strict false positives | Low | Trivial code, annotations written from scratch |
| uv.lock merge conflicts | Low | Single active branch for v001 |

No items require dedicated investigation in Task 005. All risks have mitigations in place.

## Output Documents

- **[logical-design.md](./logical-design.md)** — Complete theme breakdown, feature tables, execution order, research sources
- **[test-strategy.md](./test-strategy.md)** — Test requirements per feature
- **[risks-and-unknowns.md](./risks-and-unknowns.md)** — All identified risks for Task 005 review
