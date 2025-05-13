
class student:
    def student_data(self):
        self.name = str(input("Enter student name."))
        self.marks = float(input("Enter student marks."))
    def display(self):
        print("Students Information!") 
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")    

a = student()

a.student_data()
a.display()