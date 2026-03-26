"""
Functions Example

Demonstrates different ways to define and use functions in Python.
"""


def basic_function():
    """A simple function with no parameters."""
    return "Hello from a function!"


def function_with_params(name, age):
    """Function with parameters."""
    return f"{name} is {age} years old"


def function_with_defaults(name, greeting="Hello"):
    """Function with default parameters."""
    return f"{greeting}, {name}!"


def function_with_kwargs(name, **kwargs):
    """Function with keyword arguments."""
    result = f"Name: {name}\n"
    for key, value in kwargs.items():
        result += f"{key}: {value}\n"
    return result


def calculate_stats(numbers):
    """Function with multiple return values."""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0

    return total, count, average


def fibonacci(n):
    """Recursive function example."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Lambda functions
def square(x):
    return x**2


def add(x, y):
    return x + y


def demonstrate_functions():
    """Run all function examples."""
    print("=" * 60)
    print("FUNCTION EXAMPLES")
    print("=" * 60)

    # Basic function
    print("\n1. Basic function:")
    print(basic_function())

    # Function with parameters
    print("\n2. Function with parameters:")
    print(function_with_params("Aashish", 18))

    # Function with defaults
    print("\n3. Function with defaults:")
    print(function_with_defaults("Aashish"))
    print(function_with_defaults("Aashish", "Hi"))

    # Function with kwargs
    print("\n4. Function with kwargs:")
    print(function_with_kwargs("Aashish", age=18, city="Pokhara", country="Nepal"))

    # Multiple return values
    print("\n5. Multiple return values:")
    numbers = [1, 2, 3, 4, 5]
    total, count, avg = calculate_stats(numbers)
    print(f"Numbers: {numbers}")
    print(f"Total: {total}, Count: {count}, Average: {avg}")

    # Recursive function
    print("\n6. Recursive function (Fibonacci):")
    for i in range(10):
        print(f"fib({i}) = {fibonacci(i)}")

    # Lambda functions
    print("\n7. Lambda functions:")
    print(f"square(5) = {square(5)}")
    print(f"add(3, 4) = {add(3, 4)}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    demonstrate_functions()
    print("\n✓ All examples complete!")
