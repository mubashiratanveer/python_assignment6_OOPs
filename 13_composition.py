
class Engine:
    def start(self):
        return "Engine Start"

class Car:
    def __init__(self, engine:Engine):
        self.engine = engine
    
    def start_car(self):
        return self.engine.start()
    
my_engine = Engine()

my_car = Car(my_engine)

print(my_car.start_car())
            