Read AGENTS.md first and follow all instructions there.

## Objective

Compile all findings from tasks 001-006 into a single proposals document using the Crystal Clear Actions format. All proposals are auto-approved.

## Context

Post-version retrospective for `auto-dev-test-target-2-python` version `v001`. This task synthesizes all verification and analysis results into actionable remediation proposals.

## Tasks

### 1. Read All Previous Task Outputs

Read the README.md from each completed task:
- `comms/outbox/versions/retrospective/v001/001-environment/README.md`
- `comms/outbox/versions/retrospective/v001/002-documentation/README.md`
- `comms/outbox/versions/retrospective/v001/003-backlog/README.md`
- `comms/outbox/versions/retrospective/v001/004-quality/README.md`
- `comms/outbox/versions/retrospective/v001/005-architecture/README.md`
- `comms/outbox/versions/retrospective/v001/006-learnings/README.md`

Read detailed reports where the README references them.

### 2. Identify All Findings Requiring Action

From each task, extract items that need remediation:
- **001**: Environment blockers (stale branches, dirty working tree)
- **002**: Missing documentation artifacts
- **003**: Backlog items that failed to complete
- **004**: Quality gate failures not yet fixed
- **005**: Architecture drift items (already handled via backlog — reference only)
- **006**: Learning extraction issues (unlikely but check)

### 3. Create Proposals Document

For each finding, use this exact format:

```markdown
### Finding: [Brief description]

**Source:** Task [NNN] - [task name]

**Current State:**
[What exists now — specific file paths and content]

**Gap:**
[What's missing or incorrect]

**Proposed Actions:**
- [ ] [Action 1]: `exact/file/path` — [exact change to make]
- [ ] [Action 2]: `exact/file/path` — [exact change to make]

**Auto-approved:** Yes
```

### Anti-Patterns (DO NOT USE)

- "Review and update if needed"
- "Consider adding documentation"
- "May need to check X"
- "Should probably update Y"

Every action must specify: exact file path, exact change, no ambiguity.

### 4. Categorize Proposals

Group proposals by type:
- **Immediate Fixes**: Can be executed by the remediation exploration
- **Backlog Items**: Already created by previous tasks (reference only)
- **User Action Required**: Items requiring human intervention

### 5. Summary Statistics

Count:
- Total findings across all tasks
- Findings with no action needed (everything was clean)
- Immediate fix proposals
- Backlog items created/updated
- User actions required

## Output Requirements

Save outputs to BOTH locations:
1. `comms/outbox/versions/retrospective/v001/007-proposals/`
2. `comms/outbox/exploration/v001-retro-007-proposals/`

### README.md (required) — save in BOTH locations

First paragraph: Proposals summary (X findings, Y immediate fixes, Z backlog items, W user actions).

Then:
- **Status by Task**: Table of task -> findings count -> actions needed
- **Immediate Fixes**: List of actions for remediation exploration
- **Backlog References**: Items already handled
- **User Actions**: Items requiring human intervention

### proposals.md — save in BOTH locations

Complete proposals document with all findings in Crystal Clear Actions format. This file is the input for the remediation exploration launched by the master prompt.

When complete, commit all changes with message: "docs(v001): retrospective task 007 - stage 1 proposals"