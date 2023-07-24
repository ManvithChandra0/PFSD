# program to check whether given number is prime or not
n = int(input("Enter Number:"))
count = 0
if n == 0 or n == 1:
    print(n, "is not a prime number")
else:
    for i in range(2, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 1:
        print(n, "is a prime number")
    else:
        print(n, 'is not a prime number')
