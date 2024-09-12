# semester.py
from datetime import datetime, timedelta

class Semester:
    def __init__(self, start_date, duration):
        self.start_date = start_date
        self.duration = duration
        self.end_date = self.start_date + timedelta(days=30 * self.duration)

    def is_student_inactive(self, student):
        # Check if the student has attended any lecture
        if not student.last_attended_lecture:
            return True
        
        # Parse the last attended lecture date
        last_attendance_date = datetime.strptime(student.last_attended_lecture, "%Y-%m-%d %H:%M:%S")
        
        # Calculate if more than one month has passed since the last attendance
        return (self.end_date - last_attendance_date).days > 30

    def mark_students_active_inactive(self, students):
        # Generate a list of inactive students
        inactive_students = []
        for student in students:
            if self.is_student_inactive(student):
                inactive_students.append(student)
        return inactive_students
