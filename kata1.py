numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = int(input("vvedite chislo"))


def get_index(numbers, number):
    index_number = 0
    while index_number < len(numbers):
        if number == numbers[index_number]:
            return index_number
        index_number += 1
    return -1

    
print(get_index(numbers, number))

