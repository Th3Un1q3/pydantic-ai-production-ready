# Learning Materials

This directory contains modular learning materials for building production-ready AI applications with Pydantic AI Framework.

## Structure

The learning materials are organized in a modular, progressive structure:

```
learning/
├── 01-fundamentals/          # Basic concepts and getting started
│   ├── 01-introduction.md
│   ├── 02-setup.md
│   └── exercises/
├── 02-core-concepts/          # Core Pydantic AI concepts
│   ├── 01-agents.md
│   ├── 02-models.md
│   ├── 03-tools.md
│   └── exercises/
├── 03-advanced-patterns/      # Advanced implementation patterns
│   ├── 01-streaming.md
│   ├── 02-error-handling.md
│   └── exercises/
├── 04-production-deployment/  # Production considerations
│   ├── 01-monitoring.md
│   ├── 02-scaling.md
│   └── exercises/
└── README.md                  # This file
```

## How to Use

### For Learners

1. Start with `01-fundamentals` and progress sequentially
2. Each module contains:
   - Concept explanations (markdown files)
   - Practical exercises with sample code
   - References to working examples in `/projects`
3. Complete exercises before moving to the next module
4. Use the `/projects` directory to experiment and build

### For Content Creators

The modular structure supports easy content addition and updates:

#### Adding a New Module

1. Create a new numbered directory: `XX-module-name/`
2. Add markdown files for concepts: `01-concept-name.md`
3. Create an `exercises/` subdirectory for hands-on activities
4. Update this README with the new module

#### Module Template

Each module should follow this structure:

```
XX-module-name/
├── README.md              # Module overview and objectives
├── 01-topic-one.md       # Individual topic/concept
├── 02-topic-two.md       # Another topic
├── exercises/
│   ├── README.md         # Exercise instructions
│   ├── exercise-1/       # Self-contained exercise
│   └── exercise-2/
└── resources/            # Additional resources (optional)
    ├── diagrams/
    └── code-samples/
```

#### Content Guidelines

1. **Progressive Complexity**: Each module should build on previous ones
2. **Self-Contained**: Each topic file should be independently understandable
3. **Practical Focus**: Include code examples and real-world scenarios
4. **Clear Learning Objectives**: Start each module with clear goals
5. **Exercises**: Provide hands-on practice opportunities

#### Markdown Standards

- Use clear headings (H2 for main sections, H3 for subsections)
- Include code blocks with language specification
- Add links to related modules and external resources
- Use callouts for important notes (> **Note:** ...)

## Module Overview

### 01-fundamentals
Introduction to Pydantic AI, environment setup, and basic concepts.

**Learning Objectives:**
- Understand what Pydantic AI is and its use cases
- Set up development environment
- Create your first AI agent

### 02-core-concepts
Deep dive into Pydantic AI core concepts and components.

**Learning Objectives:**
- Understand agents, models, and tools
- Work with structured outputs using Pydantic models
- Implement tool calling and function execution

### 03-advanced-patterns
Advanced implementation patterns for production applications.

**Learning Objectives:**
- Implement streaming responses
- Handle errors and retries gracefully
- Build complex multi-agent systems

### 04-production-deployment
Production deployment, monitoring, and scaling strategies.

**Learning Objectives:**
- Monitor AI applications in production
- Scale AI workloads efficiently
- Implement security best practices

## Contributing

Content creators are encouraged to:
1. Follow the modular structure
2. Maintain consistency in formatting and style
3. Test all code examples
4. Provide clear learning paths
5. Update this README when adding new modules

## Resources

- [Pydantic AI Documentation](https://ai.pydantic.dev/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- Project examples in `/projects`
