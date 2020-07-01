"""This module contains tests for my Max Heap implementation."""


import unittest
from data_structures.heaps.binary_max_heap import BinaryMaxHeap


class BinaryMaxHeapTestCase(unittest.TestCase):
    """Class to test my implementation of a Binary Max Heap."""

    def setUp(self):
        """Create fixtures."""
        self.empty_heap = BinaryMaxHeap()
        input_list = [4, 34, 1, 2, 0, 20, 25, 14]
        self.non_empty_heap = BinaryMaxHeap()
        self.non_empty_heap.heapify(input_list)

    def tearDown(self):
        """Delete fixtures."""
        del self.empty_heap
        del self.non_empty_heap

    def test_get_max(self):
        """Test that the get_max() method returns the appropriate value
        when called on empty and non-empty heaps.
        """
        self.assertIsNone(self.empty_heap.get_max())
        self.assertEqual(self.non_empty_heap.get_max(), 34)

    def test_extract_max_on_empty_heap(self):
        """Test that calling extract_max() on an empty heap returns None."""
        self.assertIsNone(self.empty_heap.extract_max())

    def test_extract_max_on_heap_with_one_element(self):
        """Test that calling extract_max() on a heap with only one element
        returns the correct value.
        """
        # Create heap
        max_heap = BinaryMaxHeap()
        max_heap.heapify([22])

        # Confirm that heap was created successfully
        self.assertEqual(max_heap.size, 1)
        self.assertEqual(max_heap.get_max(), 22)

        # extract max value
        self.assertEqual(max_heap.extract_max(), 22)
        self.assertEqual(max_heap.size, 0)
        self.assertIsNone(max_heap.get_max())
        self.assertTrue(max_heap.is_empty())

    def test_extract_max_on_heap_with_more_than_one_element(self):
        """Test that calling extract_max() on a heap with more than one element
        returns the correct value.
        """
        # Confirm heap size and max value
        self.assertEqual(self.non_empty_heap.size, 8)
        self.assertEqual(self.non_empty_heap.get_max(), 34)

        # Removal 1
        self.assertEqual(self.non_empty_heap.extract_max(), 34)
        self.assertEqual(self.non_empty_heap.size, 7)
        self.assertEqual(self.non_empty_heap.get_max(), 25)

        # Removal 2
        self.assertEqual(self.non_empty_heap.extract_max(), 25)
        self.assertEqual(self.non_empty_heap.size, 6)
        self.assertEqual(self.non_empty_heap.get_max(), 20)

    def test_insert_into_max_heap(self):
        """Test the insertion method of the heap."""
        # Confirm heap size and max value
        self.assertEqual(self.non_empty_heap.size, 8)
        self.assertEqual(self.non_empty_heap.get_max(), 34)

        # Insert new max element
        self.non_empty_heap.insert(500)
        self.assertEqual(self.non_empty_heap.size, 9)
        self.assertEqual(self.non_empty_heap.get_max(), 500)

        # insert another element
        self.non_empty_heap.insert(3)
        self.assertEqual(self.non_empty_heap.size, 10)
        self.assertEqual(self.non_empty_heap.get_max(), 500)

        # Insert a new max element
        self.non_empty_heap.insert(501)
        self.assertEqual(self.non_empty_heap.size, 11)
        self.assertEqual(self.non_empty_heap.get_max(), 501)

    def test_heapify(self):
        """Test that the heapify() method correctly turns a list of
        elements in a max heap.
        """
        # Possible depiction
        #       18
        #     9     7
        #   5   3  1
        elements = [5, 7, 18, 9, 1, 3]
        self.non_empty_heap.heapify(elements)
        self.assertEqual(self.non_empty_heap.size, 6)
        self.assertEqual(self.non_empty_heap.get_max(), 18)

        # Perform extract_max() until the heap is empty
        # If heapify worked properly, then this new list
        # should be sorted in reverse order
        reversed_list = []
        while not self.non_empty_heap.is_empty():
            element = self.non_empty_heap.extract_max()
            reversed_list.append(element)
        self.assertEqual(reversed_list, [18, 9, 7, 5, 3, 1])

    def test_remove_at_method_on_empty_heap_raises_error(self):
        """Test that calling the remove_at() method on an empty
        heap raises an error.
        """
        with self.assertRaises(IndexError):
            self.empty_heap.remove_at(1)

    def test_remove_at_method_index_out_of_range_raises_error(self):
        """Test that calling the remove_at() method with an index
        that is out of range raises and error.
        """
        with self.assertRaises(IndexError):
            self.non_empty_heap.remove_at(-1)

        # my implementation is 1-based so this should throw an error
        with self.assertRaises(IndexError):
            self.non_empty_heap.remove_at(0)

        with self.assertRaises(IndexError):
            self.non_empty_heap.remove_at(10)

    def test_remove_at_method_on_heap_with_one_element(self):
        """Test that the remove_at() method returns the correct
        value when called on a heap with only one element.
        """
        # Create heap
        max_heap = BinaryMaxHeap()
        max_heap.heapify([22])

        # Confirm that heap was created successfully
        self.assertEqual(max_heap.size, 1)
        self.assertEqual(max_heap.get_max(), 22)

        # Remove element
        max_heap.remove_at(1)
        self.assertEqual(max_heap.size, 0)
        self.assertIsNone(max_heap.get_max())
        self.assertTrue(max_heap.is_empty())

    def test_remove_at_method_on_heap_with_more_than_one_element(self):
        """Test that the remove_at() method returns the correct
        value when the index is in range and the heap has more than
        one element.
        """
        self.assertEqual(self.non_empty_heap.size, 8)

        # Removal 1
        self.non_empty_heap.remove_at(4)
        self.assertEqual(self.non_empty_heap.size, 7)

        # Removal 2
        self.non_empty_heap.remove_at(2)
        self.assertEqual(self.non_empty_heap.size, 6)

        # Removal 3
        self.non_empty_heap.remove_at(1)
        self.assertEqual(self.non_empty_heap.size, 5)

    def test_is_empty(self):
        """Test that the is_empty() method returns the appropriate value
        when called on empty and non-empty heaps.
        """
        self.assertTrue(self.empty_heap.is_empty())
        self.assertFalse(self.non_empty_heap.is_empty())

    def test_size_getter(self):
        """Test that the size property returns the appropriate value
        when called on empty and non-empty heaps.
        """
        self.assertEqual(self.empty_heap.size, 0)
        self.assertEqual(self.non_empty_heap.size, 8)


if __name__ == "__main__":
    unittest.main()
