from student import Student
from course import Course
class University:
 def __init__(self,name, max_students ):
    self.name=name
    self.max_students= max_students
    self.students=[]
    self.courses=[]


def enroll_student (self, student):
        if len(self.students) < self.max_stusents:
         self.students.append(student)
        else: 
         print(f"Universsity {self.name} has reached it maximum number of students." )
        
def add_courses (self,course):
    self.courses.append(course)
    def get_avarage_grade(self, semester, major=None):
     active_students=[]
     for student in self.students:
        if not semester.is_student_inactive(student):
           if major:
              filleterd_students=[]
              for student in active_students:
                 if student.major == major:
                    filleterd_students.append(student)
                    active_students=filleterd_students
                    total_grades=0
                    for student in active_students:
                       total_grades+=student.academic_average
                       if active_students:
                          average_grade=total_grades/len(active_students)
                       else:
                          average_grade=0
                          return average_grade
def get_high_achievers(self):
   high_achievers=[]
   for student in self.students:
      if student.academic_average > 90:
         high_achievers.append(student)  
         return high_achievers
def get_top_courses(self):
   course_counts={}
   for student in self.students:
      for course in student.courses:
         if course in course_counts:
            course_counts[course]+=1
         else:
            course_counts[course]=1
            course_list=list(course_counts.items())
            sorted_courses=sorted(course_list,key=lambda x:x[1],reverse=True)
            top_courses= sorted_courses[:10]
            top_courses_names=[course[0] for course in top_courses]
            return top_courses_names
         

   
                           


           
           
           
           
