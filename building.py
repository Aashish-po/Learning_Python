# 1: Create a function that prints your name 3 times
def print_name():
    for _ in range(3):
        print("Aashish Paudel")


# 2: Create a function that checks if a number is even or odd
def check_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


# 3: Create a function that calculates rectangle area
def calculate_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")


# 4: Create a function that converts Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")


# 5: Create a function that checks if a string is a palindrome
def check_palindrome():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")


# 6: Create a function that calculates the factorial of a number
def calculate_factorial():
    num = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")


# 7: Create a function that generates a random number between 1 and 100
import random  # noqa: E402


def generate_random_number():
    random_number = int(random() * 100) + 1
    print(f"Generated random number: {random_number}")


# 8: Create a function that checks if a year is a leap year
def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# 9: What will be printed by this code?
score = 100


def update_score():
    score = 50
    print(f"Inside function: {score}")


update_score()
print(f"Outside function: {score}")

# What gets printed?
# Inside function: 50
# Outside function: 100


# 10: Fix this code without using 'global'

"""count = 0
def increment():
    count = count + 1  # This will error!
    return count """


# How would you rewrite this properly?
def increment(count):
    count += 1
    return count


# 11: Create a function that prints letter grade based on score
def calculate_grade():
    score = 85
    # 90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
    print(f"Score: {score}")


# Create a function that checks if password is strong
# Rules: at least 8 characters, has a number, has uppercase
def validate_password():
    password = "Secure123"
    if (
        len(password) >= 8
        and any(char.isdigit() for char in password)
        and any(char.isupper() for char in password)
    ):
        print("Password is strong.")
    else:
        print("Password is not strong.")


# 13: Create a function that checks multiple conditions for activities
def check_activities(age, has_license, weekend, holiday, raining):
    if age >= 18 and has_license:
        print("You can drive!")

    if weekend or holiday:
        print("No work today!")

    if not raining:
        print("Let's go outside!")


# 14: Create a function that prints Fibonacci sequence up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# 15: Create a function that checks if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# 16:  Create a function that takes name and age, prints a message
def display_info(name, age):
    print(f"{name} is {age} years old.")


# Call with values
display_info("Aashish", 18)
display_info("Bob", 30)


# 17: Create a function that takes two numbers and prints their sum
def add_numbers(a, b):
    total = a + b
    print(f"The sum of {a} and {b} is: {total}")


# Call with values
add_numbers(5, 10)
add_numbers(3.5, 2.5)


# 18:Create a function that calculates rectangle area with length and width
def rectangle_area(length, width):
    area = length * width
    print(f" The area of the rectangle is: {area}")


# Call with values
rectangle_area(5, 3)
rectangle_area(7.5, 4.2)


# 19: Create a function with a default greeting
def welcome_user(name, greeting="Welcome"):
    print(f"{greeting},{name}!")


# Call with values
welcome_user("Aashish")  # should print "Welcome, Aashish!"
welcome_user("Aashish", "Hello")  # should print "Hello, Aashish!"


# 20 : Create a power function with default exponent of 2
def power(base, exponent=2):
    result = base**exponent
    print(f"{base} raised to the power of {exponent} is: {result}")


# Call with values
power(5)  # should print 25
power(5, 3)  # should print 125


# 21: Call this function using keyword arguments
def book_ticket(name, destination, seat_class, meal_preference):
    print(f"Ticket for {name}")
    print(f"To: {destination}")
    print(f"Class: {seat_class}")
    print(f"Meal: {meal_preference}")


# call with values
# 1. All positional
book_ticket("Aashish", "Pokhara", "Economy", "Non-Vegetarian")

# 2. All keyword arguments (any order)
book_ticket(
    name="Aashish",
    destination="Pokhara",
    seat_class="Economy",
    meal_preference="Non-Vegetarian",
)

# 3. Mix of positional and keyword
book_ticket(
    "Aashish",
    destination="Pokhara",
    seat_class="Economy",
    meal_preference="Non-Vegetarian",
)


# 22: Create a function that converts temperature
# Parameters: value, from_unit (default 'C'), to_unit (default 'F')
# Support: Celsius (C), Fahrenheit (F), Kelvin (K)
def convert_temperature(value, from_unit="C", to_unit="F"):
    print(f"Converting {value}°{from_unit} to {to_unit}...")
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9 / 5) + 32
        elif to_unit == "K":
            return value + 273.15
    if from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5 / 9
        elif to_unit == "K":
            return (value - 32) * 5 / 9 + 273.15
    if from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9 / 5 + 32


# call with values
print(convert_temperature(100))  # default C to F
print(convert_temperature(0, from_unit="C", to_unit="K"))  # C to K
print(convert_temperature(32, from_unit="F", to_unit="C"))  # F to C
print(convert_temperature(300, from_unit="K", to_unit="F"))  # K to F


# 22: Create a function with multiple parameters and defaults
# Parameters: price, discount_percent=0, tax_rate=0.08, coupon=0
def calculate_final_price(price, discount_percent=0, tax_rate=0.08, coupon=0):
    discounted_price = price * (1 - discount_percent / 100)
    taxed_price = discounted_price * (1 + tax_rate)
    final_price = taxed_price - coupon
    print(f"Final price: {final_price:.2f}")


# Call with values
calculate_final_price(100)  # → 108.0
calculate_final_price(100, discount_percent=10)  # → 97.2
calculate_final_price(100, discount_percent=10, coupon=5)  # → 92.2


# 23: Create a function that builds a user profile
# Required: name, email
# Optional: age=None, city=None, occupation=None
def create_profile(name, email, age=None, city=None, occupation=None):
    profile = {
        "name": name,
        "email": email,
        "age": age,
        "city": city,
        "occupation": occupation,
    }
    print("User Profile:")
    for key, value in profile.items():
        if value is not None:
            print(f"{key.capitalize()}: {value}")


# call with values
create_profile("Aashish", "aashish@example.com")
create_profile("Aashish", "aashish@example.com", age=18)
create_profile("Aashish", "aashish@example.com", city="Pokhara", occupation="Student")


# 24: Create a function that simulates an API request with sensible defaults
def make_request(endpoint, method="GET", headers=None, timeout=30):
    print(f"Making {method} request to {endpoint}")
    print(f"Timeout: {timeout}s")
    if headers:
        print(f"Headers: {headers}")


# Call with values
make_request("/api/users")  # Uses defaults
make_request("/api/users", method="POST", headers={"Auth": "token123"})


# 25: Create a function that simulates fetching data with flexible filtering
def fetch_users(limit=10, offset=0, status="active", sort_by="created_at"):
    print(f"SELECT * FROM users WHERE status='{status}'")
    print(f"ORDER BY {sort_by} LIMIT {limit} OFFSET {offset}")


# Call with values
fetch_users()  # Get first 10 active users
fetch_users(limit=50, sort_by="name")  # Custom query


# 26: Create a function that simulates logging with configurable options
def log_message(message, level="INFO", timestamp=True, file="app.log"):
    import datetime

    prefix = f"[{level}]"
    if timestamp:
        prefix += f" {datetime.datetime.now()}"
    print(f"{prefix} {message}")


# Call with values
log_message("Server started")
log_message("Error occurred", level="ERROR")
log_message("Debug info", level="DEBUG", timestamp=False)


# 27: Convert the print version to return version
def multiply_print(a, b):
    print(a * b)


def multiply_return(a, b):
    return a * b


# Call with values
result = multiply_return(4, 5)
print(result)  # Should print 20


# 28: Create a function that returns the square of a number
def square(num):
    return num * num


# Call with values
print(square(5))  # Should print 25


# 29: Create a function that returns True if number is positive
def is_positive(num):
    return num > 0


# Call with values
print(is_positive(10))  # Should print True
print(is_positive(-5))  # Should print False


# 30: Use return values in calculations
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price


# Call with values
item1 = calculate_discount(100, 10)
item2 = calculate_discount(50, 20)
item3 = calculate_discount(75, 15)
total = item1 + item2 + item3
print(f"Total: Rs.{total}")


# 31: Create a function that converts Celsius to Fahrenheit, then use it to convert to Kelvin
def celsius_to_fahrenheit(celsius):  # noqa: F811
    return (celsius * 9 / 5) + 32


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


# call with values
kelvin = fahrenheit_to_kelvin(celsius_to_fahrenheit(25))
print(f"25°C = {kelvin:.2f}K")


# 32: Return multiple statistics
def calculate_stats(numbers):
    return sum(numbers), sum(numbers) / len(numbers) if numbers else 0, len(numbers)
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    count = len(numbers)
    return total, average, count


# Call with values
total, avg, count = calculate_stats([10, 20, 30, 40])
print(f"Total: {total}, Average: {avg}, Count: {count}")


# 33: Return user info as tuple
def parse_email(email):
    username, domain = email.split("@")
    return username, domain


# Call with values
username, domain = parse_email("aashish@example.com")
print(f"Username: {username}, Domain: {domain}")


# 34: Create a function that calculates letter grade based on score and returns it
def calculate_letter_grade(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Call with values
grade = calculate_letter_grade(85)
print(f"Your grade: {grade}")  # Your grade: B
if calculate_letter_grade(92) == "A":
    print("Excellent!")


# 35: Create a function that analyzes a string and returns multiple statistics
def analyze_string(text):
    chars = len(text)
    words = len(text.split())
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return chars, words, upper, lower


# Call with values
chars, words, upper, lower = analyze_string("Hello World! Python is GREAT")
print(f"Chars: {chars}, Words: {words}, Upper: {upper}, Lower: {lower}")


# 36: Create a function that processes a bank transaction and returns new balance and success status
def process_transaction(balance, amount, transaction_type):
    if transaction_type == "deposit":
        new_balance = balance + amount
        return new_balance, True, "Deposit successful."
    elif transaction_type == "withdraw":
        if amount > balance:
            return balance, False, "Withdrawal failed: Insufficient funds."
        else:
            new_balance = balance - amount
            return new_balance, True, "Withdrawal successful."
    else:
        return balance, False, "Invalid transaction type."


# Call with values
balance = 1000
new_balance, success, msg = process_transaction(balance, 500, "withdraw")
print(f"Balance: Rs.{new_balance}, Success: {success}, Message: {msg}")

new_balance, success, msg = process_transaction(new_balance, 1000, "withdraw")
print(f"Balance: Rs.{new_balance}, Success: {success}, Message: {msg}")


# 37: Create a function that takes a list of temperatures in Fahrenheit and returns min, max, average, and range category
def get_temperature_info(temps_fahrenheit):
    if not temps_fahrenheit:
        return None, None, None, "No data"

    min_temp = min(temps_fahrenheit)
    max_temp = max(temps_fahrenheit)
    avg_temp = sum(temps_fahrenheit) / len(temps_fahrenheit)
    temp_range = max_temp - min_temp

    if temp_range < 10:
        category = "Stable"
    elif temp_range <= 20:
        category = "Moderate"
    else:
        category = "Variable"
    return min_temp, max_temp, avg_temp, category


# Call with values:
min_t, max_t, avg_t, category = get_temperature_info([65, 70, 68, 72, 69])
print(f"Min: {min_t}°F, Max: {max_t}°F, Avg: {avg_t}°F, Range: {category}")


# 38: Create a function that validates API response based on HTTP status code and returns a message
def validate_api_response(response_code):
    if response_code == 200:
        return True, "Success"
    elif response_code == 404:
        return False, "Not Found"
    elif response_code == 500:
        return False, "Server Error"
    else:
        return False, "Unknown Error"


# Call with values
success, message = validate_api_response(200)
if success:
    print(f"API call successful: {message}")
else:
    print(f"API error: {message}")

success, message = validate_api_response(404)
if success:
    print(f"API call successful: {message}")
else:
    print(f"API error: {message}")


# 39: Create a function that validates user input for creating an account and returns validation status and error messages
def validate_user_input(username, password):
    errors = []

    if len(username) < 3:
        errors.append("Username too short")

    if len(password) < 8:
        errors.append("Password too short")

    if not any(char.isdigit() for char in password):
        errors.append("Password needs a number")

    is_valid = len(errors) == 0
    return is_valid, errors


# Call with values
valid, error_list = validate_user_input("aashish", "secure123")
if valid:
    print("User created successfully!")
else:
    print("Validation errors:")
    for error in error_list:
        print(f"  - {error}")


#  40: Create a function that calculates the total price of items in a shopping cart, applying tax and discounts, and returns the final amount along with breakdown of calculations.
def calculate_cart_total(items, tax_rate=0.08, coupon_code=None):
    subtotal = sum(items)
    discount = 0
    if coupon_code == "SAVE10":
        discount = subtotal * 0.10
    elif coupon_code == "SAVE20":
        discount = subtotal * 0.20

    subtotal_after_discount = subtotal - discount
    tax = subtotal_after_discount * tax_rate
    total = subtotal_after_discount + tax

    return total, subtotal, discount, tax


# Call with values
items = [29.99, 49.99, 15.99]
final, sub, disc, tax = calculate_cart_total(items, coupon_code="SAVE10")

print(f"Subtotal: ${sub:.2f}")
print(f"Discount: -${disc:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${final:.2f}")
