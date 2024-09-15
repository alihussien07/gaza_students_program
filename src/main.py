# Import necessary modules and classes
from university import University
from student import Student
from course import Course
from semester import Semester
from datetime import datetime

# Function to search for students by email, first name, or last name
def search_students(students, query):
    query = query.lower()
    results = [student for student in students if query in student.email.lower() or query in student.first_name.lower() or query in student.last_name.lower()]
    return results

# Function to create a new student
def create_student(universities):
    print("\n--- Creating a New Student ---")
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    email = input("Enter student's email: ")
    major = input("Enter student's major: ")

    for i, uni in enumerate(universities):
        print(f"{i+1}. {uni.name}")

    university_choice = int(input("Select a university by number: ")) - 1
    selected_university = universities[university_choice]

    new_student = Student(first_name, last_name, email, selected_university, major)
    selected_university.enroll_student(new_student)
    return new_student

# Function to assign grades to students interactively
def assign_grades_to_students(students):
    print("\n--- Assign Grades to Students ---")
    for student in students:
        grade = float(input(f"Enter grade for {student.first_name} {student.last_name}: "))
        student.calculate_average_grade()
        student.academic_average = grade

def main():
    # Initialize universities
    birzeit = University("Birzeit", 100)
    al_quds = University("Al-Quds", 80)
    al_najah = University("Al-Najah", 90)
    universities = [birzeit, al_quds, al_najah]

    # Initialize courses
    course1 = Course("Computer Science 101", "CS101")
    course2 = Course("Mathematics 101", "MATH101")

    # Add courses to universities
    birzeit.add_course(course1)
    birzeit.add_course(course2)

    # Allow the user to create multiple students
    students = []
    while True:
        create_another = input("Would you like to create a new student? (yes/no): ").strip().lower()
        if create_another == 'yes':
            new_student = create_student(universities)
            students.append(new_student)
        else:
            break

    # Allow assigning grades to students
    assign_grades_to_students(students)

    # Set up a semester for attendance tracking
    semester_start = datetime(2024, 1, 1)
    semester_duration = 4  # in months
    semester = Semester(semester_start, semester_duration)

    # Update last attendance for each student
    for student in students:
        zoom_entry_date_time = input(f"Enter last attendance date for {student.first_name} {student.last_name} (YYYY-MM-DD HH:MM:SS): ")
        student.update_last_attendance(zoom_entry_date_time)

    # Display high achievers
    for university in universities:
        high_achievers = university.get_high_achievers()
        print("\nEligible for $10k Award - High Achievers (Average > 90):")
        for student in high_achievers:
            print(f"Name: {student.first_name} {student.last_name}, Email: {student.email}, Average: {student.academic_average:.2f}")

    # Identify inactive students
    for university in universities:
        inactive_students = semester.mark_students_active_inactive(university.students)
        print("Inactive Students (Potentially Lost in Conflict):")
        for student in inactive_students:
            print(f"{student.first_name} {student.last_name}, Email: {student.email}, Last Attended: {student.last_attended_lecture}")

    # Perform search by email, first name, or last name
    query = input("\nEnter search query (email, first name, or last name): ")
    for university in universities:
        results = search_students(university.students, query)
        print("\nSearch Results:")
        for student in results:
            print(f"Name: {student.first_name} {student.last_name}, Email: {student.email}, Major: {student.major}, University: {student.university.name}")

    # Calculate and display average grade
    for university in universities:
        average_grade = university.get_average_grade(semester)
        print(f"\nAverage Grade at {university.name}: {average_grade:.2f}")

    # Display top 10 courses booked by Gaza students in each university
    for university in universities:
        top_courses = university.get_top_courses()
        print(f"\nTop 10 Courses Booked by Gaza Students at {university.name}:")
        for course in top_courses:
            print(course.name)

if __name__ == "__main__":
    main()

""" # main.py
from university import University
from student import Student
from course import Course
from semester import Semester
from datetime import datetime

def search_students(students, query):
    query = query.lower()
    results = []
    for student in students:
        if query in student.email.lower() or query in student.first_name.lower() or query in student.last_name.lower():
            results.append(student)
    return results

def create_student():
    # Get student details from the console
    print("\n--- Creating a New Student ---")
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    email = input("Enter student's email: ")
    major = input("Enter student's major: ")

    # Display available universities
    print("\nAvailable Universities:")
    universities = [birzeit, al_quds, al_najah]
    for i, uni in enumerate(universities):
        print(f"{i+1}. {uni.name}")

    # Choose a university for the student
    university_choice = int(input("Select a university by number: ")) - 1
    selected_university = universities[university_choice]

    # Create a new student object
    new_student = Student(first_name, last_name, email, selected_university, major)
    selected_university.enroll_student(new_student)
    
    return new_student

def main():
    # Create universities
    global birzeit, al_quds, al_najah
    birzeit = University("Birzeit", 100)
    al_quds = University("Al-Quds", 80)
    al_najah = University("Al-Najah", 90)

    # Create majors and courses
    course1 = Course("Computer Science 101", "CS101")
    course2 = Course("Mathematics 101", "MATH101")
    
    birzeit.add_course(course1)
    birzeit.add_course(course2)

    # Prompt user to create a new student
    print("Create a new student")
    new_student = create_student()

    # Display created student's information
    print(f"\n--- Student Created: ---")
    print(f"Name: {new_student.first_name} {new_student.last_name}")
    print(f"Email: {new_student.email}")
    print(f"Major: {new_student.major}")
    print(f"University: {new_student.university.name}")

    # Example of enrolling the new student in a course
    print("\nAvailable Courses:")
    available_courses = new_student.university.courses
    for i, course in enumerate(available_courses):
        print(f"{i+1}. {course.name}")

    course_choice = int(input("Select a course by number to enroll the new student: ")) - 1
    selected_course = available_courses[course_choice]
    new_student.enroll_in_course(selected_course)

    # Simulate the semester
    semester = Semester(datetime(2024, 1, 1), 4)

    # Update student attendance from a Zoom log (Example)
    zoom_user_id = "12345"  # Example Zoom user ID
    zoom_entry_date_time = "2024-02-15 10:00:00"  # Example entry date and time
    new_student.update_last_attendance(zoom_entry_date_time)

    # Calculate average grades
    new_student.calculate_average_grade()

    # At the end of the semester, get high achievers
    high_achievers = new_student.university.get_high_achievers()
    
    # Provide information about high achievers to the government
    print("\nEligible for $10k Award - High Achievers (Average > 90):")
    for student in high_achievers:
        print(f"Name: {student.first_name} {student.last_name}, Email: {student.email}, Average: {student.academic_average:.2f}")
        print(f"Student {student.first_name} {student.last_name} will receive $10,000.\n")

    # Identify inactive students
    inactive_students = semester.mark_students_active_inactive(new_student.university.students)
    print("Inactive Students (Potentially Lost in Conflict):")
    for student in inactive_students:
        print(f"{student.first_name} {student.last_name}, Email: {student.email}, Last Attended: {student.last_attended_lecture}")

    # Perform search
    query = input("\nEnter search query (email, first name, or last name): ")
    results = search_students(new_student.university.students, query)
    print("\nSearch Results:")
    for student in results:
        print(f"Name: {student.first_name} {student.last_name}, Email: {student.email}, Major: {student.major}, University: {student.university.name}")

    # Calculate and display average grade
    average_grade = new_student.university.get_average_grade(semester)
    print(f"\nAverage Grade at {new_student.university.name}: {average_grade:.2f}")

    # Get top 10 courses
    top_courses = new_student.university.get_top_courses()
    print("\nTop 10 Courses Booked by Gaza Students:")
    for course in top_courses:
        print(course.name)

if __name__ == "__main__":

    
    main()
## Create instances of the classes
semester = Semester()
university = University("Example University", 100)

# Enroll some students
student1 = Student("Alice", "Smith", "Computer Science", 85)
student2 = Student("Bob", "Johnson", "Computer Science", 90)
student3 = Student("Charlie", "Brown", "Mathematics", 95)

university.enroll_student(student1)
university.enroll_student(student2)
university.enroll_student(student3)

# Call the get_avarage_grade method
average_grade_all = university.get_avarage_grade(semester)
print(f"Average grade of all active students: {average_grade_all}")

# Call the get_avarage_grade method for a specific major
average_grade_cs = university.get_avarage_grade(semester, major="Computer Science")
print(f"Average grade of active Computer Science students: {average_grade_cs}") """