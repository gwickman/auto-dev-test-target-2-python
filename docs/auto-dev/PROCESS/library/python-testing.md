# Python Testing Standards

## Test Structure

```
tests/
├── conftest.py          # Shared fixtures
├── test_*.py            # Unit tests
└── integration/
    └── test_*.py        # Integration tests
```

## Tools

- **pytest** - Test runner
- **pytest-cov** - Coverage
- **pytest-asyncio** - Async support

## Commands

```bash
# Run all tests
uv run pytest

# With coverage
uv run pytest --cov --cov-report=term-missing

# Specific file
uv run pytest tests/test_specific.py -v

# Stop on first failure
uv run pytest -x

# Run only last failed
uv run pytest --lf
```

## Coverage Target

Maintain ≥90% coverage.

## Test Patterns

### Basic Test Structure

```python
"""Tests for module."""

import pytest
from my_module import MyClass


class TestMyClass:
    """Tests for MyClass."""

    def test_basic_functionality(self) -> None:
        """Test basic case."""
        instance = MyClass()
        result = instance.method()
        assert result == expected

    def test_edge_case(self) -> None:
        """Test edge case."""
        instance = MyClass()
        with pytest.raises(ValueError):
            instance.invalid_method()
```

### Fixtures

```python
@pytest.fixture
def sample_data() -> dict:
    """Provide sample data."""
    return {"key": "value"}

def test_with_fixture(sample_data: dict) -> None:
    """Test using fixture."""
    assert "key" in sample_data
```

### Async Tests

```python
import pytest

@pytest.mark.asyncio
async def test_async_function() -> None:
    """Test async function."""
    result = await async_function()
    assert result is not None
```

### Mocking

```python
from unittest.mock import Mock, patch

def test_with_mock() -> None:
    """Test with mocked dependency."""
    mock_dep = Mock()
    mock_dep.method.return_value = "result"

    instance = MyClass(dependency=mock_dep)
    result = instance.do_something()

    mock_dep.method.assert_called_once()
    assert result == "result"
```

## Best Practices

1. One assertion per test when possible
2. Use descriptive test names
3. Test behavior, not implementation
4. Mock at boundaries only
5. Keep tests fast
