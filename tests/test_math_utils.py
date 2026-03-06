"""Tests for the math_utils module."""

import math

from test_target_2.math_utils import (
    clamp,
    is_close,
    lerp,
    percentage,
    round_to,
    safe_divide,
)

# --- clamp ---


def test_clamp_within_range() -> None:
    """clamp returns value unchanged when within range."""
    assert clamp(5.0, 0.0, 10.0) == 5.0


def test_clamp_below_min() -> None:
    """clamp returns min_val when value is below range."""
    assert clamp(-5.0, 0.0, 10.0) == 0.0


def test_clamp_above_max() -> None:
    """clamp returns max_val when value is above range."""
    assert clamp(15.0, 0.0, 10.0) == 10.0


def test_clamp_min_equals_max() -> None:
    """clamp returns the bound when min equals max."""
    assert clamp(5.0, 3.0, 3.0) == 3.0


def test_clamp_nan_input() -> None:
    """clamp with NaN input returns min_val due to Python min/max NaN semantics."""
    result = clamp(float("nan"), 0.0, 10.0)
    assert result == 0.0


def test_clamp_infinity_input() -> None:
    """clamp with positive infinity returns max_val."""
    assert clamp(float("inf"), 0.0, 10.0) == 10.0


def test_clamp_negative_infinity_input() -> None:
    """clamp with negative infinity returns min_val."""
    assert clamp(float("-inf"), 0.0, 10.0) == 0.0


# --- lerp ---


def test_lerp_at_zero() -> None:
    """lerp at t=0.0 returns start value."""
    assert lerp(0.0, 10.0, 0.0) == 0.0


def test_lerp_at_half() -> None:
    """lerp at t=0.5 returns midpoint."""
    assert lerp(0.0, 10.0, 0.5) == 5.0


def test_lerp_at_one() -> None:
    """lerp at t=1.0 returns end value."""
    assert lerp(0.0, 10.0, 1.0) == 10.0


def test_lerp_beyond_one() -> None:
    """lerp at t>1.0 extrapolates beyond end."""
    assert lerp(0.0, 10.0, 1.5) == 15.0


def test_lerp_nan_input() -> None:
    """lerp with NaN t propagates NaN."""
    result = lerp(0.0, 10.0, float("nan"))
    assert math.isnan(result)


# --- round_to ---


def test_round_to_positive_decimals() -> None:
    """round_to rounds to specified positive decimal places."""
    assert round_to(3.14159, 2) == 3.14


def test_round_to_zero_decimals() -> None:
    """round_to with zero decimals rounds to integer."""
    assert round_to(3.7, 0) == 4.0


def test_round_to_negative_decimals() -> None:
    """round_to with negative decimals rounds to tens/hundreds."""
    assert round_to(1234.0, -2) == 1200.0


def test_round_to_nan_input() -> None:
    """round_to with NaN input returns NaN."""
    result = round_to(float("nan"), 2)
    assert math.isnan(result)


# --- is_close ---


def test_is_close_equal_values() -> None:
    """is_close returns True for equal values."""
    assert is_close(1.0, 1.0) is True


def test_is_close_close_values() -> None:
    """is_close returns True for approximately equal values."""
    assert is_close(0.1 + 0.2, 0.3) is True


def test_is_close_not_close() -> None:
    """is_close returns False for distant values."""
    assert is_close(1.0, 2.0) is False


def test_is_close_nan_comparison() -> None:
    """is_close returns False when comparing NaN."""
    assert is_close(float("nan"), float("nan")) is False


def test_is_close_infinity_comparison() -> None:
    """is_close returns True for matching infinities."""
    assert is_close(float("inf"), float("inf")) is True


def test_is_close_custom_tolerance() -> None:
    """is_close respects custom absolute tolerance."""
    assert is_close(1.0, 1.05, abs_tol=0.1) is True


# --- percentage ---


def test_percentage_normal() -> None:
    """percentage computes correct percentage."""
    assert percentage(25.0, 200.0) == 12.5


def test_percentage_negative_values() -> None:
    """percentage works with negative part."""
    assert percentage(-25.0, 100.0) == -25.0


def test_percentage_nan_input() -> None:
    """percentage with NaN input propagates NaN."""
    result = percentage(float("nan"), 100.0)
    assert math.isnan(result)


def test_percentage_infinity_total() -> None:
    """percentage with infinity total returns 0.0."""
    assert percentage(25.0, float("inf")) == 0.0


# --- safe_divide ---


def test_safe_divide_normal() -> None:
    """safe_divide performs normal division."""
    assert safe_divide(10.0, 2.0) == 5.0


def test_safe_divide_by_zero_default() -> None:
    """safe_divide returns 0.0 on division by zero."""
    assert safe_divide(10.0, 0.0) == 0.0


def test_safe_divide_by_zero_custom_default() -> None:
    """safe_divide returns custom default on division by zero."""
    assert safe_divide(10.0, 0.0, default=-1.0) == -1.0


def test_safe_divide_nan_numerator() -> None:
    """safe_divide with NaN numerator propagates NaN."""
    result = safe_divide(float("nan"), 2.0)
    assert math.isnan(result)


def test_safe_divide_inf_numerator() -> None:
    """safe_divide with inf numerator returns inf."""
    assert safe_divide(float("inf"), 2.0) == float("inf")
