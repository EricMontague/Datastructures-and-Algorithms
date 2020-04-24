"""This module contains my implementation of counting sort."""


#Naive version of counting sort that can only handle positive integers
#This implementation is unstable.
def naive_counting_sort(unsorted_list, min_value, max_value):
    """Implementation of Counting sort. Sorts a given list
    of elements where each element is within the given range.
    Only handles positive numbers and is unstable.
    """
    range_size = max_value - min_value
    counts = [0] * (range_size + 1)
    for value in unsorted_list:
        counts[value - min_value] += 1
    position = 0
    for index, count in enumerate(counts):
        for c in range(count):
            unsorted_list[position] = index + min_value
            position += 1


#The more textbook implementation of counting sort
#Can be used to sort objects or other things, by some particular key.
#This implementation is stable
def actual_counting_sort(unsorted_list, min_value, max_value):
    """Implementation of Counting sort (stable). Sorts a given list
    of elements where each element is within the given range.
    """
    range_size = max_value - min_value

    #build frequency list
    counts = [0] * (range_size + 1)

    #fill frequency list
    for value in unsorted_list:
        counts[value - min_value] += 1
    
    #overwrite values in counts
    #Each number in the new version of counts represents the number of values
    #in the lunsorted ist that are less than or equal to that index
    for index in range(1, len(counts)):
        counts[index] = counts[index] + counts[index - 1]

    #build the final sorted list from the new version of counts
    sorted_list = [None] * len(unsorted_list)
    for value in unsorted_list:
        index = counts[value - min_value] - 1
        sorted_list[index] = value
        counts[value - min_value] -= 1
    return sorted_list


#A less verbose and easier way to write counting sort
#Takes advantage of python lists to achieve the same result as above.
#This implementation is stable as well
def actual_counting_sort2(unsorted_list, min_value, max_value):
    """Implementation of Counting sort (stable). Sorts a given list
    of elements where each element is within the given range.
    """
    range_size = max_value - min_value
    #create buckets list, which is a list of lists
    buckets = [[]] * (range_size + 1)
    for value in unsorted_list:
        buckets[value - min_value].append(value)
    
    #build sorted list from buckets list
    sorted_list = []
    for bucket in buckets:
        for value in bucket:
            sorted_list.append(value + min_value)
    return sorted_list

    