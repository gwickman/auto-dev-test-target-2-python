# Evidence Log — Concrete Values for v001

## Python Version Target

| Setting | Value | Rationale |
|---------|-------|-----------|
| `requires-python` | `">=3.11"` | Specified in backlog (BL-001, BL-003, BL-004, BL-005) |
| `ruff target-version` | `"py311"` | Matches requires-python |
| `mypy python_version` | `"3.11"` | Matches requires-python |

## Build System

| Setting | Value | Source |
|---------|-------|--------|
| Build backend | `uv_build` | DeepWiki: astral-sh/uv — native backend for src layout |
| Build requires | `["uv_build>=0.9.21,<0.10.0"]` | DeepWiki: astral-sh/uv |

## ruff Rule Sets

| Rule | Name | Rationale |
|------|------|-----------|
| E | pycodestyle errors | Standard Python style errors |
| F | Pyflakes | Undefined names, unused imports |
| I | isort | Import sorting |
| UP | pyupgrade | Modernize syntax for target Python version |
| B | flake8-bugbear | Common bug patterns |
| SIM | flake8-simplify | Code simplification suggestions |

Source: BL-003 description specifies these exact rule sets. DeepWiki confirms they are standard selections.

### Ignored Rules

| Rule | Reason | Source |
|------|--------|--------|
| E501 | Line length handled by ruff formatter | DeepWiki: astral-sh/ruff |

## ruff Formatting

| Setting | Value | Source |
|---------|-------|--------|
| `line-length` | 88 | BL-003 description; matches Black convention |
| `quote-style` | `"double"` | DeepWiki: astral-sh/ruff default |
| `indent-style` | `"space"` | DeepWiki: astral-sh/ruff default |
| `line-ending` | `"auto"` | Cross-platform compatibility (Windows host) |

## mypy Strict Mode Flags

All enabled by `strict = true` (source: DeepWiki python/mypy):

1. `warn_unused_configs = True`
2. `warn_redundant_casts = True`
3. `warn_unused_ignores = True`
4. `strict_equality = True`
5. `check_untyped_defs = True`
6. `disallow_subclassing_any = True`
7. `disallow_untyped_decorators = True`
8. `disallow_any_generics = True`
9. `disallow_untyped_calls = True`
10. `disallow_incomplete_defs = True`
11. `disallow_untyped_defs = True`
12. `no_implicit_reexport = True`
13. `warn_return_any = True`
14. `extra_checks = True`

## pytest Settings

| Setting | Value | Source |
|---------|-------|--------|
| `testpaths` | `["tests"]` | Standard convention; DeepWiki: pytest-dev/pytest |
| `addopts` | `"--import-mode=importlib -ra -q"` | Recommended for src layout; DeepWiki: pytest-dev/pytest |

## GitHub Actions

| Setting | Value | Source |
|---------|-------|--------|
| Action | `astral-sh/setup-uv@v7` | DeepWiki: astral-sh/uv |
| Runner | `ubuntu-latest` | Standard for Python projects |
| Cache | `enable-cache: true` | DeepWiki: astral-sh/uv recommendation |
| Sync | `uv sync --locked --dev` | Ensures lockfile integrity |
| Triggers | push + PR to main | BL-005 acceptance criteria |

## Dev Dependencies

| Package | Purpose | Source |
|---------|---------|--------|
| pytest | Test framework | BL-002 |
| ruff | Linting + formatting | BL-003 |
| mypy | Type checking | BL-004 |
