"""This module contains an algorithm to find the total number of occurrences of a value in
a sorted array using binary search.
"""


from enum import Enum


class Occurrence(Enum):
    """Class to represent an enum."""
    FIRST = 1
    LAST = 2


#Overall time complexity: O(log n), where n is the number of elements in the list
#Overall space complexity: O(1)
def total_occurrences_iterative(input_list, target):
    """Return the total number of occurrences of the target
    in the sorted list.
    """
    first_index = binary_search_iterative(input_list, target, Occurrence.FIRST)
    last_index = binary_search_iterative(input_list, target, Occurrence.LAST)
    if first_index == -1 or last_index == -1:
        return 0
    return last_index - first_index + 1


def binary_search_iterative(input_list, target, first_or_last):
    """Return the index of the first or last occurrence of the target in
    the sorted list.
    """
    low = 0
    high = len(input_list) - 1
    index = -1 
    while low <= high:
        mid = low + (high - low) // 2
        if input_list[mid] == target and first_or_last == Occurrence.FIRST:
            index = mid
            high = mid - 1
        elif input_list[mid] == target and first_or_last == Occurrence.LAST:
            index = mid
            low = mid + 1
        elif input_list[mid] < target:
            low = mid + 1
        else: #input_list[mid] > target
            high = mid - 1
    return index
