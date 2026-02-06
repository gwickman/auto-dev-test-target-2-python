Read AGENTS.md first and follow all instructions there.

## Objective

Execute mandatory version closure tasks that apply to all auto-dev-mcp managed projects: plan updates, CHANGELOG verification, README review, repository cleanup, and documentation review.

## Context

Post-version retrospective for `auto-dev-test-target-2-python` version `v001`. These closure tasks are required for every version regardless of project.

## Tasks

### 1. Update plan.md

Read `docs/auto-dev/PLAN.md` (or `docs/auto-dev/plan.md`) and make these changes:
- Mark v001 as completed in the version list
- Update "Current Version" section to reflect the next planned version
- Move completed items from "Planned" to "Completed" section

If `PLAN.md` does not exist, document this in the output.

### 2. Verify CHANGELOG.md

Read `docs/CHANGELOG.md` and verify:
- v001 section exists with date
- Section contains categorized entries (Added, Changed, Fixed)
- Entries match the actual changes made (cross-reference with theme retrospectives)

If entries are missing or incorrect, add/fix them.

### 3. Review README.md

Read the project root `README.md` and check:
- Do any new capabilities from v001 need to be reflected?
- Are any described features now removed or changed?
- Is the project description still accurate?

If README needs updates: make the specific changes. If no changes needed: document "README current, no updates required."

### 4. Repository Cleanup

Verify repository state:
- Run `git_read(project="auto-dev-test-target-2-python", operation="prs", state="open")` — All version-related PRs should be merged
- Run `git_read(project="auto-dev-test-target-2-python", operation="stale_branches")` — No stale feature branches from this version
- Run `git_read(project="auto-dev-test-target-2-python", operation="status")` — Working tree clean

If stale branches exist, document them for cleanup.

### 5. Documentation Review

CRITICAL: Every document that references changed functionality must be checked.

Read the version and theme retrospectives to identify what changed in v001:
- `comms/outbox/versions/execution/v001/retrospective.md`

For each changed area, check the relevant documentation files:
- `docs/ARCHITECTURE.md` — if architecture changed
- `docs/DEVELOPER.md` — if developer workflow changed
- `docs/USER_MANUAL.md` — if user-facing behavior changed
- `docs/CI.md` — if CI pipeline changed
- Any other docs referenced by changes

For each document checked:
- If content is current: note "verified current"
- If content needs update: make the specific update
- If document doesn't exist: note "does not exist" (not a gap unless it should exist)

## Output Requirements

Save outputs to BOTH locations:
1. `comms/outbox/versions/retrospective/v001/008-closure/`
2. `comms/outbox/exploration/v001-retro-008-closure/`

### README.md (required) — save in BOTH locations

First paragraph: Closure summary (X items completed, Y documents updated).

Then:
- **Plan.md**: Updated/not found/no changes needed
- **CHANGELOG**: Verified complete / entries added
- **README**: Updated / no changes needed
- **Repository**: Clean / stale branches found
- **Documentation Review**: Table of document -> status (current/updated/not found)

### closure-report.md — save in BOTH locations

Detailed report of all changes made:
- Exact diffs for plan.md changes
- Exact diffs for CHANGELOG changes
- Exact diffs for README changes
- List of documents reviewed with findings
- Repository cleanup actions taken

When complete, commit all changes with message: "docs(v001): retrospective task 008 - generic closure"