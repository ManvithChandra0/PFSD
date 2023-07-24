# program to demonstrate MultiLevel Inheritance

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


class C(B):
    cgpa = 8.58
    backlogs = 0

    def display3(self):
        print("In Class C Display Method")
        print(self.cgpa, self.backlogs, self.gender, self.maritalstatus, self.id, self.name)


a = A()
b = B()
c = C()
a.display1()
b.display1()
b.display2()
c.display1()
c.display2()
c.display3()
