# Draft Verification Checklist — v001

## VERSION_DESIGN.md

- [x] Description section with version goals
- [x] Design Artifacts section referencing `comms/outbox/versions/design/v001/`
- [x] Constraints and Assumptions (6 items)
- [x] Key Design Decisions (6 decisions)
- [x] Theme Overview table (2 themes)
- [x] Lean — references artifact store, doesn't duplicate

## THEME_INDEX.md

- [x] Machine-parseable format: `- NNN-feature-name: Description`
- [x] Matches parser regex: `- (\d+)-([\w-]+):`
- [x] No numbered lists (1., 2., 3.)
- [x] No bold feature identifiers (**001-feature**)
- [x] No metadata before colon
- [x] No multi-line feature entries
- [x] Colon present after every feature name
- [x] **Features:** header with blank line before list
- [x] Theme 01: 3 features listed
- [x] Theme 02: 4 features listed

## Theme 01: 01-project-scaffolding

### THEME_DESIGN.md

- [x] Goal statement
- [x] Design artifacts reference
- [x] Backlog items table (BL-001, BL-006)
- [x] Features table with dependencies
- [x] Execution order (sequential)
- [x] Risk notes

### Feature 001-pyproject-init

- [x] requirements.md: Goal, Background, FR (4), NFR (1), Out of Scope, Test Requirements, Reference
- [x] requirements.md: BL-001 cross-referenced
- [x] implementation-plan.md: Overview, Files, Stages (2), Quality Gates, Commit Message
- [x] implementation-plan.md: Concrete pyproject.toml content

### Feature 002-package-structure

- [x] requirements.md: Goal, Background, FR (2), NFR (1), Out of Scope, Test Requirements, Reference
- [x] requirements.md: BL-001 cross-referenced
- [x] implementation-plan.md: Overview, Files, Stages (2), Quality Gates, Commit Message
- [x] implementation-plan.md: Concrete __init__.py content

### Feature 003-hello-module

- [x] requirements.md: Goal, Background, FR (3), NFR (1), Out of Scope, Test Requirements, Reference
- [x] requirements.md: BL-006 cross-referenced, BL-001 AC#3 noted
- [x] implementation-plan.md: Overview, Files, Stages (2), Quality Gates, Commit Message
- [x] implementation-plan.md: Concrete hello.py content

## Theme 02: 02-quality-and-ci

### THEME_DESIGN.md

- [x] Goal statement
- [x] Design artifacts reference
- [x] Backlog items table (BL-002, BL-003, BL-004, BL-005)
- [x] Features table with dependencies
- [x] Execution order (fan-out then converge)
- [x] Risk notes

### Feature 001-ruff-config

- [x] requirements.md: Goal, Background, FR (3), NFR (1), Out of Scope, Test Requirements, Reference
- [x] requirements.md: BL-003 cross-referenced
- [x] implementation-plan.md: Overview, Files, Stages (3), Quality Gates, Commit Message
- [x] implementation-plan.md: Concrete ruff configuration

### Feature 002-mypy-config

- [x] requirements.md: Goal, Background, FR (2), NFR (2), Out of Scope, Test Requirements, Reference
- [x] requirements.md: BL-004 cross-referenced
- [x] implementation-plan.md: Overview, Files, Stages (2), Quality Gates, Commit Message
- [x] implementation-plan.md: Concrete mypy configuration

### Feature 003-pytest-setup

- [x] requirements.md: Goal, Background, FR (3), NFR (2), Out of Scope, Test Requirements, Reference
- [x] requirements.md: BL-002 cross-referenced
- [x] implementation-plan.md: Overview, Files, Stages (4), Quality Gates, Commit Message
- [x] implementation-plan.md: Concrete test file content

### Feature 004-github-actions

- [x] requirements.md: Goal, Background, FR (4), NFR (2), Out of Scope, Test Requirements, Reference
- [x] requirements.md: BL-005 cross-referenced
- [x] implementation-plan.md: Overview, Files, Stages (3), Quality Gates, Commit Message
- [x] implementation-plan.md: Concrete CI workflow YAML

## Cross-Cutting Checks

- [x] All 6 backlog items (BL-001 through BL-006) mapped to features
- [x] No backlog items deferred
- [x] All documents reference design artifact store (not duplicating)
- [x] Feature dependencies are consistent across documents
- [x] Quality gate commands match AGENTS.md order (ruff check, ruff format, mypy, pytest)
- [x] Python version consistent: >= 3.11 / py311 / 3.11 across all configs
- [x] All implementation plans include verification steps
- [x] All implementation plans include commit message templates
