"""This module contains my implementation of a Circular Queue."""


class CircularQueue:
    """Class to represent a circular queue."""

    def __init__(self, max_capacity):
        if max_capacity < 1:
            raise ValueError("Max capacity can't be less than 1.")
        self._max_capacity = max_capacity
        self._size = 0
        self._items = [None] * max_capacity
        self._front = -1
        self._rear = -1

    def enqueue(self, item):
        """Insert item at the rear of the queue."""
        if self.is_full():
            raise ValueError("Queue is full.")
        if self.is_empty():
            self._front += 1
            self._rear += 1
        else:
            self._rear = (self._rear + 1) % self._max_capacity
        self._items[self._rear] = item
        self._size += 1

    def dequeue(self):
        """Remove and return item located at the front of the queue."""
        if self.is_empty():
            raise ValueError("Queue is empty.")
        item = self._items[self._front]
        if self._size == 1:
            self._front = -1
            self._rear = -1
        else:
            self._front = (self._front + 1) % self._max_capacity
        self.size -= 1
        return item

    def is_full(self):
        """Return True if the queue is full, else return False."""
        return self._size == self._max_capacity

    def is_empty(self):
        """Return True if the queue is empty, else return False."""
        return self.size == 0

    def peek(self):
        """Return the value of the item located at the front of the queue."""
        if self.is_empty():
            return None
        return self._items[self._front]

    @property
    def size(self):
        """Return the number of items in the queue."""
        return self._size

