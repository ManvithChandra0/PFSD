# program to demonstrate variable length argument in function
def demo(*numbers):
    print('In Demo Function ')
    for number in numbers:
        print(number)


a, b, c = 10, 20, 30
print('a = ', a)
print('b = ', b)
print('c = ', c)
demo(a, b, c)
