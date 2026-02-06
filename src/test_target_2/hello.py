"""Hello module — minimal utility for quality gate validation."""


def hello(name: str = "World") -> str:
    """Return a greeting string.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
