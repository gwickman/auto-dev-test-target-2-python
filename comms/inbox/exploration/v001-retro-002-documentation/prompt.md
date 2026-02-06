Read AGENTS.md first and follow all instructions there.

## Objective

Verify all required documentation artifacts exist for every theme and feature in v001.

## Context

Post-version retrospective for `auto-dev-test-target-2-python` version `v001`. This task checks that the version execution produced all required documentation.

## Tasks

### 1. Identify Version Structure

Read `comms/inbox/versions/execution/v001/THEME_INDEX.md` to determine:
- All themes in this version
- All features within each theme

### 2. Check Feature Completion Reports

For each feature in each theme, verify this file exists:
- `comms/outbox/versions/execution/v001/<theme>/<feature>/completion-report.md`

Record: feature path, exists (yes/no), status from report if exists.

### 3. Check Theme Retrospectives

For each theme, verify this file exists:
- `comms/outbox/versions/execution/v001/<theme>/retrospective.md`

Record: theme name, exists (yes/no).

### 4. Check Version Retrospective

Verify this file exists:
- `comms/outbox/versions/execution/v001/retrospective.md`

### 5. Check CHANGELOG.md

Read `docs/CHANGELOG.md` and verify:
- A section for v001 exists
- Section contains at least one entry

### 6. Check version-state.json

Verify `comms/outbox/versions/execution/v001/version-state.json` exists and contains:
- Correct version identifier
- Status field

## Output Requirements

Save outputs to BOTH locations:
1. `comms/outbox/versions/retrospective/v001/002-documentation/`
2. `comms/outbox/exploration/v001-retro-002-documentation/`

### README.md (required) — save in BOTH locations

First paragraph: Documentation completeness summary (X/Y artifacts present).

Then:
- **Completion Reports**: Table of feature -> status
- **Theme Retrospectives**: Table of theme -> status
- **Version Retrospective**: Present/missing
- **CHANGELOG**: Present/missing, has version section
- **Version State**: Present/missing, status value
- **Missing Artifacts**: List of all missing documents with full paths

### completeness-report.md — save in BOTH locations

Detailed table:

| Artifact Type | Path | Exists | Notes |
|---------------|------|--------|-------|
| Completion Report | comms/outbox/.../completion-report.md | Yes | status: complete |

When complete, commit all changes with message: "docs(v001): retrospective task 002 - documentation completeness"