# Codebase Patterns — v001

## Current State

This is a greenfield project. No Python source files, pyproject.toml, or CI workflows exist yet.

### Existing Structure

```
auto-dev-test-target-2-python/
├── AGENTS.md          # Development instructions and quality gate commands
├── CLAUDE.md          # Points to AGENTS.md
├── LICENSE
├── README.md
├── comms/             # auto-dev communication structure
└── docs/              # Documentation (empty of C4 docs)
```

Source: Glob searches for `**/*.py`, `**/pyproject.toml`, `**/.github/**/*` — all returned no results.

### Patterns from AGENTS.md

AGENTS.md (line 7-27) already defines the expected quality gate commands:

- `uv sync` — dependency installation
- `uv run ruff check src/` — linting
- `uv run ruff format src/` — formatting
- `uv run mypy src/` — type checking
- `uv run pytest` — testing

These commands establish the target interface. All v001 configuration must make these commands work.

### PR Workflow (AGENTS.md line 31-37)

The PR workflow uses `gh pr create --fill --base main` with CI checks via `gh pr checks --watch`. This means the GitHub Actions workflow (BL-005) must report status checks that `gh pr checks` can detect.

## Implications for v001

1. **No migration needed** — purely additive changes
2. **AGENTS.md is the contract** — quality gate commands are already defined
3. **src/ layout required** — commands reference `src/` paths
4. **Package name**: `test_target_2` (from AGENTS.md project description and backlog)
