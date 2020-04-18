"""This module contains my implementation of counting sort."""


def counting_sort(unsorted_list, min_value, max_value):
    """Implementation of Counting sort. Sorts a given list
    of elements where each element is within the given range.
    """
    range_size = max_value - min_value
    counts = [0] * (range_size + 1)
    for value in unsorted_list:
        counts[value - min_value] += 1
    for index, count in enumerate(counts):
        j = 0
        for k in range(count):
            unsorted_list[j] = index + min_value
            j += 1
    