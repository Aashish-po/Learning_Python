"""Tiny script that mimics how variables persist between notebook-style steps."""


# Let's explore interactive mode
name = "Python Learner"
print(f"Hello, {name}!")

# Some data to work with
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Calculate something
total = sum(numbers)
print(f"Total: {total}")

# First, create a variable
message = "Hello"

# Later, reuse the same variable to show that interactive sessions keep state around.
print(message + " World!")

# Reassign the variable so learners can see that later steps read the newest value.
message = message.upper()
print(message)
