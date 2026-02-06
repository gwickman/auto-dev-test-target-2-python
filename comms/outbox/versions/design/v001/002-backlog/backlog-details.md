# Backlog Details — v001

## BL-001: Python project scaffolding (pyproject.toml, src layout, __init__.py)

- **Priority:** P1
- **Size:** M
- **Tags:** v001, foundation
- **Status:** Open

**Description:**

> Set up the Python project structure using modern standards: pyproject.toml with uv as the build tool, src/test_target_2/ package layout with __init__.py, and a basic hello.py module with a hello() function so quality gates have something to run against.

**Acceptance Criteria:**

1. pyproject.toml exists with project metadata and uv configuration
2. src/test_target_2/__init__.py exists with version info
3. src/test_target_2/hello.py exists with a hello() function
4. Package is installable via uv sync

**Notes:** None

**Complexity Assessment:** Low-medium. Standard Python project scaffolding using well-known conventions. The src layout pattern is straightforward. Main risk is ensuring pyproject.toml is correctly configured for uv.

---

## BL-002: pytest setup with basic passing test

- **Priority:** P1
- **Size:** M
- **Tags:** v001, foundation
- **Status:** Open

**Description:**

> Configure pytest as the test framework in pyproject.toml, create tests/ directory structure, and write a basic passing test for the hello() function to validate the test pipeline works end-to-end.

**Acceptance Criteria:**

1. pytest is listed as a dev dependency in pyproject.toml
2. tests/ directory exists with conftest.py
3. tests/test_hello.py exists with at least one passing test
4. uv run pytest passes with green output

**Notes:** None

**Complexity Assessment:** Low-medium. Depends on BL-001 being complete (needs the hello() function to test). Standard pytest configuration.

---

## BL-003: ruff configuration (linting + formatting)

- **Priority:** P1
- **Size:** M
- **Tags:** v001, foundation
- **Status:** Open

**Description:**

> Configure ruff for both linting and formatting. Set up ruff.toml or [tool.ruff] in pyproject.toml with sensible defaults: line length 88, Python 3.11+ target, enable standard rule sets (E, F, I, UP, B, SIM).

**Acceptance Criteria:**

1. ruff is listed as a dev dependency
2. ruff configuration exists with line-length, target-version, and rule selections
3. uv run ruff check src/ passes cleanly
4. uv run ruff format --check src/ passes cleanly

**Notes:** None

**Complexity Assessment:** Low. Configuration-only task. Specific rule sets and settings are already defined in the description. Depends on BL-001 for source files to lint.

---

## BL-004: mypy configuration with strict mode

- **Priority:** P1
- **Size:** M
- **Tags:** v001, foundation
- **Status:** Open

**Description:**

> Configure mypy for strict type checking in pyproject.toml. Enable strict mode, set Python 3.11+ target, and ensure the hello module passes strict type checking with proper type annotations.

**Acceptance Criteria:**

1. mypy is listed as a dev dependency
2. [tool.mypy] section exists in pyproject.toml with strict = true
3. uv run mypy src/ passes cleanly
4. All public functions have type annotations

**Notes:** None

**Complexity Assessment:** Low. Configuration task. Requires BL-001's hello.py to have proper type annotations. Strict mode is well-defined.

---

## BL-005: GitHub Actions CI workflow (lint, typecheck, test)

- **Priority:** P1
- **Size:** M
- **Tags:** v001, foundation
- **Status:** Open

**Description:**

> Create .github/workflows/ci.yml with a CI pipeline that runs on push and PR to main. Jobs: ruff check, ruff format --check, mypy src/, pytest. Use uv for dependency management and Python 3.11+.

**Acceptance Criteria:**

1. .github/workflows/ci.yml exists
2. Workflow triggers on push and pull_request to main
3. Workflow runs ruff check, ruff format --check, mypy, and pytest
4. Workflow uses uv for Python environment setup

**Notes:** None

**Complexity Assessment:** Medium. Requires knowledge of GitHub Actions YAML syntax and uv setup actions. Depends on BL-001, BL-002, BL-003, BL-004 all being complete so CI has tools to run.

---

## BL-006: Hello world utility function for quality gate validation

- **Priority:** P1
- **Size:** M
- **Tags:** v001, foundation
- **Status:** Open

**Description:**

> Create a simple hello() utility function in src/test_target_2/hello.py that returns a greeting string. This provides the minimal code needed for all quality gates (ruff, mypy, pytest) to have something meaningful to run against.

**Acceptance Criteria:**

1. hello() function exists with proper type annotations
2. Function is importable from test_target_2 package
3. All quality gates pass against this function

**Notes:** None

**Complexity Assessment:** Low. Trivial implementation. Overlaps significantly with BL-001 which also specifies creating hello.py with a hello() function. Design phase should clarify whether these are combined or BL-006 extends BL-001.
