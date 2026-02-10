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

# Content Tailoring

When creating or updating learning materials, ensure the content is tailored to the target audience. Without explicitly referencing persona names.

## Personas

- **Enterprise AI Architect:** Prioritize enterprise-grade architecture, governance, and reliability—hybrid orchestration patterns, RBAC/least-privilege integrations, adversarial hardening, observability, and "Day 2" failure-mode strategies. [detailed](../../learning/00-misc/reports/enterprise-architect.persona.md)
- **AI Engineer:** Emphasize defensive engineering and compliance: deterministic Pydantic validators and circuit breakers, semantic firewalls and content sandboxing, and immutable audit/replay traces for verifiable deployments. [detailed](../../learning/00-misc/reports/ai-engineer.persona.md)
- **Product Manager:** Focus on product-readiness and economics: ROI and cost/latency tradeoffs, UX patterns for non-deterministic failures, and explainability/liability features such as compliance reports derived from validators and execution traces. [detailed](../../learning/00-misc/reports/product-manager.persona.md)
