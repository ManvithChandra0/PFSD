# program to demonstrate exceptional handing

try:
    print('*** Iam In Try Block***')
    print('Run this code')

except:
    print('*** Iam In except Block***')
    print('Exception Occurred')
else:
    print('*** Iam In else Block***')
    print('No Exception Occurred')
finally:
    print('*** Iam In finally Block***')
    print('Always executed')
