Read AGENTS.md first and follow all instructions there.

## Objective

Verify the environment is ready for retrospective execution: MCP server healthy, git clean, PRs merged, version execution complete.

## Context

This is the first step in the post-version retrospective for `auto-dev-test-target-2-python` version `v001`. All outputs go to the centralized retrospective deliverables store.

## Tasks

### 1. Health Check

Run `health_check()` and verify:
- MCP server is running (`success: true`)
- No critical errors reported

Document the health check result.

### 2. Git Status

Run `git_read(project="auto-dev-test-target-2-python", operation="status")` and verify:
- Working tree state
- On `main` branch
- Up to date with remote

If working tree is dirty, document all uncommitted files.

### 3. PR Status

Run `git_read(project="auto-dev-test-target-2-python", operation="prs", state="open")` and verify:
- No open PRs related to `v001` remain
- If open PRs exist: document them as blockers

### 4. Version Execution Status

Run `get_version_status(project="auto-dev-test-target-2-python", version_number=1)`.

Verify:
- Version status is "completed" or all themes show completed status
- All features within each theme have completion reports

Document the version state summary.

### 5. Branch Verification

Run `git_read(project="auto-dev-test-target-2-python", operation="branches")` and verify:
- No stale feature branches from `v001` remain
- Document any branches that should have been deleted

## Output Requirements

Save outputs to BOTH locations:
1. `comms/outbox/versions/retrospective/v001/001-environment/`
2. `comms/outbox/exploration/v001-retro-001-environment/`

### README.md (required) — save in BOTH locations

First paragraph: Environment status summary (ready/blocked) with key findings.

Then:
- **Health Check**: Pass/fail with details
- **Git Status**: Branch, working tree state, remote sync
- **Open PRs**: List or "none"
- **Version Status**: Execution state summary
- **Stale Branches**: List or "none"
- **Blockers**: Any issues preventing retrospective continuation

### environment-report.md — save in BOTH locations

Detailed results from all checks, including raw outputs.

When complete, commit all changes with message: "docs(v001): retrospective task 001 - environment verification"