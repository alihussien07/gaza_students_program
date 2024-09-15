class Course:
    def __init__(self, name, code):
        self.name = name          # Name of the course, e.g., "Computer Science 101"
        self.code = code          # Code of the course, e.g., "CS101"
        self.students = []        # List to store enrolled students
        self.grades = {}          # Dictionary to store grades for each student

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.first_name} {student.last_name} enrolled in {self.name}.")
        else:
            print(f"Student {student.first_name} {student.last_name} is already enrolled in {self.name}.")

    def assign_grade(self, student, grade):
        if student in self.students:
            self.grades[student] = grade
            print(f"Assigned grade {grade} to {student.first_name} {student.last_name}.")
        else:
            print(f"Student {student.first_name} {student.last_name} is not enrolled in {self.name}.")
