
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls
    

@add_greeting
class person:
    pass    

p = person()
print(p.greet())