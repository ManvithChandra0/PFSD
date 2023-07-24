# program to demonstrate exceptional handing

try:
    a = int(input('Enter first Number:'))
    b = int(input('Enter Second number:'))
    print(a / b)
except:
    print('Exception Occurred')
else:
    print('No Exception Occurred')
