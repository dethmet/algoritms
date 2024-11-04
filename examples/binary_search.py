def binary_search_iterative(arr, target):
    min_index = 0
    max_index = len(arr) - 1
    while min_index <= max_index:
        mid_index = (max_index + min_index) // 2
        if target == arr[mid_index]:
            return mid_index
        elif target > arr[mid_index]:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search_recursive(arr, target, mid + 1, right)
    return binary_search_recursive(arr, target, left, mid - 1)
    