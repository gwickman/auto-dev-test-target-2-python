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
