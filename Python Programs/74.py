#program to demonstrate super() method

class A:
    def __init__(self,x,y):
        self.id=x
        self.name=y
    def display1(self):
        print(self.id,self.name)

class B(A):
    def __init__(self,x,y):
        super().__init__(x,y)


b = B(101,"KLU") #b is an object of Class B
b.display1()


