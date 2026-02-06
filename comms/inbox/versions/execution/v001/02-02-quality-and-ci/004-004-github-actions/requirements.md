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