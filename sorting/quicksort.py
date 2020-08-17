"""This module contains my implementation of quicksort. This implementation
uses Lomuto's partitioning algorithm.
"""


import random

def swap(unsorted_list, index_one, index_two):
    """Swap the elements at the given indices in the list."""
    unsorted_list[index_one], unsorted_list[index_two] = (
        unsorted_list[index_two],
        unsorted_list[index_one]
    )


def partition(unsorted_list, start, end):
    """Given an unsorted list and indices that mark the start
    and end of a segment in the list, partition the list
    around a pivot and return the index of that pivot.
    """
    pivot_value = unsorted_list[end]
    pivot_index = start
    for index in range(start, end):
        if unsorted_list[index] <= pivot_value:
            swap(unsorted_list, index, pivot_index)
            pivot_index += 1
    swap(unsorted_list, pivot_index, end)
    return pivot_index


def randomized_partition(unsorted_list, start, end):
    """Given an unsorted list and indices that mark the start
    and end of a segment in the list, choose a random element
    to act as the pivot value. This is done to reduce the chance 
    of encountering the worst case runtime of quicksort, which is O(n ^2).
    """
    random_pivot_index = random.randint(start, end)
    swap(unsorted_list, random_pivot_index, end)
    return partition(unsorted_list, start, end)


def quicksort(unsorted_list, start, end):
    """Implementation of Quicksort algorithm. Given an unsorted
    list of elements, sort that list in increasing order.
    """
    if start < end:
        pivot_index = randomized_partition(unsorted_list, start, end)
        quicksort(unsorted_list, start, pivot_index - 1)
        quicksort(unsorted_list, pivot_index + 1, end)

