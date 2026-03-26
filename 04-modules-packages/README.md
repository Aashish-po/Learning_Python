# Modules and Packages

Organizing code into reusable modules.

## 📖 Topics Covered

- Creating modules
- Importing modules
- `__name__ == "__main__"` pattern
- Creating packages
- `__init__.py` files
- Relative vs absolute imports

---

## 🎯 Key Concepts

### Creating a Module
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b
```

### Importing
```python
# Different import styles
import my_module
print(my_module.greet("Aashish"))

from my_module import greet
print(greet("Aashish"))

from my_module import greet as say_hello
print(say_hello("Aashish"))

from my_module import *  # Avoid this!
```

### Package Structure
```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

---

## 🏋️ Exercises

### Exercise 1: Math Utilities Module
```python
# Create a module with:
# - Basic math functions
# - Constants (PI, E)
# - Import and use in another file
```

### Exercise 2: Package Creation
```python
# Create a package with:
# - Multiple modules
# - Proper __init__.py
# - Demonstrate imports
```

---

## 🔗 Resources

- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [Real Python - Modules and Packages](https://realpython.com/python-modules-packages/)