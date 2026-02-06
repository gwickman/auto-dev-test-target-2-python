You are executing Task 003: Research and Investigation for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Research unknowns, investigate prior art, and gather evidence for design decisions that affect version STRUCTURE (not implementation details Claude Code can figure out).

## Context

This is Phase 1 (Environment & Investigation) for auto-dev-test-target-2-python version v001.

Tasks 001-002 gathered context. This task resolves unknowns before proposing solutions.

v001 is "Foundation" with 2 themes:
- Theme 1: Project Scaffolding (pyproject.toml with uv, src/test_target_2/ package, hello.py module)
- Theme 2: Quality & CI (ruff, mypy strict, pytest, GitHub Actions CI)

Backlog items: BL-001 through BL-006.

Read the backlog details from: `comms/outbox/versions/design/v001/002-backlog/backlog-details.md`

## Tasks

### 1. Identify Research Questions

Based on backlog items from Task 002 (read from `comms/outbox/versions/design/v001/002-backlog/`), identify:
- Technologies or libraries requiring investigation
- Unclear areas of existing codebase
- Patterns needed but not yet understood
- Configuration values requiring evidence
- Integration points with existing systems

### 2. Codebase Investigation

For questions about existing code:
- Use `request_clarification` to search for patterns, classes, or files
- Read relevant source files to understand current implementation
- Document findings with file paths and line references

### 3. External Research

For questions about external libraries, patterns, or best practices:

**DeepWiki Research:**
- Use `ask_question` from mcp__deepwiki to query relevant repositories (e.g., astral-sh/ruff, astral-sh/uv, python/mypy)
- Document sources and specific implementation details found

**Key research areas for v001:**
- uv project initialization best practices (pyproject.toml format)
- ruff configuration format and recommended rules for new Python projects
- mypy strict mode configuration in pyproject.toml
- pytest configuration in pyproject.toml
- GitHub Actions workflow for Python projects with uv

### 4. Evidence Gathering for Concrete Values

For any concrete values needed:
- ruff rule sets to enable
- mypy strict mode flags
- pytest configuration options
- GitHub Actions workflow triggers and steps
- Python version targets

### 5. Impact Analysis

Document:
- **Dependencies**: What existing code/tools/configs will change?
- **Breaking changes**: Will existing workflows or APIs break?
- **Test impact**: What tests need creation or update?
- **Documentation**: What docs require update after implementation?

## Output Requirements

Write ALL output files to BOTH locations:

**Primary (design artifact store):** `comms/outbox/versions/design/v001/003-research/`
**Exploration output:** `comms/outbox/exploration/design-v001-003-research/`

### README.md (required)

First paragraph: Summary of research scope and key findings.

Then:
- **Research Questions**: List of questions investigated
- **Findings Summary**: High-level results
- **Unresolved Questions**: Items that cannot be resolved pre-implementation
- **Recommendations**: Design direction based on research

### codebase-patterns.md

Findings from codebase investigation.

### external-research.md

Findings from DeepWiki and web research.

### evidence-log.md

For all concrete values needed with sources and rationale.

### impact-analysis.md

Analysis of implementation impact.

## Guidelines

- ALL backlog items from PLAN.md are MANDATORY — research must cover all of them
- Document sources for all findings (file paths, URLs, repo names)
- Keep each document under 200 lines
- Do NOT commit — the master prompt handles commits after Phase 2

## When Complete

git add comms/outbox/exploration/design-v001-003-research/
git add comms/outbox/versions/design/v001/003-research/
git commit -m "exploration: design-v001-003-research complete"
