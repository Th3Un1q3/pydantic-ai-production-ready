---
name: learning-structure
description: "Create, validate, and update the 'learning' directory structure for modular learning materials. Use when adding a new module, verifying module README and exercises, or generating consistent module templates (numbered modules, README.md, exercises/, and resources)."
---

# Learning Structure Skill

## Quick start

- Use this skill when you need to create or validate the `learning/` structure for modular learning materials.
- Run the included script to generate module skeletons or to validate an existing structure:

```bash
python scripts/init_learning_structure.py --path ./learning --init-all
python scripts/init_learning_structure.py --path ./learning --add-module 05-ml-deployment --title "ML Deployment"
python scripts/init_learning_structure.py --path ./learning --validate
```

## When to use

- Add a new numbered module with consistent layout (e.g., `05-ml-deployment/`).
- Ensure each module contains a `README.md`, `exercises/` folder, and optional `resources/`.
- Validate the repository follows the expected learning materials layout defined in `references/structure.md`.

## Included resources

- `scripts/init_learning_structure.py` — idempotent script to create modules and validate structure.
- `references/structure.md` — canonical description of the desired directory layout and README template.
- `assets/template_readme.md` — a short README template used when initializing new modules.

## Examples

- "Add a module for deployment topics and create exercises skeleton." → run `--add-module` with `--title` and optionally `--topics`.
- "Validate the current `learning/` tree for missing files." → run `--validate`.

## Design notes

- Keep README content concise and use the template in `assets/` when creating new modules.
- Scripts are idempotent and include `--dry-run` for previewing changes.
