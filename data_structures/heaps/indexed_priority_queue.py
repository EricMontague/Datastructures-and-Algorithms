"""This module contains an implementation of an indexed priority queue
based on a binary min heap. The list in the binary min heap
for this implementation is 1-based.
"""



class PriorityQueueItem:
    """Class to represent an item in a priority queue."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        if self.key == other.key:
            return self.value < other.value
        return self.key < other.key


class IndexedPriorityQueue:
    """Class to represent an indexed priority queue based on a binary min heap. Assumes unique values."""

    def __init__(self, items=[]):
        # expects a list of tuples where the first value is the key and the second is the value
        # of a priority queue item
        self._positions = {}
        self._min_heap = [None]
        self._heapify(items)

    def _heapify(self, items):
        """Given a list, of items, change said list into a min heap."""
        for index, item in enumerate(items):
            key = item[0]
            value = item[1]
            self._min_heap.append(PriorityQueueItem(key, value))
            self._positions[value] = index + 1 # 1-base heap
        length = len(self._min_heap)
        for index in range(length // 2, 0, -1):
            item = self._min_heap[index]
            new_index = self._sift_down(index)
            self._positions[item.value] = new_index

    def _sift_down(self, parent_index):
        """Move the item located at the given index upwards in the min heap until
        it sits at its correct location, fixing the min heap invariant.
        """
        left_child_index = self._get_left_child(parent_index)
        right_child_index = self._get_right_child(parent_index)

        # Figure out if this is a leaf node
        if left_child_index >= len(self._min_heap):
            return parent_index

        # Find smallest child
        minimum_child_index = left_child_index
        if (
            right_child_index < len(self._min_heap)
            and self._min_heap[right_child_index] < self._min_heap[left_child_index]
        ):
            minimum_child_index = right_child_index

        # Compare parent and smallest child
        if self._min_heap[parent_index] > self._min_heap[minimum_child_index]:
            self._swap_items(parent_index, minimum_child_index)
            return self._sift_down(minimum_child_index)
        return parent_index

    def _get_left_child(self, parent_index):
        """Given the index of a parent node in the min heap, return the 
        index of its left child node.
        """
        return 2 * parent_index

    def _get_right_child(self, parent_index):
        """Given the index of a parent node in the min heap, return the 
        index of its right child node.
        """
        return 2 * parent_index + 1

    def _swap_items(self, index1, index2):
        """Swap the position of the items located at both indices in the
        min heap.
        """
        temp = self._min_heap[index1]
        self._min_heap[index1] = self._min_heap[index2]
        self._min_heap[index2] = temp

    def peek(self):
        """Return the item with the lowest key."""
        if self.is_empty():
            return None
        return self._min_heap[1].value

    def is_empty(self):
        """Return True if the priority queue is empty, false otherwise."""
        return len(self._min_heap) == 1 and self._min_heap[0] is None

    def extract_min(self):
        """Remove the item in the priority queue with the lowest key
        and return that item.
        """
        if self.is_empty():
            return None
        min_item = self._min_heap[1]
        last_item = self._min_heap.pop()
        if not self.is_empty():
            self._min_heap[1] = last_item
            new_index = self._sift_down(1)
            self._positions[last_item.value] = new_index
        self._positions.pop(min_item.value)
        return min_item

    def insert(self, key, value):
        """Insert a item with the given key and value into the priority queue."""
        item = PriorityQueueItem(key, value)
        self._min_heap.append(item)
        new_index = self._sift_up(len(self._min_heap) - 1)
        self._positions[item.value] = new_index

    def _sift_up(self, child_index):
        """Move the child at the given index up in the min heap until the min heap
        invariant is corrected.
        """
        parent_index = self._get_parent(child_index)
        if (
            child_index == 1
            or self._min_heap[parent_index] <= self._min_heap[child_index]
        ):
            return child_index
        self._swap_items(parent_index, child_index)
        return self._sift_up(parent_index)

    def _get_parent(self, child_index):
        """Given the index of a child node in the min heap, return the
        index of its parent.
        """
        return child_index // 2

    def change_key(self, value, new_key):
        """Increase of decrease the key of an item in teh priority queue."""
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        index = self._positions.get(value, -1)
        if index == -1:
            raise ValueError("Item not in priority queue.")
        item = self._min_heap[index]
        old_key = item.key
        item.key = new_key
        new_index = index
        if new_key > old_key:
            new_index = self._sift_down(index)
        elif new_key < old_key:
            new_index = self._sift_up(index)
        self._positions[value] = new_index

