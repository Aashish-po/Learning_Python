"""Examples of working with Python sets and why they are useful for uniqueness."""


numbers = {1, 2, 2, 3, 4, 4, 5}
print("Set removes duplicates automatically:", numbers)

first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}

print("\nFirst set:", first_set)
print("Second set:", second_set)

# These operations are the main reason sets are useful in real code.
print("Union:", first_set | second_set)
print("Intersection:", first_set & second_set)
print("Difference (first - second):", first_set - second_set)
print("Symmetric difference:", first_set ^ second_set)

# Membership test
print("\nIs 3 in first_set?", 3 in first_set)
print("Is 9 in first_set?", 9 in first_set)

# Set comprehension
even_squares = {number**2 for number in range(1, 11) if number % 2 == 0}
print("Set comprehension result:", even_squares)
