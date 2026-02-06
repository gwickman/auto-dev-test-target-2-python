"""Tests for the hello module."""

from test_target_2.hello import hello


def test_hello_default() -> None:
    """hello() with default argument returns greeting with World."""
    assert hello() == "Hello, World!"


def test_hello_custom_name() -> None:
    """hello() with custom name returns personalized greeting."""
    assert hello("Alice") == "Hello, Alice!"


def test_hello_returns_string() -> None:
    """hello() returns a string."""
    result = hello()
    assert isinstance(result, str)


def test_hello_importable() -> None:
    """hello is importable from test_target_2.hello."""
    from test_target_2.hello import hello as h

    assert callable(h)
