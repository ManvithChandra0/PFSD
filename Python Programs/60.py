# program to demonstrate method overriding
class A:
    def display(self):
        print(' Class A display method ')


class B(A):
    def display(self):
        print(' Class A display method')


a = A()
a.display()
b = B()
b.display()
