# python3
from random import randint
if __name__ == '__main__':
    print("Enter the total of numbers to generate the sample for the algorithm")
    input_number = int(input())
    numbers_to_test = [None] * input_number
    for index, number in enumerate(numbers_to_test):
        numbers_to_test[index] = randint(1,99)

    for number in numbers_to_test:
        print(str(number), end =" ")