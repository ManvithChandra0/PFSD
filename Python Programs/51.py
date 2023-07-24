# program to demonstrate class and object
class Student:
    # properties
    # methods
    def read(self, x, y):
        self.sid = x
        self.sname = y

    def display(self):
        print(self.sid, self.sname)


s = Student()  # s is an object of Student Class
id = int(input("Enter ID:"))
name = input("Enter Name:")
s.read(id, name)
s.display()
