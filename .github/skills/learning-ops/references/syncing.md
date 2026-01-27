# Synchronizing Code Examples

Guidelines for keeping learning materials in sync with the codebase.

## Single Source of Truth

- **Source Code**: The canonical source for code examples is `packages/*/src/examples/`.
- **Usage**: Learning materials should reference these files rather than duplicating logic.
- **Extracts**: If showing a partial snippet, ensure the full example file exists and runs.

## Linking Strategy

When explaining a concept in `learning/`:

1.  **Conceptual Link**: Link to the source file.
    > "See the full implementation in [chatbot.py](../../packages/shared/src/examples/chatbot.py)."
2.  **Exercise Sync**: Exercises should import from the installed packages, not re-implement core classes.

## Automation

- **CI Checks**: Ensure the `learning-ops` validation scripts are run during CI to catch broken references.
- **Drift Detection**: If an example file is modified, the corresponding learning module should be flagged for review.
