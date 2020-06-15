"""This module contains my implementation of a stack."""


class Stack:
    """Class to represent a stack."""

    def __init__(self):
        self._items = []
        self._size = 0

    def push(self, item):
        """Insert at the top of the stack."""
        self._items.append(item)
        self._size += 1

    def pop(self):
        """Remove and return the top item in the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty.")
        item = self._items.pop()
        self._size -= 1
        return item

    def is_empty(self):
        """Return True if the stack is empty, else return False."""
        return self._size == 0

    def peek(self):
        """Return the value of the item on top of the stack."""
        if self.is_empty():
            return None
        return self._items[-1]

    @property
    def size(self):
        """Return the number of items on the stack."""
        return self._size
