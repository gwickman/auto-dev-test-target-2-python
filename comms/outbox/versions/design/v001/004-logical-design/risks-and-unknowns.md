# Risks and Unknowns — v001 Foundation

## Identified Risks

### R-001: GitHub Actions CI failure on first run

- **Severity:** Medium
- **Likelihood:** Medium
- **Impact:** Low (delays, not blockers)
- **Description:** The CI workflow may fail on the first push due to misconfigured action versions, missing permissions, or uv cache issues. First-time CI setups commonly require iteration.
- **Mitigation:** AGENTS.md allows up to 3 CI fix iterations. The `gh run view --log-failed` command provides specific failure details. Research has confirmed the exact action versions and configuration (`astral-sh/setup-uv@v7`, `enable-cache: true`).
- **Investigation:** None needed — the 3-iteration limit is sufficient.

### R-002: uv.lock conflicts on parallel branches

- **Severity:** Low
- **Likelihood:** Low
- **Impact:** Low
- **Description:** If multiple branches modify dependencies simultaneously, `uv.lock` merge conflicts could occur.
- **Mitigation:** Only one version branch is active at a time. v001 is the only branch being worked on. This risk is theoretical for v001.
- **Investigation:** None needed for v001.

### R-003: mypy strict false positives

- **Severity:** Low
- **Likelihood:** Low
- **Impact:** Low
- **Description:** mypy strict mode enables 14 flags. Some may produce false positives on certain coding patterns.
- **Mitigation:** All code in v001 is new and written from scratch, so type annotations can be correct from the start. The hello module is trivial (one function with a string parameter and string return). False positives are extremely unlikely.
- **Investigation:** None needed.

### R-004: BL-001 / BL-006 overlap confusion

- **Severity:** Low
- **Likelihood:** Low
- **Impact:** Low
- **Description:** Both BL-001 and BL-006 describe creating `hello.py` with a `hello()` function. If not carefully handled, this could result in duplicate work or incomplete acceptance criteria.
- **Mitigation:** The logical design explicitly maps BL-001 to structural features (001-pyproject-init, 002-package-structure) and BL-006 to the function implementation (003-hello-module). Both are marked complete after 003-hello-module passes. This was identified in Task 002 and Task 003.
- **Investigation:** None needed — already resolved in design.

### R-005: uv_build version pinning

- **Severity:** Low
- **Likelihood:** Low
- **Impact:** Medium (if wrong version is used)
- **Description:** Research specifies `uv_build>=0.9.21,<0.10.0`. If the available version has moved beyond this range, the build backend may fail.
- **Mitigation:** Use the version range from research as a starting point. If it fails, update to the current available version. `uv sync` will report clear errors if the build backend is unavailable.
- **Investigation:** Verify the latest `uv_build` version during Theme 01 Feature 001 implementation.

---

## Unknowns

### U-001: Exact `uv_build` version at implementation time

- **Status:** Low concern
- **Description:** The researched version range (`>=0.9.21,<0.10.0`) was current at research time. The actual available version may differ at implementation time.
- **Resolution:** Check `uv init` output or uv documentation during 001-pyproject-init implementation.

### U-002: `setup-uv` action caching behavior on Windows vs Linux

- **Status:** Not applicable for v001
- **Description:** CI runs on `ubuntu-latest`. The development environment is Windows. Cache behavior differences are irrelevant since CI runs only on Linux.
- **Resolution:** No action needed.

---

## Risk Summary

| ID | Risk | Severity | Likelihood | Needs Investigation? |
|----|------|----------|------------|---------------------|
| R-001 | CI first-run failure | Medium | Medium | No — 3-iteration limit covers it |
| R-002 | uv.lock merge conflicts | Low | Low | No — single active branch |
| R-003 | mypy strict false positives | Low | Low | No — trivial code |
| R-004 | BL-001/BL-006 overlap | Low | Low | No — resolved in design |
| R-005 | uv_build version pinning | Low | Low | Minor — verify at implementation |

**Overall assessment:** v001 carries no significant risks. All technologies are well-understood, the codebase is greenfield (no migration concerns), and the AGENTS.md workflow provides iteration allowances for CI issues. No items require dedicated investigation in Task 005.
