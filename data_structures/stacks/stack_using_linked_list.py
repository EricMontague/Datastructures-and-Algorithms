"""This module contains my implementation of a stack
based on a singly linked list.
"""


class StackItem:
    """Class to represent an item in a stack."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Class to represent a stack based on a singly linked list."""

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, data):
        """Insert the given data on top of the stack."""
        item = StackItem(data)
        item.next = self._head
        self._head = item
        self._size += 1

    def pop(self):
        """Remove and return the value of the item on top of the
        stack.
        """
        if self.is_empty():
            raise IndexError("Stack is empty.")
        item = self._head.data
        self._head = self._head.next
        self._size -= 1
        return item

    def is_empty(self):
        """Return True if the stack is empty, else return False."""
        return self._size == 0

    def peek(self):
        """Return the value of the item on the top of the stack."""
        if self.is_empty():
            return None
        return self._head.data

    @property
    def size(self):
        """Return the number of items in the stack."""
        return self._size
