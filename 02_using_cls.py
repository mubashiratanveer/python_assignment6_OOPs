
class counter:
    count = 0

    def __init__(self):
        counter.count += 1

    @classmethod
    def display_count(cls):
        print(f'Total onjects: {cls.count}') 

Obj1 = counter()
Obj2 = counter()
Obj3 = counter()
obj4 = counter()

counter.display_count()