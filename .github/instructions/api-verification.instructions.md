---
description: 'Mandatory workflow for verifying external library APIs before implementation.'
applyTo: '**/*.py'
---

# API Verification Workflow

To prevent "hallucinated" or incorrect API usage, follow this mandatory verification protocol.

## STOP AND VERIFY

Before implementing any code that interacts with an external library (e.g., `pydantic-ai`, `logfire`, `openai`):

1. **Query Documentation**: Use `mcp_context7_query-docs` to retrieve exact method signatures and return types.
2. **Verify Attributes**: Do not guess attribute names (e.g., `.data` vs `.output`). You must confirm the attribute exists in the documented response structure or verified code snippets.
3. **No Unverified APIs**: If an API cannot be verified through official documentation or local source code inspection, do not write the implementation. Ask the user for clarification or expand the search.

## Verification Tools

- **External Libraries**: Use `mcp_context7_resolve-library-id` followed by `mcp_context7_query-docs`.
- **Internal APIs**: Use `list_code_usages` and `read_file` to verify signatures of internal `pydantic_ai_shared` or local package components.
- **Reference Implementation**: Refer to [packages/course-navigator/src/course_navigator/agent.py](packages/course-navigator/src/course_navigator/agent.py) for verified `pydantic-ai` patterns.
