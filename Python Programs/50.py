# program to demonstrate class and object
class Student:
    # properties
    id = 101
    name = "KLU"
    gender = "MALE"

    # methods
    def display(self):
        print(self.id, self.name, self.gender)


s = Student()  # s is an object of Student Class
s.display()
