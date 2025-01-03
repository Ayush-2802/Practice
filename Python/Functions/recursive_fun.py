factorial = lambda n : 1 if n == 0 or n == 1 else n*factorial(n-1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Factorial(number) n : "))
print(f"Factorial of {n} is", factorial(n))

#fibonacci number
fibo = lambda n : 0 if n==0 else 1 if n==1 or n==2 else fibo(n-1)+fibo(n-1)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Fibonacci(number) n : "))
print(f"Fibonacci of {n} is", fibonacci(n))

# Recursive function to print the Fibonacci series
def fib(n, prev1, prev2):
    if n < 3:
        return
    fn = prev1 + prev2
    prev2 = prev1
    prev1 = fn
    print(fn, end=" ")
    fib(n - 1, prev1, prev2)

def print_fib(n):
    if n < 1:
        print("Invalid number of terms")
    elif n == 1:
        print(0)
    elif n == 2:
        print("0 1")
    else:
        print("0 1", end=" ")
        fib(n, 1, 0)

n = 9
print_fib(n)