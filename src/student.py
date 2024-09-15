# student.py
class Student:
    def __init__(self, first_name, last_name, email, university, major):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.university = university
        self.major = major
        self.courses = []
        self.academic_average = 0
        self.last_attended_lecture = None  # Tracks the date and time of the last attended lecture

    def enroll_in_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.enroll_student(self)
            print(f"Enrolled {self.first_name} {self.last_name} in {course.name}.")
        else:
            print(f"{self.first_name} {self.last_name} is already enrolled in {course.name}.")

    def update_last_attendance(self, date):
        # Update the date and time of the last attended lecture
        self.last_attended_lecture = date
        print(f"{self.first_name} {self.last_name}'s last attended lecture updated to {self.last_attended_lecture}.")

    def calculate_average_grade(self):
        # Handle the case where there are no courses
        if not self.courses:
            return 0
        
        total_grades = sum(course.grade for course in self.courses if hasattr(course, 'grade'))
        self.academic_average = total_grades / len(self.courses)
        return self.academic_average 
        """
 def calculate_average_grade(self):
    # Check if there are any courses
     if not self.courses:
        return 0  # No courses, so return an average of 0

    # Initialize variables to store total grades and the number of graded courses
    total_grades = 0
    graded_courses_count = 0

    # Loop through each course in the courses list
    for course in self.courses:
        # Check if the course has a 'grade' attribute
        if hasattr(course, 'grade'):
            total_grades += course.grade  # Add the course's grade to the total
            graded_courses_count += 1     # Increment the count of graded courses

    # If there are no courses with grades, return 0
    if graded_courses_count == 0:
           return 0 
    
    # Calculate the academic average
    self.academic_average = total_grades / graded_courses_count
    return self.academic_average
 """
    def get_grade_breakdown(self):
        breakdown = {course.name: course.grade for course in self.courses if hasattr(course, 'grade')}
        return breakdown
