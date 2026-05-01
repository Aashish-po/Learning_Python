"""Grade analysis example used in the learning journey."""

from csv import DictReader, writer
from statistics import mean


def main():
    """Create sample data, analyze it, and print the results."""
    grades_data = [
        ["Student", "Math", "English", "Science"],
        ["Alice", "85", "90", "88"],
        ["Bob", "78", "82", "80"],
        ["Charlie", "92", "88", "95"],
    ]

    with open("grades.csv", "w", newline="") as file_handle:
        csv_writer = writer(file_handle)
        csv_writer.writerows(grades_data)

    with open("grades.csv") as file_handle:
        students = list(DictReader(file_handle))

    for student in students:
        grades = [float(student["Math"]), float(student["English"]), float(student["Science"])]
        average = mean(grades)
        print(f"{student['Student']}: Average = {average:.1f}")

    top_student = max(
        students,
        key=lambda student: sum(
            float(student[column]) for column in ["Math", "English", "Science"]
        ),
    )
    print(f"\nTop student: {top_student['Student']}")


if __name__ == "__main__":
    main()
