"""This module contains my implementation of insertion sort."""


def insertion_sort(unsorted_list):
    """Implementation of insertion sort. Insertion sort is 
    a stable sorting algorithm that sorts an 
    unsorted list of elements in-place."""
    for index in range(1, len(unsorted_list)):
        value_to_sort = unsorted_list[index]
        insertion_index = index
        while insertion_index > 0 and value_to_sort < unsorted_list[insertion_index - 1]:
            unsorted_list[insertion_index] = unsorted_list[insertion_index - 1]
            insertion_index -= 1
        unsorted_list[insertion_index] = value_to_sort

        