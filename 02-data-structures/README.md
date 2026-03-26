# Data Structures

Python's built-in data structures and their usage.

## Topics Covered

### Lists
- Creating and modifying lists
- List indexing and slicing
- List methods (`.append()`, `.extend()`, `.insert()`, etc.)
- List comprehensions
- Nested lists

### Dictionaries
- Key-value pairs
- Dictionary methods (`.get()`, `.keys()`, `.values()`, `.items()`)
- Dictionary comprehensions
- Nested dictionaries

### Sets
- Unique elements
- Set operations (union, intersection, difference)
- Set comprehensions

### Tuples
- Immutable sequences
- Tuple unpacking
- Named tuples

---

## Files in This Directory

- **`lists_example.py`** - List creation, slicing, methods, comprehensions, and nested lists
- **`dictionaries_example.py`** - Dictionary basics, methods, comprehensions, and nested dictionaries
- **`sets_example.py`** - Set uniqueness, operations, and set comprehensions
- **`tuples_example.py`** - Tuple immutability, unpacking, and named tuples
- **`practice_exercises.py`** - Worked examples for the exercises in this README

---

## Key Concepts

### List Comprehensions
```python
# Old way (verbose)
squares = []
for x in range(10):
    squares.append(x**2)

# Pythonic way (concise)
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
```

### Dictionary Power
```python
# Safe access with .get()
user = {"name": "Aashish", "age": 18}
email = user.get("email", "no-email@example.com")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = dict1 | dict2
```

### When to Use Each

| Data Structure | Use When | Example |
|---------------|----------|---------|
| **List** | Ordered, duplicate items | `[1, 2, 2, 3]` |
| **Dict** | Key-value pairs | `{"name": "Aashish"}` |
| **Set** | Unique items, fast lookup | `{1, 2, 3}` |
| **Tuple** | Immutable, fixed data | `(10, 20)` |

---

## Exercises

### Exercise 1: List Manipulation
```python
# Create a list of numbers 1-100
# Filter only even numbers
# Square each number
# Get sum of all squares
# Do it all in one line with list comprehension
```

### Exercise 2: Dictionary Operations
```python
# Create a student database (dict of dicts)
# Add students with name, age, grades
# Calculate average grade per student
# Find student with highest average
```

### Exercise 3: Set Operations
```python
# Given two lists of numbers
# Find common elements (intersection)
# Find unique to first list (difference)
# Find all unique elements (union)
```

---

## Resources

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)
