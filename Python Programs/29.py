# program to display digits of a given number
n = int(input('Enter Number : '))
while n != 0:
    digit = n%10
    print(digit, end=" ")
    n=n//10
