Read AGENTS.md first and follow all instructions there.

## Objective

Extract transferable learnings from all completion reports and theme retrospectives, then save them via the learnings system.

## Context

Post-version retrospective for `auto-dev-test-target-2-python` version `v001`. Learnings capture reusable patterns, failure modes, and decision frameworks — not implementation details.

## Tasks

### 1. Read All Completion Reports

Read every completion report for v001:
- `comms/outbox/versions/execution/v001/01-01-project-scaffolding/001-001-pyproject-init/completion-report.md`
- `comms/outbox/versions/execution/v001/01-01-project-scaffolding/002-002-package-structure/completion-report.md`
- `comms/outbox/versions/execution/v001/01-01-project-scaffolding/003-003-hello-module/completion-report.md`
- `comms/outbox/versions/execution/v001/02-02-quality-and-ci/001-001-ruff-config/completion-report.md`
- `comms/outbox/versions/execution/v001/02-02-quality-and-ci/002-002-mypy-config/completion-report.md`
- `comms/outbox/versions/execution/v001/02-02-quality-and-ci/003-003-pytest-setup/completion-report.md`
- `comms/outbox/versions/execution/v001/02-02-quality-and-ci/004-004-github-actions/completion-report.md`

For each report, identify:
- Patterns that worked well
- Approaches that failed and what replaced them
- Decision rationale worth preserving
- Debugging techniques that resolved issues

### 2. Read All Theme Retrospectives

Read every theme retrospective:
- `comms/outbox/versions/execution/v001/01-01-project-scaffolding/retrospective.md`
- `comms/outbox/versions/execution/v001/02-02-quality-and-ci/retrospective.md`

For each retrospective, identify:
- Cross-feature patterns
- Theme-level learnings
- Process observations

### 3. Read Version Retrospective

Read:
- `comms/outbox/versions/execution/v001/retrospective.md`

Identify version-level insights not covered by individual themes.

### 4. Deduplicate and Filter

From all identified learnings:
- Remove duplicates (same insight from multiple sources)
- Remove implementation-specific details (code snippets, file paths)
- Remove version-specific references that won't generalize
- Keep: transferable patterns, failure modes, decision frameworks, debugging approaches

### 5. Save Learnings

For each unique learning, call:

```python
save_learning(
    project="auto-dev-test-target-2-python",
    title="<concise title>",
    content="<full learning content in markdown>",
    tags=["<relevant-tags>"],
    source="v001/<theme>/<feature> completion-report" or "v001/<theme> retrospective",
    summary="<one-sentence summary>"
)
```

Content structure for each learning:
```markdown
## Context
[When this applies]

## Learning
[The transferable insight]

## Evidence
[What happened that demonstrated this]

## Application
[How to apply this in future work]
```

### 6. Check Existing Learnings for Updates

Call `list_learnings(project="auto-dev-test-target-2-python")` and check if any existing learnings should be updated based on new evidence from this version.

If an existing learning is reinforced or refined by new evidence, note it but do NOT modify existing learnings.

## Output Requirements

Save outputs to BOTH locations:
1. `comms/outbox/versions/retrospective/v001/006-learnings/`
2. `comms/outbox/exploration/v001-retro-006-learnings/`

### README.md (required) — save in BOTH locations

First paragraph: Learnings summary (X new learnings saved, Y existing reinforced).

Then:
- **New Learnings**: Table of title, tags, source
- **Reinforced Learnings**: Existing learnings that got additional evidence
- **Filtered Out**: Count and categories of items filtered (too specific, duplicates, etc.)

### learnings-detail.md — save in BOTH locations

For each learning saved:
- Learning title
- Tags assigned
- Source document
- Full content saved

When complete, commit all changes with message: "docs(v001): retrospective task 006 - learning extraction"