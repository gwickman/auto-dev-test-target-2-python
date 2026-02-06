# Version Context — v001 Foundation

## Version Goals

v001 "Foundation" establishes the complete project infrastructure for auto-dev-test-target-2-python. The goal is to create a working Python project with all quality gates passing and CI configured, providing the base upon which utility modules (v002) and validation (v003) will be built.

## Version Description

Two themes deliver project scaffolding and quality/CI infrastructure:

- **Theme 1 — Project Scaffolding**: Create the Python project structure using uv as the package manager, with a `src/test_target_2/` package containing a minimal `hello.py` module
- **Theme 2 — Quality & CI**: Configure ruff (linting + formatting), mypy (strict mode), pytest (with a basic passing test), and a GitHub Actions CI workflow

## Referenced Backlog Items

| Item | Theme |
|------|-------|
| BL-001 | Theme 1 (Project Scaffolding) |
| BL-002 | Theme 2 (Quality & CI) |
| BL-003 | Theme 2 (Quality & CI) |
| BL-004 | Theme 2 (Quality & CI) |
| BL-005 | Theme 2 (Quality & CI) |
| BL-006 | Theme 1 (Project Scaffolding) |

Note: Full backlog item details will be gathered in Task 002.

## Constraints and Assumptions

- **No investigation dependencies**: All technologies (pytest, ruff, mypy, GitHub Actions) are well-understood and require no spikes or explorations
- **Prerequisites**: None — v001 is the first version with no dependencies
- **Package Manager**: uv (specified in PLAN.md)
- **Destructive Test Target**: This project is marked as a disposable test target for auto-dev-mcp integration testing

## Deferred Items

- **v002 (Utility Library)**: String utils, math utils, collection utils — deferred because v001 focuses purely on infrastructure
- **v003 (Validation & Error Handling)**: Exception hierarchy, validators, property-based testing — deferred because it depends on v002 utility modules existing first

## Scoping Rationale

Everything needed for a working Python project with passing quality gates lands together in v001. Without scaffolding, there is nothing for ruff/mypy/pytest to run against. Without CI, there is no way to validate the auto-dev PR workflow. These form one cohesive foundation unit.
