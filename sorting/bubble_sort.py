"""This module contains my implementation of bubble sort."""


def bubble_sort(input_list):
    """Implementation of bubble sort. Sorts an unsorted list
    in-place."""
    for i in range(len(input_list) - 1):
        swapped = False
        for j in range(len(input_list) - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if not swapped:
            break
            