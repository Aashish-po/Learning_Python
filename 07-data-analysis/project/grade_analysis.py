# grade_analysis.py
import csv
from statistics import mean

# Create sample data
grades_data = [
    ["Student", "Math", "English", "Science"],
    ["Alice", "85", "90", "88"],
    ["Bob", "78", "82", "80"],
    ["Charlie", "92", "88", "95"],
]

# Write to CSV
with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(grades_data)

# Read and analyze
with open("grades.csv") as f:
    reader = csv.DictReader(f)
    students = list(reader)

for student in students:
    grades = [float(student["Math"]), float(student["English"]), float(student["Science"])]
    avg = mean(grades)
    print(f"{student['Student']}: Average = {avg:.1f}")

# Find top performer
top_student = max(
    students, key=lambda s: sum(float(s[col]) for col in ["Math", "English", "Science"])
)
print(f"\nTop student: {top_student['Student']}")
