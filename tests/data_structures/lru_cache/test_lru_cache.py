"""This module contains tests for the LRU Cache implementation."""
import unittest
from data_structures.lru_cache.lru_cache import CacheItem, LRUCache


class LRUCacheTestCase(unittest.TestCase):
    """Class to run tests on the LRU Cache implementation."""

    def test_invalid_max_capacity(self):
        """Test to ensure the LRU Cache can't be instantiated
        with a max capacity less than 1.
        """
        with self.assertRaises(ValueError):
            cache = LRUCache(-10)

        with self.assertRaises(ValueError):
            cache = LRUCache(0)

    def test_cache_hit(self):
        """Test that when a requested item is in the cache,
        it is returned.
        """
        cache = LRUCache(3)
        cache.put(1, "computation")
        item = cache.get(1)
        self.assertEqual(item.key, 1)
        self.assertEqual(item.value, "computation")

    def test_cache_miss(self):
        """Test that when a requested item is not in the
        cache, that the cache returns None.
        """
        cache = LRUCache(3)
        item = cache.get(1)
        self.assertIsNone(item)

    def test_updating_item(self):
        """Test to ensure that when an item is already in the
        cache and the put operation is called, its value
        is updated.
        """
        cache = LRUCache(3)
        cache.put(1, "compuation one")
        cache.put(2, "computation two")
        cache.put(3, "computation three")

        cache.put(3, "New computation")

        item = cache.get(3)
        self.assertEqual(item.key, 3)
        self.assertEqual(item.value, "New computation")

    def test_eviction_policy(self):
        """Test that when the cache gets full, that the
        last item is evicted.
        """
        cache = LRUCache(3)
        cache.put(1, "compuation one")
        cache.put(2, "computation two")
        cache.put(3, "computation three")

        #this should cause the first item to be kicked out
        cache.put(4, "computation four")

        #cache should look like this now: 4, 3, 2
        item = cache.get(1)
        self.assertIsNone(item)

        #this should move two to the top
        #cache should look like this: 2, 4, 3
        cache.get(2)

        #item 3 should get evicted
        cache.put(5, "computation five")
        item = cache.get(3)
        self.assertIsNone(item)


if __name__ == "__main__":
    unittest.main()
    