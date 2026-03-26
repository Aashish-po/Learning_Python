# Python Cheatsheet

Quick reference for Python syntax and common patterns.

> **Note:** This cheatsheet focuses on practical patterns I use daily, not exhaustive documentation.

## Table of Contents
- [Variables & Types](#variables--types)
- [Strings](#strings)
- [Lists](#lists)
- [Dictionaries](#dictionaries)
- [Sets & Tuples](#sets--tuples)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Classes](#classes)
- [File I/O](#file-io)
- [Error Handling](#error-handling)
- [Common Patterns](#common-patterns)

---

## Variables & Types
```python
# Assignment
name = "Aashish"
age = 18
height = 5.8
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Type conversion
age_str = str(age)          # "18"
num = int("42")             # 42
pi = float("3.14")          # 3.14
bool_val = bool(1)          # True

# Type checking
type(age)                   # <class 'int'>
isinstance(age, int)        # True
```

---

## Strings
```python
# Creation
name = "Aashish"
message = 'Hello'
multiline = """This is
a multiline
string"""

# F-strings (preferred)
greeting = f"Hello, {name}!"
calc = f"2 + 2 = {2 + 2}"

# String methods
text = "hello world"
text.upper()                # "HELLO WORLD"
text.capitalize()           # "Hello world"
text.title()                # "Hello World"
text.lower()                # "hello world"
text.strip()                # Remove whitespace
text.replace("world", "Python")  # "hello Python"
text.split()                # ["hello", "world"]
text.split(",")             # Split by comma

# Joining
words = ["hello", "world"]
" ".join(words)             # "hello world"
"-".join(words)             # "hello-world"

# Checking
text.startswith("hello")    # True
text.endswith("world")      # True
"hello" in text             # True
text.isdigit()              # False
text.isalpha()              # False

# Slicing
text = "Python"
text[0]                     # "P"
text[-1]                    # "n"
text[0:2]                   # "Py"
text[2:]                    # "thon"
text[:4]                    # "Pyth"
text[::-1]                  # "nohtyP" (reverse)
```

---

## Lists
```python
# Creation
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
empty = []
range_list = list(range(10))  # [0, 1, 2, ..., 9]

# Access
first = numbers[0]          # 1
last = numbers[-1]          # 5
middle = numbers[1:4]       # [2, 3, 4]

# Modify
numbers.append(6)           # Add to end
numbers.extend([7, 8])      # Add multiple
numbers.insert(0, 0)        # Insert at position
numbers.remove(3)           # Remove first occurrence
popped = numbers.pop()      # Remove and return last
popped = numbers.pop(0)     # Remove and return index

# Other operations
numbers.sort()              # Sort in place
numbers.reverse()           # Reverse in place
sorted_nums = sorted(numbers)  # Return sorted copy
reversed_nums = list(reversed(numbers))  # Return reversed copy

# Checking
3 in numbers                # True
len(numbers)                # Length
numbers.count(3)            # Count occurrences
numbers.index(3)            # Find index

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(3)]
```

---

## Dictionaries
```python
# Creation
user = {
    "name": "Aashish",
    "age": 18,
    "city": "Pokhara"
}
empty = {}
dict_comp = {x: x**2 for x in range(5)}

# Access
name = user["name"]                    # "Aashish" (KeyError if missing)
age = user.get("age")                  # 18
email = user.get("email", "no email")  # Default value

# Modify
user["email"] = "aashish@example.com"  # Add/update
user.update({"phone": "123-456"})      # Update multiple
del user["city"]                       # Delete key
popped = user.pop("age")               # Remove and return

# Checking
"name" in user              # True
"email" not in user         # False
len(user)                   # Number of keys

# Iterate
for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in user.items() if v is not None}
```

---

## Sets & Tuples
```python
# Sets (unique, unordered)
numbers = {1, 2, 3, 4, 5}
unique = set([1, 1, 2, 2, 3])  # {1, 2, 3}

# Set operations
numbers.add(6)
numbers.remove(1)              # KeyError if not exists
numbers.discard(1)             # No error if not exists

# Set math
a = {1, 2, 3}
b = {3, 4, 5}
a | b                          # Union: {1, 2, 3, 4, 5}
a & b                          # Intersection: {3}
a - b                          # Difference: {1, 2}
a ^ b                          # Symmetric difference: {1, 2, 4, 5}

# Tuples (immutable)
coords = (10, 20)
person = ("Aashish", 18, "Pokhara")

# Access
x = coords[0]
name, age, city = person       # Unpacking
```

---

## Control Flow
```python
# If/elif/else
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# For loops
for i in range(5):
    print(i)

for item in items:
    print(item)

for i, item in enumerate(items):
    print(f"{i}: {item}")

for key, value in dict.items():
    print(f"{key}: {value}")

# While loops
count = 0
while count < 5:
    print(count)
    count += 1

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)

# Else with loops
for i in range(5):
    print(i)
else:
    print("Loop completed normally")
```

---

## Functions
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Type hints
def add(a: int, b: int) -> int:
    return a + b

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

min_val, max_val, total = get_stats([1, 2, 3])

# *args and **kwargs
def func(*args, **kwargs):
    print(f"Args: {args}")      # Tuple
    print(f"Kwargs: {kwargs}")  # Dict

func(1, 2, 3, name="Aashish", age=18)

# Lambda functions
square = lambda x: x**2
add = lambda x, y: x + y

# Map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Better: Use comprehensions
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

---

## Classes
```python
class Person:
    """Represent a person."""
    
    # Class variable
    species = "Human"
    
    def __init__(self, name, age):
        """Initialize person."""
        self.name = name
        self.age = age
    
    def greet(self):
        """Return greeting."""
        return f"Hi, I'm {self.name}"
    
    def __str__(self):
        """String representation."""
        return f"Person({self.name}, {self.age})"
    
    def __repr__(self):
        """Developer representation."""
        return f"Person('{self.name}', {self.age})"

# Usage
person = Person("Aashish", 18)
print(person.greet())
print(person)
```

---

## File I/O
```python
# Read file
with open('file.txt', 'r') as f:
    content = f.read()          # Read entire file
    # or
    lines = f.readlines()       # Read as list of lines
    # or
    for line in f:
        print(line.strip())     # Process line by line

# Write file
with open('file.txt', 'w') as f:
    f.write("Hello\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Append
with open('file.txt', 'a') as f:
    f.write("Appended line\n")

# CSV
import csv

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['column'])

# Write CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerow({'name': 'Aashish', 'age': 18})

# JSON
import json

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Write JSON
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

---

## Error Handling
```python
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    # risky code
    pass
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch all (use sparingly)
try:
    # risky code
    pass
except Exception as e:
    print(f"Error: {e}")

# Else and finally
try:
    result = operation()
except ValueError:
    print("Invalid value")
else:
    # Runs if no exception
    print("Success!")
finally:
    # Always runs
    cleanup()

# Raising exceptions
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## Common Patterns
```python
# Enumerate
for i, item in enumerate(items):
    print(f"{i}: {item}")

# Zip
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Any/All
has_negative = any(x < 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]

# Dict comprehension
squares = {x: x**2 for x in range(5)}

# Set comprehension
unique = {x % 3 for x in range(10)}

# Generator expression (memory efficient)
gen = (x**2 for x in range(1000000))

# Unpacking
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2,3,4,5]
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5

# Walrus operator (Python 3.8+)
if (n := len(items)) > 10:
    print(f"List is long: {n} items")

# Context managers
class DatabaseConnection:
    def __enter__(self):
        # Setup
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup
        pass

with DatabaseConnection() as db:
    # Use db
    pass
```

---

## Quick Tips

### Do's
✅ Use f-strings for formatting  
✅ Use list comprehensions when readable  
✅ Use `with` for file operations  
✅ Use `enumerate()` instead of `range(len())`  
✅ Use `.get()` for dictionaries  
✅ Use type hints for clarity  

### Don'ts
❌ Don't use bare `except`  
❌ Don't use mutable default arguments  
❌ Don't modify list while iterating  
❌ Don't use `==` to compare to `None` (use `is`)  
❌ Don't use `from module import *`  

---

*Last Updated: March 2026*