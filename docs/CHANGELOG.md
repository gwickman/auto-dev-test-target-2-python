# Changelog

All notable changes to this project will be documented in this file.

## [v001] - 2026-02-06

### Added
- Project scaffolding with uv build backend and src-layout package structure
- `test_target_2` package with typed `hello()` function
- Ruff linting and formatting configuration (E, F, I, UP, B, SIM rule sets)
- Mypy strict mode with Python 3.11 target
- Pytest setup with importlib mode and 4 unit tests for hello module
- GitHub Actions CI workflow running ruff, mypy, and pytest on push/PR
