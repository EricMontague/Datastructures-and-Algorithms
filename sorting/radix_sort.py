"""This module contains my implementation of radix sort."""


def radix_sort2(unsorted_list):
    """Implementation of radix sort."""
    pass


def radix_sort(unsorted_list, base=10):
    """Implementation of radix sort."""
    power = 0
    sorted_list = []
    while unsorted_list:
        #create buckets list
        buckets = [[] for num in range(base)]

        #fill buckets
        for number in unsorted_list:
            digit = number // base ** power % base
            buckets[digit].append(number)
        
        #empty the buckets list
        unsorted_list = []
        for bucket in buckets:
            for number in bucket:
                #figure out if you are at the most significant digit
                if number < base ** (power + 1):
                    sorted_list.append(number)
                else:
                    unsorted_list.append(number)
        power += 1
    return sorted_list

