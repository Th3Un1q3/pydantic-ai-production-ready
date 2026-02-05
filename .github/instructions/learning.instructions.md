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

# Use Learning Ops Skill

Important: As you work within the `learning/` directory, you must read the `learning-ops` [skill](../skills/learning-ops/SKILL.md).
