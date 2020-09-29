"""This module contains my implementation of a hash table using
linear probing (open addressing) to handle key collisions.
"""


class Tombstone:
    """Class to act as a placeholder for a deleted item in a hash
    table that uses linear probing to handle collisions.
    """

    def __repr__(self):
        """Return a string representation of a Tombstone."""
        return "Tombstone"


class HashItem:
    """Class to represent a key-value pair in a hash table."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        """Return a string representation of a HashItem."""
        return "HashItem(%r, %r)" % (self.key, self.value)


class HashTable:
    """Class to represent a hash table."""

    def __init__(self, capacity=8, min_load_factor=0.25, max_load_factor=0.75):
        if capacity < 1:
            raise ValueError("Capacity must be greater than 1.")
        if min_load_factor <= 0 or min_load_factor > 1:
            raise ValueError(
                "Min load factor must be greater than 0 but less than or equal to 1."
            )
        if max_load_factor <= 0 or max_load_factor > 1:
            raise ValueError(
                "Max load factor must be greater than 0 but less than or equal to 1."
            )
        self._capacity = capacity
        self._min_load_factor = min_load_factor
        self._max_load_factor = max_load_factor
        self._num_items = 0
        self._table = [None] * self._capacity

    def get(self, key):
        """Return the item associated with the given key."""
        if key is not None:
            bucket_index = self._hash(key)
            item_index = self._find_item_index(key, bucket_index)
            if self._table[item_index] is not None:
                return self._table[item_index].value
        return None

    def put(self, key, value):
        """Insert the given value into the hash table. If there is
        already a value associated with the given key, then the
        value will be overwritten.
        """
        if key is None:
            raise KeyError("None is not a valid key.")
        bucket_index = self._hash(key)
        item_index = self._find_item_index(key, bucket_index)
        if self._table[item_index] is None:
            self._table[item_index] = HashItem(key, value)
            self._num_items += 1
            if self._should_double():
                self._resize_table(2)
        else:
            self._table[item_index].value = value

    def delete(self, key):
        """Delete an item in the hash table with the given key."""
        if key is None:
            raise KeyError("None is not a valid key")
        bucket_index = self._hash(key)
        item_index = self._find_item_index(key, bucket_index)
        if self._table[item_index] is None:
            raise KeyError("Key not in hash table.")
        self._table[item_index] = Tombstone()
        self._num_items -= 1
        if self._should_halve():
            self._resize_table(0.5)

    def _find_item_index(self, key, bucket_index):
        while True:
            item = self._table[bucket_index]
            if item is None or (isinstance(item, HashItem) and item.key == key):
                return bucket_index
            bucket_index = (bucket_index + 1) % self._capacity

    def exists(self, key):
        """Return True if there is a value associated with the given key 
        in the hash table.
        """
        return self.get(key) is not None

    def is_empty(self):
        """Returns True or False depending on whether the hash table is empty."""
        return self._num_items == 0

    def clear(self):
        """Clear all of the contents of the hash table."""
        self._table = [None] * self._capacity
        self._num_items = 0

    @property
    def num_items(self):
        """Returns the number of items currently in the hash table."""
        return self._num_items

    def keys(self):
        """Return a list of keys found in the hash table."""
        keys = [item.key for item in self._table if isinstance(item, HashItem)]
        return keys

    def values(self):
        """Return a list of values found in the hash table."""
        values = [item.value for item in self._table if isinstance(item, HashItem)]
        return values

    def items(self):
        """Return a list of tuples that contains the key-value
        pairs found in the hash table.
        """
        items = [
            (item.key, item.value) for item in self._table if isinstance(item, HashItem)
        ]
        return items

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

    def _hash(self, key):
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
        old_table = self._table[:]
        self._capacity = int(self._capacity * multiple)
        self._table = [None] * self._capacity
        self._num_items = 0
        for item in old_table:
            if item is not None and not isinstance(item, Tombstone):
                self.put(item.key, item.value)

