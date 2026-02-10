# Validation Patterns

Patterns for validating implementations against specification criteria.

## Acceptance Criteria Validation

### Pattern: Checklist Verification

For each acceptance criterion in a user story:

1. **Identify the criterion type**:
   - Functional: Test with unit/integration test
   - Performance: Use dedicated perf tests/benchmarks (e.g., pytest-benchmark)
   - Documentation: Manual verification

2. **Create verification method**:

```python
# Functional criteria → pytest
def test_search_returns_result():
    result = search("query")
    assert result is not None

# Performance criteria → dedicated perf/benchmark test (not regular unit test)
# Use pytest-benchmark or dedicated perf runs for stable measurements
# Wall-clock assertions in regular tests are often flaky across CI environments
def test_search_latency_benchmark(benchmark):
    """Performance test using pytest-benchmark for stable measurements."""
    def _run():
        search("query")
    
    result = benchmark(_run)
    # Check benchmark results with generous margins for CI variability
```

> **Note**: Avoid hard-coded time assertions in regular tests (e.g., `assert elapsed < 0.5`).
> These are flaky across CI environments and produce non-deterministic failures.
> Reserve strict latency SLO checks for controlled performance runs.

3. **Document verification status**:

```markdown
### Story: Search Results

**Acceptance Criteria:**
- [x] Search endpoint returns results within 500ms ✓ (verified: test_search_performance.py)
- [x] Results are ranked by relevance score ✓ (verified: test_search_ranking.py)
- [ ] Empty query returns validation error ⏳ (in progress)
```

## Success Criteria Validation

Success criteria from the Executive Summary must be measurable. Use this pattern:

| Criterion | Measurement Method | Target | Actual | Status |
|-----------|-------------------|--------|--------|--------|
| Response time < 200ms | `just test` | <200ms | 185ms | ✓ PASS |
| Test coverage > 90% | `just test` | >90% | 92% | ✓ PASS |
| Zero type errors | `just check` | 0 | 0 | ✓ PASS |

## Phase Gate Validation

Before proceeding to the next phase, run validation gates:

### Standard Validation Gate

```bash
# Run after each phase
just check
just lint {package}
just test {package}
```

### Extended Validation (for production-critical phases)

```bash
# Full validation
just test
just check
just lint
```

## Iterative Refinement Pattern

When implementation doesn't meet criteria:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Implement → Validate → [PASS] → Continue to next phase     │
│      │                                                       │
│      └── [FAIL] → Analyze → Refine → Re-validate            │
│                      │                    │                  │
│                      │                    └── (max 3 loops)  │
│                      │                                       │
│                      └── If still failing → Report blocker  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Failure Analysis Template

When validation fails, document:

```markdown
## Validation Failure Report

**Phase**: 2 - Core Implementation
**Criterion**: Response time < 200ms
**Attempt**: 2 of 3

### Observation
Response time is 350ms, exceeding target by 75%.

### Root Cause Analysis
1. Database query is not using index
2. N+1 query pattern in relationship loading

### Refinement Plan
1. Add database index on `search_field`
2. Use eager loading for relationships

### Re-validation Result
After refinement: 180ms ✓ PASS
```

## Regression Testing

Ensure changes don't break existing functionality:

```bash
# Before implementing changes
just test > baseline_results.txt

# After implementing changes
just test > new_results.txt

# Compare (no new failures allowed)
diff baseline_results.txt new_results.txt
```

## Documentation Validation

Verify documentation accuracy:

| Check | Method | Status |
|-------|--------|--------|
| Examples executable | Run in Python REPL | ✓/✗ |
| Links valid | Check href targets exist | ✓/✗ |
| API docs match code | Compare signatures | ✓/✗ |
| README up to date | Manual review | ✓/✗ |

## Completion Verification

Final checklist before marking specification as `implemented`:

```markdown
## Implementation Complete Checklist

### Code
- [ ] All phases completed
- [ ] All tests pass
- [ ] Type checking passes
- [ ] Linting passes

### Specification Compliance
- [ ] All acceptance criteria verified
- [ ] All success criteria met
- [ ] Non-goals confirmed not implemented

### Documentation  
- [ ] Package README updated
- [ ] API documentation accurate
- [ ] Examples tested and working
- [ ] CHANGELOG updated

### Quality
- [ ] Code coverage meets target
- [ ] No TODO/FIXME comments unresolved
- [ ] No security issues identified
```
