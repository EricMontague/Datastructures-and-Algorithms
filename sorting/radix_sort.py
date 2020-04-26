"""This module contains my implementations of radix sort."""


def radix_sort2(unsorted_list, base=10):
    """Implementation of radix sort. Assumes only positive integer inputs."""
    if not unsorted_list:
        return unsorted_list
    power = 0
    max_digits = find_max_digits(unsorted_list)
    for digit in range(max_digits):
        unsorted_list = counting_sort2(unsorted_list, base, power)
        power += 1
    return unsorted_list


def find_max_digits(unsorted_list):
    """Find the number of digits in the longest number in
    the list.
    """
    max_number = max(unsorted_list)
    if max_number == 0:
        return 1
    num_digits = 0
    while max_number > 0:
        num_digits += 1
        max_number //= 10
    return num_digits


def counting_sort2(unsorted_list, base, power):
    """Implementation of counting sort to be used in radix sort."""
    #build counts list
    counts = [0] * base

    #fill counts list
    for number in unsorted_list:
        digit = number // base ** power % base
        counts[digit] += 1
    
    #overwrite counts list
    #value at each index represents the number of values <= that index
    #in th original list
    for index in range(1, len(counts)):
        counts[index] = counts[index] + counts[index - 1]
    
    #fill sorted list
    sorted_list = [None] * len(unsorted_list)
    for number in unsorted_list:
        digit = number // base ** power % base
        index = counts[digit] - 1
        sorted_list[index] = number
        counts[digit] -= 1
    return sorted_list
    

#Another way to write radix sort using a different version of counting sort
def radix_sort(unsorted_list, base=10):
    """Implementation of radix sort."""
    power = 0
    #find the number of digits in the longest number
    max_digits = find_max_digits(unsorted_list)
    for digit in range(max_digits):
        counting_sort(unsorted_list, base, power)
        power += 1


def counting_sort(unsorted_list, base, power):
    """Implementation of counting sort to be used in radix sort."""
    #create buckets list
    buckets = [[] for num in range(base)]

    #fill buckets
    for number in unsorted_list:
        digit = number // base ** power % base
        buckets[digit].append(number)
    
    #overwrite values in unsorted_list
    index = 0
    for bucket in buckets:
        for number in bucket:
            unsorted_list[index] = number
            index += 1

