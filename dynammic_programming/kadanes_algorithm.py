"""This module contains my implementation of Kadane's algorithm."""


def find_max_subarray_sum(nums):
    """Given a list of numbers, return the sum
    of the contiguous subarray with the largest
    sum.
    """
    max_sum = float("-inf")
    current_sum = 0
    for index, num in enumerate(nums):
        new_sum = current_sum + num
        current_sum = max(num, new_sum)
        max_sum = max(current_sum , max_sum)
    return max_sum
    