---
description: 'Guidelines for the Test-Driven Development (TDD) process and ZOMBIE testing methodology.'
applyTo: '**/*.py, **/tests/*.py'
---

# Test Implementation & TDD Process

This repository enforces a strict Test-Driven Development (TDD) workflow using the ZOMBIE methodology. This process ensures behavioral coverage and prevents implementation drift.

## Core Principle: Strict TDD

1. **Never write functional code without a failing test.**
2. **Only write enough code to pass the current test.**
3. **Refactor only on green.**
4. If functional code is implemented without tests, it MUST be rolled back and implemented following the TDD process.

## The ZOMBIE Methodology

When defining test cases, you must systematically brainstorm scenarios covering the following categories:

| Letter | Category | Description | Example |
| :--- | :--- | :--- | :--- |
| **Z** | Zero | Default behaviors, empty inputs, simple instantiation. | Calculator with no input returns 0. |
| **O** | One | Simple functionality, single unit, happy path. | Adding two small numbers. |
| **M** | Many | Complex scenarios, table-driven tests, multiple items. | Adding a list of numbers, complex formulas. |
| **B** | Boundary | Edge cases, limits, max/min values. | Division by zero, MAX_INT, empty lists. |
| **I** | Interface | API contract checks, invalid types, arguments outside schema. | Passing string to math function, check for graceful failure. |
| **E** | Exceptions | Error handling, missing dependencies, external failures. | Service provider unavailable, file not found. |

## Development Workflow

Follow this cycle for every feature:

### 1. Brainstorm & Plan
Analyze the requirements and list potential ZOMBIE test cases.
**Action**: Ask the user to confirm the plan if there is ambiguity.

### 2. Create Pending Tests
Implement a test file with **all** identified cases marked as pending (e.g., using `pytest.skip` or empty functions). Do not implement test logic yet.

### 3. Implement One Case (Red)
Pick the simplest failure (usually Zero or One). Write the full test logic.
**Verify**: Run the test using `just test <package>` and ensure it fails for the expected reason.

### 4. Implement Code (Green)
Write the **simplest possible code** to make that specific test pass. Do not over-engineer.
**Verify**: Run the test and ensure it passes.

### 5. Iterate
Repeat steps 3-4 for the next test case in the ZOMBIE list. Refer to [.github/instructions/python-tests.instructions.md](.github/instructions/python-tests.instructions.md) for implementation mechanics.

## Static Analysis Enforcement

**RUN CHECKS**: You must run the static analysis suite to catch type errors immediately after implementation.

1. **Command**: Use `just check` (or `just typecheck <package_name>`) after every implementation step.
2. **Fix Errors**: If `just check` fails, **stop**. Fix the type errors before proceeding. Do not ignore them.
