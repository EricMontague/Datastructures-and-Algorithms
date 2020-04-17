"""This module contains my implementation of a Binary Max Heap. Unlike my sorting
implementation of heapsort, this uses a 1-based list to make calculating parent and
child relationships more natural.
"""


class BinaryMaxHeap:
    """Class to represent a Binary Max Heap."""

    def __init__(self):
        self._heap = [None]
        self.size = 0

    def get_max(self):
        """Return the largest value in the max heap."""
        return self._heap[1]

    def extract_max(self):
        """Remove the largest element from the heap and return its value."""
        if self.is_empty():
            return None
        max_value = self._heap[1]
        last_value = self._heap.pop()
        self.size -= 1
        # Check for the edge case of removing the last element from the heap
        if not self.is_empty():
            self._heap[1] = last_value
            self._sift_down(1)
        return max_value

    def insert(self, value):
        """Insert the given value into the heap."""
        self._heap.append(value)
        self.size += 1
        self._sift_up(self.size)

    def heapify(self, input_list):
        """Given a list, turn it into a max heap."""
        self._heap += input_list
        self.size = len(input_list)
        for index in range(self.size // 2, 0, -1):
            self._sift_down(index)

    def remove_at(self, index):
        """Given an index in the heap, remove that element from the heap."""
        if self.is_empty():
            raise IndexError("Max heap is empty.")
        if index < 1 or index > self.size:
            raise IndexError("Index out of range.")
        last_value = self._heap.pop()
        self.size -= 1
        # Check for the edge case of removing the last element from the heap
        if not self.is_empty():
            self._heap[1] = last_value
            self._sift_down(index)

    def is_empty(self):
        """Return True if the heap is empty."""
        return self.size == 0

    def _sift_down(self, parent):
        """Continuously swap the parent node with its children until it's in its proper
        location in the max heap.
        """
        while parent <= self.size:
            left_child = self._get_left_child(parent)
            right_child = self._get_right_child(parent)
            # check if parent is a leaf node
            if left_child > self.size:
                break
            # find largest child node
            largest_child = left_child
            if (
                right_child <= self.size
                and self._heap[right_child] > self._heap[largest_child]
            ):
                largest_child = right_child
            # compare parent and largest child, swapping if necessary
            if self._heap[parent] < self._heap[largest_child]:
                self._heap[parent], self._heap[largest_child] = (
                    self._heap[largest_child],
                    self._heap[parent],
                )
                parent = largest_child
            else:
                break

    def _sift_up(self, child):
        """Continuously swap the child node with its parent until it's in its proper
        location in the heap.
        """
        while child > 1:
            parent = self._get_parent(child)
            if self._heap[parent] < self._heap[child]:
                self._heap[parent], self._heap[child] = (
                    self._heap[child],
                    self._heap[parent],
                )
                child = parent
            else:
                break

    def _get_left_child(self, parent):
        """Return the left child index of the given parent index in the heap."""
        return 2 * parent

    def _get_right_child(self, parent):
        """Return the left child index of the given parent index in the heap."""
        return 2 * parent + 1

    def _get_parent(self, child):
        """Return the parent index of the given child index in the heap."""
        return child // 2

    def __contains__(self, value):
        """Return True if the given value is in the heap."""
        return value in self._heap

