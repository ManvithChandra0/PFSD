# program to demonstrate default arguments in function
def demo(x, y=34):
    print("In demo function")
    print("X=", x)
    print("y=", y)


def demo1(x=11, y=22):
    print("In demo 1 function")
    print("X=", x)
    print("y=", y)


print("Outside of functions")
a, b = 27, 42
print("a=", a)
print("b=", b)
demo(a, b)
demo(34, 35)
demo(15)
demo()
