"""This module contains my implementation of selection sort."""


def selection_sort(input_list):
    """Implementation of selection sort. Selection sort
    is a non-stable sorting algorithm that sorts an unsorted list
    of elements in place.
    """
    for i in range(len(input_list) - 1):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
