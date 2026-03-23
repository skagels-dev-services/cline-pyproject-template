---
description: Python coding style guidelines (PEP 8, Ruff, Black)
author: Claude
version: 1.0
category: "Language-Specific"
tags: ["python", "style", "pep8", "ruff", "black"]
globs: ["**/*.py"]
---

# Python Style Guide

## Code Formatting (Automated)

- Use **Black** for code formatting (line-length: 100)
- Use **Ruff** for linting
- Run `ruff check .` before committing
- Run `black .` to fix formatting issues

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Functions | snake_case | `def calculate_total()` |
| Variables | snake_case | `user_name = "Alice"` |
| Classes | PascalCase | `class UserService` |
| Constants | UPPER_SNAKE | `MAX_RETRY_COUNT = 3` |
| Private methods | _prefix | `def _internal_method()` |
| Modules | short, lowercase | `utils.py`, `helpers.py` |

## Imports

```python
# Standard library
import os
import sys
from typing import Optional, List

# Third party
import pytest
from fastapi import APIRouter

# Local application
from src.models import User
from src.utils import format_date
```

- Use `isort` (via Ruff) for import sorting
- Group: standard library → third party → local
- Avoid wildcard imports: `from module import *`

## Type Hints

```python
# Good - explicit types
def greet(name: str) -> str:
    return f"Hello, {name}"

def process_items(items: List[int]) -> dict[str, int]:
    return {"sum": sum(items)}

# Optional types
def find_user(user_id: int) -> Optional[User]:
    ...

# Use typing module for complex types
from typing import Optional, Union, Callable
```

## Functions

- Keep functions small and focused (single responsibility)
- Use type hints for all function arguments and return values
- Maximum 50 lines per function
- Document complex logic with docstrings

## Classes

```python
class UserService:
    """Service for managing user operations."""
    
    def __init__(self, db: Database) -> None:
        self._db = db  # Private attribute
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieve user by ID."""
        ...
```

## Error Handling

```python
# Preferred - specific exceptions
try:
    result = fetch_data()
except ValueError as e:
    logger.error(f"Invalid input: {e}")
    raise CustomError("Failed to fetch data") from e

# Avoid bare except
try:
    risky_operation()
except Exception:  # BAD - too broad
    pass
```

## Constants and Magic Numbers

```python
# Good - named constants
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30

# Bad - magic numbers
for i in range(3):  # What does 3 mean?
    ...
```

## Documentation

```python
def calculate_metrics(data: list[float]) -> dict[str, float]:
    """Calculate statistical metrics for the provided data.
    
    Args:
        data: List of numeric values to analyze.
        
    Returns:
        Dictionary containing mean, median, and std dev.
        
    Raises:
        ValueError: If data list is empty.
    """
    if not data:
        raise ValueError("Data list cannot be empty")
    
    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "std": statistics.stdev(data),
    }