# program to display 0 to n even numbers using while loop
n = int(input('enter range : '))
i = 0
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1
