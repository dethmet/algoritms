#Программа написана для определения количества необходимых и тераций для поиска числа
border_min = int(input('Vvedite nizhniy predel poiska: '))
border_max = int(input('Vvedite verhniy predel poiska: '))
random_number = int(input('Vvedite chislo dlya poiska: '))

def search_number(min, max, num):
    searcher = (max + min) //2
    count = 0
    while num != searcher:
        if num < searcher:
            max = searcher
            searcher = (searcher + min) // 2
        else:
            min = searcher
            searcher = (max + searcher) //2
        count += 1
    return count


print(search_number(border_min, border_max, random_number))