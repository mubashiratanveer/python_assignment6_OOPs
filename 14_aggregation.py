
class Employe:
    def __init__(self , name):
        self.name = name

    def get_details(self):
        return f"Employe name: {self.name}"

class Department:
    def __init__(self , department , employe :Employe):
        self.department = department
        self.employe = employe

    def show(self):    
        return f"Department name: {self.department}.{self.employe.get_details()}"


emp1 = Employe("Mubashira")

dep1 = Department("IT" , emp1)

print(dep1.show())