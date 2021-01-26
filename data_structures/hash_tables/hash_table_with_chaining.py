"""This module contains my implementation of a hash table using chaining to 
handle key collisions.
"""


from data_structures.linked_lists.singly_linked_list_no_tail_pointer import (
    SinglyLinkedList,
)


class HashTableItem:
    """Class to represent a key-value pair in a hash table that uses
    chaining to handle key collisions.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key


class HashTable:
    """Class to represent a hash table."""

    def __init__(self, capacity=8, max_load_factor=0.75, min_load_factor=0.25):
        if capacity < 1:
            raise ValueError("Capacity must be greater than 1.")
        if max_load_factor <= 0 or max_load_factor > 1:
            raise ValueError(
                "Max load factor must be greater than 0, but less than or equal to 1."
            )
        if min_load_factor <= 0 or min_load_factor > 1:
            raise ValueError(
                "Min load factor must be greater than 0, but less than or equal to 1."
            )
        self._capacity = capacity
        self._max_load_factor = max_load_factor
        self._min_load_factor = min_load_factor
        self._table = [None] * self._capacity
        self._num_items = 0

    def get(self, key):
        """Return the item associated with the given key."""
        if key is None:
            raise KeyError("None is not a valid key")
        bucket_index = self._hash_key(key)
        linked_list = self._table[bucket_index]
        if not linked_list:
            return None
        hash_table_item = HashTableItem(key, None)
        returned_item = linked_list.find_value(hash_table_item)
        if not returned_item:
            return None
        return returned_item.value

    def put(self, key, value):
        """Insert the given value into the hash table. If there is
        already a value associated with the given key, then the
        value will be overwritten.
        """
        if key is None:
            raise KeyError("None is not a valid key")
        bucket_index = self._hash_key(key)
        hash_table_item = HashTableItem(key, value)
        if not self._table[bucket_index]:
            self._table[bucket_index] = SinglyLinkedList()
        linked_list = self._table[bucket_index]
        returned_item = linked_list.find_value(hash_table_item)
        if not returned_item:
            linked_list.push_front(hash_table_item)
            self._num_items += 1
            if self._should_double():
                self._resize_table(2)
        else:
            returned_item.value = value

    def delete(self, key):
        """Delete an item in the hash table with the given key."""
        if key is None:
            raise KeyError("None is not a valid key")
        bucket_index = self._hash_key(key)
        hash_table_item = HashTableItem(key, None)
        linked_list = self._table[bucket_index]
        if linked_list is None:
            raise KeyError("Key not in hash table.")
        node = linked_list.find_value(hash_table_item)
        if not node:
            raise KeyError("Key not in hash table")
        linked_list.remove_node(hash_table_item)
        self._num_items -= 1
        if self._should_halve():
            self._resize_table(0.5)

    def exists(self, key):
        """Return True if there is a value associated with the given key 
        in the hash table.
        """
        return self.get(key) is not None

    def is_empty(self):
        """Returns True or False depending on whether the hash table is empty."""
        return self._num_items == 0

    def keys(self):
        """Return a list of keys found in the hash table."""
        keys = []
        for linked_list in self._table:
            if linked_list:
                for hash_table_item in linked_list:
                    keys.append(hash_table_item.key)
        return keys

    def values(self):
        """Return a list of values found in the hash table."""
        values = []
        for linked_list in self._table:
            if linked_list:
                for hash_table_item in linked_list:
                    values.append(hash_table_item.value)
        return values

    def items(self):
        """Return a list of tuples that contains the key-value
        pairs found in the hash table.
        """
        pairs = []
        for linked_list in self._table:
            if linked_list:
                for hash_table_item in linked_list:
                    pairs.append((hash_table_item.key, hash_table_item.value))
        return pairs

    def clear(self):
        """Clear all of the contents of the hash table."""
        self._table = [None] * self._capacity
        self._num_items = 0

    @property
    def num_items(self):
        """Returns the number of items currently in the hash table."""
        return self._num_items

    def _hash_key(self, key):
        """Map the given key to a value from 0 to num_buckets - 1."""
        return hash(key) % self._capacity

    def _should_double(self):
        """Return True if the table size should be doubled."""
        return self._num_items >= self._capacity * self._max_load_factor

    def _should_halve(self):
        """Return True if the table size should be halved."""
        return self._num_items <= self._capacity * self._min_load_factor

    def _resize_table(self, multiple):
        """Rehash the contents of the current hash table into a new
        table by growing or shrinking the table, depending on the multiple
        that is passed in.
        """
        old_table = self._table.copy()
        self._num_items = 0
        self._capacity = int(self._capacity * multiple)
        self._table = [None] * self._capacity
        for linked_list in old_table:
            if linked_list:
                for hash_table_item in linked_list:
                    self.put(hash_table_item.key, hash_table_item.value)

    def __getitem__(self, key):
        """"Return the item associated with the given key."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Insert the given value into the hash table. If there is
        already a value associated with the given key, then the
        value will be overwritten.
        """
        self.put(key, value)

    def __delitem__(self, key):
        """Delete an item in the hash table with the given key."""
        self.delete(key)

    def __contains__(self, key):
        """Return True if there is a value associated with the given key
        in the hash table.
        """
        return self.get(key) is not None

