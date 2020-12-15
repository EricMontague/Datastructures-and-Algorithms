"""This module contains an implementation of Quick Select using Hoare's
partioning scheme to find the Kth smallest element in an array.
"""


def quick_select2(array, k):
    low = 0
    high = len(array) - 1
    while low != high:
        split_index = partition(array, low, high)
        if k - 1 <= split_index:
            high = split_index
        else:
            low = split_index + 1
    return array[low]


def partition(array, low, high):
    pivot_index = (low + high) // 2
    pivot_value = array[pivot_index]
    left = low
    right = high
    while True:
        while array[left] < pivot_value:
            left += 1
        while array[right] > pivot_value:
            right -= 1
        if left >= right:
            return right
        swap(array, left, right)
        left += 1
        right -= 1


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

