# program to demonstrate function with arguments and with return value
def add(x, y):  # function definition
    print("In add function")
    print("x=", x)
    print("y=", y)
    return x + y


a, b = 10, 20
print("a=", a)
print("b=", b)
result = add(a, b)
print("Result=", result)
print("Result=", add(a, b))
