"""This module contains an implementation of an LRU Cache."""

class CacheItem:
    """Class to represent an item in a cache."""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """Class to represent a LRU Cache."""

    def __init__(self, max_capacity):
        if max_capacity <= 0:
            raise ValueError("Max capacity must be greater than 0.")
        self.max_capacity = max_capacity
        self.items = {}
        self.total_items = 0

        #dummy pointers to avoid NoneType exception when removing nodes
        self.head = CacheItem(None, None)
        self.tail = CacheItem(None, None)

        #wire the head and the tail together
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """Given a key, return an item from the cache.
        Return None if the item is not in the cache.
        """
        #return none if the item isn't in the cache
        if key not in self.items:
            return None

        #retrieve the item from the dictionary
        item = self.items[key]

        #move it to the front of the list since it is the
        #most recently accessed item
        self._move_to_head(item)
        return item

    def put(self, key, value):
        """Given a key and a value, add an item to the cache.
        If the cache is full, the least recently used item
        will be evicted.
        """
        #first check if item in already in the cache
        item = self.items.get(key, None)

        #if not create a new item
        if item is None:
            #if the cache is full, evict the last item
            if self.is_full():
                self._evict()
            item = CacheItem(key, value)

            #add it to the dictionary
            self.items[key] = item

            #insert it at the front on the linked list
            self._push_front(item)

            #increment number of items by 1
            self.total_items += 1
        else:
            #update the value of the found item
            #move it to the front of the list since it is now
            #the most recently accessed item
            item.value = value
            self._move_to_head(item)

    def _push_front(self, item):
        """Insert the given item to the front of the linked list."""
        #point the item's previous pointer to head and its
        #next pointer to the item after the head
        item.prev = self.head
        item.next = self.head.next

        #the item is still not fully in the linked list yet
        #point the item after the head's previous pointer to
        #the new item and point the head's next pointer to the item

        self.head.next.prev = item
        self.head.next = item

    def _pop_tail(self):
        """Remove the item that is at the end of the linked list."""
        #get item before the tail pointer
        previous_item = self.tail.prev

        #call to method to remove from linked list
        self._remove_from_list(previous_item)
        return previous_item

    def _move_to_head(self, item):
        """Remove the item from where it is in the list and 
        move it to the head of the list.
        """
        #call to method to remove item from the linked list
        self._remove_from_list(item)

        #insert item at the head of the list
        self._push_front(item)

    def _remove_from_list(self, item):
        """Remove the given item from the linked list."""
        #get previous an next items in the list
        previous_item = item.prev
        next_item = item.next

        #change their pointers to point towards one another
        previous_item.next = next_item
        next_item.prev = previous_item

    def _evict(self):
        """Remove the last item in the linked list and delete it from
        the self.items dictionary.
        """
        #call to method to remove the last item
        tail = self._pop_tail()

        #delete item from self.items dictionary
        self.items.pop(tail.key)

        #reduce number of items in the cache by 1
        self.total_items -= 1

    def is_full(self):
        """Return True if the cache has reached max capacity."""
        return self.total_items == self.max_capacity

