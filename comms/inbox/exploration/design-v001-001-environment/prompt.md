You are executing Task 001: Environment Verification for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Verify the design environment is ready and gather essential context about the project and version scope.

## Tasks

### 1. Environment Health Check

Run `health_check()` and verify:
- MCP server is running (success: true)
- Claude Code is configured and available
- No critical errors reported

### 2. Project Configuration Check

Run `get_project_info(project="auto-dev-test-target-2-python")` and verify:
- Project exists and is properly configured
- Note any active themes or execution state

### 3. Git Status Check

Run `git_read(project="auto-dev-test-target-2-python", operation="status")` and verify:
- Working tree state
- Current branch
- Remote tracking configured

### 4. C4 Architecture Review

Check for C4 documentation:
- Read `docs/C4-Documentation/README.md` if it exists
- Note timestamp and currency
- Document any architectural context relevant to version planning

### 5. Gather Version Context from PLAN.md

Read `docs/auto-dev/PLAN.md` to understand:
- The version description and goals for v001
- All backlog items referenced for this version (BL-001 through BL-006)
- Any deferred items from previous versions
- Constraints or assumptions documented

## Output Requirements

Write ALL output files to BOTH locations:

**Primary (design artifact store):** `comms/outbox/versions/design/v001/001-environment/`
**Exploration output:** `comms/outbox/exploration/design-v001-001-environment/`

### README.md (required)

First paragraph: Summary of environment status (ready/blocked) and key context.

Then:
- **Environment Status**: Health check results, any issues
- **Project Status**: Current state, active work
- **Git Status**: Branch, working tree state
- **Architecture Context**: C4 docs status, key architectural patterns
- **Version Scope**: Backlog items, goals, constraints from PLAN.md

### environment-checks.md

Detailed results from all health and status checks.

### version-context.md

Complete context from PLAN.md including:
- Version goals and description
- All referenced backlog items (IDs only: BL-001, BL-002, BL-003, BL-004, BL-005, BL-006)
- Constraints and assumptions
- Deferred items to be aware of

## Guidelines

- Keep documents focused and under 200 lines each
- If environment checks fail, clearly document blockers
- Do not fetch full backlog item details here (that's Task 002)
- Do NOT commit — the master prompt handles commits

## When Complete

git add comms/outbox/exploration/design-v001-001-environment/
git add comms/outbox/versions/design/v001/001-environment/
git commit -m "exploration: design-v001-001-environment complete"
