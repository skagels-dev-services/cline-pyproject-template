---
description: Comprehensive testing guidelines for Python projects
author: Claude
version: 1.0
category: "Development"
tags: ["testing", "pytest", "quality-assurance"]
globs: ["**/*.py", "**/test_*.py", "**/*_test.py"]
---

# Testing Strategy

## Core Directive
Tests are mandatory deliverables. Generate or update tests alongside code unless explicitly opts out.

Before completing any task, verify:
- [ ] New/modified code has corresponding test coverage
- [ ] Tests pass
- [ ] Edge cases and error paths are covered

## Test Pyramid

- **Unit Tests (70%)**: Test individual functions/methods in isolation, mock external dependencies
- **Integration Tests (20%)**: Test interactions between modules
- **E2E Tests (10%)**: Test critical user journeys

## Python-Specific (pytest)

```python
import pytest

class TestFeature:
    def test_happy_path(self):
        # Test valid inputs produce expected outputs
        pass
    
    def test_edge_cases(self):
        # Test empty, null, boundary values
        pass
    
    def test_error_handling(self):
        # Test invalid inputs raise appropriate errors
        with pytest.raises(ValueError, match="error message"):
            pass
```

## Quality Checklist

- [ ] Descriptive test names (describe scenario, not implementation)
- [ ] Follow Arrange-Act-Assert pattern
- [ ] No test interdependence (can run in any order)
- [ ] No hardcoded delays
- [ ] Tests are fast (<100ms each) and deterministic
