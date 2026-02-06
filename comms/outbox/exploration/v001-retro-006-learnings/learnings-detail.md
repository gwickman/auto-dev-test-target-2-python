# Learnings Detail: v001 Retrospective Task 006

## LRN-001: Structural Placeholder Pattern Enables Incremental Validation

**Tags:** pattern, scaffolding, incremental-delivery, quality-gates
**Source:** v001/01-project-scaffolding retrospective

### Content

#### Context

When building a project incrementally across multiple features, later features often depend on structural prerequisites (directories, package files, configuration) that are formally delivered by earlier features.

#### Learning

Create minimal structural placeholders in early features so that build tools, quality gates, and dependency managers can run successfully from the very first feature onward. The placeholder will be populated with real content by the feature that formally owns it.

#### Evidence

In v001, feature 001 (pyproject-init) needed to create an empty `src/test_target_2/__init__.py` because the `uv_build` backend requires the src-layout package to exist for `uv sync` to succeed. Feature 002 then formally populated that file with version metadata. This allowed quality gates (ruff, mypy) to run green from feature 001 onward rather than failing until feature 002 was complete.

#### Application

- When designing feature sequences, identify structural prerequisites that downstream features and tooling depend on
- Create minimal placeholders in the earliest possible feature rather than deferring until the feature that formally owns that artifact
- Document the placeholder relationship so future developers understand why a file exists before its "real" feature

---

## LRN-002: Start Strict Stay Strict for Quality Tools

**Tags:** pattern, quality-gates, configuration, tech-debt-prevention
**Source:** v001/02-quality-and-ci retrospective

### Content

#### Context

When setting up quality tools (linters, type checkers, formatters) for a new project, there is a choice between starting with relaxed defaults and tightening later, or starting strict from the outset.

#### Learning

Adopt strict configurations for all quality tools from the very beginning of a project. Starting strict is painless when the codebase is small, but retrofitting strictness onto a permissive codebase accumulates tech debt that is harder to resolve later.

#### Evidence

In v001, mypy was configured with `strict = true` and ruff was configured with broad rule sets (E, F, I, UP, B, SIM) from the first feature. Because the codebase was small and fully typed from the start, strict mode passed immediately with no issues. The version retrospective explicitly noted this as a cross-theme learning: "Both themes adopted strict configurations from the outset... Retrofitting strictness later would have been harder."

#### Application

- Enable strict/comprehensive modes for type checkers and linters in the initial project setup, not as a later enhancement
- When adding a new quality tool, configure it at its strictest reasonable level immediately
- Treat quality tool strictness as a one-way ratchet — never relax rules once established

---

## LRN-003: Gate Integrator Pattern for Quality Themes

**Tags:** pattern, ci-cd, quality-gates, theme-design
**Source:** v001/02-quality-and-ci retrospective

### Content

#### Context

When a theme involves configuring multiple independent quality tools (linter, type checker, test framework), the individual tool configurations need an integration point to verify they work together.

#### Learning

Cap a quality-tooling theme with a CI/CD feature that combines all quality gates into a single workflow. This final feature acts as an integration test for all prior quality gate configurations, verifying they work together in an automated environment.

#### Evidence

In v001 Theme 02, features 001-003 individually configured ruff, mypy, and pytest. Feature 004 (GitHub Actions CI) combined all three into a single workflow. The theme retrospective noted: "Feature 004 (CI) was effectively an integration test of all three prior features, confirming they work together." This pattern caught no issues in v001, but its value is as a safety net for future changes.

#### Application

- When designing quality/tooling themes, plan a CI integration feature as the final deliverable
- The CI feature should run every quality gate configured in prior features
- This pattern provides a natural verification that independent tool configurations are compatible
- Consider this the "capstone" feature that proves the theme's deliverables work as a system

---

## LRN-004: Small Sequential Features for Foundational Work

**Tags:** pattern, feature-design, scaffolding, incremental-delivery
**Source:** v001 version retrospective

### Content

#### Context

When establishing a project foundation (scaffolding, build system, package structure), the work could be done as one large feature or broken into small sequential steps.

#### Learning

Break foundational work into 3-4 small, focused features with explicit sequential dependencies. Each feature should be independently verifiable with quality gates. This provides clear progression, easy rollback points, and independent verification at each step.

#### Evidence

v001 Theme 01 used a 3-feature pattern: build system (001) -> package structure (002) -> first module (003). Each feature was completed successfully with all quality gates green. The theme retrospective noted: "Sequential feature ordering with clear dependencies worked cleanly" and "Each feature was small, focused, and independently verifiable." Zero rework was required across all 7 features in the version.

#### Application

- For scaffolding themes, use the pattern: build system -> package structure -> first module
- For quality themes, use the pattern: linter -> type checker -> test framework -> CI
- Keep each feature to 2-4 acceptance criteria
- Ensure each feature can run quality gates independently after completion
- Use handoff documents between sequential features to maintain context continuity

---

## LRN-005: Configure Quality Tools Before Writing Tests

**Tags:** pattern, quality-gates, feature-ordering, theme-design
**Source:** v001/02-quality-and-ci retrospective

### Content

#### Context

When setting up a project's quality infrastructure, there is a question of ordering: configure tools first then write tests, or write tests alongside tool configuration.

#### Learning

Configure quality tools (linter, type checker) before writing the test framework and tests. This incremental approach means each tool validates its own configuration in isolation before tests add complexity. The test framework then benefits from already-configured linting and type checking.

#### Evidence

In v001 Theme 02, ruff was configured first (feature 001), then mypy (feature 002), then pytest with tests (feature 003). Each tool validated itself against the existing codebase before the next was added. The theme retrospective identified this as a discovered pattern: "Configuring quality tools before writing tests means each tool validates itself incrementally."

#### Application

- Order quality tool configuration features from least to most complex: formatter/linter -> type checker -> test framework
- Run each tool's quality gate after its configuration to validate the config in isolation
- Only write tests after the linter and type checker are configured, so tests are validated by all tools from creation
- Independent tool configurations (e.g., ruff and mypy) can optionally run in parallel if execution time is a concern

---

## LRN-006: Pytest Exit Code 5 Expected in Pre-Test Phases

**Tags:** debugging, pytest, quality-gates, automated-reporting
**Source:** v001/02-quality-and-ci/001-001-ruff-config completion-report

### Content

#### Context

When running quality gates across all features in a version — including features that precede test creation — pytest may return exit code 5 ("no tests collected").

#### Learning

Pytest exit code 5 (no tests collected) is expected behavior during scaffolding and tool-configuration features that precede test creation. Automated reporting systems should treat exit code 5 as a pass during these phases, not as a failure. Document this as a known pattern to prevent confusion.

#### Evidence

In v001, features 001-002 of Theme 01 and features 001-002 of Theme 02 all reported "pytest: no tests collected (exit code 5)." The completion reports correctly noted this as expected, but the Theme 02 retrospective flagged it as a potential improvement area: "pytest reported exit code 5... this is correct behavior but could confuse automated reporting if not handled as an expected result."

#### Application

- When designing quality gate checks for pre-test features, configure the check runner to accept exit code 5 as a pass
- In completion report templates, include guidance that exit code 5 is expected when no test files exist yet
- Consider adding a note in feature requirements when tests are intentionally out of scope for that feature
