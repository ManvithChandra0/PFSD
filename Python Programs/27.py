# program to demonstrate while loop with else statement
print('case:1')
n = int(input('Enter Range : '))
i = 1
while i <= n:
    print(i)
    i += 1
else:
    print('End of loop')
    
print('case:2')
n = int(input('Enter Range : '))
i = 1
while i <= n:
    if(i % 5 ==0):
        break
    else:
        print(i)
    i += 1
else:
    print('End of loop')
