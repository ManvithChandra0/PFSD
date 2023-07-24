# program to demonstrate exceptional handing

try:
    demo = [10,20,30,40]
    print(len(demo))
    # print(demo[2])
    print(demo[5])

except:
    print('Exception Occurred')
