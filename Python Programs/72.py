# program to demonstrate Method Resolution Order
class A:
    def display1(self):
        print("In Class C Display Method")


class B(A):
    def display2(self):
        print("In Class C Display Method")


class C(A):
    def display3(self):
        print("In Class C Display Method")


class D(B, C):
    def display4(self):
        print("In Class D Display Method")


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
