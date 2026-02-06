## Context

When establishing a project foundation (scaffolding, build system, package structure), the work could be done as one large feature or broken into small sequential steps.

## Learning

Break foundational work into 3-4 small, focused features with explicit sequential dependencies. Each feature should be independently verifiable with quality gates. This provides clear progression, easy rollback points, and independent verification at each step.

## Evidence

v001 Theme 01 used a 3-feature pattern: build system (001) -> package structure (002) -> first module (003). Each feature was completed successfully with all quality gates green. The theme retrospective noted: "Sequential feature ordering with clear dependencies worked cleanly" and "Each feature was small, focused, and independently verifiable." Zero rework was required across all 7 features in the version.

## Application

- For scaffolding themes, use the pattern: build system -> package structure -> first module
- For quality themes, use the pattern: linter -> type checker -> test framework -> CI
- Keep each feature to 2-4 acceptance criteria
- Ensure each feature can run quality gates independently after completion
- Use handoff documents between sequential features to maintain context continuity