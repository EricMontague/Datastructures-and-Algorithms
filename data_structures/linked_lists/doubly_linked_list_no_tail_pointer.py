"""This module contains my implementation of a doubly linked list with no tail pointer."""


class DoublyLinkedListNode:
    """Class to represent a node in a doubly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a representation of the doubly linked list node."""
        return "<SinglyLinkedListNode(%r)>" %self.data


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
        The list starts at index 0. Only handles positive indices.
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
        """Iterative helper method to reverse the linked list."""
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

    #alternate iterative method to reversing a linked list
    def _reverse2(self, head):
        """Iterative helper method to reverse the linked list."""
        if head is None:
            return head
        stack = []
        current = head
        while current is not None:
            stack.append(current)
            current = current.next
        head = stack.pop()
        head.prev = None
        current = head
        while stack:
            node = stack.pop()
            current.next = node
            node.prev = current
            node.next = None
            current = node
        return head    
    
    def _reverse3(self, head):
        """Recursive helper method to reverse the linked list."""
        if head is None:
            return head
        if head.next is None:
            head.prev = None
            return head
        new_head = self._reverse3(head.next)
        head.next.next = head
        head.prev = head.next
        head.next = None
        return new_head
        
    def is_empty(self):
        """Return True if the linked list is empty."""
        return self.head is None

    def insert(self, index, data):
        """Insert a node with the given data at the given index
        in the linked list.
        """
        if index >= self.size or index < 0:
            raise IndexError("Index out of range.")
        if index == 0:
            self.push_front(data)
        else:
            node = DoublyLinkedListNode(data)
            current = self.head
            for num in range(index):
                current = current.next
            current.prev.next = node
            node.prev = current.prev
            current.prev = node
            node.next = current
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
            current = self.head
            for num in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1

    def remove_value(self, data):
        """Remove the first node in the linked list with the given data."""
        if self.is_empty():
            raise ValueError("Linked list is empty.")
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is None: #at the head of the list
                    self.pop_front()
                elif current.next is None: #at the tail of the list
                    self.pop_back()
                else: #middle of list
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                return
            current = current.next
        raise ValueError("Data not in linked list.")

    def search(self, data):
        """Return the value of the first node in the linked list with the given data."""
        if self.is_empty():
            return self.head
        current = self.head
        while current is not None:
            if current.data == data:
                return current.data
            current = current.next
        return current
    
    def __len__(self):
        """Return the number of nodes in the linked list."""
        return self.size

    def __contains__(self, data):
        """Return True if the given data is in the linked list."""
        return self.search(data) is not None
    
    def __iter__(self):
        """Return an iterator of nodes' values."""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
        