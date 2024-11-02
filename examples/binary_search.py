def binary_search_iterative(arr, target):
    min_index = 0
    max_index = len(arr) - 1
    mid_index = len(arr) // 2
    while arr[mid_index] != target and min_index <= max_index:
        if target > arr[mid_index]:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
        mid_index = (max_index + min_index) // 2
    
    if min_index > max_index:
        return -1
    else:
        return mid_index


def binary_search_recursive(arr, target, left=None, right=None):

    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
        
    if left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:
            return binary_search_recursive(arr, target, mid + 1, right)
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, left, mid - 1)
        else:
            return mid
    else:
        return -1
    