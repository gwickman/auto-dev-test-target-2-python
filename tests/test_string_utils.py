"""Tests for the string_utils module."""

from test_target_2.string_utils import (
    camel_to_snake,
    slugify,
    snake_to_camel,
    title_case,
    truncate,
)

# --- slugify ---


def test_slugify_basic() -> None:
    """slugify converts simple string to lowercase hyphenated slug."""
    assert slugify("Hello World!") == "hello-world"


def test_slugify_empty_string() -> None:
    """slugify returns empty string for empty input."""
    assert slugify("") == ""


def test_slugify_unicode() -> None:
    """slugify handles Unicode via NFKD normalization."""
    assert slugify("Héllo Wörld") == "hello-world"


def test_slugify_multiple_spaces_and_hyphens() -> None:
    """slugify collapses multiple separators into single hyphen."""
    assert slugify("hello   world---foo") == "hello-world-foo"


def test_slugify_special_characters() -> None:
    """slugify strips special characters."""
    assert slugify("foo@bar#baz!") == "foo-bar-baz"


# --- truncate ---


def test_truncate_shorter_than_limit() -> None:
    """truncate returns original string if shorter than limit."""
    assert truncate("Hi", 10) == "Hi"


def test_truncate_at_limit() -> None:
    """truncate returns original string if exactly at limit."""
    assert truncate("Hello", 5) == "Hello"


def test_truncate_longer_than_limit() -> None:
    """truncate cuts string and appends suffix."""
    assert truncate("Hello World", 8) == "Hello..."


def test_truncate_custom_suffix() -> None:
    """truncate uses custom suffix."""
    assert truncate("Hello World", 8, suffix="~") == "Hello W~"


def test_truncate_empty_string() -> None:
    """truncate returns empty string for empty input."""
    assert truncate("", 5) == ""


# --- camel_to_snake ---


def test_camel_to_snake_basic() -> None:
    """camel_to_snake converts simple camelCase."""
    assert camel_to_snake("helloWorld") == "hello_world"


def test_camel_to_snake_pascal_case() -> None:
    """camel_to_snake converts PascalCase."""
    assert camel_to_snake("HelloWorld") == "hello_world"


def test_camel_to_snake_consecutive_capitals() -> None:
    """camel_to_snake handles consecutive capitals like HTMLParser."""
    assert camel_to_snake("HTMLParser") == "html_parser"


def test_camel_to_snake_consecutive_capitals_mid() -> None:
    """camel_to_snake handles consecutive capitals mid-string."""
    assert camel_to_snake("getHTTPSResponse") == "get_https_response"


def test_camel_to_snake_empty_string() -> None:
    """camel_to_snake returns empty string for empty input."""
    assert camel_to_snake("") == ""


def test_camel_to_snake_single_word() -> None:
    """camel_to_snake returns lowercase single word."""
    assert camel_to_snake("hello") == "hello"


# --- snake_to_camel ---


def test_snake_to_camel_basic() -> None:
    """snake_to_camel converts simple snake_case."""
    assert snake_to_camel("hello_world") == "helloWorld"


def test_snake_to_camel_leading_underscore() -> None:
    """snake_to_camel handles leading underscore."""
    assert snake_to_camel("_hello_world") == "helloWorld"


def test_snake_to_camel_trailing_underscore() -> None:
    """snake_to_camel handles trailing underscore."""
    assert snake_to_camel("hello_world_") == "helloWorld"


def test_snake_to_camel_double_underscore() -> None:
    """snake_to_camel handles double underscores."""
    assert snake_to_camel("hello__world") == "helloWorld"


def test_snake_to_camel_empty_string() -> None:
    """snake_to_camel returns empty string for empty input."""
    assert snake_to_camel("") == ""


def test_snake_to_camel_single_word() -> None:
    """snake_to_camel returns lowercase single word."""
    assert snake_to_camel("hello") == "hello"


# --- title_case ---


def test_title_case_basic() -> None:
    """title_case converts string to title case."""
    assert title_case("hello world") == "Hello World"


def test_title_case_empty_string() -> None:
    """title_case returns empty string for empty input."""
    assert title_case("") == ""


def test_title_case_already_titled() -> None:
    """title_case returns same string if already title-cased."""
    assert title_case("Hello World") == "Hello World"


def test_title_case_all_caps() -> None:
    """title_case converts ALL CAPS to title case."""
    assert title_case("HELLO WORLD") == "Hello World"
