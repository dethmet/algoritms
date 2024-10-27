list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = int(input("vvedite chislo"))


def get_calculation(numbers, num):
    count = 0
    if num not in numbers:
        return int(-1)
    else:
        for i in numbers:
            if i != num:
                count +=1
            else:
                return count


print(get_calculation(list_numbers, number))

