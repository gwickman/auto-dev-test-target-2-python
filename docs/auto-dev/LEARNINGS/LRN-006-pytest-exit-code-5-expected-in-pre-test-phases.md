## Context

When running quality gates across all features in a version — including features that precede test creation — pytest may return exit code 5 ("no tests collected").

## Learning

Pytest exit code 5 (no tests collected) is expected behavior during scaffolding and tool-configuration features that precede test creation. Automated reporting systems should treat exit code 5 as a pass during these phases, not as a failure. Document this as a known pattern to prevent confusion.

## Evidence

In v001, features 001-002 of Theme 01 and features 001-002 of Theme 02 all reported "pytest: no tests collected (exit code 5)." The completion reports correctly noted this as expected, but the Theme 02 retrospective flagged it as a potential improvement area: "pytest reported exit code 5... this is correct behavior but could confuse automated reporting if not handled as an expected result."

## Application

- When designing quality gate checks for pre-test features, configure the check runner to accept exit code 5 as a pass
- In completion report templates, include guidance that exit code 5 is expected when no test files exist yet
- Consider adding a note in feature requirements when tests are intentionally out of scope for that feature