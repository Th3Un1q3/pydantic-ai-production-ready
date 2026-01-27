---
description: 'Guidelines for creating modular, high-quality learning content and course structures'
applyTo: 'learning/**/*.md'
---

# Modular Course Structure & Content Guidelines

These instructions define the standards for creating, organizing, and maintaining modular learning content within the `learning/` directory. They are designed to ensure content is digestible, reusable, and engaging, drawing from best practices in modular course design.

## General Instructions

- **Audience-First Design**: always define clear learning objectives (LOs) and target audience before writing content.
- **One Concept, One Module**: Each file or module should focus on a single specific skill, concept, or task to facilitate microlearning.
- **Iterative Development**: Start with a high-level outline or "slides" (headers/bullet points) before fleshing out detailed prose and code examples.

## Best Practices

### Modularity & Reusability
- **Self-Contained Units**: Modules should stand alone where possible. If a module relies on another, link to it explicitly rather than assuming sequential reading.
- **Reusable Patterns**: Structure explanations using a consistent "Problem -> Solution -> Benefits" pattern. This allows content to be adapted for different contexts (e.g., beginner vs. advanced tracks) easily.
- **Microlearning**: Aim for detailed content that can be consumed in 5-10 minutes. If a topic is too large, break it down into sub-modules.

### Engagement
- **Action-Oriented**: Include "Try it yourself" sections or small exercises in every module.
- **Visuals & Examples**: Use code blocks, diagrams (Mermaid), or tables to break up walls of text.
- **Hooks**: Start each module with a "Hook" — a brief statement explaining *why* this matters to the learner immediately.

## Directory & File Structure

The `learning/` directory follows a numbered structure to indicate recommended progression, but individual modules should remain loosely coupled.

- **Naming**: Use `DD-topic-name` for ordering (e.g., `01-fundamentals`).
- **Index Files**: Every directory must have a `README.md` that serves as a syllabus/index for that module.
- **Knowledge Tracks**: Group related modules into folders (e.g., `fundamentals`, `core-concepts`).

```text
learning/
├── 01-fundamentals/            # Category
│   ├── README.md               # Overview & Index
│   ├── 01-introduction.md      # Micro-module
│   ├── 02-setup.md             # Micro-module
│   └── exercises/              # Practical tasks
```

## Content Standards

### Module Template
Every learning module (`.md` file) should roughly follow this structure:

1.  **Title**: Clear and descriptive.
2.  **Hook/Objective**: 1-2 sentences on what will be learned and why.
3.  **Concept/Theory**: Brief explanation of the "What".
4.  **Practical Application**: Code examples, step-by-step guides (the "How").
5.  **Summary/Checklist**: Key takeaways.

### Code Examples
- Use standard markdown code blocks.
- Ensure all code snippets are complete enough to be understood (or runnable if comprehensive).
- Comment complex lines to explain the "why".

### Bad and Good Examples

#### Bad Example (Monolithic & Vague)
```markdown
# Python Stuff
Here is everything about Python. Variables use `=`, loops use `for`.
(followed by 20 pages of text)
```

#### Good Example (Modular & Structured)
```markdown
# 03-variables-and-types.md

## Why this matters
Understanding how to store data is the first step to manipulating it.

## The Concept
Variables are containers for storing ...

## Example
```python
user_name = "Alice" # String variable
```

## Exercise
Create a variable for your age.
```

## Validation

- **Link Checking**: Ensure all relative links between modules work.
- **Time Check**: Read through; if it takes >15 mins, consider splitting.
- **Objective Check**: Does the content directly satisfy the specific Learning Objective defined at the start?
