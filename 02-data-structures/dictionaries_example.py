"""Examples of working with Python dictionaries."""


student = {
    "name": "Aashish",
    "age": 20,
    "course": "Computer Science",
}
print("Original dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Email with default:", student.get("email", "no-email@example.com"))

# Adding and updating values
student["age"] = 21
student["city"] = "Kathmandu"
print("\nUpdated dictionary:", student)

# Dictionary methods
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Dictionary comprehension
squares = {number: number**2 for number in range(1, 6)}
print("\nSquares dictionary:", squares)

# Nested dictionaries
classroom = {
    "student_1": {"name": "Aashish", "grade": 88},
    "student_2": {"name": "Sita", "grade": 92},
}
print("\nNested dictionary:", classroom)
print("Student 2 grade:", classroom["student_2"]["grade"])

# Merging dictionaries
contact = {"email": "aashish@example.com"}
profile = student | contact
print("Merged dictionary:", profile)
