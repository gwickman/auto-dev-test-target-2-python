# Theme Design: 02-quality-and-ci

## Goal

Configure all quality gate tooling (ruff, mypy, pytest) and a GitHub Actions CI workflow so that every push and PR is automatically validated. This theme transforms the raw scaffolding from Theme 01 into a fully gated project with automated enforcement.

## Design Artifacts

Full design analysis: `comms/outbox/versions/design/v001/`

Key references:
- Logical design: `004-logical-design/logical-design.md` (Theme 02 section)
- Refined design: `005-critical-thinking/refined-logical-design.md`
- Research: `003-research/external-research.md` (ruff, mypy, pytest, GitHub Actions)
- Evidence: `003-research/evidence-log.md` (concrete configuration values)
- Test strategy: `004-logical-design/test-strategy.md`

## Backlog Items

| Item | Scope |
|------|-------|
| BL-002 | pytest setup with basic passing test |
| BL-003 | ruff configuration (linting + formatting) |
| BL-004 | mypy configuration with strict mode |
| BL-005 | GitHub Actions CI workflow |

## Features

| Feature | Goal | Backlog | Dependencies |
|---------|------|---------|--------------|
| 001-ruff-config | Configure ruff lint and format rules | BL-003 | Theme 01 complete |
| 002-mypy-config | Configure mypy strict mode | BL-004 | Theme 01 complete |
| 003-pytest-setup | Set up pytest with passing test | BL-002 | Theme 01 complete |
| 004-github-actions | Create CI workflow with all gates | BL-005 | 001, 002, 003 |

## Execution Order

Features 001, 002, 003 can execute in any order (all depend only on Theme 01). Feature 004 must execute last (depends on all three tools being configured).

```
001-ruff-config   ─┐
002-mypy-config   ─┼─> 004-github-actions
003-pytest-setup  ─┘
```

## Risks

- R-001 (CI first-run failure): Mitigated by AGENTS.md 3-iteration CI fix limit
- R-003 (mypy strict): Negligible — trivial code with primitive types only