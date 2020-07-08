"""This module contains my implementation of a hash table using chaining to 
handle key collisions.
"""


class HashItem:
    """Class to represent a key-value pair in a hash table that uses
    chaining to handle key collisions.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

class HashTable:
    """Class to represent a hash table."""

    def __init__(self):
        self._buckets = [None] * 8
    
    def get_item(self, key):
        """Return the item associated with the given key."""
        index = self._hash(key, len(self._buckets))
        head = self._buckets[index]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def set_item(self, key, value):
        """Insert the given value into the hash table. If there is
        already a value associated with the given key, then the
        value will be overwritten.
        """
        index = self._hash(key, len(self._buckets))
        head = self._buckets[index]
        new_item = HashItem(key, value)
        if head is not None:
            new_item.next = head
        self._buckets[index] = new_item

    def delete_item(self, key):
        """Delete an item in the hash table with the given key."""
        index = self._hash(key, len(self._buckets))
        head = self._buckets[index]
        if head is None:
            raise ValueError("Key not in hash table.")
        # Remove from head
        if head.key == key:
            self._buckets[index] = self._buckets[index].next
        else: # Remove from middle or end
            target = head.next
            while True:
                if target is None:
                    raise ValueError("Key not in hash table.")
                if target.key == key:
                    head.next = target.next
                    break
                target = target.next
                head = head.next
            
    def __getitem__(self, key):
        """"Return the item associated with the given key."""
        return self.get_item(key)

    def __setitem__(self, key, value):
        """Insert the given value into the hash table. If there is
        already a value associated with the given key, then the
        value will be overwritten.
        """
        self.set_item(key, value)
    
    def __delitem__(self, key):
        """Delete an item in the hash table with the given key."""
        self.delete_item(key)
    
    def __contains__(self, key):
        """Return True if there is a value associated with the given key
        in the hash table.
        """
        return self.get_item(key) is not None
        
    def _hash(self, key, num_buckets):
        """Map the given key to a value from 0 to num_buckets - 1."""
        return hash(key) % num_buckets
    
    def _grow(self):
        """Double the size of the hash table."""
        pass

    def _shrink(self):
        """Halve the size of the hash table."""
        pass

