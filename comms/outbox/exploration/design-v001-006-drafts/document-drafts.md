# Document Drafts - v001

## VERSION_DESIGN.md

# Version Design: v001

## Description

v001 "Foundation" establishes the complete project infrastructure for auto-dev-test-target-2-python. It delivers a working Python project with uv-based packaging, src-layout package structure, quality gates (ruff, mypy, pytest), and GitHub Actions CI — providing the base upon which utility modules (v002) and validation (v003) will be built.

## Design Artifacts

Full design analysis available at: `comms/outbox/versions/design/v001/`

- `001-environment/` — Environment verification and version context
- `002-backlog/` — Backlog analysis (BL-001 through BL-006)
- `003-research/` — External research, evidence log
- `004-logical-design/` — Theme/feature structure, test strategy
- `005-critical-thinking/` — Refined design, risk assessment

## Constraints and Assumptions

- **Package Manager:** uv with `uv_build` backend
- **Python Target:** >= 3.11 (consistent across ruff, mypy, requires-python)
- **No investigation dependencies:** All technologies are well-understood
- **Destructive test target:** Project is disposable; used for auto-dev-mcp integration testing
- **Single config file:** All tool configuration in pyproject.toml (no separate ruff.toml or mypy.ini)

## Key Design Decisions

- **BL-001/BL-006 overlap resolved:** BL-001 maps to structural features (pyproject-init, package-structure); BL-006 maps to functional implementation (hello-module)
- **Dev dependencies via `[dependency-groups]`:** Modern uv pattern replacing deprecated `tool.uv.dev-dependencies`
- **`uv_build>=0.9.21,<0.10.0`:** Confirmed current range from research
- **E501 ignored in ruff:** Line length enforced by formatter, not linter
- **pytest importlib mode:** Recommended for src layout to avoid sys.path hacks
- **CI on ubuntu-latest only:** Development is Windows but CI runs Linux

## Theme Overview

| Theme | Name | Features | Backlog Items |
|-------|------|----------|---------------|
| 01 | project-scaffolding | 3 | BL-001, BL-006 |
| 02 | quality-and-ci | 4 | BL-002, BL-003, BL-004, BL-005 |

---

## THEME_INDEX.md

# Theme Index: v001

## 01-project-scaffolding

**Goal:** Establish the complete Python project structure with uv build backend, src-layout package, and minimal hello module.

**Features:**

- 001-pyproject-init: Initialize pyproject.toml with uv build backend and project metadata
- 002-package-structure: Create src/test_target_2/ package with __init__.py
- 003-hello-module: Create hello.py with typed hello() function

## 02-quality-and-ci

**Goal:** Configure quality gates (ruff, mypy, pytest) and GitHub Actions CI workflow.

**Features:**

- 001-ruff-config: Configure ruff linting and formatting rules
- 002-mypy-config: Configure mypy with strict mode
- 003-pytest-setup: Set up pytest with basic passing test for hello module
- 004-github-actions: Create GitHub Actions CI workflow with all quality gates

---

## Theme 01: 01-project-scaffolding

### THEME_DESIGN.md

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

### Feature 001-pyproject-init

#### requirements.md

# Requirements: 001-pyproject-init

## Goal

Initialize pyproject.toml with uv build backend, project metadata, and dev dependencies.

## Background

This is the first feature of v001, creating the project manifest from which all other features build. The project uses uv as its package manager with the native `uv_build` backend for src-layout projects.

- **Backlog:** BL-001 (Python project scaffolding)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: Project metadata**
- pyproject.toml contains `[project]` section with:
  - `name = "test-target-2"`
  - `version = "0.1.0"`
  - `description = "A minimal Python utility library for auto-dev-mcp integration testing"`
  - `requires-python = ">=3.11"`
- Acceptance: Fields present and correctly formatted

**FR-002: Build system**
- pyproject.toml contains `[build-system]` section with:
  - `requires = ["uv_build>=0.9.21,<0.10.0"]`
  - `build-backend = "uv_build"`
- Acceptance: `uv sync` completes without error

**FR-003: Dev dependencies**
- pyproject.toml contains `[dependency-groups]` section with:
  - `dev = ["pytest", "ruff", "mypy"]`
- Acceptance: `uv sync` installs all dev dependencies

**FR-004: Lock file generation**
- `uv.lock` is auto-generated by `uv sync`
- Acceptance: `uv.lock` exists after `uv sync`

## Non-Functional Requirements

**NFR-001: Configuration standard**
- All tool configuration will be added to pyproject.toml in later features (no separate config files)

## Out of Scope

- Tool configuration sections (ruff, mypy, pytest) — added in Theme 02
- Source code files — added in features 002 and 003
- `.python-version` file — uv manages Python version from requires-python

## Test Requirements

- Verification only: `uv sync` completes successfully
- No automated test file for this feature

## Reference

Design artifacts: `comms/outbox/versions/design/v001/003-research/evidence-log.md` (build system values)

#### implementation-plan.md

# Implementation Plan: 001-pyproject-init

## Overview

Create the project's pyproject.toml with uv build backend, metadata, and dev dependencies. Run `uv sync` to generate the lock file.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Create | Project manifest with metadata, build system, dev deps |

## Files Generated (by tooling)

| File | Action | Description |
|------|--------|-------------|
| `uv.lock` | Auto-generated | Lock file created by `uv sync` |

## Implementation Steps

### Stage 1: Create pyproject.toml

Create `pyproject.toml` with the following content:

```toml
[project]
name = "test-target-2"
version = "0.1.0"
description = "A minimal Python utility library for auto-dev-mcp integration testing"
requires-python = ">=3.11"

[build-system]
requires = ["uv_build>=0.9.21,<0.10.0"]
build-backend = "uv_build"

[dependency-groups]
dev = ["pytest", "ruff", "mypy"]
```

### Stage 2: Generate lock file

```bash
uv sync
```

**Verify:**
```bash
# Lock file exists
ls uv.lock

# No errors from sync
uv sync 2>&1 | tail -1
```

## Quality Gates

```bash
uv sync  # Must complete without error
```

## Commit Message

```
feat(scaffold): initialize pyproject.toml with uv build backend

- Add project metadata (name, version, requires-python >= 3.11)
- Configure uv_build as build backend
- Add dev dependencies (pytest, ruff, mypy)
- Generate uv.lock
```

### Feature 002-package-structure

#### requirements.md

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

#### implementation-plan.md

# Implementation Plan: 002-package-structure

## Overview

Create the src-layout package directory with __init__.py.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `src/test_target_2/__init__.py` | Create | Package init with __version__ |

## Implementation Steps

### Stage 1: Create package directory and __init__.py

Create `src/test_target_2/__init__.py`:

```python
"""test_target_2 — A minimal Python utility library."""

__version__ = "0.1.0"
```

### Stage 2: Verify

```bash
# Package is importable
uv run python -c "from test_target_2 import __version__; print(__version__)"
```

Expected output: `0.1.0`

## Quality Gates

```bash
uv run python -c "from test_target_2 import __version__; assert __version__ == '0.1.0'"
```

## Commit Message

```
feat(scaffold): create src/test_target_2 package with __init__.py

- Create src-layout package directory
- Add __init__.py with __version__ = "0.1.0"
```

### Feature 003-hello-module

#### requirements.md

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

#### implementation-plan.md

# Implementation Plan: 003-hello-module

## Overview

Create the hello module with a typed hello() function.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `src/test_target_2/hello.py` | Create | Hello module with typed hello() function |

## Implementation Steps

### Stage 1: Create hello.py

Create `src/test_target_2/hello.py`:

```python
"""Hello module — minimal utility for quality gate validation."""


def hello(name: str = "World") -> str:
    """Return a greeting string.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
```

### Stage 2: Verify

```bash
# Function works
uv run python -c "from test_target_2.hello import hello; print(hello()); print(hello('Alice'))"
```

Expected output:
```
Hello, World!
Hello, Alice!
```

## Quality Gates

```bash
uv run python -c "from test_target_2.hello import hello; assert hello() == 'Hello, World!'; assert hello('Alice') == 'Hello, Alice!'"
```

## Commit Message

```
feat(scaffold): add hello module with typed hello() function

- Create src/test_target_2/hello.py
- Implement hello(name: str = "World") -> str
- Full type annotations for mypy strict compliance
```

---

## Theme 02: 02-quality-and-ci

### THEME_DESIGN.md

# Theme Design: 02-quality-and-ci

## Goal

Configure all quality gate tooling (ruff, mypy, pytest) and a GitHub Actions CI workflow so that every push and PR is automatically validated. This theme transforms the raw scaffolding from Theme 01 into a fully gated project with automated enforcement.

## Design Artifacts

Full design analysis: `comms/outbox/versions/design/v001/`

Key references:
- Logical design: `004-logical-design/logical-design.md` (Theme 02 section)
- Refined design: `005-critical-thinking/refined-logical-design.md`
- Research: `003-research/external-research.md` (ruff, mypy, pytest, GitHub Actions)
- Evidence: `003-research/evidence-log.md` (concrete configuration values)
- Test strategy: `004-logical-design/test-strategy.md`

## Backlog Items

| Item | Scope |
|------|-------|
| BL-002 | pytest setup with basic passing test |
| BL-003 | ruff configuration (linting + formatting) |
| BL-004 | mypy configuration with strict mode |
| BL-005 | GitHub Actions CI workflow |

## Features

| Feature | Goal | Backlog | Dependencies |
|---------|------|---------|--------------|
| 001-ruff-config | Configure ruff lint and format rules | BL-003 | Theme 01 complete |
| 002-mypy-config | Configure mypy strict mode | BL-004 | Theme 01 complete |
| 003-pytest-setup | Set up pytest with passing test | BL-002 | Theme 01 complete |
| 004-github-actions | Create CI workflow with all gates | BL-005 | 001, 002, 003 |

## Execution Order

Features 001, 002, 003 can execute in any order (all depend only on Theme 01). Feature 004 must execute last (depends on all three tools being configured).

```
001-ruff-config   ─┐
002-mypy-config   ─┼─> 004-github-actions
003-pytest-setup  ─┘
```

## Risks

- R-001 (CI first-run failure): Mitigated by AGENTS.md 3-iteration CI fix limit
- R-003 (mypy strict): Negligible — trivial code with primitive types only

### Feature 001-ruff-config

#### requirements.md

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

#### implementation-plan.md

# Implementation Plan: 001-ruff-config

## Overview

Add ruff linting and formatting configuration to pyproject.toml.

## Files to Modify

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Modify | Add [tool.ruff], [tool.ruff.lint], [tool.ruff.format] sections |

## Implementation Steps

### Stage 1: Add ruff configuration to pyproject.toml

Append to `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```

### Stage 2: Run ruff and fix any issues

```bash
# Check linting
uv run ruff check src/

# Check formatting
uv run ruff format --check src/
```

If formatting issues exist:
```bash
uv run ruff format src/
```

### Stage 3: Verify

```bash
uv run ruff check src/
uv run ruff format --check src/
```

Both must pass with exit code 0.

## Quality Gates

```bash
uv run ruff check src/
uv run ruff format --check src/
```

## Commit Message

```
feat(quality): configure ruff linting and formatting

- Add [tool.ruff] with line-length 88, target Python 3.11
- Select rules: E, F, I, UP, B, SIM (ignore E501)
- Configure format: double quotes, space indent, auto line-ending
```

### Feature 002-mypy-config

#### requirements.md

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

#### implementation-plan.md

# Implementation Plan: 002-mypy-config

## Overview

Add mypy strict configuration to pyproject.toml.

## Files to Modify

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Modify | Add [tool.mypy] section |

## Implementation Steps

### Stage 1: Add mypy configuration to pyproject.toml

Append to `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.11"
strict = true
```

### Stage 2: Verify

```bash
uv run mypy src/
```

Must pass with exit code 0 and no errors.

## Quality Gates

```bash
uv run mypy src/
```

## Commit Message

```
feat(quality): configure mypy with strict mode

- Add [tool.mypy] with python_version 3.11 and strict = true
- Enables all 14 strict type checking flags
```

### Feature 003-pytest-setup

#### requirements.md

# Requirements: 003-pytest-setup

## Goal

Set up pytest with importlib import mode, create the tests/ directory, and write a basic passing test for the hello() function.

## Background

pytest is the project's test framework. It needs importlib import mode to work correctly with the src-layout package structure. This feature creates the first test file, validating the full test pipeline end-to-end.

- **Backlog:** BL-002 (pytest setup with basic passing test)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: pytest configuration**
- `[tool.pytest.ini_options]` section in pyproject.toml with:
  - `testpaths = ["tests"]`
  - `addopts = "--import-mode=importlib -ra -q"`
- Acceptance: Configuration is present and valid

**FR-002: Test directory structure**
- `tests/conftest.py` exists (empty or minimal)
- Acceptance: File is present

**FR-003: Test file**
- `tests/test_hello.py` exists with passing tests for hello():
  1. `hello()` returns `"Hello, World!"`
  2. `hello("Alice")` returns `"Hello, Alice!"`
  3. Return type is `str`
  4. Function is importable from `test_target_2.hello`
- Acceptance: `uv run pytest` passes with all tests green

## Non-Functional Requirements

**NFR-001: Dev dependency**
- pytest is listed in `[dependency-groups]` dev (already added in 001-pyproject-init)

**NFR-002: Import mode**
- importlib mode avoids sys.path manipulation; recommended for src layout

## Out of Scope

- Coverage configuration — no backlog item for v001
- Fixtures beyond conftest.py placeholder
- Integration tests

## Test Requirements

- `uv run pytest` passes with green output
- All 4 test cases pass
- importlib mode works correctly with src layout

## Reference

Design artifacts: `comms/outbox/versions/design/v001/003-research/evidence-log.md` (pytest settings)

#### implementation-plan.md

# Implementation Plan: 003-pytest-setup

## Overview

Configure pytest in pyproject.toml, create tests/ directory with conftest.py, and write tests for the hello() function.

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Modify | Add [tool.pytest.ini_options] section |
| `tests/conftest.py` | Create | Empty conftest placeholder |
| `tests/test_hello.py` | Create | Unit tests for hello() function |

## Implementation Steps

### Stage 1: Add pytest configuration to pyproject.toml

Append to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--import-mode=importlib -ra -q"
```

### Stage 2: Create test directory and conftest

Create `tests/conftest.py`:

```python
"""Shared test configuration and fixtures."""
```

### Stage 3: Create test file

Create `tests/test_hello.py`:

```python
"""Tests for the hello module."""

from test_target_2.hello import hello


def test_hello_default() -> None:
    """hello() with default argument returns greeting with World."""
    assert hello() == "Hello, World!"


def test_hello_custom_name() -> None:
    """hello() with custom name returns personalized greeting."""
    assert hello("Alice") == "Hello, Alice!"


def test_hello_returns_string() -> None:
    """hello() returns a string."""
    result = hello()
    assert isinstance(result, str)


def test_hello_importable() -> None:
    """hello is importable from test_target_2.hello."""
    from test_target_2.hello import hello as h

    assert callable(h)
```

### Stage 4: Verify

```bash
uv run pytest
```

Expected: All 4 tests pass.

## Quality Gates

```bash
uv run pytest
```

## Commit Message

```
feat(quality): set up pytest with hello module tests

- Configure pytest with importlib mode and testpaths
- Create tests/conftest.py
- Add 4 passing tests for hello() function
```

### Feature 004-github-actions

#### requirements.md

# Requirements: 004-github-actions

## Goal

Create a GitHub Actions CI workflow that runs all quality gates (ruff, mypy, pytest) on push and pull request to main.

## Background

This feature creates the automated enforcement layer. Every push and PR to main triggers the full quality gate suite, ensuring no regressions reach the main branch. The workflow uses uv for environment setup and tool execution.

- **Backlog:** BL-005 (GitHub Actions CI workflow)
- **Design artifacts:** `comms/outbox/versions/design/v001/`

## Functional Requirements

**FR-001: Workflow file**
- `.github/workflows/ci.yml` exists
- Acceptance: File is present and valid YAML

**FR-002: Triggers**
- Workflow triggers on:
  - `push` to `main` branch
  - `pull_request` to `main` branch
- Acceptance: Trigger configuration is correct

**FR-003: Environment setup**
- Workflow uses `astral-sh/setup-uv@v7` with `enable-cache: true`
- Workflow runs `uv sync --locked --dev` to install dependencies
- Acceptance: Setup steps are present and correctly configured

**FR-004: Quality gate steps**
- Workflow runs in order:
  1. `uv run ruff check src/`
  2. `uv run ruff format --check src/`
  3. `uv run mypy src/`
  4. `uv run pytest`
- Acceptance: All four steps are present as separate `run` steps

## Non-Functional Requirements

**NFR-001: Runner**
- Uses `ubuntu-latest` runner

**NFR-002: Caching**
- uv cache is enabled for faster subsequent runs

## Out of Scope

- Matrix builds (multiple Python versions)
- Deployment steps
- Branch protection rules
- Code coverage reporting

## Test Requirements

- Integration verification: CI workflow triggers and passes on PR
- Verified via `gh pr checks --watch` during PR workflow
- No test file — CI is verified by successful workflow run

## Reference

Design artifacts: `comms/outbox/versions/design/v001/003-research/external-research.md` (GitHub Actions workflow template)

#### implementation-plan.md

# Implementation Plan: 004-github-actions

## Overview

Create the GitHub Actions CI workflow file that runs all quality gates.

## Files to Create

| File | Action | Description |
|------|--------|-------------|
| `.github/workflows/ci.yml` | Create | CI workflow with all quality gates |

## Implementation Steps

### Stage 1: Create workflow directory and file

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v7
        with:
          enable-cache: true
      - run: uv sync --locked --dev
      - run: uv run ruff check src/
      - run: uv run ruff format --check src/
      - run: uv run mypy src/
      - run: uv run pytest
```

### Stage 2: Verify locally

```bash
# Validate YAML syntax (basic check)
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))" 2>/dev/null || echo "Note: yaml module not available, will verify via CI"
```

### Stage 3: Verify via PR

The CI workflow is ultimately verified by creating a PR and watching checks:

```bash
gh pr create --fill --base main
gh pr checks --watch
```

If CI fails, follow AGENTS.md workflow: `gh run view --log-failed`, fix, push (max 3 iterations).

## Quality Gates

CI verification happens during the PR workflow for Theme 02. All four quality gate steps must pass:
1. `uv run ruff check src/`
2. `uv run ruff format --check src/`
3. `uv run mypy src/`
4. `uv run pytest`

## Commit Message

```
feat(ci): add GitHub Actions CI workflow

- Trigger on push and PR to main
- Use astral-sh/setup-uv@v7 with caching
- Run ruff check, ruff format --check, mypy, and pytest
```
