# program to demonstrate Hybrid Inheritance

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


class C(A):
    cgpa = 8.58
    backlogs = 0

    def display3(self):
        print("In Class C Display Method")
        print(self.cgpa, self.backlogs, self.id, self.name)


class D(B, C):
    dept = "CSE"

    def display4(self):
        print("In Class D Display Method")
        print(self.dept, self.gender, self.maritalstatus, self.cgpa, self.backlogs, self.id, self.name)


a = A()
b = B()
c = C()
d = D()
a.display1()
b.display1()
b.display2()
c.display3()
c.display1()
d.display4()
d.display2()
d.display3()
d.display1()
