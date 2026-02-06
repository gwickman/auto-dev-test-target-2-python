You are executing Task 006: Document Drafts for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Draft the complete content for all design documents: VERSION_DESIGN.md, THEME_INDEX.md, THEME_DESIGN.md per theme, and requirements.md + implementation-plan.md per feature. Documents must be lean and reference the design artifact store.

## Context

This is Phase 3 (Document Drafts & Persistence) for auto-dev-test-target-2-python version v001.

The refined logical design from Phase 2 (Task 005) is complete. Now create the actual document content that will be persisted to the inbox.

**WARNING:** Do NOT modify any files in `comms/outbox/versions/design/v001/`. These are the reference artifacts.

## Tasks

### 1. Read the Design Artifact Store

Read ALL outputs from the centralized store:
- `comms/outbox/versions/design/v001/001-environment/README.md`
- `comms/outbox/versions/design/v001/001-environment/version-context.md`
- `comms/outbox/versions/design/v001/002-backlog/README.md`
- `comms/outbox/versions/design/v001/002-backlog/backlog-details.md`
- `comms/outbox/versions/design/v001/003-research/README.md`
- `comms/outbox/versions/design/v001/003-research/external-research.md`
- `comms/outbox/versions/design/v001/003-research/evidence-log.md`
- `comms/outbox/versions/design/v001/004-logical-design/logical-design.md`
- `comms/outbox/versions/design/v001/004-logical-design/test-strategy.md`
- `comms/outbox/versions/design/v001/005-critical-thinking/refined-logical-design.md`
- `comms/outbox/versions/design/v001/005-critical-thinking/risk-assessment.md`

Use Task 005's refined-logical-design.md as the primary design source.

### 2. Draft VERSION_DESIGN.md

Create version-level design document. Keep it lean — reference the artifact store:

```markdown
# Version Design: v001

## Description
[Version description and goals]

## Design Artifacts
Full design analysis available at: `comms/outbox/versions/design/v001/`

## Constraints and Assumptions
[Brief list]

## Key Design Decisions
[Brief list]

## Theme Overview
[Brief table of themes]
```

### 3. Draft THEME_INDEX.md

**CRITICAL: Machine-Parseable Format**

Parser regex: `- (\d+)-([\w-]+):`

**REQUIRED format for feature lists:**
```
**Features:**

- 001-feature-name: Brief description text here
- 002-another-feature: Another description text
```

**FORBIDDEN formats:**
- Numbered lists: `1.` `2.` `3.`
- Bold feature identifiers: `**001-feature-name**`
- Metadata before colon: `001-feature (BL-123, P0, XL)`
- Multi-line feature entries
- Missing colon after feature name

For v001, the THEME_INDEX.md should look like:

```markdown
# Theme Index: v001

## 01-project-scaffolding

**Goal:** Establish the complete Python project structure with uv build backend, src-layout package, and minimal hello module.

**Features:**

- 001-pyproject-init: Initialize pyproject.toml with uv build backend and project metadata
- 002-package-structure: Create src/test_target_2/ package with __init__.py
- 003-hello-module: Create hello.py with typed hello() function

## 02-quality-and-ci

**Goal:** Configure quality gates (ruff, mypy, pytest) and GitHub Actions CI workflow.

**Features:**

- 001-ruff-config: Configure ruff linting and formatting rules
- 002-mypy-config: Configure mypy with strict mode
- 003-pytest-setup: Set up pytest with basic passing test for hello module
- 004-github-actions: Create GitHub Actions CI workflow with all quality gates
```

### 4. Draft THEME_DESIGN.md (per theme)

For EACH theme, create a lean THEME_DESIGN.md referencing the artifact store.

### 5. Draft requirements.md (per feature)

For EACH feature (7 total), create requirements.md:
- Goal (one sentence)
- Background (context, backlog items)
- Functional Requirements (FR-001, FR-002, etc. with acceptance criteria)
- Non-Functional Requirements (NFR-001, etc.)
- Out of Scope
- Test Requirements
- Reference to design artifact store

**CRITICAL — Backlog ID Cross-Reference:**
Cross-reference BL numbers against the backlog analysis:
- BL-001: Project initialization / pyproject.toml
- BL-002: pytest setup
- BL-003: ruff configuration
- BL-004: mypy configuration
- BL-005: GitHub Actions CI
- BL-006: hello module

### 6. Draft implementation-plan.md (per feature)

For EACH feature (7 total), create implementation-plan.md:
- Overview
- Files to Create/Modify
- Implementation Stages with verification commands
- Quality Gates
- Commit Message template

## Output Requirements

Create in comms/outbox/exploration/design-v001-006-drafts/:

### README.md (required)

First paragraph: Summary of document drafts created (2 themes, 7 features).

Then:
- **Document Inventory**: List of all drafted documents
- **Reference Pattern**: How documents reference the artifact store
- **Completeness Check**: All backlog items covered
- **Format Verification**: Machine-parseable formats validated

### document-drafts.md

Complete document drafts organized by type:

```markdown
# Document Drafts - v001

## VERSION_DESIGN.md
[Full draft content]

---

## THEME_INDEX.md
[Full draft content]

---

## Theme 01: 01-project-scaffolding

### THEME_DESIGN.md
[Full draft content]

### Feature 001-pyproject-init

#### requirements.md
[Full draft content]

#### implementation-plan.md
[Full draft content]

### Feature 002-package-structure
[... etc]

### Feature 003-hello-module
[... etc]

---

## Theme 02: 02-quality-and-ci

### THEME_DESIGN.md
[Full draft content]

### Feature 001-ruff-config
[... etc]

### Feature 002-mypy-config
[... etc]

### Feature 003-pytest-setup
[... etc]

### Feature 004-github-actions
[... etc]
```

### draft-checklist.md

Verification checklist for all documents.

## Guidelines

- ALL backlog items from PLAN.md are MANDATORY
- Documents must be LEAN — reference the artifact store, don't duplicate it
- Follow machine-parseable format for THEME_INDEX.md
- The consolidated document-drafts.md may be LONG (1000+ lines) — that's expected
- Do NOT modify the design artifact store

## When Complete

git add comms/outbox/exploration/design-v001-006-drafts/
git commit -m "exploration: design-v001-006-drafts - document drafts complete"
