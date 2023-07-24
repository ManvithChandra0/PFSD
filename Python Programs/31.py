# program to display digits count,individual digits,sum of digits of a given number
n = int(input())
count = 0
sum = 0
while n != 0:
    digit = n % 10
    print(digit, end=" ")
    count += 1
    sum += digit
    n = n//10
print(end="\n")
print('digit count = ', count)
print("sum of digit = ", sum)
