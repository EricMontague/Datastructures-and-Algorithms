"""This module contains my implementation of merge sort."""


def merge(parent, left, right):
    """Given two sorted child lists, merge the contents of both 
    lists into their parent list in sorted order. The total number 
    of elements in between both child lists equals the number of 
    elemnts in the parent list, and all elements in the parent list 
    occur in the child lists.
    """
    parent_index = 0
    left_index = 0
    right_index = 0
    #merge smallest elements into parent list until one child
    #list is exhausted
    while left_index < len(left) and right_index < len(right):
        #need to use <= so that the sort is stable
        if left[left_index] <= right[right_index]:
            parent[parent_index] = left[left_index]
            left_index += 1
        else:
            parent[parent_index] = right[right_index]
            right_index += 1
        parent_index += 1
    
    #merge the remaining values from the non-empty child list
    #into the parent list
    while left_index < len(left):
        parent[parent_index] = left[left_index]
        left_index += 1
        parent_index += 1

    while right_index < len(right):
        parent[parent_index] = right[right_index]
        right_index += 1
        parent_index += 1


def merge_sort(unsorted_list):
    """Implementation of merge sort. Given an unsorted list,
    sort the list in increasing order.
    """
    #list of size 1 is by definition, sorted
    if len(unsorted_list) < 2:
        return
    #calculate mid index in list
    mid_index = len(unsorted_list) // 2

    #split list into two halves
    left = unsorted_list[0: mid_index]
    right = unsorted_list[mid_index:]

    #recursive calls to split the halves into halves
    merge_sort(left)
    merge_sort(right)

    #merge sorted child lists into their parent
    merge(unsorted_list, left, right)

