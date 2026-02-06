# v001 Version Design

## Overview

**Version:** v001
**Title:** Foundation - Project scaffolding, quality gates, CI
**Themes:** 2

## Backlog Items

- [BL-001](docs/auto-dev/BACKLOG.md#bl-001)
- [BL-002](docs/auto-dev/BACKLOG.md#bl-002)
- [BL-003](docs/auto-dev/BACKLOG.md#bl-003)
- [BL-004](docs/auto-dev/BACKLOG.md#bl-004)
- [BL-005](docs/auto-dev/BACKLOG.md#bl-005)
- [BL-006](docs/auto-dev/BACKLOG.md#bl-006)

## Design Context

### Rationale

v001 Foundation establishes complete project infrastructure with uv-based packaging, src-layout, quality gates (ruff, mypy, pytest), and GitHub Actions CI

### Constraints

- Package manager: uv with uv_build backend
- Python target: >= 3.11
- All tool config in pyproject.toml
- Destructive test target project

### Assumptions

- All technologies well-understood, no spikes needed
- uv_build >= 0.9.21 is current
- CI runs on ubuntu-latest

### Deferred Items

- Utility functions deferred to v002
- Validation and error handling deferred to v003

## Themes

| # | Theme | Goal | Features |
|---|-------|------|----------|
| 1 | 01-01-project-scaffolding | Establish the complete Python project structure with uv build backend, src-layout package, and minimal hello module. | 3 |
| 2 | 02-02-quality-and-ci | Configure quality gates (ruff, mypy, pytest) and GitHub Actions CI workflow. | 4 |

## Success Criteria

Version is complete when:

- [ ] Theme 01 (01-project-scaffolding): Establish the complete Python project structure with uv build backend, src-layout package, and minimal hello module.
- [ ] Theme 02 (02-quality-and-ci): Configure quality gates (ruff, mypy, pytest) and GitHub Actions CI workflow.
