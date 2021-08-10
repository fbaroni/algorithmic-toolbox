# python3
from random import randint

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

if __name__ == '__main__':
    input_n = 10000
    input_numbers = [9999]*input_n
    print(max_pairwise_product(input_numbers))