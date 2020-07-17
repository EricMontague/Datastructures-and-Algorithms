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

    def __repr__(self):
        """Return a string representation of a HashItem."""
        return "HashItem(%r, %r)" %(self.key, self.value)


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
        if key is not None:
            bucket_index = self._hash(key)
            print(f"Index of {key} should be {bucket_index}")
            head = self._table[bucket_index]
            value = self._find_item(key, head)
            print(f"Returned value from the get method is: {value}")
            return value

    def _find_item(self, key, head):
        """Traverse the linked list of HashItems and return the value of the item
        with the given key.
        """
        while head:
            print(f"Head is {head}")
            if head.key == key:
                print(f"Key match the value {head.value}")
                return head.value
            head = head.next
        print("Returned None")
        return None

    def put(self, key, value):
        """Insert the given value into the hash table. If there is
        already a value associated with the given key, then the
        value will be overwritten.
        """
        # check whether key exists in hash table already
        existing_value = self.get(key)
        bucket_index = self._hash(key)
        head = self._table[bucket_index]
        if existing_value is not None:
            self._update_item(key, value, head)
        else:
            new_item = HashItem(key, value)
            self._insert_item(new_item, bucket_index, head)
            self._num_items += 1
            if self._should_double():
                self._resize_table(2)

    def _update_item(self, key, value, head):
        """Traverse the linked list of HashItems and update the item's value whose
        key matches the given key.
        """
        while head:
            if head.key == key:
                head.value = value
                break
            head = head.next

    def _insert_item(self, new_item, bucket_index, head):
        """Insert a new HashItem at the given index in the hash table."""
        if head is not None:
            new_item.next = head
        self._table[bucket_index] = new_item

    def delete(self, key):
        """Delete an item in the hash table with the given key."""
        bucket_index = self._hash(key)
        head = self._table[bucket_index]
        if head is None:
            raise KeyError("Key not in hash table.")
        self._delete_item(key, head, bucket_index)
        self._num_items -= 1
        if self._should_halve():
            self._resize_table(0.5)

    def _delete_item(self, key, item, bucket_index):
        """Delete the given item from its linked list in the hash table."""
        # Remove from head of linked list
        if item.key == key:
            self._table[bucket_index] = self._table[bucket_index].next
        else:  # Remove from middle or end
            target = item.next
            while True:
                if target is None:
                    raise KeyError("Key not in hash table.")
                if target.key == key:
                    item.next = target.next
                    break
                target = target.next
                item = item.next

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
        for item in self._table:
            while item:
                keys.append(item.key)
                item = item.next
        return keys

    def values(self):
        """Return a list of values found in the hash table."""
        values = []
        for item in self._table:
            while item:
                values.append(item.value)
                item = item.next
        return values

    def items(self):
        """Return a list of tuples that contains the key-value
        pairs found in the hash table.
        """
        pairs = []
        for item in self._table:
            while item:
                pairs.append((item.key, item.value))
                item = item.next
        return pairs

    def clear(self):
        """Clear all of the contents of the hash table."""
        self._table = [None] * self._capacity
        self._num_items = 0

    @property
    def num_items(self):
        """Returns the number of items currently in the hash table."""
        return self._num_items

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
        old_table = self._table.copy()
        self._num_items = 0
        self._capacity = int(self._capacity * multiple)
        self._table = [None] * self._capacity
        for item in old_table:
            while item:
                self.put(item.key, item.value)
                item = item.next

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

