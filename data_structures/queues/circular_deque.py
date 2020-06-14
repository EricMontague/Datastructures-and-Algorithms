"""This module contains my implementation of a circular deque."""


class CircularDeque:
    """Class to represent a circular deque."""

    def __init__(self, max_capacity):
        if max_capacity < 1:
            raise ValueError("Max capacity must be at least 1.")
        self._max_capacity = max_capacity
        self._size = 0
        self._items = [None] * self._max_capacity
        self._front = -1
        self._back = -1

    def peek_front(self):
        """Return the value of the item at the
        front of the deque.
        """
        if self.is_empty():
            return None
        return self._items[self._front]

    def peek_back(self):
        """Return the value of the item at the back of
        the deque.
        """
        if self.is_empty():
            return None
        return self._items[self._back]

    def is_empty(self):
        """Return True if the deque if empty, else return False."""
        return self._size == 0

    def is_full(self):
        """Return True if the deque is full, else return False."""
        return self._size == self._max_capacity

    def push_front(self, item):
        """Insert an item at the front of the deque."""
        if self.is_full():
            raise ValueError("Deque is full.")
        if self.is_empty():
            self._front = 0
            self._back = 0
        else:
            self._front = (self._front + self._max_capacity - 1) % self._max_capacity
        self._items[self._front] = item
        self._size += 1

    def push_back(self, item):
        """Insert an item at the back of the deque."""
        if self.is_full():
            raise ValueError("Deque is full.")
        if self.is_empty():
            self._front = 0
            self._back = 0
        else:
            self._back = (self._back + 1) % self._max_capacity
        self._items[self._back] = item
        self._size += 1

    def pop_front(self):
        """Remove and return the item at the front of the deque."""
        if self.is_empty():
            raise ValueError("Deque is empty.")
        item = self._items[self._front]
        if self._size == 1:
            self._front = -1
            self._back = -1
        else:
            self._front = (self._front + 1) % self._max_capacity
        self._size -= 1
        return item

    def pop_back(self):
        """Remove and return the item at the back of the deque."""
        if self.is_empty():
            raise ValueError("Deque is empty.")
        item = self._items[self._back]
        if self.size == 1:
            self._front = -1
            self._back = -1
        else:
            self._back = (self._back + self._max_capacity - 1) % self._max_capacity
        self._size -= 1
        return item

    @property
    def size(self):
        """Return the number of items in the deque."""
        return self._size

