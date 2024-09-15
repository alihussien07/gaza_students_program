# course.py
class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []
        self.grades = {}

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.first_name} {student.last_name} enrolled in {self.name}.")
        else:
            print(f"Student {student.first_name} {student.last_name} is already enrolled in {self.name}.")

    def assign_grade(self, student, grade):
        if student in self.students:
            self.grades[student] = grade
        else:
            print(f"Student {student.first_name} {student.last_name} is not enrolled in {self.name}.")


#class Course:
    def __init__(self):
        # List of students in the course
        self.students = ["Alice", "Bob", "Charlie"]
        # Dictionary to store grades for each student
        self.grades = {}

    def assign_grade(self, student, grade):
        # Check if the student is enrolled in the course
        if student in self.students:
            # Assign the grade to the student
            self.grades[student] = grade
            print(f"Assigned grade {grade} to {student}.")
        else:
            print(f"Student {student} is not enrolled in the course.")

# Example usage
course = Course()

# Assign grades to students
course.assign_grade("Alice", "A")   # Output: Assigned grade A to Alice.
course.assign_grade("Bob", 85)      # Output: Assigned grade 85 to Bob.
course.assign_grade("David", 90)    # Output: Student David is not enrolled in the course.

# Check the grades dictionary
print(course.grades)  # Output: {'Alice': 'A', 'Bob': 85}
