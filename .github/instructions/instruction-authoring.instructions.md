---
description: 'Meta-guidance for creating and maintaining modular instruction files, enforcing single source of truth, and progressive disclosure.'
applyTo: '**/*.instructions.md'
---

# Instruction Authoring

Guidelines for creating effective modular instruction files (`.instructions.md`) that guide GitHub Copilot through domain-specific workflows and project conventions.

## Core Principles

### 1. Concise is Key
The context window is a shared resource. Assume the assistant is already highly capable.
- **Minimalism**: Only add context the assistant does not already have.
- **Efficiency**: Favor concise examples over verbose explanations.
- **Constraint**: If a section doesn't justify its token cost during a code generation task, remove it.

### 2. Single Source of Truth (SSOT)
- **No Redundancy**: Information must reside in exactly one place.
- **Reference, Don't Copy**: If a pattern is defined in [.github/instructions/python.instructions.md](.github/instructions/python.instructions.md), link to it rather than duplicating the rules.
- **Conflict Resolution**: Follow the precedence hierarchy (e.g., `monorepo` > `command-execution` > `test-implementation` > `python-tests` > `python`).

### 3. Progressive Disclosure
Manage context efficiency using a tiered structure:
1. **Metadata (`description` + `applyTo`)**: Determines when the module is loaded.
2. **Instruction Body**: Core procedural guidance and non-obvious rules.
3. **Bundled Resources**: Detailed schemas, API logs, or variants linked from the body for optional loading.

### 4. Degrees of Freedom
Match the specificity to the task's fragility:
- **High Freedom**: Use for heuristic-based tasks where multiple approaches are valid.
- **Medium Freedom**: Use for tasks with preferred patterns but allow for some variation.
- **Low Freedom**: Use for fragile, error-prone sequences where specific commands or patterns are mandatory.

## File Standards

### Required Frontmatter
Every instruction file MUST include YAML frontmatter:

```yaml
---
description: 'Single-quoted string, 1-500 chars, clearly stating purpose'
applyTo: 'glob pattern for target files (e.g., **/*.ts, src/**/*.py)'
---
```

### Frontmatter Schema Gate
- Validate frontmatter keys against the artifact's documented schema before editing metadata.
- Do not infer key validity from another artifact type (for example, prompt-file keys vs instruction-file keys).
- For metadata disputes, cite the canonical source in your reasoning before applying edits.

### File Naming
- **Convention**: Lowercase with hyphens (e.g., `api-verification.instructions.md`).
- **Location**: `.github/instructions/`.

## Structural Anatomy

| Section | Purpose |
| :--- | :--- |
| **Frontmatter** | Metadata for loading and discovery (`description`, `applyTo`). |
| **Instruction Body** | procedural guidance, rules, and best practices. |
| **Bundled Resources** | Scripts, references, and assets for complex tasks. |

### Bundled Resources

| Type | Purpose | Loaded into Context? |
| :--- | :--- | :--- |
| `scripts/` | Executable automation for deterministic tasks. | Only when executed. |
| `references/` | Detailed documentation/schemas read as needed. | Yes, when referenced. |
| `assets/` | Static files used AS-IS in output (not modified). | No. |
| `templates/` | Starter code/scaffolds modified by the AI. | Yes, when referenced. |

## Content Guidelines

### Writing Style
- **Imperative Mood**: Use "Implement", "Use", "Avoid". Not "You should consider...".
- **Actionable**: Every rule must be testable or verifiable.
- **No Fluff**: Remove introductory qualifiers ("In this project...", "It is important to...").

### Examples
Always provide context for snippets:
```markdown
### Good: Descriptive Table Labels
| Field | Type   | Description      |
| ----- | ------ | ---------------- |
| id    | string | UUIDv4 identifier|

### Bad: Ambiguous Names
| Name | Val |
| ---- | --- |
| x    | str |
```

## Quality Standards

### What to NOT Include
Do NOT create extraneous documentation or auxiliary files, including:
- `README.md`
- `INSTALLATION_GUIDE.md`
- `QUICK_REFERENCE.md`
- `CHANGELOG.md`

Instruction modules should only contain information needed for an AI agent to do the job. Clutter reduces token efficiency.

### Progressive Disclosure Patterns
- **Pattern 1**: High-level guide with references to detailed files.
- **Pattern 2**: Domain-specific organization (e.g., separate files for AWS vs GCP).
- **Pattern 3**: Conditional details linked for advanced scenarios.

## Anti-Duplication Workflow
Before creating a new instruction module:
1. **Search**: Check the root `pyproject.toml` and `.github/instructions/` for existing coverage.
2. **Extend**: If a concept is related to an existing file, add a section there instead of creating a new file.
3. **Decompose**: If a file exceeds 500 lines, extract detailed reference patterns into a separate file in a sub-folder (e.g., `.github/instructions/references/`).
