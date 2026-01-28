---
name: learning-ops
description: Guide on managing learning materials. Use for structure validation, creating/editing new learning modules, maintaining material freshness, changing/synchronizing code examples, and cross-referencing learningcontent."
---

# Learning Operations Skill

## Quick Start

This skill helps you manage the lifecycle of educational content in `learning/`.

### Common Tasks

1. **Create a new module**:

    ```bash
    python .github/skills/learning-ops/scripts/init_learning_structure.py --path ./learning --add-module 05-new-topic --title "New Topic"
    ```

2. **Validate structure and links**:

    ```bash
    python .github/skills/learning-ops/scripts/init_learning_structure.py --path ./learning --validate
    ```

3. **Sync check (conceptual)**:
    Refer to [syncing.md](./references/syncing.md) for verifying code examples match documentation.

## When to Use

- **Structure**: Adding new numbered modules, ensuring READMEs and exercises exist.
- **Maintenance**: Auditing content for freshness or deprecation.
- **Syncing**: Linking code examples in `packages/` to explanations in `learning/`.
- **References**: Creating cross-links between modules or from code to docs.

## Reference Guides

- [Structure Layout](./references/structure.md): The canonical directory tree rules.
- [Material Maintenance](./references/maintenance.md): How to audit and update content.
- [Code Syncing](./references/syncing.md): Keeping docs and code in harmony.
- [Cross-Referencing](./references/cross-referencing.md): Linking strategies.

## Included Resources

### Scripts

- `scripts/init_learning_structure.py`: Idempotent structure generator and validator.

### Assets

- `assets/template_readme.md`: Standard template for new modules.

## Workflow: Adding a New Educational Concept

1. **Identify the Code**: Find or create the example code in `packages/*/src/examples/`.
2. **Create Module**: Use the script to scaffold the `learning/XX-topic/` folder.
3. **Write Content**: Use the templates. Reference the code using `[File Link](../../packages/...)`.
4. **Cross-Ref**: Update previous modules to point to the new advanced topic if relevant.
5. **Validate**: Run the validation script to check file presence.
