def get_index(arr, target):
    i_target = 0
    while i_target < (len(arr) - 1):
        if target == arr[i_target]:
            return i_target
        i_target += 1
    return -1
