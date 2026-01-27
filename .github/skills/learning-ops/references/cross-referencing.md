# Cross-Referencing Guidelines

Strategies for linking between learning materials and code.

## Internal Linking (Material to Material)

- **Prerequisites**: Link to prerequisite modules at the top of a `README.md`.
    > "Before starting this module, ensure you are familiar with [01-fundamentals](../01-fundamentals/README.md)."
- **Progression**: Use "Next Steps" at the end of a module to guide the user.

## Material to Code

- **Relative Paths**: Always use relative paths from the markdown file.
    - Correct: `[Chatbot Example](../../packages/shared/src/examples/chatbot.py)`
    - Incorrect: `/workspace/packages/shared/src/examples/chatbot.py`
- **Line Numbers**: Use line numbers for specific block references, but be aware they are brittle.
    > "The `__init__` method (lines 10-15) initializes the agent."

## Code to Material

- **Docstrings**: In the source code examples, link back to the learning module that explains the concept.
    ```python
    # For a detailed explanation, see learning/02-core-concepts/01-agents.md
    ```
