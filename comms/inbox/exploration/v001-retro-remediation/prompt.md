Read AGENTS.md first and follow all instructions there.

## Objective
Execute all remediation actions from the Stage 1 proposals document.

## Input
Read: comms/outbox/versions/retrospective/v001/007-proposals/proposals.md

## Tasks
For each proposed action in the "Immediate Fixes" section:

### 1. Delete stale remote branches
Run the following git commands to delete the 7 stale v001 feature branches:
- `git push origin --delete v001/01-01-project-scaffolding/001-001-pyproject-init`
- `git push origin --delete v001/01-01-project-scaffolding/002-002-package-structure`
- `git push origin --delete v001/01-01-project-scaffolding/003-003-hello-module`
- `git push origin --delete v001/02-02-quality-and-ci/001-001-ruff-config`
- `git push origin --delete v001/02-02-quality-and-ci/002-002-mypy-config`
- `git push origin --delete v001/02-02-quality-and-ci/003-003-pytest-setup`
- `git push origin --delete v001/02-02-quality-and-ci/004-004-github-actions`

### 2. Commit retrospective artifacts
Stage and commit all uncommitted retrospective/exploration/state files:
- `git add comms/ docs/CHANGELOG.md docs/auto-dev/`
- `git commit -m "docs(v001): retrospective artifacts and execution state"`

### 3. Push to remote
- `git push origin main`

## Output Requirements
Save outputs to comms/outbox/exploration/v001-retro-remediation/:

### README.md (required)
First paragraph: Summary of remediation actions executed.
Then: Table of each action, its status, and any notes.

When complete, commit all changes with message: "docs(v001): retrospective remediation actions"