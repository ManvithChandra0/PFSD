# program to demonstrate exceptional handing

try:
    name = 'KLUNIVERSITY'
    print(len(name))
    print(name[2])
    # print[name[15]]
    print(name[1:10:2])
    print(name[::-1])
except:
    print('Exception Occurred')
