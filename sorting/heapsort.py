"""This module contains my implementation of heap sort. Note this uses a zero-based
implementation of a heap to keep consistent with Python's zero-based lists.
"""


def _get_left_child(parent):
    """Return the left child of a parent index in a max heap."""
    return 2 * parent + 1


def _get_right_child(parent):
    """Return the right child of a parent index in a max heap."""
    return 2 * parent + 2


def _sift_down(heap, heap_size, parent):
    """Correct a single violation of the heap invariant by shifting the parent
    element down in the heap, until it is in its proper place.
    """
    while parent < heap_size:
        left_child = _get_left_child(parent)
        right_child = _get_right_child(parent)
        #check to see if you are at a leaf node
        if left_child >= heap_size:
            break
        largest_child = left_child
        #compare child nodes
        if right_child < heap_size and heap[right_child] > heap[largest_child]:
            largest_child = right_child
        #compare parent and largest child
        if heap[parent] < heap[largest_child]:
            heap[parent], heap[largest_child] = heap[largest_child], heap[parent]
            parent = largest_child
        else: 
            break


def _heapify(input_list):
    """In-place algorithm to transform the input list into a max heap."""
    list_length = len(input_list)
    for index in range(list_length // 2, -1, -1):
        _sift_down(input_list, list_length, index)


def heapsort(unsorted_list):
    """Implementation of heapsort. Heapsort is an in-place,
    unstable sorting algorithm.
    """
    _heapify(unsorted_list)
    for index in range(len(unsorted_list) - 1, 0, -1):
        #swap greatest element in heap with last element
        unsorted_list[0], unsorted_list[index] = unsorted_list[index], unsorted_list[0]
        #correct violation of heap invariant
        _sift_down(unsorted_list, index, 0)


