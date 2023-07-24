# program to demonstrate keyword arguments in function
def demo(x, y):
    print("In demo function")
    print("×=", x)
    print("y=", y)


print("Outside of demo function")
a, b = 27, 42
print("a=", a)
print("b=", b)
demo(a, b)
demo(16, 32)
demo(x=100, y=200)
