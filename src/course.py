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
