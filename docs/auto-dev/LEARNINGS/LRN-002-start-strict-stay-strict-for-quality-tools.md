## Context

When setting up quality tools (linters, type checkers, formatters) for a new project, there is a choice between starting with relaxed defaults and tightening later, or starting strict from the outset.

## Learning

Adopt strict configurations for all quality tools from the very beginning of a project. Starting strict is painless when the codebase is small, but retrofitting strictness onto a permissive codebase accumulates tech debt that is harder to resolve later.

## Evidence

In v001, mypy was configured with `strict = true` and ruff was configured with broad rule sets (E, F, I, UP, B, SIM) from the first feature. Because the codebase was small and fully typed from the start, strict mode passed immediately with no issues. The version retrospective explicitly noted this as a cross-theme learning: "Both themes adopted strict configurations from the outset... Retrofitting strictness later would have been harder."

## Application

- Enable strict/comprehensive modes for type checkers and linters in the initial project setup, not as a later enhancement
- When adding a new quality tool, configure it at its strictest reasonable level immediately
- Treat quality tool strictness as a one-way ratchet — never relax rules once established