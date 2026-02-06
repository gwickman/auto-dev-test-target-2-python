# Risk Assessment — v001 Foundation

## Risk Triage Summary

| ID | Risk | Category | Resolution |
|----|------|----------|------------|
| R-001 | CI first-run failure | Accept with mitigation | 3-iteration workflow handles it |
| R-002 | uv.lock merge conflicts | Accept with mitigation | Single branch eliminates risk |
| R-003 | mypy strict false positives | Accept with mitigation | Trivial code, new codebase |
| R-004 | BL-001/BL-006 overlap | Resolved in design | Explicit mapping in logical design |
| R-005 | uv_build version pinning | Investigated | Version range confirmed valid |
| U-001 | Exact uv_build version | Investigated | Range `>=0.9.21,<0.10.0` confirmed |
| U-002 | setup-uv caching on Windows | Not applicable | CI runs on Linux only |

---

## Detailed Assessments

### R-001: GitHub Actions CI failure on first run

- **Original severity:** Medium
- **Category:** Accept with mitigation
- **Investigation:** DeepWiki confirms `astral-sh/setup-uv@v7` (latest v7.1.6) is the current recommended action. The workflow template from Task 003 research matches official documentation exactly. No version drift detected.
- **Finding:** The researched workflow configuration (`setup-uv@v7`, `enable-cache: true`, `uv sync --locked --dev`) matches current official recommendations. Risk of misconfiguration is lower than initially assessed.
- **Resolution:** Accept. AGENTS.md 3-iteration limit provides sufficient safety net. Configuration is research-validated.
- **Affected themes:** Theme 02 (004-github-actions)

### R-002: uv.lock merge conflicts on parallel branches

- **Original severity:** Low
- **Category:** Accept with mitigation
- **Investigation:** Not needed — structural mitigation is sufficient.
- **Finding:** v001 is the only version being developed. No parallel branches will modify dependencies.
- **Resolution:** Accept. Risk is theoretical for v001. No design change needed.
- **Affected themes:** None (cross-cutting concern)

### R-003: mypy strict false positives

- **Original severity:** Low
- **Category:** Accept with mitigation
- **Investigation:** The `hello()` function signature is `def hello(name: str = "World") -> str`. This uses only basic types (`str`). mypy strict mode's 14 flags target complex patterns (generics, decorators, subclassing Any). None apply to this trivial function.
- **Finding:** Zero false positive risk for v001's code surface. All 14 strict flags are irrelevant to a single function using primitive types.
- **Resolution:** Accept. Downgraded from Low to Negligible severity.
- **Affected themes:** Theme 02 (002-mypy-config)

### R-004: BL-001 / BL-006 overlap confusion

- **Original severity:** Low
- **Category:** Resolved in design
- **Investigation:** Task 004 logical design explicitly addresses this: BL-001 maps to structural features (001-pyproject-init, 002-package-structure), BL-006 maps to function implementation (003-hello-module). Both marked complete after 003-hello-module passes.
- **Finding:** Design already resolves this cleanly. No further action needed.
- **Resolution:** Closed. No design change needed.
- **Affected themes:** Theme 01

### R-005: uv_build version pinning

- **Original severity:** Low (Medium impact)
- **Category:** Investigated
- **Investigation:** DeepWiki query on astral-sh/uv confirms `uv_build>=0.9.21,<0.10.0` is the current recommended range. The `uv init --package` command generates this range dynamically based on the installed uv version. The upper bound `<0.10.0` provides protection against breaking changes.
- **Finding:** Version range is confirmed valid as of current documentation. The range is intentionally broad enough (`>=0.9.21`) to accommodate minor updates while the upper bound (`<0.10.0`) prevents breaking changes.
- **Resolution:** Use `>=0.9.21,<0.10.0` as specified. If it fails at implementation time, `uv sync` will report a clear error and the implementer can update the range.
- **Affected themes:** Theme 01 (001-pyproject-init)

### U-001: Exact uv_build version at implementation time

- **Original status:** Low concern
- **Category:** Investigated
- **Investigation:** DeepWiki confirms the version range is dynamically calculated by `uv init`. The `>=0.9.21,<0.10.0` range from Task 003 research remains current.
- **Finding:** Resolved. The version range is valid. Even if a newer minor version exists (e.g., 0.9.25), it falls within the specified range.
- **Resolution:** Closed. No design change needed.

### U-002: setup-uv action caching on Windows vs Linux

- **Original status:** Not applicable
- **Category:** Not applicable
- **Investigation:** None needed. CI runs exclusively on `ubuntu-latest`.
- **Finding:** Confirmed not applicable. Development environment is Windows but CI is Linux-only.
- **Resolution:** Closed. No action needed.
