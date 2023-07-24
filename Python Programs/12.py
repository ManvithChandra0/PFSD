# program to display large number among 3 numbers using nested if else
a = int(input('enter first number : '))
b = int(input('enter second number : '))
c = int(input('enter third number : '))
if a > b:
    if a > c:
        print(a, 'big number')
    else:
        print(c, 'big number')
else:
    if b > c:
        print(b, 'big number')
    else:
        print(c, 'big number')
