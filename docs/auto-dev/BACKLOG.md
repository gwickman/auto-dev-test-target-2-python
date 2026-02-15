# Project Backlog

*Last updated: 2026-02-15 01:19*

**Total completed:** 6 | **Cancelled:** 0

## Priority Summary

| Priority | Name | Count |
|----------|------|-------|
| P0 | Critical | 0 |
| P1 | High | 3 |
| P2 | Medium | 7 |
| P3 | Low | 0 |

## Quick Reference

| ID | Pri | Size | Title | Description |
|----|-----|------|-------|-------------|
| <a id="bl-014-ref"></a>[BL-014](#bl-014) | P1 | m | Add Windows bash /dev/null guidance to AGENTS.md and nul to .gitignore | Add Windows bash null redirect guidance to AGENTS.md and ... |
| <a id="bl-015-ref"></a>[BL-015](#bl-015) | P1 | l | Add PR vs BL routing guidance to AGENTS.md (auto-dev-test-target-2-python) | AGENTS.md in the auto-dev-test-target-2-python project li... |
| <a id="bl-016-ref"></a>[BL-016](#bl-016) | P1 | l | Add WebFetch safety rules to AGENTS.md | Mirror of auto-dev-mcp BL-517. Add WebFetch safety block ... |
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
| agents-md | 3 | BL-014, BL-015, BL-016 |
| testing | 1 | BL-013 |
| windows | 1 | BL-014 |
| gitignore | 1 | BL-014 |
| product-requests | 1 | BL-015 |
| documentation | 1 | BL-015 |
| decision-framework | 1 | BL-015 |
| webfetch | 1 | BL-016 |
| safety | 1 | BL-016 |
| hang-prevention | 1 | BL-016 |

## Item Details

### P1: High

#### 📋 BL-014: Add Windows bash /dev/null guidance to AGENTS.md and nul to .gitignore

**Status:** open
**Tags:** windows, agents-md, gitignore

Add Windows bash null redirect guidance to AGENTS.md and add `nul` to .gitignore. In bash contexts on Windows: Always use `/dev/null` for output redirection (Git Bash correctly translates this to the Windows null device). Never use bare `nul` which gets interpreted as a literal filename in MSYS/Git Bash environments. Correct: `command > /dev/null 2>&1`. Wrong: `command > nul 2>&1`.

**Use Case:** This feature addresses: Add Windows bash /dev/null guidance to AGENTS.md and nul to .gitignore. It improves the system by resolving the described requirement.

[↑ Back to list](#bl-014-ref)

#### 📋 BL-015: Add PR vs BL routing guidance to AGENTS.md (auto-dev-test-target-2-python)

**Status:** open
**Tags:** agents-md, product-requests, documentation, decision-framework

AGENTS.md in the auto-dev-test-target-2-python project lists both add_product_request and add_backlog_item in the tool inventory but provides no guidance on when to use which. Claude Code sessions following AGENTS.md have no routing guidance for capturing ideas vs filing structured bugs.

The exploration pr-vs-bl-guidance on auto-dev-mcp (Gap 4) identified that AGENTS.md across all managed projects has zero PR vs BL routing guidance. Since AGENTS.md is the first document Claude Code reads in every session, it is the highest-leverage location for this guidance.

Without this, Claude Code defaults to add_backlog_item for all discoveries, bypassing the lightweight product request pathway entirely.

**Use Case:** During any Claude Code session on auto-dev-test-target-2-python, the agent reads AGENTS.md first. When it discovers an improvement opportunity mid-implementation, it currently has no guidance on whether to file a PR or BL. With this change, AGENTS.md tells it to default to product requests for ideas and reserve backlog items for structured problems.

**Acceptance Criteria:**
- [ ] AGENTS.md contains a section documenting when to create a Product Request vs a Backlog Item
- [ ] Section includes the maturity gradient: PR for ideas/observations, BL for structured problems with acceptance criteria
- [ ] Section includes the default rule: when in doubt, start with a Product Request
- [ ] Section cross-references add_product_request and add_backlog_item tool_help for detailed guidance

**Notes:** Mirror of BL-510 (auto-dev-mcp). Keep the AGENTS.md addition concise — 3-5 lines max. Content should be identical across all managed projects for consistency.

[↑ Back to list](#bl-015-ref)

#### 📋 BL-016: Add WebFetch safety rules to AGENTS.md

**Status:** open
**Tags:** agents-md, webfetch, safety, hang-prevention

Mirror of auto-dev-mcp BL-517. Add WebFetch safety block to AGENTS.md. Exact text:

## WebFetch Safety (mandatory)
- NEVER WebFetch a URL you generated from memory — only WebFetch URLs returned by WebSearch
- Prefer WebSearch over WebFetch for research
- MANDATORY: Before every WebFetch call you MUST run: curl -sL --max-time 10 -o /dev/null -w "%{http_code}" &lt;url&gt; and ONLY proceed with WebFetch if curl returns 2xx/3xx

**Use Case:** Same as BL-517: prevent WebFetch hangs from freezing sessions by requiring URL verification before every WebFetch call.

**Acceptance Criteria:**
- [ ] AGENTS.md contains a '## WebFetch Safety (mandatory)' section with all 3 rules verbatim
- [ ] The section is placed near top-level instructions, not buried at the end
- [ ] No other changes to AGENTS.md beyond the insertion

[↑ Back to list](#bl-016-ref)

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
