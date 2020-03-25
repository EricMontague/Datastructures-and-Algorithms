"""This module contains my implementation of a singly linked list with no tail pointer."""


class Node:
    """Class to represent a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Class to represent a singly linked list."""

    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, data):
        """Insert a new node at the front of the linked list."""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop_front(self):
        """Remove and return the first node in the linked list."""
        if self.is_empty():
            raise IndexError("Linked list is empty")
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node

    def push_back(self, data):
        """Insert a new node at the tail of the linked list."""
        node = Node(data)
        if self.is_empty():
            self.head = node
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        self.size += 1

    def pop_back(self):
        """Remove and return the last item in the linked list."""
        if self.is_empty():
            raise IndexError("Linked list is empty")
        dummy_node = Node(None)
        first = dummy_node
        second = dummy_node.next
        while second.next is not None:
            first = first.next
            second = second.next
        first.next = second.next
        self.head = dummy_node.next
        self.size -= 1
        return second

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
        if index >= self.size or index < self.size:
            raise IndexError("List index out of range")

        current = self.head
        if index >= 0: #index is positive
            for _ in range(index):
                current = current.next
        else: #index is negative
            index = self.size - abs(index)
            for _ in range(index):
                current = current.next
        return current
    
    def is_empty(self):
        """Return True if the linked list is empty."""
        return self.size == 0
    
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
            previous = current
            current = next_
        head = previous
        return head

    #a recursive way to reverse a linked list
    def _reverse2(self, head):
        """Helper method to reverse a linked list."""
        if head is None or head.next is None:
            return head
        previous = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return previous
