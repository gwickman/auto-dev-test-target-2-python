# Project Backlog

*Last updated: 2026-02-06 18:58*

**Total completed:** 6 | **Cancelled:** 0

## Priority Summary

| Priority | Name | Count |
|----------|------|-------|
| P0 | Critical | 0 |
| P1 | High | 0 |
| P2 | Medium | 7 |
| P3 | Low | 0 |

## Quick Reference

| ID | Pri | Size | Title | Description |
|----|-----|------|-------|-------------|
| <a id="bl-007-ref"></a>[BL-007](#bl-007) | P2 | m | String utilities module (slugify, truncate, case_convert, etc.) | Create src/test_target_2/string_utils.py with idiomatic P... |
| <a id="bl-008-ref"></a>[BL-008](#bl-008) | P2 | m | Math/number utilities module (clamp, lerp, round_to, is_close, etc.) | Create src/test_target_2/math_utils.py with numeric utili... |
| <a id="bl-009-ref"></a>[BL-009](#bl-009) | P2 | m | Collection utilities module (chunk, flatten, unique_by, group_by, etc.) | Create src/test_target_2/collection_utils.py with collect... |
| <a id="bl-010-ref"></a>[BL-010](#bl-010) | P2 | m | Custom exception hierarchy (ValidationError, NotFoundError, etc.) | Create src/test_target_2/exceptions.py with a custom exce... |
| <a id="bl-011-ref"></a>[BL-011](#bl-011) | P2 | m | Input validation functions (validate_range, validate_non_empty, validate_type, etc.) | Create src/test_target_2/validators.py with reusable inpu... |
| <a id="bl-012-ref"></a>[BL-012](#bl-012) | P2 | m | Retrofit validation into existing v002 utility functions | Add input validation to existing string_utils, math_utils... |
| <a id="bl-013-ref"></a>[BL-013](#bl-013) | P2 | m | Property-based testing with Hypothesis for edge case coverage | Add Hypothesis as a dev dependency and create property-ba... |

## Tags Summary

| Tag | Count | Items |
|-----|-------|-------|
| v003 | 4 | BL-010, BL-011, BL-012, BL-013 |
| validation | 4 | BL-010, BL-011, BL-012, BL-013 |
| v002 | 3 | BL-007, BL-008, BL-009 |
| utility | 3 | BL-007, BL-008, BL-009 |
| testing | 1 | BL-013 |

## Item Details

### P2: Medium

#### 📋 BL-007: String utilities module (slugify, truncate, case_convert, etc.)

**Status:** open
**Tags:** v002, utility

Create src/test_target_2/string_utils.py with idiomatic Python string manipulation functions: slugify, truncate, camel_to_snake, snake_to_camel, title_case, capitalize_words, etc. Full test coverage in tests/test_string_utils.py.

**Use Case:** This feature addresses: String utilities module (slugify, truncate, case_convert, etc.). It improves the system by resolving the described requirement.

**Acceptance Criteria:**
- [ ] string_utils.py exists with at least 5 string utility functions
- [ ] All functions have type annotations and docstrings
- [ ] tests/test_string_utils.py exists with comprehensive test coverage
- [ ] All tests pass, ruff and mypy clean

[↑ Back to list](#bl-007-ref)

#### 📋 BL-008: Math/number utilities module (clamp, lerp, round_to, is_close, etc.)

**Status:** open
**Tags:** v002, utility

Create src/test_target_2/math_utils.py with numeric utility functions: clamp, lerp, round_to, is_close, percentage, safe_divide, etc. Full test coverage in tests/test_math_utils.py.

**Use Case:** This feature addresses: Math/number utilities module (clamp, lerp, round_to, is_close, etc.). It improves the system by resolving the described requirement.

**Acceptance Criteria:**
- [ ] math_utils.py exists with at least 5 math utility functions
- [ ] All functions have type annotations and docstrings
- [ ] tests/test_math_utils.py exists with comprehensive test coverage
- [ ] Edge cases (division by zero, overflow) are handled and tested

[↑ Back to list](#bl-008-ref)

#### 📋 BL-009: Collection utilities module (chunk, flatten, unique_by, group_by, etc.)

**Status:** open
**Tags:** v002, utility

Create src/test_target_2/collection_utils.py with collection manipulation functions: chunk, flatten, unique_by, group_by, partition, compact, take, drop, etc. Full test coverage in tests/test_collection_utils.py.

**Use Case:** This feature addresses: Collection utilities module (chunk, flatten, unique_by, group_by, etc.). It improves the system by resolving the described requirement.

**Acceptance Criteria:**
- [ ] collection_utils.py exists with at least 6 collection utility functions
- [ ] Functions use generics/TypeVar for type safety
- [ ] tests/test_collection_utils.py exists with comprehensive test coverage
- [ ] All tests pass, ruff and mypy clean

[↑ Back to list](#bl-009-ref)

#### 📋 BL-010: Custom exception hierarchy (ValidationError, NotFoundError, etc.)

**Status:** open
**Tags:** v003, validation

Create src/test_target_2/exceptions.py with a custom exception hierarchy: base TestTarget2Error, plus ValidationError, NotFoundError, ConfigError, etc. Use dataclass-style attributes for structured error context.

**Use Case:** This feature addresses: Custom exception hierarchy (ValidationError, NotFoundError, etc.). It improves the system by resolving the described requirement.

**Acceptance Criteria:**
- [ ] exceptions.py exists with base error and at least 3 specific error types
- [ ] Exceptions carry structured context (field name, invalid value, etc.)
- [ ] tests/test_exceptions.py validates error construction and inheritance
- [ ] All quality gates pass

[↑ Back to list](#bl-010-ref)

#### 📋 BL-011: Input validation functions (validate_range, validate_non_empty, validate_type, etc.)

**Status:** open
**Tags:** v003, validation

Create src/test_target_2/validators.py with reusable input validation functions: validate_range, validate_non_empty, validate_type, validate_pattern, validate_length, etc. Raise custom exceptions from exceptions.py on failure.

**Use Case:** This feature addresses: Input validation functions (validate_range, validate_non_empty, validate_type, etc.). It improves the system by resolving the described requirement.

**Acceptance Criteria:**
- [ ] validators.py exists with at least 5 validation functions
- [ ] Validators raise appropriate custom exceptions
- [ ] tests/test_validators.py covers both valid and invalid inputs
- [ ] All quality gates pass

[↑ Back to list](#bl-011-ref)

#### 📋 BL-012: Retrofit validation into existing v002 utility functions

**Status:** open
**Tags:** v003, validation

Add input validation to existing string_utils, math_utils, and collection_utils functions using the validators module. Functions should raise ValidationError for invalid inputs instead of silently failing or returning unexpected results.

**Use Case:** This feature addresses: Retrofit validation into existing v002 utility functions. It improves the system by resolving the described requirement.

**Acceptance Criteria:**
- [ ] Existing utility functions validate their inputs
- [ ] Invalid inputs raise ValidationError with descriptive messages
- [ ] Existing tests still pass (non-breaking for valid inputs)
- [ ] New tests cover validation error cases

[↑ Back to list](#bl-012-ref)

#### 📋 BL-013: Property-based testing with Hypothesis for edge case coverage

**Status:** open
**Tags:** v003, validation, testing

Add Hypothesis as a dev dependency and create property-based tests for utility functions. Focus on invariants: e.g., clamp always returns within bounds, slugify output is always URL-safe, chunk preserves all elements, etc.

**Use Case:** This feature addresses: Property-based testing with Hypothesis for edge case coverage. It improves the system by resolving the described requirement.

**Acceptance Criteria:**
- [ ] hypothesis is listed as a dev dependency
- [ ] tests/test_properties.py exists with property-based tests
- [ ] At least 5 properties are tested across different utility modules
- [ ] All tests pass including hypothesis-generated cases

[↑ Back to list](#bl-013-ref)
