"""This module contains my implementation of a stack."""


class Stack:
    """Class to represent a stack."""

    def __init__(self):
        self.items = []
        self.size = 0
    
    def push(self, item):
        """Insert at the top of the stack."""
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        """Remove and return the top item in the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty.")
        item = self.items.pop()
        self.size -= 1
        return item
    
    def is_empty(self):
        """Return True if the stack is empty, else return False."""
        return self.size == 0
    
    def peek(self):
        """Return the value of the item on top of the stack."""
        if self.is_empty():
            return None
        return self.items[-1]
    
