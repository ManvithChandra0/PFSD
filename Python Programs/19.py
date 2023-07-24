# program to demonstrate continue statement
n = int(input('Enter Range : '))
for i in range(1, n+1):
    if i == 4:
        continue
    else:
        print(i)
