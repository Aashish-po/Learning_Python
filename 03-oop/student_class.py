"""
Student Class Example

Demonstrates OOP concepts with a practical Student class.
"""


class Student:
    """Represent a student with grades."""

    # Class variable (shared by all students)
    school = "Nepal University"
    total_students = 0

    def __init__(self, name, roll_number, email=""):
        """Initialize a student."""
        self.name = name
        self.roll_number = roll_number
        self.email = email
        self.grades = {}  # subject: grade

        # Increment total students
        Student.total_students += 1

    def add_grade(self, subject, grade):
        """Add a grade for a subject."""
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")

        self.grades[subject] = grade
        print(f"✓ Added {subject}: {grade}")

    def get_average(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_letter_grade(self):
        """Get letter grade based on average."""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def get_report_card(self):
        """Generate a report card."""
        report = []
        report.append("=" * 50)
        report.append(f"REPORT CARD - {self.school}")
        report.append("=" * 50)
        report.append(f"Name: {self.name}")
        report.append(f"Roll Number: {self.roll_number}")
        report.append("")
        report.append("Grades:")
        report.append("-" * 50)

        for subject, grade in self.grades.items():
            report.append(f"  {subject:<20} {grade:>5}")

        report.append("-" * 50)
        report.append(f"Average: {self.get_average():.2f}")
        report.append(f"Letter Grade: {self.get_letter_grade()}")
        report.append("=" * 50)

        return "\n".join(report)

    def __str__(self):
        """String representation."""
        return f"Student({self.name}, {self.roll_number})"

    def __repr__(self):
        """Developer representation."""
        return f"Student('{self.name}', '{self.roll_number}', '{self.email}')"

    @classmethod
    def get_total_students(cls):
        """Get total number of students."""
        return cls.total_students


def demonstrate_student_class():
    """Demonstrate the Student class."""
    print("=" * 60)
    print("STUDENT CLASS DEMONSTRATION")
    print("=" * 60)

    # Create students
    student1 = Student("Aashish Poudel", "CS-2024-001", "aashish@example.com")
    student2 = Student("Alice Smith", "CS-2024-002")

    # Add grades
    print("\nAdding grades for Aashish:")
    student1.add_grade("Mathematics", 95)
    student1.add_grade("Physics", 88)
    student1.add_grade("Chemistry", 92)
    student1.add_grade("Computer Science", 98)

    print("\nAdding grades for Alice:")
    student2.add_grade("Mathematics", 85)
    student2.add_grade("Physics", 90)
    student2.add_grade("Chemistry", 87)

    # Display report cards
    print("\n" + student1.get_report_card())
    print("\n" + student2.get_report_card())

    # Class information
    print(f"\nTotal Students: {Student.get_total_students()}")
    print(f"School: {Student.school}")


if __name__ == "__main__":
    demonstrate_student_class()
    print("\n✓ Demonstration complete!")
