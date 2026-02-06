You are executing Task 008: Pre-Execution Validation for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Perform READ-ONLY validation of all persisted design documents to ensure they are complete, consistent, and ready for autonomous execution.

## Context

This is Phase 4 (Validation) for auto-dev-test-target-2-python version v001.

All design documents have been persisted. This task validates completeness without modifying anything.

**CRITICAL:** This task is READ-ONLY. Do NOT modify any persisted documents. If validation fails, document the failure and STOP.

## Tasks

### 1. Content Completeness Check

Compare Task 006 drafts against persisted inbox documents:
- Read `comms/outbox/exploration/design-v001-006-drafts/document-drafts.md`
- Read all documents in `comms/inbox/versions/execution/v001/`
- Check for truncation or missing content
- Document any discrepancies

### 2. Reference Resolution

For each document, verify:
- All references to `comms/outbox/versions/design/v001/` resolve to existing files
- No broken links to missing artifacts
- Design artifact store is intact and complete

### 3. Notes Propagation

Verify migration notes and caveats made it into documents:
- Check requirements.md for notes from backlog items
- Check implementation-plan.md for risk mitigation notes

### 4. validate_version_design Tool

Run `validate_version_design(project="auto-dev-test-target-2-python", version="v001")`:
- Confirm 0 missing documents
- Document the validation result

### 5. Backlog Alignment (MANDATORY SCOPE)

ALL backlog items from PLAN.md for v001 are mandatory:
- BL-001: Project initialization / pyproject.toml → must be in Theme 01
- BL-002: pytest setup → must be in Theme 02
- BL-003: ruff configuration → must be in Theme 02
- BL-004: mypy configuration → must be in Theme 02
- BL-005: GitHub Actions CI → must be in Theme 02
- BL-006: hello module → must be in Theme 01

Verify EVERY backlog item is mapped to at least one feature. If any is missing, this is a BLOCKING FAILURE.

### 6. File Paths Exist

Review implementation plans:
- For new files, verify parent directories exist or will be created
- Document any invalid file references

### 7. Dependency Accuracy

Review stated dependencies:
- Theme 01 must complete before Theme 02
- Feature 004-github-actions depends on 001, 002, 003 in Theme 02
- Check for circular dependencies

### 8. Mitigation Strategy

If this version fixes bugs affecting execution, document workarounds. For v001 (first version), this is likely N/A.

### 9. Design Docs Committed

Verify all design documents are committed:
- Check git status for uncommitted changes in `comms/inbox/versions/execution/v001/`

### 10. Handover Document

Verify STARTER_PROMPT.md exists and is complete:
- Read `comms/inbox/versions/execution/v001/STARTER_PROMPT.md`
- Check it includes project context
- Verify it references all necessary documents

### 11. Impact Analysis Completeness

Review VERSION_DESIGN.md and THEME_DESIGN.md files:
- Dependencies identified
- Breaking changes documented
- Test impact assessed

## Output Requirements

Create in comms/outbox/exploration/design-v001-008-validation/:

### README.md (required)

First paragraph: Summary of validation result (PASS/FAIL) with confidence level.

Then:
- **Checklist Status**: X/11 items passed
- **Blocking Issues**: Any failures requiring fix
- **Warnings**: Non-blocking concerns
- **Ready for Execution**: Yes/No with rationale

### pre-execution-checklist.md

Detailed checklist with PASS/FAIL status for each of the 11 items.

### validation-details.md

Detailed findings for each checklist item.

### discrepancies.md

Document any issues found. If none: "No discrepancies identified."

## Guidelines

- ALL backlog items from PLAN.md are MANDATORY — any missing item is a blocking failure
- This task is READ-ONLY — do not modify any documents
- Be thorough — this is the final check before execution
- Document all findings, even minor issues

## When Complete

git add comms/outbox/exploration/design-v001-008-validation/
git commit -m "exploration: design-v001-008-validation complete - [PASS/FAIL]"
