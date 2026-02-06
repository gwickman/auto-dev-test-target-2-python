# auto-dev-test-target-2-python - Development Plan

> Bridge between strategic roadmap and auto-dev execution.
>
> Strategic Roadmap: N/A — this project IS the test target. The roadmap is "become a useful Python utility library for testing auto-dev workflows."
> Last Updated: 2026-02-06

## Roadmap → Version Mapping

| Version | Roadmap Reference | Focus | Prerequisites | Status |
|---------|-------------------|-------|---------------|--------|
| v001 | Foundation | Project scaffolding, quality gates, CI | None | **completed** |
| v002 | Utility Library | String, math, and collection utils | v001 | planned |
| v003 | Validation & Errors | Exception hierarchy, validators, property tests | v002 | planned |

## Investigation Dependencies

No investigation dependencies exist. This is a straightforward Python utility library — all technologies (pytest, ruff, mypy, GitHub Actions, Hypothesis) are well-understood and require no spikes or explorations before implementation.

| ID | Question | Informs | Status | Results |
|----|----------|---------|--------|---------|
| — | None required | — | — | — |

## Version Details

### v001 - Foundation (2 themes)

**Theme 1: Project Scaffolding**
- pyproject.toml with uv as package manager
- `src/test_target_2/` package with `__init__.py`
- Basic `hello.py` module with a `hello()` function
- Backlog: BL-001, BL-006

**Theme 2: Quality & CI**
- ruff configuration (linting + formatting)
- mypy configuration with strict mode
- pytest setup with basic passing test
- GitHub Actions CI workflow (lint, typecheck, test)
- Backlog: BL-002, BL-003, BL-004, BL-005

### v002 - Utility Library (2 themes)

**Theme 1: String & Math Utils**
- `string_utils.py` — slugify, truncate, camel_to_snake, snake_to_camel, title_case
- `math_utils.py` — clamp, lerp, round_to, is_close, percentage, safe_divide
- Full test coverage for both modules
- Backlog: BL-007, BL-008

**Theme 2: Collection Utils**
- `collection_utils.py` — chunk, flatten, unique_by, group_by, partition, compact
- Generic type annotations with TypeVar
- Full test coverage
- Backlog: BL-009

### v003 - Validation & Error Handling (2 themes)

**Theme 1: Error Types & Validators**
- `exceptions.py` — TestTarget2Error base, ValidationError, NotFoundError, ConfigError
- `validators.py` — validate_range, validate_non_empty, validate_type, validate_pattern, validate_length
- Tests for both modules
- Backlog: BL-010, BL-011

**Theme 2: Retrofit & Property Testing**
- Add input validation to existing string_utils, math_utils, collection_utils
- Add Hypothesis as dev dependency
- Property-based tests for key invariants across all utility modules
- Backlog: BL-012, BL-013

## Scoping Decisions

### v001 Boundary

**Included:** Project scaffolding, all quality gate tooling, CI, and a minimal hello function.
**Rationale:** Everything needed to have a working Python project with passing quality gates must land together. Without scaffolding, there's nothing for ruff/mypy/pytest to run against. Without CI, there's no way to validate the auto-dev PR workflow. These form one cohesive foundation unit.
**Deferred:** Actual utility functions deferred to v002 — v001 focuses purely on infrastructure.

### v002 Boundary

**Included:** String, math, and collection utility modules with full test coverage.
**Rationale:** These are independent utility modules that can be developed and tested in isolation. Grouping string+math together (Theme 1) keeps related numeric/text operations close, while collections (Theme 2) is a natural separate theme due to its generic type complexity. No validation logic yet — functions accept inputs as-is.
**Deferred:** Input validation and error handling deferred to v003 to keep v002 focused on core functionality.

### v003 Boundary

**Included:** Custom exceptions, validation functions, retrofitting validation into v002 utils, and property-based testing.
**Rationale:** Validation and error handling form a cross-cutting concern that builds on top of existing utilities. Property-based testing belongs here because it exercises the validation boundaries. Retrofit is grouped with validators because they're developed together — you need the validators module before you can use it in existing code.

## Completed Versions

### v001 - Foundation (completed 2026-02-06)
- 2 themes, 7 features, 25/25 acceptance criteria passed
- Project scaffolding with uv, src-layout package, typed hello() function
- Quality gates: ruff, mypy (strict), pytest
- GitHub Actions CI workflow

## Backlog Integration

| Tag | Purpose |
|-----|---------|
| `v001` | Foundation version work items |
| `v002` | Utility library work items |
| `v003` | Validation & error handling work items |
| `foundation` | Project setup and infrastructure |
| `utility` | Core utility function modules |
| `validation` | Validation and error handling |
| `testing` | Test infrastructure and property tests |

Query backlog: `list_backlog_items(project="auto-dev-test-target-2-python", tags=["v001"])`

## Change Log

| Date | Change | Rationale |
|------|--------|-----------|
| 2026-02-06 | Initial plan created | Project bootstrap — mapped 3 versions with 6 themes total covering foundation through validation |
| 2026-02-06 | v001 marked completed | Version closure — all themes/features completed successfully |
