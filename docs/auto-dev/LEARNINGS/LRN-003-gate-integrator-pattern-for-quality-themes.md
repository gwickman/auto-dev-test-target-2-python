## Context

When a theme involves configuring multiple independent quality tools (linter, type checker, test framework), the individual tool configurations need an integration point to verify they work together.

## Learning

Cap a quality-tooling theme with a CI/CD feature that combines all quality gates into a single workflow. This final feature acts as an integration test for all prior quality gate configurations, verifying they work together in an automated environment.

## Evidence

In v001 Theme 02, features 001-003 individually configured ruff, mypy, and pytest. Feature 004 (GitHub Actions CI) combined all three into a single workflow. The theme retrospective noted: "Feature 004 (CI) was effectively an integration test of all three prior features, confirming they work together." This pattern caught no issues in v001, but its value is as a safety net for future changes.

## Application

- When designing quality/tooling themes, plan a CI integration feature as the final deliverable
- The CI feature should run every quality gate configured in prior features
- This pattern provides a natural verification that independent tool configurations are compatible
- Consider this the "capstone" feature that proves the theme's deliverables work as a system