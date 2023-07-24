# program to display 1 to n odd numbers
n = int(input('enter range : '))
for i in range(1, n + 1):  # for i in range(1, n+1, 2): print(i, end=" ")
    if i % 2 != 0:
        print(i)
