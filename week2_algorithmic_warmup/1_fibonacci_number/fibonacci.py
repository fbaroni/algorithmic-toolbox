# Uses python3
from random import randint
def naive_fib(n):
    if (n <= 1):
        return n

    return naive_fib(n - 1) + naive_fib(n - 2)

#n = int(input())
number = randint(1, 45)
print("computing fib of " + str(number))
print(naive_fib(number))
