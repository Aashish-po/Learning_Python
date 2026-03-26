# Object-Oriented Programming

Building reusable, maintainable code with classes.

## 📖 Topics Covered

### Classes and Objects
- Class definition with `class` keyword
- `__init__()` constructor
- Instance attributes vs class attributes
- `self` parameter

### Methods
- Instance methods
- Class methods (`@classmethod`)
- Static methods (`@staticmethod`)
- Special methods (`__str__`, `__repr__`)

### Inheritance
- Creating child classes
- Overriding methods
- `super()` function
- Multiple inheritance

### When to Use Classes
- Classes vs functions decision framework
- Single Responsibility Principle
- Avoiding over-engineering

---

## 🎯 Key Concepts

### Basic Class Structure
```python
class Student:
    """Represent a student."""
    
    # Class variable (shared by all instances)
    school = "Nepal University"
    
    def __init__(self, name, age):
        """Constructor - runs when creating instance."""
        self.name = name  # Instance variable
        self.age = age
    
    def study(self, subject):
        """Instance method."""
        return f"{self.name} is studying {subject}"
    
    def __str__(self):
        """String representation."""
        return f"Student({self.name}, {self.age})"

# Create instances
student1 = Student("Aashish", 18)
student2 = Student("Alice", 20)

# Each has independent data
print(student1.study("Python"))
print(student2.study("Math"))
```

### When to Use Classes

✅ **Use classes when:**
- Maintaining state between operations
- Creating multiple instances with similar behavior
- Grouping related data and functions
- Modeling real-world objects

❌ **Use functions when:**
- Simple transformations (input → output)
- Stateless operations
- One-off calculations

---

## 🏋️ Exercises

### Exercise 1: Bank Account Class
```python
# Create a BankAccount class with:
# - owner, balance attributes
# - deposit(), withdraw() methods
# - Check for sufficient funds
# - Track transaction history
```

### Exercise 2: Shopping Cart
```python
# Create classes:
# - Product (name, price)
# - ShoppingCart (add_item, remove_item, get_total)
# - Apply discounts
```

### Exercise 3: Student Grade System
```python
# Create Student class with:
# - Add grades for subjects
# - Calculate average
# - Get letter grade
# - Compare students
```

---

## 🔗 Resources

- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)