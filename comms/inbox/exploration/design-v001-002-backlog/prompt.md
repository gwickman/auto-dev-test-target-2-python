You are executing Task 002: Backlog Analysis and Retrospective Review for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Gather complete details for all backlog items in the version scope and learn from the previous version's retrospective.

## Context

This is Phase 1 (Environment & Investigation) for auto-dev-test-target-2-python version v001. Task 001 identified backlog item IDs: BL-001, BL-002, BL-003, BL-004, BL-005, BL-006. This task gathers full details.

## Tasks

### 1. Fetch Complete Backlog Items

For each of these backlog IDs, call `get_backlog_item(project="auto-dev-test-target-2-python", item_id="BL-XXX")`:
- BL-001
- BL-002
- BL-003
- BL-004
- BL-005
- BL-006

Extract full details: title, description, acceptance criteria, priority, tags, notes.
Document any missing or incomplete backlog items.

**MANDATORY SCOPE:** ALL 6 backlog items listed in PLAN.md for v001 are mandatory. No items may be deferred, descoped, or deprioritized.

### 2. Identify Previous Version

Call `list_versions(project="auto-dev-test-target-2-python")` to find the most recent completed version before v001. Since v001 is the first version, there likely is no previous version.

### 3. Review Previous Retrospective

If a previous version exists, locate and read its retrospective. If no previous version exists, document that this is the first version and no retrospective is available.

### 4. Search Project Learnings

Run `search_learnings(project="auto-dev-test-target-2-python", tags=["design", "architecture"])` to find relevant documented learnings. Also try `list_learnings(project="auto-dev-test-target-2-python")`.

## Output Requirements

Write ALL output files to BOTH locations:

**Primary (design artifact store):** `comms/outbox/versions/design/v001/002-backlog/`
**Exploration output:** `comms/outbox/exploration/design-v001-002-backlog/`

### README.md (required)

First paragraph: Summary of backlog scope and key insights from retrospective.

Then:
- **Backlog Overview**: Count of items, priority distribution
- **Previous Version**: Version number, retrospective location (or "N/A - first version")
- **Key Learnings**: Top insights applicable to current version
- **Tech Debt**: Any debt items to address
- **Missing Items**: Any referenced backlog items not found

### backlog-details.md

For each backlog item, include:
- ID, Title, Priority
- Full description (quoted)
- Acceptance criteria (listed)
- Tags and notes
- Complexity assessment (based on description, not title)

### retrospective-insights.md

Synthesized insights from previous version (or note that this is v001 with no prior retrospective).

### learnings-summary.md

Relevant learnings from project learning repository.

## Guidelines

- ALL backlog items from PLAN.md are MANDATORY — no deferrals, no descoping
- Quote actual backlog text when documenting items
- Keep documents under 200 lines each
- Do NOT commit — the master prompt handles commits after Phase 2

## When Complete

git add comms/outbox/exploration/design-v001-002-backlog/
git add comms/outbox/versions/design/v001/002-backlog/
git commit -m "exploration: design-v001-002-backlog complete"
