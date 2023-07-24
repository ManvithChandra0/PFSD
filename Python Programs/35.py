# program to demonstrate function with no arguments and with return value
def add():  # function definition
    print("In add function")
    x, y = 1, 2
    print("x=", x)
    print("y=", y)
    return x + y


result = add()
print("Result=", result)
print("Result=", add())
