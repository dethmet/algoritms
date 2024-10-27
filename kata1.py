list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = int(input("vvedite chislo"))


def function(x, a):
    if a in x:
        a_index = x.index(a)
    else:
        a_index = -1
    return a_index


a_index = function(list, number)
print(a_index)

