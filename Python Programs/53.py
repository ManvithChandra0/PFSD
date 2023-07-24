# program to demonstrate parameterized constructor
class Student:
    def __init__(self, x, y):
        self.sid = x
        self.sname = y

    def display(self):
        print(self.sid, self.sname)


id = 101
name = "KLU"
s1 = Student(id, name)  # s1 is an object of Student Class
s1.display()
s2 = Student(32079, "Manvith")  # s2 is an object of Student Class
s2.display()
