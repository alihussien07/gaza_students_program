import tkinter as tk
from tkinter import ttk, messagebox
from university import University
from university1 import University
from student import Student
from course import Course

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Create universities
        self.birzeit = University("Birzeit", 100)
        self.al_quds = University("Al-Quds", 80)
        self.al_najah = University("Al-Najah", 90)

        # Create courses
        self.course1 = Course("Computer Science 101", "CS101")
        self.course2 = Course("Mathematics 101", "MATH101")
        self.birzeit.add_course(self.course1)
        self.birzeit.add_course(self.course2)

        self.universities = [self.birzeit, self.al_quds, self.al_najah]

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Student information input fields
        self.label_first_name = tk.Label(self.root, text="First Name:")
        self.label_first_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_first_name = tk.Entry(self.root)
        self.entry_first_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_last_name = tk.Label(self.root, text="Last Name:")
        self.label_last_name.grid(row=1, column=0, padx=10, pady=10)

        self.entry_last_name = tk.Entry(self.root)
        self.entry_last_name.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10)

        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        self.label_major = tk.Label(self.root, text="Major:")
        self.label_major.grid(row=3, column=0, padx=10, pady=10)

        self.entry_major = tk.Entry(self.root)
        self.entry_major.grid(row=3, column=1, padx=10, pady=10)

        # University selection
        self.label_university = tk.Label(self.root, text="Select University:")
        self.label_university.grid(row=4, column=0, padx=10, pady=10)

        self.university_var = tk.StringVar()
        self.university_combobox = ttk.Combobox(self.root, textvariable=self.university_var)
        self.university_combobox['values'] = [uni.name for uni in self.universities]
        self.university_combobox.grid(row=4, column=1, padx=10, pady=10)

        # Buttons
        self.button_add_student = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.button_add_student.grid(row=5, column=0, columnspan=2, pady=10)

        self.button_show_students = tk.Button(self.root, text="Show All Students", command=self.show_students)
        self.button_show_students.grid(row=6, column=0, columnspan=2, pady=10)

        self.student_listbox = tk.Listbox(self.root, width=50)
        self.student_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_student(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        major = self.entry_major.get()
        university_name = self.university_var.get()

        # Find selected university object
        selected_university = next((uni for uni in self.universities if uni.name == university_name), None)
        if not selected_university:
            messagebox.showerror("Error", "Please select a valid university.")
            return

        # Create student and enroll in university
        new_student = Student(first_name, last_name, email, selected_university, major)
        selected_university.enroll_student(new_student)

        messagebox.showinfo("Success", f"Student {first_name} {last_name} added successfully.")

    def show_students(self):
        self.student_listbox.delete(0, tk.END)
        for university in self.universities:
            for student in university.students:
                self.student_listbox.insert(tk.END, f"{student.first_name} {student.last_name} - {student.email} ({student.university.name})")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
