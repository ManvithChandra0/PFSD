# program to check given number is amstorng or not
n = int(input('Enter Number : '))
temp = n
sum = 0
while n != 0:
    digit = n%10
    sum += pow(digit,3)
    n=n//10
if temp == sum :
    print('is an amstrong number')
else:
    print('it is not an amstrong number')
