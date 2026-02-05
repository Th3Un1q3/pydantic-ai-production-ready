# Learning Module Specification Template

<!--
Use this template for new educational content.
Replace all placeholders in {{BRACKETS}}.
Delete helper comments before finalizing.
-->

---
spec-id: SPEC-{{ID}}
title: {{Module Title}}
type: learning
status: draft
created: {{YYYY-MM-DD}}
module-number: {{XX}}
author: {{author}}
---

## Executive Summary

### Problem Statement

{{Describe the knowledge gap this module addresses.}}

### Proposed Solution

{{Describe the learning module and its educational goals.}}

### Success Criteria

- {{Learner completes module in < X minutes}}
- {{Learner can demonstrate skill Y}}
- {{Module includes Z practical exercises}}

## Learning Objectives

By the end of this module, learners will be able to:

1. {{Objective 1: Use action verb - "Implement", "Explain", "Design"}}
2. {{Objective 2}}
3. {{Objective 3}}

## Target Audience

### Primary Persona: Enterprise AI Architect

- **Background**: {{Relevant experience level}}
- **Goals**: Build reliable, auditable, and scalable AI agents
- **Prior Knowledge**: {{What they already know}}

### Prerequisites

- Completed: `learning/{{XX-prerequisite-module}}/`
- Familiar with: {{concept 1}}, {{concept 2}}

## Content Structure

### Module Directory

```
learning/{{XX-module-name}}/
├── README.md           # Module overview and navigation
├── 01-{{topic}}.md     # First concept
├── 02-{{topic}}.md     # Second concept
├── 03-{{topic}}.md     # Third concept
├── exercises/          # Hands-on practice
│   ├── 01-{{exercise}}.md
│   └── 02-{{exercise}}.md
└── solutions/          # Exercise solutions
    └── ...
```

### Content Outline

#### 1. Introduction (5 minutes)

- Hook: {{Why this matters for enterprise AI}}
- Context: {{Connection to previous modules}}
- Overview: {{What we'll cover}}

#### 2. Core Concepts (15 minutes)

| Concept | Key Points | Example |
|---------|------------|---------|
| {{Concept 1}} | {{Point 1, Point 2}} | {{Brief example}} |
| {{Concept 2}} | {{Point 1, Point 2}} | {{Brief example}} |
| {{Concept 3}} | {{Point 1, Point 2}} | {{Brief example}} |

#### 3. Practical Application (20 minutes)

- **Demo**: {{What to demonstrate}}
- **Code Walkthrough**: Link to `packages/{{package-name}}/`
- **Exercise**: {{What learners will build}}

#### 4. Enterprise Considerations (10 minutes)

- **Governance**: {{RBAC, auditing considerations}}
- **Reliability**: {{Error handling, fallbacks}}
- **Scalability**: {{Performance considerations}}

#### 5. Summary and Next Steps (5 minutes)

- Key takeaways
- Link to advanced topics in `learning/{{next-module}}/`

## Code Examples

### Primary Example

Link to implementation: `packages/{{package-name}}/src/{{module}}.py`

```python
# Simplified example for documentation
{{code_example}}
```

### Exercise Scaffold

```python
# Starter code for learners
{{exercise_scaffold}}
```

## Exercises

### Exercise 1: {{Title}}

**Objective**: {{What learners will accomplish}}

**Instructions**:

1. {{Step 1}}
2. {{Step 2}}
3. {{Step 3}}

**Acceptance Criteria**:

- [ ] {{Verifiable outcome 1}}
- [ ] {{Verifiable outcome 2}}

**Hints**:

- {{Hint 1}}
- {{Hint 2}}

### Exercise 2: {{Title}}

**Objective**: {{What learners will accomplish}}

**Instructions**:

1. {{Step 1}}
2. {{Step 2}}

**Acceptance Criteria**:

- [ ] {{Verifiable outcome 1}}
- [ ] {{Verifiable outcome 2}}

## Implementation Plan

### Phase 1: Structure & Outline

**Deliverables**:

- [ ] Module directory created
- [ ] README.md with navigation
- [ ] Content outline in each file

**Validation**:

- Structure follows learning-ops conventions
- Links are valid

### Phase 2: Content Writing

**Deliverables**:

- [ ] Core concept explanations
- [ ] Code examples (linked to packages/)
- [ ] Exercise descriptions

**Validation**:

- Content aligns with learning objectives
- Examples are executable

### Phase 3: Exercises & Polish

**Deliverables**:

- [ ] Exercise files with scaffolds
- [ ] Solution files
- [ ] Cross-references to other modules

**Validation**:

- Exercises are completable
- Solutions are correct
- `python .github/skills/learning-ops/scripts/init_learning_structure.py --path ./learning --validate` passes

## Quality Standards

### Content Requirements

- [ ] Uses enterprise-focused framing
- [ ] Includes "Why This Matters" sections
- [ ] Links to real implementations in `packages/`
- [ ] Avoids dummy code - references actual agents

### Formatting Requirements

- [ ] YAML frontmatter with tags
- [ ] Consistent heading hierarchy
- [ ] Code blocks with language specifiers
- [ ] Accessible language (no jargon without definition)

## Cross-References

### Links To

- `learning/{{prerequisite-module}}/` - Required background
- `packages/{{related-package}}/` - Implementation reference

### Links From

- Update `learning/README.md` with new module
- Update `learning/MATERIALS.md` if applicable

## Constraints

### Content Constraints

- Align with Enterprise Architect persona
- Focus on "Day 2" operations (production concerns)
- Maximum 50 minutes total reading time

### Non-Goals

- {{Non-goal 1: e.g., Not covering basic Python}}
- {{Non-goal 2: e.g., Not implementing production infrastructure}}

## References

- [Enterprise Architect Persona](../../learning/00-misc/reports/enterprise-architect.persona.md)
- [Learning Ops Skill](../learning-ops/SKILL.md)
- {{Additional references}}
