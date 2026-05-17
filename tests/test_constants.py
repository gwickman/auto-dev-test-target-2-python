"""Tests for test_target_2.constants module."""

from test_target_2 import constants


def test_default_hello_target_value() -> None:
    """Test that DEFAULT_HELLO_TARGET has the expected value."""
    assert constants.DEFAULT_HELLO_TARGET == "world"


def test_default_hello_target_type() -> None:
    """Test that DEFAULT_HELLO_TARGET is a string."""
    assert isinstance(constants.DEFAULT_HELLO_TARGET, str)


def test_constants_module_importable() -> None:
    """Test that constants module can be imported from package."""
    # Import succeeds at module scope; this test verifies the object exists
    assert hasattr(constants, "DEFAULT_HELLO_TARGET")


def test_default_farewell_value() -> None:
    assert constants.DEFAULT_FAREWELL == "goodbye"


def test_default_farewell_type() -> None:
    assert isinstance(constants.DEFAULT_FAREWELL, str)


def test_default_language_value() -> None:
    """DEFAULT_LANGUAGE has expected value."""
    assert constants.DEFAULT_LANGUAGE == "en"


def test_default_language_type() -> None:
    """DEFAULT_LANGUAGE is string type."""
    assert isinstance(constants.DEFAULT_LANGUAGE, str)


def test_default_region_value() -> None:
    assert constants.DEFAULT_REGION == "us"


def test_default_region_type() -> None:
    assert isinstance(constants.DEFAULT_REGION, str)


def test_default_currency_value() -> None:
    assert constants.DEFAULT_CURRENCY == "usd"


def test_default_currency_type() -> None:
    assert isinstance(constants.DEFAULT_CURRENCY, str)
