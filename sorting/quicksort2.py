"""THis module contains my implementation of Quicksort
using Hoare's partitioning algorithm.
"""


def hoare_partition(unsorted_list, start, end):
    """Given an unsorted list and indices that mark the start
    and end of a segment in the list, partition the list
    around a pivot and return the index of that pivot.
    """
    pass


def quicksort(unsorted_list, start, end):
    """Implementation of Quicksort algorithm. Given an unsorted
    list of elements, sort that list in increasing order.
    """
    if len(unsorted_list) > 1:
        pivot_index = hoare_partition(unsorted_list, start, end)
        quicksort(unsorted_list, start, pivot_index - 1)
        quicksort(unsorted_list, pivot_index + 1, end)

