# Theme Design: 01-project-scaffolding

## Goal

Establish the complete Python project structure using uv as the package manager, with a src-layout package containing a minimal hello module. This theme delivers the foundational files that all quality gates and CI depend on.

## Design Artifacts

Full design analysis: `comms/outbox/versions/design/v001/`

Key references:
- Logical design: `004-logical-design/logical-design.md` (Theme 01 section)
- Refined design: `005-critical-thinking/refined-logical-design.md`
- Research: `003-research/external-research.md` (uv configuration)
- Evidence: `003-research/evidence-log.md` (concrete values)

## Backlog Items

| Item | Scope |
|------|-------|
| BL-001 | Project scaffolding — pyproject.toml, src layout, __init__.py |
| BL-006 | Hello world utility function for quality gate validation |

BL-001 covers structural aspects (pyproject.toml, package directory). BL-006 covers the hello() function implementation. Both are complete when feature 003-hello-module passes.

## Features

| Feature | Goal | Backlog | Dependencies |
|---------|------|---------|--------------|
| 001-pyproject-init | Initialize pyproject.toml with uv build backend | BL-001 | None |
| 002-package-structure | Create src/test_target_2/ package with __init__.py | BL-001 | 001 |
| 003-hello-module | Create hello.py with typed hello() function | BL-006 | 002 |

## Execution Order

Strictly sequential: 001 -> 002 -> 003

Each feature depends on the previous one's deliverables.

## Risks

- R-005 (uv_build version): Use `>=0.9.21,<0.10.0`. Confirmed valid by research.
- R-004 (BL overlap): Resolved. Clear structural vs functional split.