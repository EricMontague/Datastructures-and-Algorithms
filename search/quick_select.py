"""This module contains an implementation of Quick Select using Lomuto's
partioning scheme to find the Kth smallest element in an array.
"""


def quick_select(array, k):
    if not array or (k < 1 or k > len(array)):
        return -1
    low = 0
    high = len(array) - 1
    while True:
        pivot_index = partition(array, low, high)
        kth_smallest_index = k - 1
        if kth_smallest_index == pivot_index:
            return array[kth_smallest_index]
        elif kth_smallest_index < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1


def partition(array, low, high):
    pivot_value = array[high]
    pivot_index = low
    for index in range(low, high):
        if array[index] <= pivot_value:
            swap(array, index, pivot_index)
            pivot_index += 1
    swap(array, pivot_index, high)
    return pivot_index


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

