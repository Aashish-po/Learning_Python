name = "Aashish"
age = 25
is_student = True

user_name = "Aashish"  # lowercase with underscores (Python style)
userName = "Aashish"  # camelCase (works but not Python style)
age2 = 30  # numbers are OK (not at start)
_private = "secret"  # underscore at start is OK

# Start with one value
score = 0
print(score)  # Shows: 0

# Change it
score = 10
print(score)  # Shows: 10

# Change it again
score = score + 5
print(score)  # Shows: 15

# This is a comment
print("Hello")  # This is also a comment

# You can have multiple lines
# of comments by starting
# each line with a hash

age = 25  # Store user's age
print(age)  # Output the age

"""
This is a multi-line comment.
It can span several lines.
Great for longer explanations.
"""


def calculate_tip(bill):
    """
    Calculate 20% tip for a restaurant bill.
    Takes the bill amount and returns the tip.
    """
    return bill * 0.20


bill_amount = 50
tip = calculate_tip(bill_amount)
print(f"The tip for a ${bill_amount} bill is: ${tip:.2f}")


# Integers - Whole numbers without decimals
age = 25
score = -10
print(age)  # Shows: 25
print(score)  # Shows: -10


# Floats - Numbers with decimal points
price = 19.99
temperature = -5.5
pi = 3.14159
print(price)  # Shows: 19.99
print(temperature)  # Shows: -5.5
print(pi)  # Shows: 3.14159


# Addition and subtraction
total = 10 + 5  # 15
change = 20 - 7  # 13

# Multiplication and division
area = 6 * 4  # 24
half = 10 / 2  # 5.0 (always returns float)

# Powers
squared = 5**2  # 25
cubed = 2**3  # 8

# Regular division (always float)
result = 10 / 3  # 3.333...

# Integer division (rounds down)
result = 10 // 3  # 3

# Regular division (always float)
result = 10 / 3  # 3.333...

# Integer division (rounds down)
result = 10 // 3  # 3


# Even when dividing evenly
result = 10 / 2
print(result)  # 5.0 (not 5)
print(type(result))  # <class 'float'>

# Use // for integer result
result = 10 // 2  # 5
print(result)  # 5
print(type(result))  # <class 'int'>


# Wrong
million = 1, 000, 000  # Creates a tuple, not a number!

# Right
million = 1000000  # Hard to read
million = 1_000_000  # Python style
print(million)  # Shows: 1000000

name = "Aashish"
message = "Hello, World!"
print(name)  # Shows: Aashish
print(message)  # Shows: Hello, World!


# Single quotes
first = "Python"

# Double quotes
second = "Python"

# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""
