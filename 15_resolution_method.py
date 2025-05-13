
class A:
    def show(self):
        print("Show from class A.")

class B:
    def show(A):
        print("Show from class B.")

class C:
    def show(A):
        print("Show from class C.")


class D(B,C):
    pass

obj = D()
obj.show()


print(D.__mro__)

