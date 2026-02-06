# Task 003: Research & Investigation — v001 Foundation

Research covered all 6 backlog items (BL-001 through BL-006) for v001 Foundation. Key findings: uv uses `[dependency-groups]` for dev deps (not the deprecated `tool.uv.dev-dependencies`), ruff configuration goes under `[tool.ruff]` with `[tool.ruff.lint]` for rule selection, mypy strict mode enables 14 flags via a single `strict = true`, pytest supports `[tool.pytest.ini_options]` in pyproject.toml, and GitHub Actions should use `astral-sh/setup-uv@v7` with `uv run` for all tool execution. No blockers or unresolved technical questions remain.

## Research Questions

1. **BL-001**: What is the correct pyproject.toml format for uv with src layout?
2. **BL-001**: What build backend should be used with uv?
3. **BL-002**: How should pytest be configured in pyproject.toml?
4. **BL-002**: What import mode should be used with src layout?
5. **BL-003**: What ruff rule sets and configuration format for Python 3.11+?
6. **BL-004**: What does mypy strict mode enable and how to configure it?
7. **BL-005**: What GitHub Actions workflow structure works with uv?
8. **BL-006**: How should hello() be typed for mypy strict compliance?

## Findings Summary

| Area | Key Finding | Source |
|------|-------------|--------|
| uv pyproject.toml | Use `[dependency-groups]` dev table, `uv_build` backend | DeepWiki: astral-sh/uv |
| ruff config | `[tool.ruff.lint]` select with E, F, I, UP, B, SIM; ignore E501 | DeepWiki: astral-sh/ruff |
| mypy strict | `strict = true` enables 14 flags; set `python_version = "3.11"` | DeepWiki: python/mypy |
| pytest config | `[tool.pytest.ini_options]` with testpaths and importlib mode | DeepWiki: pytest-dev/pytest |
| GitHub Actions | `astral-sh/setup-uv@v7` with `uv sync` then `uv run` | DeepWiki: astral-sh/uv |

## Unresolved Questions

None. All technologies are well-documented and the configuration patterns are clear. BL-001 and BL-006 overlap (both specify hello.py) — recommendation is to combine them in Theme 1.

## Recommendations

1. **Single pyproject.toml**: All tool configs (ruff, mypy, pytest) in pyproject.toml — no separate config files
2. **uv_build backend**: Use `uv_build` as the build backend for src layout
3. **Combine BL-001 + BL-006**: Both create hello.py; implement together in Theme 1
4. **Python 3.11+ target**: Consistent across ruff, mypy, and requires-python
5. **importlib import mode**: Use `--import-mode=importlib` for pytest with src layout
6. **uv run for CI**: Use `uv run` (not `uvx`) for project tools to ensure correct environment
