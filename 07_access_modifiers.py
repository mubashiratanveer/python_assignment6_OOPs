

class Employee:

    def __init__(self , name , salary , ssn):
        self.name = name  
        self._salary = salary 
        self.__ssn = ssn

emp = Employee("Mubashira" , 50000 , '00000000')
print('Name (Public):'  , emp.name)
print('Salary (Protect):' , emp._salary)

try:
    print("Private" , emp.__ssn)
except AttributeError:
    print("SSN (Private):  cannot be excessed directly!")    
        