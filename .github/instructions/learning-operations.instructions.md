---
description: 'Maintenance and lifecycle guidelines for educational modules in /learning, persona alignment, and code-sync standards.'
applyTo: '**/learning/**/*.md'
---

# Learning Operations

Guidelines for maintaining, auditing, and expanding the educational materials in the `learning/` directory.

## Core Responsibilities

- **Module Lifecycle**: Scaffolding new modules, validating structure, and ensuring consistent documentation.
- **Persona Alignment**: Framing all content for the target audience (primary: Sarah Jenkins).
- **Code Synchronization**: Linking documentation to real-world implementations in `packages/`.
- **Integrity**: Maintaining cross-references and resolving broken links.

## Metadata Standards

Every markdown file in `learning/` MUST start with a YAML frontmatter block:

```yaml
---
description: 'A brief description of the learning material.'
tags:
  - status:draft # Possible values: draft, published, archived
  - verified:false # Boolean for technical verification
---
```

## Persona Alignment: Sarah Jenkins

Frame all content through the lens of **Sarah Jenkins (Enterprise AI Architect)**.

- **Primary Goal**: Build reliable, auditable, and scalable AI agents for regulated enterprise environments.
- **Key Themes**: "Day 2" operations, governance, security, and failure engineering.
- **Architectural Reference**: [learning/00-misc/reports/enterprise-architect.persona.md](learning/00-misc/reports/enterprise-architect.persona.md)
- **Core Focus Areas**:
  - **Hybrid Orchestration**: Combining Pydantic AI with established workflows.
  - **Governance**: RBAC, JWT scopes, and least privilege in agent tool execution.
  - **Hardening**: Semantic firewalls and prompt injection defense.
  - **Failure Engineering**: Circuit breakers and deterministic fallbacks for non-deterministic LLM calls.

### Secondary Personas

While Sarah is the primary frame, ensure relevance for:

| Persona             | Focus                                                                           |
| ------------------- | ------------------------------------------------------------------------------- |
| **AI Engineer**     | Defensive engineering, validators, circuit breakers, and audit traces.           |
| **Product Manager** | ROI, cost/latency tradeoffs, and UX patterns for non-deterministic failures.    |

## Structure and Validation

### Module Organization (Structure Layout)

The `learning/` directory follows a strict numbering and naming convention to ensure logical progression.

| Component                  | Rule                                                                          |
| -------------------------- | ----------------------------------------------------------------------------- |
| **Module Directories**     | Must be prefixed with 2-digit number and dash (e.g., `01-fundamentals/`).       |
| **`README.md`**            | Required in every module. Must contain description and **Learning objectives**. |
| **Naming**                 | Use kebab-case for directories and files.                                      |
| **Assets**                 | Store module-specific images or diagrams in a local `assets/` folder.         |

Standard hierarchy:
1. `XX-topic/README.md`: Module overview, learning objectives, and implementation links.
2. `XX-topic/YY-subtopic.md`: Specific conceptual deep-dives or procedural guides.
3. `XX-topic/spec.md`: Internal specification for the module content.

### Tooling

Operations are managed via `just` recipes which wrap the [scripts/learning/init_learning_structure.py](scripts/learning/init_learning_structure.py) script.

- `just learning-init <name> <title>`: Idempotently scaffold a new module structure.
- `just learning-validate`: Audit `learning/` for structure, metadata, and link integrity.

Manual execution of the scaffolding script:
```bash
uv run python scripts/learning/init_learning_structure.py --path ./learning --add-module 05-new-topic --title "New Topic"
```

## Workflow: Adding a New Educational Concept

1. **Identify implementation**: Every concept MUST be backed by a real package in `packages/`. Avoid dummy exercises.
2. **Review Persona Alignment**: Ensure the topic addresses Sarah Jenkins' goals (Reliability, Auditability, Scalability).
3. **Scaffold Module**: Use `just learning-init` to create the directory and initial `README.md`.
4. **Draft Content**:
   - Start with "Why this matters" for an Enterprise Architect.
   - Use absolute workspace-relative links for implementation files.
   - Reference the actual source (e.g., [packages/course-navigator/src/course_navigator/agent.py](packages/course-navigator/src/course_navigator/agent.py)).
5. **Cross-Reference**: Update related modules to point to the new content if applicable.
6. **Validate**: Run `just learning-validate` and fix any structural or link errors.

## Progressive Disclosure in Learning

1. **README.md**: High-level "Why this matters" for Sarah Jenkins.
2. **Guides**: Progressive deep dives into implementation details.
3. **References**: Links to standard specs (e.g., `specs/features/`) and external library docs.
