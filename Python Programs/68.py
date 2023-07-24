# program to demonstrate exceptional handing

try:
    # x = 10
    name = 'KLU'
    demo = [10,20,3.5,'klu',40]
    a = 10
    b = 0
    print(x)
    print(name[2])
    print(demo[3])
    print(a/b)
except Exception as e:
    print(e)
