def get_index(arr, target):
    index_target = 0
    while index_target < (len(arr) - 1):
        if target == arr[index_target]:
            return index_target
        index_target += 1
    return -1
