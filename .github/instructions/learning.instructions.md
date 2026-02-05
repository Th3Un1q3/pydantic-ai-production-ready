---
description: Instructions on how to maintain /learning directory and its content.
applyTo: "**/learning/**/*.md"
---

# Materials Metadata

Each learning material file should start with a YAML front matter block containing metadata about the material. The required fields are:
```markdown
---
description: A brief description of the learning material.
tags:
  - status:draft # Possible values: draft, published, archived
  - verified:false  # Optional list of tags for the document
---
```

# Structure

The canonical directory layout and module structure for `learning/` is maintained by the [learning-structure skill](.github/skills/learning-structure). Use the skill's script to create, validate, or manage modules.

For the canonical structure definition, see [learning-structure references](.github/skills/learning-structure/references/structure.md).
