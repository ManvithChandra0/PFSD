# program to demonstrate global keyword in function

z = 10  # global variable


def demo():
    s = 6  # local variable
    print("In demo function")
    print("s=", s)
    #  z=z+23    It will throw an error z is not defined as local variable
    global z
    z = z + 23
    print("z=", z)


print("Before Calling demo function")
print("z=", z)
demo()
print("After Calling demo function")
print("z=", z)
