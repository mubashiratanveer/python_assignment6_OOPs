
class Dog:
    def __init__(self , name , breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name}  says:woof ,woof....")



dog1 = Dog("Bari" , "Labrador")

dog1.bark()

