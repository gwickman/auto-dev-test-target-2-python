## Context

When building a project incrementally across multiple features, later features often depend on structural prerequisites (directories, package files, configuration) that are formally delivered by earlier features.

## Learning

Create minimal structural placeholders in early features so that build tools, quality gates, and dependency managers can run successfully from the very first feature onward. The placeholder will be populated with real content by the feature that formally owns it.

## Evidence

In v001, feature 001 (pyproject-init) needed to create an empty `src/test_target_2/__init__.py` because the `uv_build` backend requires the src-layout package to exist for `uv sync` to succeed. Feature 002 then formally populated that file with version metadata. This allowed quality gates (ruff, mypy) to run green from feature 001 onward rather than failing until feature 002 was complete.

## Application

- When designing feature sequences, identify structural prerequisites that downstream features and tooling depend on
- Create minimal placeholders in the earliest possible feature rather than deferring until the feature that formally owns that artifact
- Document the placeholder relationship so future developers understand why a file exists before its "real" feature