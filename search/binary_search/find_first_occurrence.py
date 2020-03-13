"""This module contains an algorithm to find the first occurrence of a value in
a sorted array using binary search.
"""


#Overall time complexity: O(log n), where n is the number of elements in the list
#Overall space complexity: O(1)
def binary_search_iterative(input_list, target):
    """Return the index of the first occurrence of
    the target in the sorted input_list. If the target
    does not exist in the list, return -1.
    """
    low = 0
    high = len(input_list) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if input_list[mid] > target:
            high = mid - 1
        elif input_list[mid] < target:
            low = mid + 1
        else: #input_list[mid] == target
            index = mid
            high = mid - 1
    return index


#Overall time complexity: O(log n), where n is the number of elements in the list
#Overall space complexity: O(log n), due to implicit function calls building on 
#the function call stack
def binary_search_recursive(input_list, target, low, high):
    """Return the index of the first occurrence of
    the target in the sorted input_list. If the target
    does not exist in the list, return infinity.
    """ 
    if low > high:
        return float("inf")
    mid = low + (high - low) // 2
    if input_list[mid] > target:
        return binary_search_recursive(input_list, target, low, mid - 1)
    elif input_list[mid] < target:
        return binary_search_recursive(input_list, target, mid + 1, high)
    else: #input_list[mid] == target
        return min(mid, binary_search_recursive(input_list, target, low, mid - 1))
        