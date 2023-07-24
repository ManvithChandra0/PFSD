# program to display 0 to n even numbers using for loop
n = int(input('Enter Range :'))
for i in range(n + 1):
    if i % 2 == 0:
        print(i)
