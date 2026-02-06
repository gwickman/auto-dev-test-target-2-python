You are executing Task 004: Logical Design Proposal for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Synthesize findings from Tasks 001-003 into a coherent logical design proposal with theme groupings, feature breakdowns, and test strategy.

## Context

This is Phase 2 (Logical Design & Critical Thinking) for auto-dev-test-target-2-python version v001.

All context is gathered. Now propose the structure. This proposal feeds into Task 005 (Critical Thinking) for risk review before document drafting begins.

## Tasks

### 1. Read Phase 1 Outputs

Read all design artifacts from the centralized store:
- `comms/outbox/versions/design/v001/001-environment/README.md`
- `comms/outbox/versions/design/v001/001-environment/version-context.md`
- `comms/outbox/versions/design/v001/002-backlog/README.md`
- `comms/outbox/versions/design/v001/002-backlog/backlog-details.md`
- `comms/outbox/versions/design/v001/003-research/README.md`
- `comms/outbox/versions/design/v001/003-research/external-research.md`
- `comms/outbox/versions/design/v001/003-research/evidence-log.md`
- `comms/outbox/versions/design/v001/003-research/impact-analysis.md`

### 2. Theme Groupings

Based on PLAN.md, v001 has 2 themes:
- Theme 01: Project Scaffolding (BL-001, BL-006)
- Theme 02: Quality & CI (BL-002, BL-003, BL-004, BL-005)

Propose theme names in slug format: `01-project-scaffolding`, `02-quality-and-ci`

For each theme provide:
- Theme name (slug format)
- Theme goal (one paragraph)
- Features included (with backlog mappings)

### 3. Feature Breakdown

For each feature within themes:
- Feature name (slug format: NNN-descriptive-name)
- Feature goal (one sentence)
- Backlog item(s) addressed (BL-XXX references)
- Dependencies

Theme 01 features should include:
- 001-pyproject-init: Initialize pyproject.toml with uv (BL-001)
- 002-package-structure: Create src/test_target_2/ package (BL-001)
- 003-hello-module: Create hello.py with hello() function (BL-006)

Theme 02 features should include:
- 001-ruff-config: Configure ruff linting and formatting (BL-002)
- 002-mypy-config: Configure mypy with strict mode (BL-003)
- 003-pytest-setup: Set up pytest with basic passing test (BL-004)
- 004-github-actions: Create GitHub Actions CI workflow (BL-005)

### 4. Execution Order

Document dependencies between themes and features. Theme 01 must complete before Theme 02 (CI needs code to lint/test).

### 5. Test Strategy

For each feature, identify test requirements (unit tests, integration tests, etc.)

### 6. Research Sources Adopted

Reference evidence from Task 003 research for specific approaches.

### 7. Risks and Unknowns

List all identified risks with severity and what investigation would help.

## Output Requirements

Write ALL output files to BOTH locations:

**Primary (design artifact store):** `comms/outbox/versions/design/v001/004-logical-design/`
**Exploration output:** `comms/outbox/exploration/design-v001-004-logical-design/`

### README.md (required)

First paragraph: Summary of proposed structure (2 themes, 7 features total).

Then:
- **Theme Overview**: List of themes with goals
- **Key Decisions**: Major grouping decisions
- **Dependencies**: High-level execution order rationale
- **Risks and Unknowns**: Items needing investigation in Task 005

### logical-design.md

Complete logical design proposal with theme breakdown, feature tables, execution order, and research sources.

### test-strategy.md

Test requirements per feature.

### risks-and-unknowns.md

All identified risks and unknowns for Task 005.

## Guidelines

- ALL backlog items from PLAN.md are MANDATORY and must be mapped to a feature
- Theme names should be descriptive and URL-friendly
- Feature names should be action-oriented
- Evidence must come from Task 003, not new assumptions
- Keep documents under 200-300 lines
- Do NOT commit — the master prompt handles commits after Phase 2

## When Complete

git add comms/outbox/exploration/design-v001-004-logical-design/
git add comms/outbox/versions/design/v001/004-logical-design/
git commit -m "exploration: design-v001-004-logical-design complete"
