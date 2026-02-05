# Package Specification Template

<!--
Use this template for new packages or major components.
Replace all placeholders in {{BRACKETS}}.
Delete helper comments before finalizing.
-->

---
spec-id: SPEC-{{ID}}
title: {{Package Name}}
type: package
status: draft
created: {{YYYY-MM-DD}}
author: {{author}}
---

## Executive Summary

### Problem Statement

{{Describe the problem this package addresses.}}

### Proposed Solution

{{Describe the package and its primary purpose.}}

### Success Criteria

- {{KPI 1: e.g., Package installable and functional within 2 weeks}}
- {{KPI 2: e.g., 90%+ test coverage}}
- {{KPI 3: e.g., Documentation complete with 3+ usage examples}}

## Package Overview

### Name

`{{package-name}}`

### Description

{{One paragraph describing what this package does and why it exists.}}

### Target Users

| Persona | Use Case |
|---------|----------|
| {{Persona 1}} | {{How they use this package}} |
| {{Persona 2}} | {{How they use this package}} |

## Architecture

### Package Structure

```
packages/{{package-name}}/
├── src/
│   └── {{package_name}}/
│       ├── __init__.py
│       ├── {{module1}}.py
│       └── {{module2}}.py
├── tests/
│   ├── test_{{module1}}.py
│   └── test_{{module2}}.py
├── pyproject.toml
└── README.md
```

### Core Components

| Component | Purpose | Key Interfaces |
|-----------|---------|----------------|
| {{Component 1}} | {{Purpose}} | `{{Interface}}` |
| {{Component 2}} | {{Purpose}} | `{{Interface}}` |

### Data Flow

```
{{Input}} → {{Component 1}} → {{Component 2}} → {{Output}}
```

## API Design

### Public Interface

```python
# Main entry point
class {{MainClass}}:
    """{{Description}}."""
    
    def __init__(self, {{params}}):
        """Initialize the {{component}}.
        
        Args:
            {{param}}: {{description}}
        """
        ...
    
    async def {{primary_method}}(self, {{params}}) -> {{ReturnType}}:
        """{{Description}}.
        
        Args:
            {{param}}: {{description}}
            
        Returns:
            {{description of return value}}
        """
        ...
```

### Models

```python
from pydantic import BaseModel

class {{ModelName}}(BaseModel):
    """{{Description}}."""
    
    {{field1}}: {{type}}
    {{field2}}: {{type}}
```

## Dependencies

### External Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| pydantic-ai | >=0.1.0 | {{Purpose}} |
| {{package}} | {{version}} | {{Purpose}} |

### Internal Dependencies

| Package | Purpose |
|---------|---------|
| pydantic-ai-shared | Shared configuration and utilities |

## User Stories

### Story 1: Basic Usage

As a {{user type}}, I want to {{action}} so that {{benefit}}.

**Acceptance Criteria:**

- [ ] {{Criterion 1}}
- [ ] {{Criterion 2}}

### Story 2: Advanced Usage

As a {{user type}}, I want to {{action}} so that {{benefit}}.

**Acceptance Criteria:**

- [ ] {{Criterion 1}}
- [ ] {{Criterion 2}}

## Implementation Plan

### Phase 1: Scaffold & Core

**Deliverables:**

- [ ] Package scaffold created with pyproject.toml
- [ ] Core data models defined
- [ ] Basic agent structure implemented
- [ ] Unit tests for models

**Validation:**

- `just test {{package-name}}` passes
- `just check` passes

### Phase 2: Feature Implementation

**Deliverables:**

- [ ] Primary functionality implemented
- [ ] Integration with shared package
- [ ] Integration tests added

**Validation:**

- All user stories have passing tests
- `just lint {{package-name}}` passes

### Phase 3: Documentation & Integration

**Deliverables:**

- [ ] README.md with usage examples
- [ ] API documentation
- [ ] Added to monorepo README
- [ ] Learning module link (if applicable)

**Validation:**

- Documentation is accurate and complete
- Examples are executable

## Testing Strategy

### Unit Tests

- Model validation tests
- Business logic tests
- Error handling tests

### Integration Tests

- End-to-end workflow tests
- External service mock tests

### ZOMBIE Coverage

- **Zero**: Empty inputs, default states
- **One**: Single item happy paths
- **Many**: Multiple items, complex scenarios
- **Boundary**: Edge cases, limits
- **Interface**: API contract validation
- **Exceptions**: Error scenarios

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `{{VAR_NAME}}` | {{Yes/No}} | {{default}} | {{description}} |

### Configuration File

```python
# Example configuration
class {{PackageName}}Config(BaseModel):
    """Configuration for {{package-name}}."""
    
    {{field}}: {{type}} = {{default}}
```

## Constraints

### Technical Constraints

- Must follow monorepo conventions
- Must use pydantic-ai for agent implementation
- Must integrate with shared configuration

### Non-Goals

- {{Non-goal 1}}
- {{Non-goal 2}}

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| {{Risk 1}} | {{Impact}} | {{Mitigation}} |

## References

- [Monorepo Guide](../../packages/README.md)
- [Pydantic AI Documentation](https://ai.pydantic.dev/)
- {{Additional references}}
