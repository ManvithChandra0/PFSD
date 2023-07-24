# program to demonstrate if else to check given number is even or odd
n = int(input("Enter number : "))
if n & 1 == 0:  # n % 2 == 0:
    print(n, "is Even Number")
else:
    print(n, 'is Odd Number')
