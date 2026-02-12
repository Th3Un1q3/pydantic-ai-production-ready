---
spec-id: SPEC-002
title: Add GitHub Copilot Hooks for Markdown Linting with Auto-Fix
type: change
status: implemented
created: 2026-02-11
affected-areas: repository configuration (.github/hooks/)
author: GitHub Copilot
---

## Specification Progress

- [x] Complete discovery phase
- [x] Determine specification type
- [x] Draft specification from template
- [x] Validate against quality standards
- [x] Finalize specification

## Implementation Progress

- [x] Phase 1: Preparation - Install markdownlint-cli, create config
- [x] Phase 2: Implementation - Create hooks.json, add just lint-md command
- [x] Phase 3: Cleanup & Documentation - Update CONTRIBUTING.md, README.md
- [x] Final validation - All deliverables complete

## Executive Summary

### Problem Statement

GitHub Copilot consistently produces markdown content that fails linting checks, leading to manual fixes that are time-consuming and error-prone. Instructing Copilot to produce compliant markdown is exhausting, and using tool calls for linting is too slow for efficient workflow. There is a need for a deterministic, automated hook that automatically fixes markdown formatting issues after file edits.

### Proposed Change

Implement GitHub Copilot hooks using the postToolUse hook to automatically run markdownlint with auto-fix on markdown files after any file editing operations. This will ensure all markdown content adheres to linting standards without manual intervention.

### Success Criteria

- Markdown files edited by Copilot are automatically linted and fixed
- Reduction in manual markdown formatting fixes by 90%
- No performance degradation in Copilot's response times
- All existing markdown files continue to pass linting checks

## Current State

### Existing Behavior

Currently, markdown files are created and edited manually or by Copilot without automatic linting. Linting issues are only caught during CI/CD pipelines or manual checks, requiring developers to manually fix formatting problems.

### Issues with Current State

| Issue                                   | Impact                                               | Evidence                                      |
| --------------------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| Inconsistent markdown formatting        | High - affects documentation quality and readability | Frequent PR comments on markdown formatting   |
| Manual intervention required            | Medium - slows down development workflow             | Time spent on manual fixes instead of coding  |
| Copilot produces non-compliant markdown | High - undermines automation benefits                | Observed in multiple file edits               |

### Affected Components

| Component                | Location                       | Impact                              |
| ------------------------ | ------------------------------ | ----------------------------------- |
| Repository configuration | `.github/hooks/`               | New hooks configuration added       |
| Devcontainer setup       | `.devcontainer/post-create.sh` | markdownlint-cli installation added |
| Markdown files           | `**/*.md`                      | Automatic formatting applied        |

## Proposed State

### New Behavior

After any file editing operation by Copilot, the postToolUse hook will automatically run `just lint-md`, which executes `markdownlint --fix */**.md` to lint and fix all markdown files in the repository, ensuring they conform to the project's linting standards.

### Changes Overview

| Change                     | Before                        | After                                              |
| -------------------------- | ----------------------------- | -------------------------------------------------- |
| Markdown editing workflow  | Manual linting and fixes      | Automatic linting and auto-fix                     |
| Copilot markdown output    | May contain linting errors    | Always lint-compliant                              |
| Developer workflow         | Check and fix markdown issues | Focus on content, formatting handled automatically |

### Code Changes

```json
// .github/hooks/hooks.json (new file)
{
  "version": 1,
  "hooks": {
    "postToolUse": [
      {
        "type": "command",
        "bash": "just lint-md",
        "cwd": ".",
        "timeoutSec": 30
      }
    ]
  }
}
```

```bash
# .devcontainer/post-create.sh (modification)
# Add after existing installations:
if ! command -v markdownlint &> /dev/null; then
    echo "Installing markdownlint-cli..."
    npm install -g markdownlint-cli
fi
```

## Migration Strategy

### Backward Compatibility

- [x] Change is backward compatible
- [ ] Deprecation warnings added (if applicable)
- [ ] Migration guide provided (if breaking)

### Migration Steps

1. Modify `.devcontainer/post-create.sh` to install `markdownlint-cli` globally using npm
2. Add `lint-md` command to root `justfile` for markdown linting
3. Create `.markdownlint.json` configuration file
4. Create `.github/hooks/hooks.json` with the hook configuration
5. Test the hook with a sample markdown edit

## Implementation Plan

### Phase 1: Preparation

**Deliverables**:

- [ ] Verify Node.js and npm are available in devcontainer (pre-installed)
- [ ] Modify `.devcontainer/post-create.sh` to install `markdownlint-cli` globally
- [ ] Create `.markdownlint.json` configuration file
- [ ] Test markdownlint --fix command locally

**Validation**:

- markdownlint --fix works on sample files
- Configuration file is valid
- Devcontainer rebuild installs markdownlint successfully

### Phase 2: Implementation

**Deliverables**:

- [ ] Create .github/hooks/hooks.json
- [ ] Add `lint-md` command to root justfile
- [ ] Ensure `markdownlint-cli` is installed via devcontainer rebuild
- [ ] Test hook execution with sample edits

**Validation**:

- Hook triggers on markdown file changes
- Files are automatically fixed
- No errors in hook execution

### Phase 3: Cleanup & Documentation

**Deliverables**:

- [ ] Update CONTRIBUTING.md with markdown standards
- [ ] Document the hook in README.md
- [ ] Add troubleshooting section for hook issues

**Validation**:

- Documentation is clear and accurate
- Hook behavior is well-documented

## Testing Strategy

### Regression Tests

- [ ] All existing markdown files pass linting after hook application
- [ ] No unintended changes to non-markdown files
- [ ] Hook only runs when markdown files are modified

### New Tests

| Test                    | Purpose                                                  |
| ----------------------- | -------------------------------------------------------- |
| Hook trigger test       | Validates hook runs on markdown file edits               |
| Auto-fix validation     | Confirms linting errors are automatically resolved       |
| Performance test        | Ensures hook doesn't significantly slow down edits       |

### Performance Tests (if applicable)

| Metric              | Before   | Target          |
| ------------------- | -------- | --------------- |
| Edit response time  | Baseline | <5% increase    |

## Risk Assessment

### Risks

| Risk                   | Probability | Impact | Mitigation                                            |
| ---------------------- | ----------- | ------ | ----------------------------------------------------- |
| Hook execution errors  | Low         | Medium | Add error handling and logging to hook                |
| Over-aggressive fixing | Low         | Medium | Test with various markdown patterns before deployment |
| Performance impact     | Medium      | Low    | Monitor and optimize hook execution time              |

### Rollback Plan

If the change causes issues:

1. Remove or disable the hook in hooks.json
2. Manually run markdownlint --fix on affected files
3. Review and adjust markdownlint configuration

## Constraints

### Technical Constraints

- Must use markdownlint with auto-fix capability
- Hook must be compatible with GitHub Copilot's hook system
- Configuration must be explicit and version-controlled

### Non-Goals

- Implementing custom linting rules beyond standard markdownlint
- Modifying Copilot's content generation behavior
- Adding hooks for other file types at this time

## Review Checklist

Before implementation:

- [ ] markdownlint configuration reviewed and approved
- [ ] Hook syntax validated
- [ ] Test cases identified

After implementation:

- [ ] Hook executes without errors
- [ ] Markdown files are properly formatted
- [ ] No performance regressions observed

## References

- [GitHub Copilot Hooks documentation](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide#using-hooks)
- [markdownlint-cli documentation](https://github.com/igorshubovych/markdownlint-cli)
- [Devcontainer documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [markdownlint configuration](https://github.com/DavidAnson/markdownlint#configuration)
- Project's existing linting setup
