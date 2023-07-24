# program to demonstrate for loop
print('Case 1')
for i in range(5):
    print(i)

print('Case 2')
n = int(input('Enter Range : '))
for i in range(n):
    print(i)

print('Case 3')
n = int(input('Enter Range : '))
for i in range(1, n, 2):
    print(i)

print('Case 4')
n = int(input('Enter Range : '))
for i in range(n, 1, -1):
    print(i)
