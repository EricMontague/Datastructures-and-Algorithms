"""This module contains my implementation of a doubly linked list with no tail pointer."""


class DoublyLinkedListNode:
    """Class to represent a node in a doubly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a representation of a node."""
        return "<Node(%r)>" %self.data


class DoublyLinkedList:
    """Class to represent a doubly linked list."""

    def __init__(self):
        self.head = None
        self.size = 0

    def peek_front(self):
        """Return the value of the first node in the linked list."""
        if self.is_empty():
            return self.head
        return self.head.data

    def peek_back(self):
        """Return the value of the last node in the linked list."""
        if self.is_empty():
            return self.head
        current = self.head
        while current.next is not None:
            current = current.next
        return current.data

    def push_front(self, data):
        """Insert a new node with the given data at the head of the linked list."""
        node = DoublyLinkedListNode(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
    
    def push_back(self, data):
        """insert a new node with the given data at the tail of the linked list."""
        node = DoublyLinkedListNode(data)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current
        self.size += 1
    
    def pop_front(self):
        """Remove the node at the head of the linked list and return its value."""
        if self.is_empty():
            raise IndexError("Linked list is empty.")
        if self.size == 1:
            data = self.head.data
            self.head = None
        else:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def pop_back(self):
        """Remove the node at the tail of the linked list and return its value."""
        if self.is_empty():
            raise IndexError("Linked list is empty.")
        if self.size == 1:
            data = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            data = current.data
            current.prev.next = current.next
        self.size -= 1
        return data

    def count(self, data):
        """Return the number of nodes in the linked list that contains the given data."""
        count = 0
        current = self.head
        while current is not None:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def value_at(self, index):
        """Return the value of the node at the given index in the linked list.
        The list starts at index 0.
        """
        if index >= self.size:
            raise IndexError("List index out of range")
        current = self.head
        for num in range(index):
            current = current.next
        return current.data

    def reverse(self):
        """Reverse the linked list."""
        self.head = self._reverse(self.head)

    def _reverse(self, head):
        """Helper method to reverse the linked list."""
        previous = None
        current = head
        while current is not None:
            next_ = current.next
            current.next = previous
            current.prev = next_
            previous = current
            current = next_
        head = previous
        return head

    def is_empty(self):
        """Return True if the linked list is empty."""
        return self.head is None

    def search(self, data):
        """Return the value of the first node in the linked list with the given data."""
        if self.is_empty():
            raise ValueError("Linked list is empty.")
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return current.data
    
    def __len__(self):
        """Return the number of nodes in the linked list."""
        return self.size

    def __contains__(self, data):
        """Return True if the given data is in the linked list."""
        return self.search(data) is not None
        