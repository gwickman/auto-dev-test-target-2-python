You are executing Task 007: Persist Documents for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Call the MCP design tools to persist all drafted documents to the inbox folder structure.

## Context

This is Phase 3 (Document Drafts & Persistence) for auto-dev-test-target-2-python version v001.

Task 006 created all document drafts in `comms/outbox/exploration/design-v001-006-drafts/document-drafts.md`. Now persist them using MCP tools.

**WARNING:** Do NOT modify any files in `comms/outbox/versions/design/v001/`. These are the reference artifacts.

## CRITICAL: Machine-Parseable Format Requirements

### THEME_INDEX.md - Feature List Format

**Parser regex:** `- (\d+)-([\w-]+):`

**REQUIRED format for feature lists:**
```
**Features:**

- 001-feature-name: Brief description text here
- 002-another-feature: Another description text
```

**FORBIDDEN formats that break parser:**
- Numbered lists: `1.` `2.` `3.`
- Bold feature identifiers: `**001-feature-name**`
- Metadata before colon: `001-feature (BL-123, P0, XL)`
- Multi-line feature entries
- Missing colon after feature name

## Tasks

### 1. Read Phase 3 Drafts

Read `comms/outbox/exploration/design-v001-006-drafts/document-drafts.md` to extract all document content.

### 2. Prepare Context Object

```json
{
    "rationale": "v001 Foundation establishes complete project infrastructure with uv-based packaging, src-layout, quality gates (ruff, mypy, pytest), and GitHub Actions CI",
    "constraints": ["Package manager: uv with uv_build backend", "Python target: >= 3.11", "All tool config in pyproject.toml", "Destructive test target project"],
    "assumptions": ["All technologies well-understood, no spikes needed", "uv_build >= 0.9.21 is current", "CI runs on ubuntu-latest"],
    "deferred_items": ["Utility functions deferred to v002", "Validation and error handling deferred to v003"]
}
```

### 3. Prepare Themes Array

```json
[
    {
        "name": "01-project-scaffolding",
        "goal": "Establish the complete Python project structure with uv build backend, src-layout package, and minimal hello module.",
        "features": [
            {"name": "001-pyproject-init", "goal": "Initialize pyproject.toml with uv build backend and project metadata"},
            {"name": "002-package-structure", "goal": "Create src/test_target_2/ package with __init__.py"},
            {"name": "003-hello-module", "goal": "Create hello.py with typed hello() function"}
        ]
    },
    {
        "name": "02-quality-and-ci",
        "goal": "Configure quality gates (ruff, mypy, pytest) and GitHub Actions CI workflow.",
        "features": [
            {"name": "001-ruff-config", "goal": "Configure ruff linting and formatting rules"},
            {"name": "002-mypy-config", "goal": "Configure mypy with strict mode"},
            {"name": "003-pytest-setup", "goal": "Set up pytest with basic passing test for hello module"},
            {"name": "004-github-actions", "goal": "Create GitHub Actions CI workflow with all quality gates"}
        ]
    }
]
```

### 4. Call design_version

Call `design_version` with:
- project: "auto-dev-test-target-2-python"
- version: "v001"
- description: "Foundation - Project scaffolding, quality gates, CI"
- themes: [the themes array from step 3]
- backlog_ids: ["BL-001", "BL-002", "BL-003", "BL-004", "BL-005", "BL-006"]
- context: [the context object from step 2]
- overwrite: false

### 5. Call design_theme for Each Theme

For EACH theme, read the full document drafts from `comms/outbox/exploration/design-v001-006-drafts/document-drafts.md` and extract the THEME_DESIGN.md content, requirements.md content, and implementation-plan.md content for each feature.

**CRITICAL - Feature Object Required Fields:**
Each feature dict MUST contain ALL of these fields:
- `number` (int): Feature number within the theme, 1-indexed sequential
- `name` (str): Feature slug (e.g., "001-pyproject-init")
- `requirements` (str): Full requirements.md markdown content
- `implementation_plan` (str): Full implementation-plan.md markdown content (NOTE: underscore, not hyphen)

Call `design_theme` for Theme 01:
- project: "auto-dev-test-target-2-python"
- version: "v001"
- theme_number: 1
- theme_name: "01-project-scaffolding"
- theme_design: [THEME_DESIGN.md content for Theme 01 from drafts]
- features: [array of 3 feature objects with number, name, requirements, implementation_plan]
- mode: "full"

Call `design_theme` for Theme 02:
- project: "auto-dev-test-target-2-python"
- version: "v001"
- theme_number: 2
- theme_name: "02-quality-and-ci"
- theme_design: [THEME_DESIGN.md content for Theme 02 from drafts]
- features: [array of 4 feature objects with number, name, requirements, implementation_plan]
- mode: "full"

### 6. Validate Design Completeness

Call `validate_version_design(project="auto-dev-test-target-2-python", version="v001")`.

Expected: All documents exist, no missing files.

## Output Requirements

Create in comms/outbox/exploration/design-v001-007-persist/:

### README.md (required)

First paragraph: Summary of persistence operation (success/failure, documents created).

Then:
- **Design Version Call**: Result and any errors
- **Design Theme Calls**: Result for each theme
- **Validation Result**: Output from validate_version_design
- **Missing Documents**: Any documents not created (should be none)

### persistence-log.md

Detailed log of all MCP calls with parameters, results, and outputs.

### verification-checklist.md

Document existence verification using read_document to verify each file exists.

## Error Handling

If any MCP call fails:
1. Document the exact error message
2. Document parameters used
3. Do NOT continue to subsequent calls
4. Mark exploration as requiring manual intervention

## Guidelines

- ALL backlog items from PLAN.md are MANDATORY
- Verify array structure before calling design_version
- Content passed to MCP tools should be the lean referenced versions from Task 006
- If any MCP call fails, document the error and STOP
- Do NOT modify the design artifact store

## When Complete

git add comms/outbox/exploration/design-v001-007-persist/
git commit -m "exploration: design-v001-007-persist - documents persisted to inbox"
