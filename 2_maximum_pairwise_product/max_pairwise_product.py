# python3
def max_pairwise_product(numbers):
    n = len(numbers)
    max1 = 0
    index_max1 = 0
    max2 = 0
    index_max2 = 0
    for index in range(n):
        if(numbers[index]) > max1:
            index_max1 = index
            max1 = numbers[index]

    for index in range(n):
        if(numbers[index]) > max2 and index_max1 != index:
            index_max2 = index
            max2 = numbers[index]

    return numbers[index_max1] * numbers[index_max2] 

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))