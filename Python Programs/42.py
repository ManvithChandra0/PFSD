# program to find Fibonacci of a given number

def fib(x):
    if x == 0 or x == 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


n = int(input("Enter Input:"))
print("Fibonacci of", n, ":", fib(n))
