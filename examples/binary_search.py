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


def binary_search_iterative(arr, target):
    pass 


def binary_search_recursive(arr, target, left=None, right=None): ...


if __name__ == '__main__':
    print('hello')