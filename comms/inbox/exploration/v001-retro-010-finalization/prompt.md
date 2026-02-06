Read AGENTS.md first and follow all instructions there.

## Objective

Verify all retrospective tasks completed, run final quality gates, and generate the final summary. Do NOT commit or push — the calling orchestrator handles that.

## Context

Post-version retrospective for `auto-dev-test-target-2-python` version `v001`. This is the final task — it wraps up everything and produces the official version completion.

## Tasks

### 1. Verify All Previous Tasks Completed

Read the README.md from each task folder and verify it exists and indicates successful completion:

| Task | Folder | Required |
|------|--------|----------|
| 001 | `comms/outbox/versions/retrospective/v001/001-environment/` | Yes |
| 002 | `comms/outbox/versions/retrospective/v001/002-documentation/` | Yes |
| 003 | `comms/outbox/versions/retrospective/v001/003-backlog/` | Yes |
| 004 | `comms/outbox/versions/retrospective/v001/004-quality/` | Yes |
| 005 | `comms/outbox/versions/retrospective/v001/005-architecture/` | Yes |
| 006 | `comms/outbox/versions/retrospective/v001/006-learnings/` | Yes |
| 007 | `comms/outbox/versions/retrospective/v001/007-proposals/` | Yes |
| 008 | `comms/outbox/versions/retrospective/v001/008-closure/` | Yes |
| 009 | `comms/outbox/versions/retrospective/v001/009-project-closure/` | Conditional (skipped) |

If any required task is missing or reports failure, document the gap.

### 2. Run Final Quality Gates

Call:
```python
run_quality_gates(project="auto-dev-test-target-2-python")
```

All checks must pass. If any fail:
- Document the failure
- Do NOT attempt fixes at this stage

### 3. Generate Final Summary

Create a summary of the entire retrospective process:
- Total tasks executed
- Findings count by category
- Remediation actions taken
- Backlog items created/completed
- Learnings saved

## Output Requirements

Save outputs to BOTH locations:
1. `comms/outbox/versions/retrospective/v001/010-finalization/`
2. `comms/outbox/exploration/v001-retro-010-finalization/`

### README.md (required) — save in BOTH locations

First paragraph: Finalization summary (version officially closed / blocked with reason).

Then:
- **Task Verification**: All tasks confirmed complete
- **Final Quality Gates**: All passed
- **Retrospective Summary**: High-level metrics

### final-summary.md — save in BOTH locations

Complete retrospective summary:

```markdown
# v001 Retrospective Summary

## Overview
- **Project**: auto-dev-test-target-2-python
- **Version**: v001
- **Status**: Complete

## Verification Results
| Task | Status | Key Findings |
|------|--------|-------------|
| 001 Environment | Pass | [summary] |
| 002 Documentation | Pass | [summary] |
...

## Actions Taken
- Backlog items completed: X
- Documentation gaps fixed: Y
- Learnings saved: Z
- Architecture drift items: W

## Outstanding Items
- [Any items requiring future attention]
```

Do NOT commit — the calling orchestrator handles commits.
Do NOT call complete_version — the calling orchestrator handles that.