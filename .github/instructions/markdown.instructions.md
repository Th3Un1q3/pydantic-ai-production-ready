---
description: This file describes the Markdown formatting and style guidelines for the project.
applyTo: "**/*.md"
---

# Markdown Style Guidelines

- Only use numbered headings when order of following matters; otherwise, use unnumbered headings.

## Code Blocks

- Always specify a language for fenced code blocks (```language)
- Use appropriate languages: `bash` for shell commands, `python` for Python code, `text` for plain text/directory structures, `json` for JSON, etc.
- Never use bare ``` without a language specifier

## Tables

- Use compact table style (no spaces around pipes): `|Header|Data|` not `| Header | Data |`
- Ensure consistent column alignment across all rows
- Keep table formatting simple and readable

## Headings

- Use only one H1 (#) heading per document (typically the main title)
- Use ATX heading style (# ## ###) consistently
- Do not use emphasis (**text**) as headings - use proper heading syntax
- Avoid setext headings (underlines with === or ---)

## General

- Follow standard markdown conventions for links, lists, and emphasis
- Keep formatting consistent within each document
- Run `just lint-md` to check and fix formatting issues automatically
