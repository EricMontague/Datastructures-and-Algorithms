"""This module contains an algorithm to find the last occurrence of a value in
a sorted array using binary search.
"""


#Overall time complexity: O(log n), where n is the number of elements in the list
#Overall space complexity: O(1)
def binary_search_iterative(input_list, target):
    """Return the index of the last occurrence of
    the target in the sorted input_list. If the target
    does not exist in the list, return -1.
    """
    low = 0
    high = len(input_list) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if input_list[mid] < target:
            low = mid + 1
        elif input_list[mid] > target:
            high = mid - 1
        else: #input_list[mid] == target
            index = mid
            low = mid + 1
    return index
    