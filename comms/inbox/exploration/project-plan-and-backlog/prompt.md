Set up auto-dev-test-target-2-python as a fully planned Python test target project for testing auto-dev-mcp tools and workflows.

## Context

This is a bare Python repo (README, LICENSE, .gitignore, AGENTS.md, docs/auto-dev/ structure). It needs to become a meaningful Python utility library that serves as a destructive test target — a safe place to run auto-dev version executions, test quality gates (ruff, mypy, pytest), and validate the full design → execute → PR → merge pipeline with Python tooling.

The existing TypeScript test target (auto-dev-test-target-1) has 4 versions that progressively built it from empty to a utility library with string utils, number utils, array utils, validation, and custom errors. This Python target should follow a similar trajectory but be idiomatic Python (dataclasses, type hints, pytest, src layout, pyproject.toml).

## Tasks

### Task 1: Create Backlog Items

Use `add_backlog_item` MCP tool to create backlog items for all planned work across 3 versions. Tag items with the target version (e.g., `v001`, `v002`, `v003`).

Items should cover:

**v001 - Foundation:**
- Python project scaffolding (pyproject.toml, src layout, __init__.py)
- pytest setup with basic passing test
- ruff configuration (linting + formatting)
- mypy configuration with strict mode
- GitHub Actions CI workflow (lint, typecheck, test)
- A "hello world" utility function so quality gates have something to run against

**v002 - Utility Library:**
- String utilities module (slugify, truncate, case_convert, etc.) with tests
- Math/number utilities module (clamp, lerp, round_to, is_close, etc.) with tests
- Collection utilities module (chunk, flatten, unique_by, group_by, etc.) with tests

**v003 - Validation & Error Handling:**
- Custom exception hierarchy (ValidationError, NotFoundError, etc.)
- Input validation functions (validate_range, validate_non_empty, validate_type, etc.)
- Retrofit validation into existing v002 utility functions
- Property-based testing with Hypothesis for edge case coverage

Use appropriate priorities: `high` for v001 foundation items, `medium` for v002 utility items, `medium` for v003 validation items.

### Task 2: Create docs/auto-dev/PLAN.md

Read the template at `docs/auto-dev/PROCESS/generic/00-PROJECT-PLAN.md` and use it to create `docs/auto-dev/PLAN.md`.

The plan should:
- Reference that this project has no separate strategic roadmap (it IS the test target — the roadmap is "become a useful Python utility library for testing auto-dev")
- Map out v001, v002, v003 with theme breakdowns
- Include scoping decisions explaining why boundaries are drawn where they are
- Note that no investigation dependencies exist (this is straightforward library code)
- Leave the "Completed Versions" section empty
- Include a change log entry for initial plan creation

Version details for the plan:

**v001 - Foundation** (2 themes)
- Theme 1: Project Scaffolding (pyproject.toml with uv, src/test_target_2/ package, __init__.py, basic module with a hello function)
- Theme 2: Quality & CI (ruff.toml, mypy config in pyproject.toml, GitHub Actions workflow, first passing pytest)

**v002 - Utility Library** (2 themes)
- Theme 1: String & Math Utils (string_utils.py, math_utils.py with full test coverage)
- Theme 2: Collection Utils (collection_utils.py with full test coverage)

**v003 - Validation & Error Handling** (2 themes)
- Theme 1: Error Types & Validators (exceptions.py, validators.py)
- Theme 2: Retrofit & Property Testing (add validation to existing utils, add Hypothesis tests)

## Output Requirements

Create findings in comms/outbox/exploration/project-plan-and-backlog/:

### README.md (required)
First paragraph: Summary of what was created.
Then: List of backlog items created (IDs and titles) and confirmation that PLAN.md was written.

### backlog-summary.md
Full list of backlog items created with their IDs, titles, priorities, and tags.

## Guidelines
- Under 200 lines per document
- Use the 00-PROJECT-PLAN.md template faithfully for PLAN.md structure
- Create backlog items BEFORE writing PLAN.md so you can reference item IDs
- Commit all changes when complete

## When Complete
```bash
git add docs/auto-dev/PLAN.md comms/outbox/exploration/project-plan-and-backlog/
git commit -m "docs: initial project plan and backlog for v001-v003"
git push
```