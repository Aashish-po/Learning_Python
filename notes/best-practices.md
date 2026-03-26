# Python Best Practices

Lessons learned and patterns that work.

## Code Style

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "Aashish"
def calculate_total(items):
    pass

# Classes: PascalCase
class UserAccount:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRY_COUNT = 3
API_BASE_URL = "https://api.example.com"

# Private: Leading underscore
class MyClass:
    def __init__(self):
        self._private_var = "internal use"
    
    def _private_method(self):
        pass
```

### Import Organization
```python
# Standard library
import os
import sys
from pathlib import Path

# Third-party packages
import pandas as pd
import requests

# Local imports
from my_module import MyClass
from .utils import helper_function
```

---

## Error Handling

### Validate Early
```python
# ❌ Bad
def process_data(data):
    result = []
    for item in data:
        result.append(transform(item))
    return result  # Crashes if data is None!

# ✅ Good
def process_data(data):
    if data is None:
        raise ValueError("Data cannot be None")
    
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    
    return [transform(item) for item in data]
```

### Be Specific
```python
# ❌ Bad
try:
    process()
except:  # Catches everything!
    pass

# ✅ Good
try:
    process()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
except FileNotFoundError as e:
    logger.error(f"File not found: {e}")
```

---

## Functions

### Single Responsibility
```python
# ❌ Bad
def process_and_save(data, filepath):
    cleaned = clean_data(data)
    transformed = transform_data(cleaned)
    save_to_file(transformed, filepath)

# ✅ Good
def process_data(data):
    cleaned = clean_data(data)
    return transform_data(cleaned)

def save_data(data, filepath):
    save_to_file(data, filepath)

# Usage
processed = process_data(data)
save_data(processed, filepath)
```

### Use Type Hints
```python
# ❌ Without hints
def calculate(a, b):
    return a + b

# ✅ With hints
def calculate(a: int, b: int) -> int:
    return a + b
```

---

## Classes

### When to Use

✅ **Use classes when:**
- Maintaining state between operations
- Creating multiple instances
- Grouping related data and behavior

❌ **Don't use classes when:**
- Simple transformation (use function)
- Only one method (use function)
- No shared state

---

## File Handling

### Always Use Context Managers
```python
# ❌ Bad
f = open('file.txt')
data = f.read()
f.close()  # Might not execute if error!

# ✅ Good
with open('file.txt') as f:
    data = f.read()
# Guaranteed to close
```

---

## Performance

### Use Comprehensions
```python
# Slower
result = []
for x in range(1000):
    result.append(x**2)

# Faster
result = [x**2 for x in range(1000)]
```

### Use Generators for Large Data
```python
# Memory intensive
def get_numbers(n):
    return [x for x in range(n)]

# Memory efficient
def get_numbers(n):
    for x in range(n):
        yield x
```

---

*More practices to be added as I learn!*