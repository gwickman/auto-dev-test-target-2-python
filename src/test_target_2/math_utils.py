"""Math utilities — clamp, lerp, round_to, is_close, percentage, safe_divide."""

import math


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value to a [min_val, max_val] range.

    Args:
        value: The value to clamp.
        min_val: The minimum bound.
        max_val: The maximum bound.

    Returns:
        The clamped value. NaN input propagates naturally (IEEE 754).
    """
    return max(min_val, min(value, max_val))


def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolation between two values.

    Args:
        a: Start value.
        b: End value.
        t: Interpolation factor (0.0 returns a, 1.0 returns b).

    Returns:
        The interpolated value. NaN input propagates naturally.
    """
    return a + (b - a) * t


def round_to(value: float, decimals: int) -> float:
    """Round a number to specified decimal places.

    Uses Python built-in ``round()`` (banker's rounding).

    Args:
        value: The number to round.
        decimals: Number of decimal places.

    Returns:
        The rounded value. NaN input propagates naturally.
    """
    return float(round(value, decimals))


def is_close(
    a: float,
    b: float,
    rel_tol: float = 1e-09,
    abs_tol: float = 0.0,
) -> bool:
    """Check if two floats are approximately equal.

    Wraps ``math.isclose`` with simpler interface. Returns ``False`` for NaN
    comparisons and ``True`` for matching infinities.

    Args:
        a: First value.
        b: Second value.
        rel_tol: Relative tolerance.
        abs_tol: Absolute tolerance.

    Returns:
        True if the values are close, False otherwise.
    """
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def percentage(part: float, total: float) -> float:
    """Calculate percentage: ``(part / total) * 100``.

    Args:
        part: The part value.
        total: The total value.

    Returns:
        The percentage. NaN input propagates naturally.
    """
    return (part / total) * 100.0


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safe division with default on division by zero.

    Args:
        numerator: The dividend.
        denominator: The divisor.
        default: Value returned when denominator is zero. Defaults to 0.0.

    Returns:
        The quotient, or default if denominator is zero.
        NaN/inf numerator propagates through division.
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return default
