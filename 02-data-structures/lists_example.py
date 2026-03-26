"""
Lists Example

Comprehensive demonstration of Python lists and list operations.
"""


def basic_list_operations():
    """Demonstrate basic list operations."""
    print("=" * 60)
    print("BASIC LIST OPERATIONS")
    print("=" * 60)

    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "two", 3.0, True]
    empty = []

    print(f"\nNumbers: {numbers}")
    print(f"Mixed types: {mixed}")
    print(f"Empty list: {empty}")

    # Accessing elements
    print(f"\nFirst element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    print(f"Middle elements: {numbers[1:4]}")

    # Modifying lists
    numbers.append(6)
    print(f"\nAfter append(6): {numbers}")

    numbers.extend([7, 8, 9])
    print(f"After extend([7,8,9]): {numbers}")

    numbers.insert(0, 0)
    print(f"After insert(0, 0): {numbers}")

    numbers.remove(5)
    print(f"After remove(5): {numbers}")

    popped = numbers.pop()
    print(f"After pop(): {numbers} (popped: {popped})")

    print("=" * 60)


def list_comprehensions():
    """Demonstrate list comprehensions."""
    print("\nLIST COMPREHENSIONS")
    print("=" * 60)

    # Basic comprehension
    squares = [x**2 for x in range(10)]
    print(f"\nSquares: {squares}")

    # With condition
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Even numbers: {evens}")

    # Multiple conditions
    nums = [x for x in range(50) if x % 2 == 0 if x % 3 == 0]
    print(f"Divisible by 2 and 3: {nums}")

    # Nested comprehension
    matrix = [[i * j for j in range(5)] for i in range(5)]
    print("\nMultiplication table:")
    for row in matrix:
        print(row)

    # String manipulation
    words = ["hello", "world", "python"]
    capitals = [word.upper() for word in words]
    print(f"\nCapitalized: {capitals}")

    print("=" * 60)


def advanced_list_operations():
    """Demonstrate advanced list operations."""
    print("\nADVANCED OPERATIONS")
    print("=" * 60)

    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    # Sorting
    sorted_nums = sorted(numbers)
    print(f"\nOriginal: {numbers}")
    print(f"Sorted (new list): {sorted_nums}")

    numbers.sort()
    print(f"Sorted (in-place): {numbers}")

    # Reversing
    numbers.reverse()
    print(f"Reversed: {numbers}")

    # Counting
    print(f"\nCount of 5: {numbers.count(5)}")
    print(f"Index of 9: {numbers.index(9)}")

    # List operations
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print(f"\nCombined: {combined}")

    repeated = list1 * 3
    print(f"Repeated 3x: {repeated}")

    # Checking membership
    print(f"\n5 in numbers: {5 in numbers}")
    print(f"10 in numbers: {10 in numbers}")

    print("=" * 60)


def practical_examples():
    """Real-world list usage examples."""
    print("\nPRACTICAL EXAMPLES")
    print("=" * 60)

    # Example 1: Filter and transform
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"\nEven squares: {even_squares}")

    # Example 2: Process strings
    names = ["aashish", "alice", "bob", "charlie"]
    capitalized = [name.capitalize() for name in names]
    print(f"Capitalized names: {capitalized}")

    # Example 3: Flatten nested list
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = [item for sublist in nested for item in sublist]
    print(f"Flattened: {flattened}")

    # Example 4: Statistics
    scores = [85, 92, 78, 90, 88, 76, 95, 89]
    print(f"\nScores: {scores}")
    print(f"Average: {sum(scores) / len(scores):.2f}")
    print(f"Highest: {max(scores)}")
    print(f"Lowest: {min(scores)}")
    print(f"Above 85: {[s for s in scores if s > 85]}")

    print("=" * 60)


if __name__ == "__main__":
    basic_list_operations()
    list_comprehensions()
    advanced_list_operations()
    practical_examples()

    print("\n✓ All examples complete!")
