---
description: 'Guidelines for writing useful, non‑redundant comments in source and test files.'
applyTo: '**/*.{py,js,ts,md}'
---

# Commenting Guidelines

Comments should be the exception — code must be the first and clearest form of documentation. Use comments only when intent, rationale or non-obvious behavior cannot be expressed clearly in code or a docstring. Comments must never duplicate what the code already says.

## Core rules (short)

- Prefer self‑documenting code over comments. Rename variables/functions or extract helpers instead of adding explanatory comments.
- Do not duplicate the interface or restate the obvious (e.g., `# increment i` above `i += 1`).
- Comments explain "why" or "why not" — not "how". Implementation belongs in code.
- No dates, authors, or long change-history comments in source files. Use git for history.
- Avoid commented-out code — delete it or keep it in VCS.
- Use `TODO:` with an issue/PR reference when needed (e.g. `TODO(#123): handle edge case`).

## Where comments are appropriate

- Rationale for non-obvious design decisions or trade-offs.
- Algorithmic intent when the implementation is dense or relies on a mathematical/engineering insight.
- Public API usage notes, side-effects, and stability guarantees (use docstrings for API-level docs).
- Quick in-line clarification for unusual edge-cases (keep these < 2 lines).

## Style and tone

- Keep comments short, present-tense, and factual.
- Write in English. Use complete sentences for multi-line comments.
- Prefer `#`/`//` inline comments for brief notes; reserve block comments for rationale or longer explanations.

## Examples

Bad (duplicates code):

```python
count = count + 1  # increment count
```

Good (explain intent):

```python
# Use an extra iteration to let the background worker flush its queue.
count = count + 1
```

Bad (dated header):

```python
# 2023-03-01 - added by alice
```

Good: rely on `git blame` / PR history.

## Enforcement & review

- Code reviewers should flag comments that restate code or contain dated/author metadata.
- If a comment becomes incorrect, update or remove it during the same change that makes the code correct.

> Rule of thumb: if you can rename a variable or extract a helper to make the code clearer, do that — avoid adding a comment.
