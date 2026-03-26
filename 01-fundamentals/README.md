# Python Fundamentals

Core Python syntax and basic concepts.

## 📖 Topics Covered

### Variables & Data Types
- Dynamic typing vs static typing (C++/Java)
- Type conversion and type checking
- Mutable vs immutable types
- Variable scope (local, global)

### Control Flow
- `if/elif/else` statements
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- `for` loops and `range()`
- `while` loops
- `break`, `continue`, `pass`

### Functions
- Function definition with `def`
- Parameters and arguments
- Return values
- Default parameters
- Keyword arguments
- `*args` and `**kwargs`
- Lambda functions

### Input/Output
- `print()` function
- `input()` for user input
- String formatting (f-strings, `.format()`, `%`)

---

## 📁 Files in This Directory

- **`Python_Basics.py`** - Variables, data types, basic operations
- **`hello.py`** - First Python program
- **`interactive_demo.py`** - Interactive Python features
- **`variables_example.py`** - Variable scope demonstration
- **`functions_example.py`** - Function examples

---

## 🎯 Key Concepts

### Dynamic Typing
```python
# Python uses dynamic typing
x = 5           # x is an integer
x = "hello"     # now x is a string
x = [1, 2, 3]   # now x is a list

# C++ requires type declaration
# int x = 5;
# x = "hello";  // Error!
```

### Indentation Matters
```python
# Python uses indentation for blocks
if condition:
    print("True")   # 4 spaces
    print("Still true")
else:
    print("False")

# C++/Java use braces
# if (condition) {
#     printf("True");
# }
```

### Everything is an Object
```python
# Even functions are objects
def greet():
    return "Hello"

# Can assign to variable
my_func = greet
print(my_func())  # "Hello"

# Can pass as argument
def call_function(func):
    return func()

call_function(greet)  # "Hello"
```

---

## 💡 Comparison with Other Languages

| Feature | Python | C++ | JavaScript |
|---------|--------|-----|------------|
| **Typing** | Dynamic | Static | Dynamic |
| **Syntax** | Indentation | Braces | Braces |
| **Variables** | No declaration | Type required | `let`/`const` |
| **Functions** | First-class | Not first-class | First-class |
| **Main** | Optional | Required | Optional |

---

## 🏋️ Exercises

### Exercise 1: Variables and Types
```python
# Create variables of different types
# Convert between types
# Check types with type() and isinstance()
```

### Exercise 2: Control Flow
```python
# Write a program that:
# 1. Asks user for a number
# 2. Prints if it's positive, negative, or zero
# 3. Prints if it's even or odd
```

### Exercise 3: Functions
```python
# Write a function that:
# 1. Takes a list of numbers
# 2. Returns the sum, average, min, and max
# Use multiple return values
```

### Exercise 4: Temperature Converter
```python
# Create functions to convert:
# - Celsius to Fahrenheit
# - Fahrenheit to Celsius
# - Celsius to Kelvin
# - Kelvin to Celsius
```

---

## 🔗 Resources

- [Python Tutorial - Basics](https://docs.python.org/3/tutorial/introduction.html)
- [Real Python - Python Basics](https://realpython.com/python-basics/)
- [W3Schools Python](https://www.w3schools.com/python/)

---

## 🚀 Next Steps

After mastering fundamentals, move to:
- **02-data-structures** - Lists, dicts, sets, tuples
- **03-oop** - Classes and objects