# Variable names should be descriptive and follow Python's naming conventions:
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

# Variable names can be reused and updated:
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


# Join strings together with +:
first_name = "Aashish"
last_name = "Paudel"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # Aashish Paudel

# Repetition
stars = "*" * 5
print(stars)  # *****


# Use len() to count characters:
message = "Hello"
print(len(message))  # 5

empty = ""
print(len(empty))  # 0

# Use str() to convert numbers to strings:
age = 30
age_str = str(age)
print(age_str)  # "30"
print("I am " + str(age) + " years old.")  # I am 30 years old.

# Use int() to convert strings to integers:
num_str = "100"
num = int(num_str)
print(num)  # 100
print(num + 50)  # 150


# Direct assignment
is_ready = True

# From comparisons
age = 18
can_vote = age >= 18  # True

score = 75
passed = score > 60  # True


age = 25

# Equality
print(age == 25)  # True - equals
print(age != 30)  # True - not equals

# Greater/Less than
print(age > 20)  # True - greater than
print(age < 30)  # True - less than
print(age >= 25)  # True - greater or equal
print(age <= 25)  # True - less or equal


# Basic math
print(10 + 3)  # 13 - Addition
print(10 - 3)  # 7  - Subtraction
print(10 * 3)  # 30 - Multiplication
print(10 / 3)  # 3.333... - Division (always gives float)

# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)  # 1  - Modulo (remainder)
print(10**3)  # 1000 - Exponent (power)


# Python follows math rules (PEMDAS)
result = 2 + 3 * 4  # 14 (not 20!)
result = (2 + 3) * 4  # 20 (parentheses first)


# Comparison operators return True or False
age = 18
print(age == 18)  # True  - Equal to
print(age != 21)  # True  - Not equal to
print(age > 17)  # True  - Greater than
print(age < 20)  # True  - Less than
print(age >= 18)  # True  - Greater than or equal
print(age <= 18)  # True  - Less than or equal


# Logical operators combine conditions
age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False


# Understanding how and, or, and not work:
# AND: Both must be True
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False

# OR: At least one must be True
print(True and True)  # True
print(True or False)  # True
print(False or False)  # False

# NOT: Flips the value
print(not True)  # False
print(not False)  # Trues


# These shortcuts update variables in place:
# Instead of:
score = score + 10

# Write:
score += 10

# Works with all operators
x = 10
x += 5  # x is now 15
x *= 2  # x is now 30


# String concatenation and f-strings:
first_name = "Aashish"
last_name = "Paudel"

# Using +
full_name = first_name + " " + last_name  # "Aashish Paudel"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Aashish!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"


# Repetition with *
star = "*"
stars = star * 10  # "**********"
separator = "-" * 20  # "--------------------"


# String methods to change case:
text = "Python Programming"
print(text.lower())  # "python programming"
print(text.upper())  # "PYTHON PROGRAMMING"
print(text.title())  # "Python Programming"


# String methods to check content:
text = "Hello123"
print(text.isalpha())  # False (contains numbers)
print(text.isdigit())  # False (contains letters)
print(text.isalnum())  # True (letters and numbers)


# String methods to remove whitespace:
messy = "  hello world  "
print(messy.strip())  # "hello world" (removes whitespace)


# String methods to replace text:
price = "$19.99"
print(price.strip("$"))  # "19.99"


# String methods to find and count:
message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)  # True
print(message.startswith("I"))  # True
print(message.endswith("Python"))  # True

# Find position
print(message.find("Python"))  # 7 (first occurrence)
print(message.count("Python"))  # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"
print(message.replace("Python", "JavaScript"))  # "I love JavaScript programming with JavaScript"


# Let's explore interactive mode

age = 18
if age >= 18:
    print("you can vote")
    print("you are an adult")

# This is a simple if-else statement
age = 18
if age >= 18:
    print("you can vote")
else:
    print("you are a minor")


# This is an if-elif-else statement
age = 18
if age < 13:
    print("you are a child")
elif age < 18:
    print("you are a teenager")
else:
    print("you are an adult")


# You can have multiple conditions with logical operators
age = 25
has_license = True
weekend = False
holiday = False
raining = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")


# Nested if statements
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

# Loops
for i in range(5):
    print("Hello!")


# Print numbers 0 through 4
for i in range(5):
    print(i)


# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8


name = "Python"
for letter in name:
    print(letter)


colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")

# Output:
# I like red
# I like blue
# I like green


count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1  # Increase count by 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4


# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types OK!


# Lists can contain any type of data:
fruits = [
    "apple",
    "banana",
    "orange",
    "Mango",
    "grape",
    "kiwi",
    "pineapple",
    "strawberry",
    "blueberry",
    "watermelon",
]

# Get items
print(fruits[0])  # "apple" (first item)
print(fruits[1])  # "banana"
print(fruits[-1])  # "watermelon" (last item)
print(fruits[-2])  # "blueberry" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:3])  # ["banana", "orange"]
print(fruits[:2])  # ["apple", "banana"]
print(fruits[-2:])  # ["blueberry", "watermelon"]


# Lists are mutable (can be changed):
numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))  # 6 (length)
print(numbers.count(1))  # 2 (count occurrences)
print(numbers.index(4))  # 2 (find position)

# Sorting
numbers.sort()  # Sort in place
print(numbers)  # [1, 1, 3, 4, 5, 9]

numbers.reverse()  # Reverse order
print(numbers)  # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()  # Create a copy
print(new_list)  # [9, 5, 4, 3, 1, 1]


# Check if item exists
fruits = ["apple", "banana", "orange"]
hello = []

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")


# Empty dictionary
my_dict = {}

# Dictionary with data
person = {"name": "Aashish", "age": 18, "city": "Pokhara"}

# Different ways to create
scores = {"math": 95, "english": 87, "science": 92}

person = {"name": "Aashish", "age": 18, "city": "Pokhara"}

# Get values by key
print(person["name"])  # "Aashish"
print(person["age"])  # 18

# Safer with get()
print(person.get("job"))  # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)


person = {"name": "Aashish", "age": 18, "city": "Pokhara"}

# Check if key exists
if "email" in person:
    print("Email is present")

# Add or update
person["email"] = "aashish@email.com"  # Add new
person["age"] = 18  # Update existing

# Remove items
del person["email"]  # Remove by key
age = person.pop("age")  # Remove and return
person.clear()  # Remove all items
age = person.get("age", "Not found")  # "Not found" (after clear)

# Dictionaries have useful methods:
person = {"name": "Aashish", "age": 18, "city": "Pokhara"}

# Get all keys, values, or items
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Aashish', 18, 'Pokhara'])
print(person.items())

# Check if  "Engineer"})


# Dictionary of dictionaries
students = {
    "Aashish": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"},
}

# Access nested data
print(students["Aashish"]["grade"])  # "A"
print(students["bob"]["age"])  # 21
[print(students[student]["grade"]) for student in students]  # Loop through all students
print(students["charlie"]["age"])  # 19


# Tuples are like lists but immutable (cannot be changed):
# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = 42  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20


point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])  # 3
print(colors[-1])  # "blue"

# Slicing works too
print(colors[0:2])  # ("red", "green")


# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!


# Sets are unordered collections of unique items:
# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")  # Error if not found
colors.discard("yellow")  # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")

# Set operations
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

# Fast membership testing
allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")
