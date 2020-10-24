"""This module contains my implementation of a Bloom Filter."""



class BloomFilter:
    """Class to represent a bloom filter."""

    def __init__(self, size=997):
        self._bloom_filter = [0] * size
        self._size = size


    def exists(self, element):
        """Return True is the given element exists within the bloom filter,
        otherwise return False. Note that a return value of True may be 
        a false positive due to hash collisions, but a return value of False
        means the element is definitely not in the bloom filter.
        """
        index1 = self._hash_function1(element)
        index2 = self._hash_function2(element)
        index3 = self._hash_function3(element)
        return (
            self._bloom_filter[index1] == 1
            and self._bloom_filter[index2] == 1
            and self._bloom_filter[index3] == 1
        )
        

    def insert(self, element):
        """Insert the given element into the bloom filter."""
        index1 = self._hash_function1(element)
        index2 = self._hash_function2(element)
        index3 = self._hash_function3(element)
        self._bloom_filter[index1] = 1
        self._bloom_filter[index2] = 1
        self._bloom_filter[index3] = 1

    def reset(self):
        """Clear the bloom filter and reset the bit array to contain all 0's."""
        self._bloom_filter = [0] * self._size


    def _hash_function1(self, element):
        pass

    def _hash_function2(self, element):
        pass

    def _hash_function3(self, element):
        pass

