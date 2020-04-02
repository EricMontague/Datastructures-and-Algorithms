"""This module contains my implementation of a singly linked list with no tail pointer."""


class SinglyLinkedListNode:
    """Class to represent a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a representation of a node."""
        return "<SinglyLinkedListNode(%r)>" %self.data


class SinglyLinkedList:
    """Class to represent a singly linked list."""

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
        """Insert a new node at the front of the linked list."""
        node = SinglyLinkedListNode(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop_front(self):
        """Remove the node at the head of the linked list and return its value."""
        if self.is_empty():
            raise IndexError("Linked list is empty")
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.data

    def push_back(self, data):
        """Insert a new node at the tail of the linked list."""
        node = SinglyLinkedListNode(data)
        if self.is_empty():
            self.head = node
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        self.size += 1

    def pop_back(self):
        """Remove the node at the tail of the linked list and return its value."""
        if self.is_empty():
            raise IndexError("Linked list is empty")
        dummy_node = SinglyLinkedListNode(None)
        first = dummy_node
        second = dummy_node.next
        while second.next is not None:
            first = first.next
            second = second.next
        first.next = second.next
        self.head = dummy_node.next
        self.size -= 1
        return second.data

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
        previous = self._reverse2(head.next)
        head.next.next = head
        head.next = None
        return previous

    def insert(self, index, data):
        """Insert a node with the given data at the given index
        in the linked list. If the list is empty, the node
        will become the head of the list.
        """
        if index >= self.size:
            raise IndexError("Index out of range.")
        if index == 0:
            self.push_front(data)
        else:
            node = SinglyLinkedListNode(data)
            if self.is_empty():
                self.head = node
            else:
                target_index = 0
                previous = self.head
                current = self.head.next
                while target_index != index:
                    target_index += 1
                    previous = previous.next
                    current = current.next
                node.next = current
                previous.next = node
                self.size += 1
    
    def remove_at_index(self, index):
        """Remove the node from the linked list at the given index."""
        if self.is_empty():
            raise IndexError("List is empty.")
        if index >= self.size:
            raise IndexError("Index out of range.")
        if index == 0:
            self.pop_front()
        else:
            target_index = 0
            previous = self.head
            current = self.head.next
            while target_index != index:
                target_index += 1
                previous = previous.next
                current = current.next
            previous.next = current.next

    def remove_value(self, data):
        """Remove the first node in the linked list with the given data."""
        if self.is_empty():
            raise ValueError("Linked list is empty.")
        dummy = SinglyLinkedListNode(data)
        dummy.next = self.head
        previous = dummy
        current = self.head
        while current.data != data:
            if current is None:
                raise ValueError("Data not in linked list.")
            previous = previous.next
            current = current.next
        if current.data == self.head.data:
            self.pop_front()
        else:
            previous.next = current.next
    
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
