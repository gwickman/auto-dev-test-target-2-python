# Changelog

All notable changes to this project will be documented in this file.

## v008 (2026-05-17)

- **BL-023:** Add DEFAULT_CURRENCY constant to constants module
  - Add `DEFAULT_CURRENCY: str = "usd"` to `src/test_target_2/constants.py`
  - Add `test_default_currency_value()` and `test_default_currency_type()` to `tests/test_constants.py`
  - All quality gates pass (ruff, mypy --strict, pytest)

## [v007] - 2026-05-14

### Added
- `DEFAULT_REGION: str = "us"` constant to `constants` module (BL-022)
- Test functions `test_default_region_value` and `test_default_region_type` in `test_constants.py`

## [v006] - 2026-05-14

### Added
- `DEFAULT_LANGUAGE: str = "en"` constant to `constants` module (BL-020)
- Test functions `test_default_language_value` and `test_default_language_type` in `test_constants.py`

## [v005] - 2026-05-13

### Added
- `DEFAULT_FAREWELL: str = "goodbye"` constant to `constants` module (BL-019)
- Test functions `test_default_farewell_value` and `test_default_farewell_type` in `test_constants.py`

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
