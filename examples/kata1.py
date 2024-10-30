def get_index(numbers, number):
    index_number = 0
    while index_number < len(numbers):
        if number == numbers[index_number]:
            return index_number
        index_number += 1
    return -1
