# Learnings Summary — v001

## Search Results

- **Query:** tags: ["design", "architecture"] — 0 results
- **Full listing:** 0 learnings in repository

## Analysis

No documented learnings exist yet. This is expected for a new project at its first version.

## Applicable Guidance

Since no project-specific learnings are available, the following general best practices apply to v001's foundation work:

1. **pyproject.toml is the standard** — PEP 621 metadata in pyproject.toml is the modern Python convention; avoid setup.py/setup.cfg
2. **src layout prevents import confusion** — the src/ layout ensures tests import the installed package, not local source
3. **Strict mypy from day one** — enabling strict mode early is easier than retrofitting type annotations later
4. **ruff replaces multiple tools** — ruff handles both linting (replacing flake8, isort, pyupgrade) and formatting (replacing black)
5. **uv is fast and deterministic** — using uv for dependency management provides fast, reproducible builds

## Post-v001 Recommendation

After v001 completion, extract learnings about:
- uv + pyproject.toml configuration patterns that worked
- GitHub Actions CI setup decisions
- Any issues encountered with strict mypy on a new codebase
