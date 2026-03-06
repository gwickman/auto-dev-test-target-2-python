"""Tests for the collection_utils module."""

from dataclasses import dataclass

from test_target_2.collection_utils import (
    chunk,
    compact,
    flatten,
    group_by,
    partition,
    unique_by,
)

# --- chunk ---


def test_chunk_even_division() -> None:
    """chunk splits evenly divisible list."""
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunk_uneven_remainder() -> None:
    """chunk handles remainder in last chunk."""
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_size_greater_than_list() -> None:
    """chunk returns single chunk when size exceeds list length."""
    assert chunk([1, 2, 3], 10) == [[1, 2, 3]]


def test_chunk_size_one() -> None:
    """chunk with size 1 wraps each element."""
    assert chunk([1, 2, 3], 1) == [[1], [2], [3]]


def test_chunk_empty_list() -> None:
    """chunk returns empty list for empty input."""
    assert chunk([], 3) == []


# --- flatten ---


def test_flatten_nested_lists() -> None:
    """flatten merges nested lists into one."""
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_flatten_empty_outer() -> None:
    """flatten returns empty list for empty input."""
    assert flatten([]) == []


def test_flatten_empty_inner() -> None:
    """flatten handles empty inner iterables."""
    assert flatten([[], [1], []]) == [1]


def test_flatten_single_level_only() -> None:
    """flatten only removes one level of nesting."""
    result = flatten([[[1, 2]], [[3]]])
    assert result == [[1, 2], [3]]


# --- unique_by ---


def test_unique_by_identity() -> None:
    """unique_by with identity key removes duplicates."""
    assert unique_by([1, 2, 3, 2, 1], lambda x: x) == [1, 2, 3]


def test_unique_by_preserves_order() -> None:
    """unique_by preserves first occurrence order."""
    assert unique_by([3, 1, 2, 1, 3], lambda x: x) == [3, 1, 2]


def test_unique_by_key_function() -> None:
    """unique_by deduplicates by key function result."""
    assert unique_by(["hello", "HELLO", "world"], lambda s: s.lower()) == [
        "hello",
        "world",
    ]


def test_unique_by_all_same_key() -> None:
    """unique_by returns first item when all keys are the same."""
    assert unique_by([1, 2, 3], lambda x: "same") == [1]


def test_unique_by_empty() -> None:
    """unique_by returns empty list for empty input."""
    assert unique_by([], lambda x: x) == []


# --- group_by ---


def test_group_by_modulo() -> None:
    """group_by groups integers by modulo."""
    assert group_by([1, 2, 3, 4], lambda x: x % 2) == {1: [1, 3], 0: [2, 4]}


def test_group_by_single_group() -> None:
    """group_by with constant key produces one group."""
    assert group_by([1, 2, 3], lambda x: "all") == {"all": [1, 2, 3]}


def test_group_by_preserves_order_within_groups() -> None:
    """group_by preserves insertion order within groups."""
    result = group_by([4, 1, 3, 2], lambda x: x % 2)
    assert result[0] == [4, 2]
    assert result[1] == [1, 3]


def test_group_by_string_key() -> None:
    """group_by works with string keys."""
    result = group_by(["apple", "avocado", "banana"], lambda s: s[0])
    assert result == {"a": ["apple", "avocado"], "b": ["banana"]}


def test_group_by_empty() -> None:
    """group_by returns empty dict for empty input."""
    assert group_by([], lambda x: x) == {}


# --- partition ---


def test_partition_even_odd() -> None:
    """partition splits by even/odd predicate."""
    assert partition([1, 2, 3, 4], lambda x: x % 2 == 0) == ([2, 4], [1, 3])


def test_partition_all_true() -> None:
    """partition puts all items in first list when all match."""
    assert partition([2, 4, 6], lambda x: x % 2 == 0) == ([2, 4, 6], [])


def test_partition_all_false() -> None:
    """partition puts all items in second list when none match."""
    assert partition([1, 3, 5], lambda x: x % 2 == 0) == ([], [1, 3, 5])


def test_partition_empty() -> None:
    """partition returns two empty lists for empty input."""
    assert partition([], lambda x: x) == ([], [])


# --- compact ---


def test_compact_removes_none() -> None:
    """compact removes None values."""
    assert compact([1, None, 2, None, 3]) == [1, 2, 3]


def test_compact_no_none() -> None:
    """compact returns same list when no None present."""
    assert compact([1, 2, 3]) == [1, 2, 3]


def test_compact_all_none() -> None:
    """compact returns empty list when all are None."""
    assert compact([None, None, None]) == []


def test_compact_empty() -> None:
    """compact returns empty list for empty input."""
    assert compact([]) == []


def test_compact_preserves_falsy_values() -> None:
    """compact keeps falsy values like 0 and empty string."""
    assert compact([0, None, "", None, False]) == [0, "", False]


# --- type safety with dataclass ---


def test_chunk_with_strings() -> None:
    """chunk works with string sequences."""
    assert chunk(["a", "b", "c"], 2) == [["a", "b"], ["c"]]


def test_group_by_with_dataclass() -> None:
    """group_by works with dataclass items."""

    @dataclass
    class Item:
        name: str
        category: str

    items = [Item("a", "x"), Item("b", "y"), Item("c", "x")]
    result = group_by(items, lambda i: i.category)
    assert len(result["x"]) == 2
    assert len(result["y"]) == 1
