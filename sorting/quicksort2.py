"""THis module contains my implementation of Quicksort
using Hoare's partitioning algorithm.
"""


def swap(list_, index_one, index_two):
    """Swap the elements at the two indices in the list."""
    list_[index_one], list_[index_two] = list_[index_two], list_[index_one]


def hoare_partition(unsorted_list, start, end):
    """Given an unsorted list and indices that mark the start
    and end of a segment in the list, partition the list
    around a pivot and return the index of that pivot.
    """
    pivot_index = (start + end) // 2
    pivot_value = unsorted_list[pivot_index]
    left = start
    right = end
    while True:
        while unsorted_list[left] < pivot_value:
            left += 1
        while unsorted_list[right] > pivot_value:
            right -= 1
        if left >= right:
            return right
        swap(unsorted_list, left, right)
        left += 1
        right -= 1


def quicksort(unsorted_list, start, end):
    """Implementation of Quicksort algorithm. Given an unsorted
    list of elements, sort that list in increasing order.
    """
    if start < end:
        split_index = hoare_partition(unsorted_list, start, end)
        quicksort(unsorted_list, start, split_index)
        quicksort(unsorted_list, split_index + 1, end)


array = [2, 3, 1, 5, 3, 6]
quicksort(array, 0, len(array) - 1)
print(array)
