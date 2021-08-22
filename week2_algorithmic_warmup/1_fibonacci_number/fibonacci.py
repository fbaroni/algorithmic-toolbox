# Uses python3
from random import randint
def naive_fib(n):
    if (n <= 1):
        return n

    return naive_fib(n - 1) + naive_fib(n - 2)

def efficient_fib(n):
    if 0 == n:
        return 0 
    if 1 == n:
        return 1 

    fibonacci_numbers = [None] * n
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n):
        fibonacci_numbers[i] = fibonacci_numbers[i-1] + fibonacci_numbers[i-2]

    return fibonacci_numbers[n-1] + fibonacci_numbers[n-2]
n = int(input())
print(efficient_fib(n))