# program to demonstrate exceptional handing

try:
    name = ['surya', 'kiran', 'klu']
    print(name[14])
except IndexError as e:
    print(e)
