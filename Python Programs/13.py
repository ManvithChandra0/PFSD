# program to display large number among 3 numbers using elif ladder
a = int(input('enter first number : '))
b = int(input('enter second number : '))
c = int(input('enter third number : '))
if a > b and a > c:
    print(a, 'big number')
elif b > c:
    print(b, 'big number')
else:
    print(c, 'big number')
