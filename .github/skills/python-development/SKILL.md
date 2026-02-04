---
name: python-development
description: Guide for Python development enforcing ZOMBIE TDD workflow. Use this skill whenever writing or modifying Python code.
---

# Python Development

This skill enforces a strict Test Driven Development (TDD) workflow using the **ZOMBIE** methodology.

## Core Principle: Strict TDD

1. **Never write functional code without a failing test.**
2. **Only write enough code to pass the current test.**
3. **Refactor only on green.**

## The ZOMBIE Methodology

When defining test cases, you must systematically brainstorm scenarios covering the following categories:

* **Z**ero (Zero state): Default behaviors, empty inputs, simple instantiation.
  * *Example*: Calculator with no input returns 0.
* **O**ne (One item): Simple functionality, single unit, happy path.
  * *Example*: Adding two small numbers.
* **M**any (Many items/Complex): Complex scenarios, table-driven tests, multiple items.
  * *Example*: Adding a list of numbers, complex formulas.
* **B**oundary (Boundaries): Edge cases, limits, max/min values.
  * *Example*: Division by zero, MAX_INT, empty lists.
* **I**nterface (Interface): API contract checks, invalid types, arguments outside schema.
  * *Example*: Passing string to math function, check for graceful failure.
* **E**xceptions (Exceptions): Error handling, missing dependencies, external failures.
  * *Example*: Service unavailable, file not found.

## Development Workflow

Follow this cycle for every feature:

### 1. Brainstorm & Plan

Before writing code, analyze the requirement and list potential test cases for each ZOMBIE category.
**Action**: Ask the user to confirm the plan if there is ambiguity.

### 2. Create Pending Tests

Implement a test file with **all** identified cases marked as pending or using placeholders (e.g., `pytest.skip` or empty functions). Do not implement the test logic yet.

```python
def test_zero_case():
    """Pending: Verify default state"""
    pass
```

### 3. Implement One Case (Red)

Pick the simplest failure (usually Zero or One). Write the full test logic.
**Verify**: Run the test and ensure it fails for the expected reason.

### 4. Implement Code (Green)

Write the **simplest possible code** to make that specific test pass. Do not over-engineer.
**Verify**: Run the test and ensure it passes.

### 5. Iterate

Repeat steps 3-4 for the next test case in the ZOMBIE list.

## Strict Quality Enforcement

### 1. Mandatory API Verification

**STOP AND VERIFY**: Before implementing any code that interacts with an external library (e.g., `pydantic-ai`, `logfire`):

1. **Query Documentation**: Run `mcp_context7_query-docs` to get the exact method signatures and return types.
2. **Verify Attributes**: Do not "guess" attribute names (e.g., `.data` vs `.output`). **You must see the attribute in the documentation output or code snippet.**
3. **No "Dreamed" APIs**: If you cannot verify the API, do not write the code. Ask the user for clarification or search again.

### 2. Static Analysis Enforcement

**RUN CHECKS**: You must run the static analysis suite to catch type errors immediately.

1. **Command**: Run `just check` (or `just typecheck {{package_name}}`) after every implementation step.
2. **Fix Errors**: If `just check` fails, **stop**. Fix the type errors before proceeding. Do not ignore them.
3. **Spec-Compliant Mocks**: When using `unittest.mock`, you **MUST** use `spec=True` or `spec=Class` to ensures your mocks adhere to the real interface.
    * *Bad*: `Mock()` (accepts anything)
    * *Good*: `Mock(spec=Agent)` (raises AttributeError on invalid access)

## Testing Guidelines

* Use `pytest` as the testing framework.
* Place tests in a `tests/` directory mirroring the source structure.
* Test files should be named `test_<module>.py`.
* Keep tests independent.

## Professional Testing with Pytest

Use `pytest` features to write readable, maintainable, and "professional" tests that check all ZOMBIE categories.

### 1. Fixtures for Setup (Context)

Use `@pytest.fixture` to provide the "Zero" state or common resources. This avoids duplication in "Arrange" steps.

```python
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_initial_state(calculator):
    assert calculator.value == 0
```

### 2. Parametrization for Many/Boundary

Use `@pytest.mark.parametrize` for "Many" and "Boundary" cases. This keeps tests concise and makes it easy to add new cases (table-driven testing).

```python
@pytest.mark.parametrize("inputs,expected", [
    ([1, 1], 2),            # One
    ([1, 2, 3], 6),         # Many
    ([], 0),                # Zero/Boundary
    ([-1, 1], 0),           # Boundary
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

When using parametrization, use the `ids` argument or `pytest.param(..., id="name")` to make test output readable. The test output should tell a story.

```python
@pytest.mark.parametrize("input_val", [
    pytest.param(None, id="null_input"),
    pytest.param("", id="empty_string"),
], ids=str)
def test_invalid_input(input_val):
    ...
```
