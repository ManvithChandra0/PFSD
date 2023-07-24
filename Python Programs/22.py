"""python program to display n natural numbers in such a way that
if the numbers are divisible by 5 print klu else print number"""
n = int(input('Enter Range : '))
for i in range(1, n+1):  
    if i % 5 == 0:
        print('KLU')
    else:
        print(i)  
