# Refined Logical Design — v001 Foundation

## Changes from Task 004

**No structural changes.** All investigations confirmed the Task 004 design is sound. The refinements below are confidence annotations and minor clarifications, not structural modifications.

---

## Theme 01: `01-project-scaffolding`

**Goal:** Establish the complete Python project structure with uv build backend, src-layout package, and minimal hello module.

**Backlog items:** BL-001, BL-006

| Feature | Goal | Backlog | Dependencies | Confidence |
|---------|------|---------|--------------|------------|
| `001-pyproject-init` | Initialize pyproject.toml with `uv_build>=0.9.21,<0.10.0`, metadata, dev deps | BL-001 | None | High |
| `002-package-structure` | Create `src/test_target_2/__init__.py` with `__version__` | BL-001 | 001 | High |
| `003-hello-module` | Create `hello.py` with typed `hello(name: str = "World") -> str` | BL-006 | 002 | High |

**Risk notes:**
- R-005 (uv_build version): Confirmed valid. Use `>=0.9.21,<0.10.0`.
- R-004 (BL-001/BL-006 overlap): Resolved. BL-001 structural, BL-006 functional.

---

## Theme 02: `02-quality-and-ci`

**Goal:** Configure quality gates and CI workflow for automated enforcement.

**Backlog items:** BL-002, BL-003, BL-004, BL-005

| Feature | Goal | Backlog | Dependencies | Confidence |
|---------|------|---------|--------------|------------|
| `001-ruff-config` | Configure ruff lint (E,F,I,UP,B,SIM) and format (line-length 88) | BL-003 | Theme 01 | High |
| `002-mypy-config` | Configure mypy `strict = true`, Python 3.11 target | BL-004 | Theme 01 | High |
| `003-pytest-setup` | Set up pytest with importlib mode, create tests for `hello()` | BL-002 | Theme 01 | High |
| `004-github-actions` | Create CI workflow with `setup-uv@v7`, all quality gates | BL-005 | 001, 002, 003 | High |

**Risk notes:**
- R-001 (CI first-run): Mitigated by 3-iteration limit. Config matches official docs.
- R-003 (mypy strict): Negligible risk — trivial code with primitive types.

---

## Execution Order (Unchanged)

```
Theme 01 (sequential):
  001-pyproject-init -> 002-package-structure -> 003-hello-module
                                                       |
Theme 02 (fan-out then converge):              +-----------------+
                                               | 001-ruff-config |
                                               | 002-mypy-config |-> 004-github-actions
                                               | 003-pytest-setup|
                                               +-----------------+
```

Theme 01 must complete before Theme 02 begins (source files needed for all quality gates).

Within Theme 02, features 001-003 can execute in any order. Feature 004 depends on all three.

---

## Backlog Coverage Matrix (Verified)

| Backlog | Theme | Feature(s) | Status |
|---------|-------|------------|--------|
| BL-001 | 01 | 001-pyproject-init, 002-package-structure | Mapped |
| BL-002 | 02 | 003-pytest-setup | Mapped |
| BL-003 | 02 | 001-ruff-config | Mapped |
| BL-004 | 02 | 002-mypy-config | Mapped |
| BL-005 | 02 | 004-github-actions | Mapped |
| BL-006 | 01 | 003-hello-module | Mapped |

All 6 backlog items mapped. None deferred. No circular dependencies.

---

## Research Sources Validated

| Decision | Status | Source |
|----------|--------|--------|
| `uv_build>=0.9.21,<0.10.0` | Confirmed current | DeepWiki: astral-sh/uv (Task 005) |
| `astral-sh/setup-uv@v7` | Confirmed current (v7.1.6) | DeepWiki: astral-sh/uv (Task 005) |
| `enable-cache: true` | Confirmed recommended | DeepWiki: astral-sh/uv (Task 005) |
| All other settings | Unchanged from Task 003/004 | No contradicting evidence found |

---

## Test Strategy (Unchanged)

No changes to test strategy from Task 004. The two test files (`tests/conftest.py`, `tests/test_hello.py`) remain sufficient. Quality gate verification order remains: ruff check, ruff format --check, mypy, pytest.

One clarification: the test for `hello()` should cover:
1. Default argument: `hello()` returns a greeting with "World"
2. Custom argument: `hello("Alice")` returns a greeting with "Alice"
3. Return type is `str`
4. Function is importable from `test_target_2.hello`
