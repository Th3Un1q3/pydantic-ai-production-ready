# Learning Materials Structure (canonical reference)

This document describes the canonical layout for the `learning/` directory used across the repository.

Root layout

```
learning/
├── 01-fundamentals/
│   ├── 01-introduction.md
│   ├── 02-setup.md
│   └── exercises/
├── 02-core-concepts/
│   ├── 01-agents.md
│   ├── 02-models.md
│   └── exercises/
├── 03-advanced-patterns/
│   └── exercises/
├── 04-production-deployment/
│   └── exercises/
└── README.md
```

Module expectations

- Module directories should be prefixed with a 2-digit number and a dash (e.g., `01-fundamentals`).
- Each module should include a `README.md` with a short description and **Learning objectives**.
- Each module should include an `exercises/` directory with an `README.md` describing the exercises.
- Optional `resources/` or `references/` directories are permitted inside a module.

Module README template

Use the template in `assets/template_readme.md` when creating new modules.
