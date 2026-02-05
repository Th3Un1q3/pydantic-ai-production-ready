---
name: learning-ops
description: Scaffold and validate /learning modules; refresh content; sync code examples with packages; add cross-references. Improve learning experience and maintainability.
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

- **Structure**: Adding new numbered modules, ensuring READMEs and links to implementations in `packages/` exist.
- **Maintenance**: Auditing content for freshness or deprecation.
- **Syncing**: Linking code examples in `packages/` to explanations in `learning/`.
- **References**: Creating cross-links between modules or from code to docs.

## Persona Alignment

Frame all content for **Sarah Jenkins (Enterprise AI Architect)**.

- **Goal**: Build reliable, auditable, and scalable AI agents in regulated environments.
- **Focus**: "Day 2" operations, governance, security, and failure engineering.
- **Reference**: [enterprise-architect.persona.md](../../../../learning/00-misc/reports/enterprise-architect.persona.md)

Ensure learning modules address:

1. **Hybrid Orchestration**: Combining Pydantic AI with workflows.
2. **Governance**: RBAC, JWT scopes, and least privilege.
3. **Hardening**: Semantic firewalls and prompt injection defense.
4. **Failure Engineering**: Circuit breakers and deterministic fallbacks.

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

1. **Identify the Package**: Identify or create the agent package in `packages/` that implements the concept. Avoid dummy exercises; build complete agents.
2. **Review Persona Strategy**: Ensure the topic aligns with the [Enterprise Architect Persona](../../../../learning/00-misc/reports/enterprise-architect.persona.md) goals (Reliability, Auditability, Scalability).
3. **Create Module**: Use the script to scaffold the `learning/XX-topic/` folder.
4. **Write Content**: Use the templates. Explain *why* this matters for enterprise production. Reference the actual implementation in `packages/`.
    - If implemented: `[Implementation](../../packages/<package-name>/src/...)`
    - If pending: Link to a partial example or placeholder with a "Not Implemented" note.
5. **Cross-Ref**: Update previous modules to point to the new advanced topic if relevant.
6. **Validate**: Run the validation script to check structure.
