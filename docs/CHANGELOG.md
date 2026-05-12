# Changelog

All notable changes to this project will be documented in this file.

## [v004] - 2026-05-12

### Added
- `constants` module with `DEFAULT_HELLO_TARGET: str = "world"` package-level constant (BL-018)
- `test_constants.py` with value, type, and importability assertions
- Module re-export in `__init__.py`

## [v002] - 2026-03-06

### Added
- `string_utils` module with slugify, truncate, case conversion (snake_case, camelCase, PascalCase), and more (BL-007)
- `math_utils` module with clamp, lerp, safe_divide, remap, and more (BL-008)
- `collection_utils` module with chunk, flatten, unique_by, group_by, partition, compact (BL-009)
- Module-level re-exports in `__init__.py` for string_utils, math_utils, and collection_utils
- Version bump to 0.2.0

## [v001] - 2026-02-06

### Added
- Project scaffolding with uv build backend and src-layout package structure
- `test_target_2` package with typed `hello()` function
- Ruff linting and formatting configuration (E, F, I, UP, B, SIM rule sets)
- Mypy strict mode with Python 3.11 target
- Pytest setup with importlib mode and 4 unit tests for hello module
- GitHub Actions CI workflow running ruff, mypy, and pytest on push/PR
