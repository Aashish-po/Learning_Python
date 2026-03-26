# Error Handling

Writing robust code that handles failures gracefully.

## 📖 Topics Covered

- `try`/`except` blocks
- Multiple exception types
- `else` and `finally` clauses
- Raising exceptions
- Custom exceptions
- Best practices for error handling

---

## 🎯 Key Concepts

### Basic Error Handling
```python
# Catch specific exception
try:
    age = int(input("Enter age: "))
except ValueError:
    print("That's not a valid number!")

# Catch multiple exceptions
try:
    process_data()
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
except FileNotFoundError:
    print("File not found")
```

### Complete Pattern
```python
try:
    # Try something risky
    result = risky_operation()
except SpecificError:
    # Handle the error
    print("Error occurred")
else:
    # Runs if no exception
    print("Success!")
finally:
    # Always runs (cleanup)
    cleanup()
```

### Custom Exceptions
```python
class InvalidAgeError(Exception):
    """Raised when age is invalid."""
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 150:
        raise InvalidAgeError("Age unrealistic")
    return age
```

---

## 🏋️ Exercises

### Exercise 1: Safe Calculator
```python
# Create a calculator that:
# - Handles division by zero
# - Handles invalid input
# - Handles unknown operators
# - Never crashes
```

### Exercise 2: File Processor
```python
# Create a file processor that:
# - Handles missing files
# - Handles permission errors
# - Handles corrupt data
# - Logs all errors
```

---

## 🔗 Resources

- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python - Exceptions](https://realpython.com/python-exceptions/)