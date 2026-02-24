---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

# Python Coding Conventions

## Python Instructions

- Write clear and concise comments for each function.
- Ensure functions have descriptive names and include type hints.
- Provide docstrings following PEP 257 conventions.
- **Use built-in generics for type annotations** (Python 3.12+). Write `list[str]`, `dict[str, int]`, `tuple[int, ...]` — NOT `typing.List`, `typing.Dict`, `typing.Tuple`. Only import from `typing` for constructs that have no built-in equivalent (e.g., `Any`, `Optional`, `Union`, `Callable`, `TypeVar`).
- Break down complex functions into smaller, more manageable functions.

## General Instructions

- Always prioritize readability and clarity.
- **Verify usages before any destructive edit**: Before removing or renaming an import, symbol, function, or parameter, confirm it is no longer referenced anywhere in ALL affected files. Silent breakage from still-used removals is discovered at runtime or in a subsequent check — and fixing it requires a separate correction. Use `grep` or file search to verify the full usage surface before committing to any destructive change.
- For algorithm-related code, include explanations of the approach used.
- Write code with good maintainability practices, including comments on why certain design decisions were made.
- Handle edge cases and write clear exception handling.
- For libraries or external dependencies, mention their usage and purpose in comments.
- Use consistent naming conventions and follow language-specific best practices.
- Write concise, efficient, and idiomatic code that is also easily understandable.

## Code Style and Formatting

- Follow the **PEP 8** style guide for Python.
- Maintain proper indentation (use 4 spaces for each level of indentation).
- Ensure lines do not exceed 79 characters.
- Place function and class docstrings immediately after the `def` or `class` keyword.
- Use blank lines to separate functions, classes, and code blocks where appropriate.

## Edge Cases and Testing

- Always include test cases for critical paths of the application.
- Account for common edge cases like empty inputs, invalid data types, and large datasets.
- Include comments for edge cases and the expected behavior in those cases.
- Write unit tests for functions and document them with docstrings explaining the test cases.

## Example of Proper Documentation

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle, calculated as π * radius^2.
    """
    import math
    return math.pi * radius ** 2
```
