"""Collection utilities — chunk, flatten, unique_by, group_by, partition, compact."""

from collections.abc import Callable, Iterable, Sequence
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K")


def chunk(items: Sequence[T], size: int) -> list[list[T]]:
    """Split a sequence into chunks of specified size.

    Args:
        items: The sequence to split.
        size: Maximum number of items per chunk.

    Returns:
        A list of lists, where the last chunk may be smaller than size.
    """
    return [list(items[i : i + size]) for i in range(0, len(items), size)]


def flatten(items: Iterable[Iterable[T]]) -> list[T]:
    """Flatten a single level of nesting from an iterable of iterables.

    Args:
        items: An iterable of iterables to flatten.

    Returns:
        A single flat list.
    """
    result: list[T] = []
    for sub in items:
        result.extend(sub)
    return result


def unique_by(items: Iterable[T], key: Callable[[T], object]) -> list[T]:
    """Return unique items determined by a key function, preserving order.

    Args:
        items: The items to deduplicate.
        key: Function to compute a hashable key for each item.

    Returns:
        A list of unique items in original order.
    """
    seen: set[object] = set()
    result: list[T] = []
    for item in items:
        k = key(item)
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result


def group_by(items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    """Group items by a key function into a dict of lists.

    Args:
        items: The items to group.
        key: Function to compute the grouping key.

    Returns:
        A dict mapping keys to lists of items, preserving order within groups.
    """
    result: dict[K, list[T]] = {}
    for item in items:
        k = key(item)
        result.setdefault(k, []).append(item)
    return result


def partition(
    items: Iterable[T], predicate: Callable[[T], bool]
) -> tuple[list[T], list[T]]:
    """Split items into two lists based on a predicate.

    Args:
        items: The items to partition.
        predicate: Function returning True for the first group.

    Returns:
        A tuple of (true_items, false_items).
    """
    true_items: list[T] = []
    false_items: list[T] = []
    for item in items:
        if predicate(item):
            true_items.append(item)
        else:
            false_items.append(item)
    return true_items, false_items


def compact(items: Iterable[T | None]) -> list[T]:
    """Remove None values from an iterable.

    Args:
        items: An iterable that may contain None values.

    Returns:
        A list with all None values removed.
    """
    return [item for item in items if item is not None]
