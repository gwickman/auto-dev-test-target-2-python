"""String utilities — slugify, truncate, and case conversion functions."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert arbitrary string to URL-safe slug.

    Args:
        text: The string to slugify.

    Returns:
        A lowercase, hyphen-separated slug.
    """
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text)
    slug = slug.strip("-").lower()
    return slug


def truncate(text: str, length: int, suffix: str = "...") -> str:
    """Truncate string to exact length including suffix.

    Args:
        text: The string to truncate.
        length: Maximum total length (including suffix).
        suffix: The suffix to append when truncating. Defaults to "...".

    Returns:
        The truncated string, or the original if shorter than length.
    """
    if len(text) <= length:
        return text
    return text[: length - len(suffix)] + suffix


def camel_to_snake(text: str) -> str:
    """Convert camelCase or PascalCase to snake_case.

    Args:
        text: The camelCase or PascalCase string.

    Returns:
        The snake_case equivalent.
    """
    # Two-pass regex: handle consecutive capitals then normal boundaries
    result = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", text)
    result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", result)
    return result.lower()


def snake_to_camel(text: str) -> str:
    """Convert snake_case to camelCase.

    Args:
        text: The snake_case string.

    Returns:
        The camelCase equivalent (first word lowercase).
    """
    parts = text.split("_")
    # Filter out empty parts from leading/trailing/double underscores
    parts = [p for p in parts if p]
    if not parts:
        return ""
    return parts[0].lower() + "".join(word.capitalize() for word in parts[1:])


def title_case(text: str) -> str:
    """Convert string to title case.

    Args:
        text: The string to convert.

    Returns:
        The title-cased string.
    """
    return text.title()
