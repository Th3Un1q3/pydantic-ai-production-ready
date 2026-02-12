---
description: 'Pytest mechanics, fixture usage, parametrization, and mocking standards.'
applyTo: '**/tests/*.py'
---

# Python Testing Mechanics

Standardized approach for writing maintainable and expressive tests using `pytest`. This module implements the mechanics for the [.github/instructions/test-implementation.instructions.md](.github/instructions/test-implementation.instructions.md).

## Framework & Organization

- **Tooling**: Use `pytest` for all Python tests.
- **Location**: Place tests in a `tests/` directory mirroring the source structure.
- **Naming**: Test files MUST be named `test_<module>.py`.
- **Independence**: Keep tests independent and side-effect free.

## Professional Pytest Patterns

### 1. Fixtures for Setup
Use `@pytest.fixture` to provide the "Zero" state (context) or common resources. This avoids duplication in "Arrange" steps.

```python
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_initial_state(calculator):
    assert calculator.value == 0
```

### 2. Parametrization
Use `@pytest.mark.parametrize` for "Many" and "Boundary" cases. This keeps tests concise and makes it easy to add new cases (table-driven testing).

```python
@pytest.mark.parametrize("inputs,expected", [
    pytest.param([1, 1], 2, id="one_plus_one"),
    pytest.param([1, 2, 3], 6, id="multiple_items"),
    pytest.param([], 0, id="empty_list"),
    pytest.param([-1, 1], 0, id="boundary_negative"),
])
def test_addition(calculator, inputs, expected):
    assert calculator.add(inputs) == expected
```

### 3. Testing Exceptions
Use `pytest.raises` to verify "Exceptions" and "Interface" contract violations.

```python
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(1, 0)
```

### 4. Descriptive IDs
ALWAYS use `pytest.param(..., id="name")` or the `ids` argument in parametrization to ensure test outputs are readable and descriptive. The test output should tell a story.

## Mocking Standards

When using `unittest.mock`, you **MUST** use `spec=True` or `spec=Class` to ensure your mocks adhere to the real interface and prevent silent failures on misspelled attributes.

- **Bad**: `Mock()` (accepts anything, hides errors)
- **Good**: `Mock(spec=Agent)` (raises `AttributeError` on invalid access)
- **Prefer**: `pytest-mock` (via `mocker` fixture) for cleaner injection and automatic cleanup.

```python
def test_agent_interaction(mocker):
    # Ensures the mock ONLY has methods/attributes of the actual Agent class
    mock_agent = mocker.Mock(spec=Agent)
    ...
```
