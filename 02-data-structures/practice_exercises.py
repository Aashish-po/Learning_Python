"""Worked examples for the data structures exercises."""


def list_manipulation_exercise() -> None:
    """Create numbers 1-100, keep evens, square them, and sum them."""
    sum_of_even_squares = sum(number**2 for number in range(1, 101) if number % 2 == 0)
    print("Exercise 1 - Sum of even squares from 1 to 100:", sum_of_even_squares)


def dictionary_operations_exercise() -> None:
    """Create a small student database and find the top student."""
    students = {
        "Aashish": {"age": 20, "grades": [85, 90, 88]},
        "Sita": {"age": 19, "grades": [92, 95, 91]},
        "Ram": {"age": 21, "grades": [78, 82, 80]},
    }

    averages = {
        name: sum(details["grades"]) / len(details["grades"]) for name, details in students.items()
    }
    top_student = max(averages, key=averages.get)  # pyright: ignore[reportArgumentType, reportCallIssue]

    print("\nExercise 2 - Student averages:", averages)
    print("Top student:", top_student)


def set_operations_exercise() -> None:
    """Compare two lists using sets."""
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = [4, 5, 6, 7, 8, 9]

    first_set = set(first_list)
    second_set = set(second_list)

    print("\nExercise 3 - Intersection:", first_set & second_set)
    print("Unique to first list:", first_set - second_set)
    print("Union:", first_set | second_set)


list_manipulation_exercise()
dictionary_operations_exercise()
set_operations_exercise()
