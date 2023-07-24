# program to demonstrate Single Inheritance

class A:
    id = 101
    name = "KLU"

    def display1(self):
        print("In Class A Display Method")
        print(self.id, self.name)


class B(A):
    gender = "FEMALE"
    maritalstatus = True

    def display2(self):
        print("In Class B Display Method")
        print(self.gender, self.maritalstatus, self.id, self.name)


a = A()
a.display1()
b = B()
b.display2()
b.display1()
print("Outside of Classes")
print(b.id, b.name, b.gender, b.maritalstatus)
