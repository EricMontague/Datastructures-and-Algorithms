"""This module contains my implementation of selection sort."""


def selection_sort(unsorted_list):
    """Implementation of selection sort. Selection sort
    is a non-stable sorting algorithm that sorts an unsorted list
    of elements in place.
    """
    for i in range(len(unsorted_list) - 1):
        minimum_value_index = i
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[minimum_value_index]:
                minimum_value_index = j
        unsorted_list[i], unsorted_list[minimum_value_index] = unsorted_list[minimum_value_index], unsorted_list[i]

