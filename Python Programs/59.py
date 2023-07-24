# program to demonstrate Method Overloading (Polymorphism)
class Demo:
    def add(self, a=None, b=None):
        if a != None and b != None:
            self.x = a
            self.y = b
            print(self.x + self.y)
        elif a != None or b != None:
            self.x = a
            self.y = "world"
            print(self.x + self.y)
        else:
            self.x = 100
            self.y = 200
            print(self.x + self.y)


d = Demo()
d.add()
d.add("Hello")
d.add(10, 20)
d.add(1.3, 1.2)
d.add("Chat", "GPT")
