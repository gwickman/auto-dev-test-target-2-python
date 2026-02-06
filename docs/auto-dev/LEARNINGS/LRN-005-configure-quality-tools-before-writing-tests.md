## Context

When setting up a project's quality infrastructure, there is a question of ordering: configure tools first then write tests, or write tests alongside tool configuration.

## Learning

Configure quality tools (linter, type checker) before writing the test framework and tests. This incremental approach means each tool validates its own configuration in isolation before tests add complexity. The test framework then benefits from already-configured linting and type checking.

## Evidence

In v001 Theme 02, ruff was configured first (feature 001), then mypy (feature 002), then pytest with tests (feature 003). Each tool validated itself against the existing codebase before the next was added. The theme retrospective identified this as a discovered pattern: "Configuring quality tools before writing tests means each tool validates itself incrementally."

## Application

- Order quality tool configuration features from least to most complex: formatter/linter -> type checker -> test framework
- Run each tool's quality gate after its configuration to validate the config in isolation
- Only write tests after the linter and type checker are configured, so tests are validated by all tools from creation
- Independent tool configurations (e.g., ruff and mypy) can optionally run in parallel if execution time is a concern