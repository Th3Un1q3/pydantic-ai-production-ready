# Contributing to Pydantic AI Production Ready

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest features
- Provide clear, detailed descriptions
- Include reproduction steps for bugs
- Tag issues appropriately

### Adding Learning Materials

1. **Choose a Module**: Determine which module your content fits into
2. **Follow the Structure**: Use the module template in `learning/README.md`
3. **Write Clear Content**: 
   - Use simple language
   - Include code examples
   - Test all examples
4. **Add Exercises**: Provide hands-on practice opportunities
5. **Update Documentation**: Update module READMEs

### Contributing Code

1. **Fork the Repository**
2. **Create a Branch**: `git checkout -b feature/your-feature-name`
3. **Make Changes**: Follow the coding standards below
4. **Test Your Changes**: Run the test suite
5. **Submit a Pull Request**

## Coding Standards

### Python Code

- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for classes and functions
- Use `black` for formatting: `uv run black .`
- Use `ruff` for linting: `uv run ruff check --fix .`
- Use `mypy` for type checking: `uv run mypy src`

### Documentation

- Write clear, concise documentation
- Include code examples that work
- Use proper markdown formatting
- Link to related content

## Development Workflow

1. **Setup Environment**
   ```bash
   # Use devcontainer (recommended)
   # OR
   cd projects
   uv sync --all-extras
   ```

2. **Make Changes**
   ```bash
   # Edit files
   # Add tests
   ```

3. **Run Tests**
   ```bash
   cd projects
   uv run pytest
   ```

4. **Format and Lint**
   ```bash
   uv run black .
   uv run ruff check --fix .
   uv run mypy src
   ```

5. **Commit**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md if applicable
5. Request review from maintainers

## Code Review

- Be respectful and constructive
- Focus on the code, not the person
- Explain your reasoning
- Be open to feedback

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion in GitHub Discussions
- Reach out to maintainers

Thank you for contributing! 🎉
