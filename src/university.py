# university.py
from student import Student
from course import Course

class University:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.courses = []

    def enroll_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Student {student.first_name} {student.last_name} has been enrolled in {self.name}.")
        else:
            print(f"University {self.name} has reached its maximum capacity.")

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course {course.name} has been added to {self.name}.")

    def get_average_grade(self, semester, major=None):
        # Filter active students, and optionally filter by major
        active_students = [s for s in self.students if not semester.is_student_inactive(s) and (not major or s.major == major)]
        
        if not active_students:
            return 0

        # Calculate the average grade
        total_grades = sum(s.academic_average for s in active_students)
        return total_grades / len(active_students)

    def get_high_achievers(self):
        # Get all students with an average grade over 90
        return [s for s in self.students if s.academic_average > 90]

    def get_top_courses(self):
        # Count the number of students in each course
        course_counts = {}
        for student in self.students:
            for course in student.courses:
                course_counts[course] = course_counts.get(course, 0) + 1

        # Sort courses by the number of students and return the top 10
        sorted_courses = sorted(course_counts, key=course_counts.get, reverse=True)
        return sorted_courses[:10]
