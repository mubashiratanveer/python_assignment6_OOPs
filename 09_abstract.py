from abc import ABC , abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
            return self.length    * self.width
        
rect = Rectangle(3 , 5)
print(f"Recatangle: {rect.area()}")
