# Learning Material Maintenance

Guidelines for maintaining the quality and relevance of learning materials.

## Content Audits

- **Frequency**: Conduct content audits quarterly.
- **Scope**: Check for outdated libraries, deprecated APIs, and broken links.
- **Action**: Update `MATERIALS.md` with the last audit date.

## Updating Content

1.  **Identify Changes**: When the core codebase changes (e.g., new `packages/` version), identify impacted learning modules.
2.  **Versioning**: Ensure learning materials reflect the current version of the software. Use callouts for version-specific instructions.
3.  **Deprecation**: Mark old patterns as "Deprecated" or remove them if they are no longer supported.

## Synchronization

- **Code Snippets**: Never hardcode long code snippets in markdown if possible. Reference actual files in `packages/shared/examples` or `packages/*/examples`.
- **Validation**: Run the `scripts/validate_links.py` (if available) to ensure all file references point to existing files.
