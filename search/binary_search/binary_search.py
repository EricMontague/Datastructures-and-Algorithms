"""This module contains implementations of binary search."""


def binary_search_iterative(input_list, target):
    """Return the index of the target,
    if it exists, in sorted input list. If the target does 
    not exist in the list, return -1.
    """
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if input_list[mid] == target:
            return mid
        if input_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recursive(input_list, target, low, high):
    """Return the index of the target,
    if it exists, in sorted input list. If the target does 
    not exist in the list, return -1.
    """
    # base case
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if target == input_list[mid]:
        return mid
    if target < input_list[mid]:
        return binary_search_recursive(input_list, target, low, mid - 1)
    else: #target > input_list[mid]
        return binary_search_recursive(input_list, target, mid + 1, high)


