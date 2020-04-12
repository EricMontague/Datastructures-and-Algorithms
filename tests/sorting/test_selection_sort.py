"""This module contains tests for my implementation of selection sort."""


import unittest
from sorting.selection_sort import selection_sort
from tests.sorting.stable import TestProduct


class SelectionSortTestCase(unittest.TestCase):
    """Class to run tests on my selection sort implementation."""

    def setUp(self):
        """Create fixtures."""
        self.empty_list = []
        self.sorted_list_of_integers = [0, 1, 2, 3, 4, 5]
        self.unsorted_list_of_integers = [4, -7, 1, 10, 0, -1, -2]
        self.list_of_objects = [
            TestProduct("bread", 2),
            TestProduct("eggs", 10),
            TestProduct("milk", 10),
            TestProduct("cereal", 3),
            TestProduct("apples", 0),
            TestProduct("cheese", 1),
        ]

    def tearDown(self):
        """Delete fixtures."""
        del self.empty_list
        del self.sorted_list_of_integers
        del self.unsorted_list_of_integers
        del self.list_of_objects

    def test_sort_empty_list(self):
        """Test that when selection sort is passed an empty list,
        that nothing happens."""
        selection_sort(self.empty_list)
        self.assertEqual(self.empty_list, [])

    def test_sort_unsorted_list_of_integers(self):
        """Test that when selection sort is passed an unsorted list
        of integers that the list is properly sorted.
        """
        selection_sort(self.unsorted_list_of_integers)
        self.assertEqual([-7, -2, -1, 0, 1, 4, 10], self.unsorted_list_of_integers)

    def test_sort_sorted_list_of_integers(self):
        """Test that when selection sort is passed a sorted list
        of integers that the list remains sorted.
        """
        selection_sort(self.sorted_list_of_integers)
        self.assertEqual([0, 1, 2, 3, 4, 5], self.sorted_list_of_integers)

    def test_selection_sort_is_stable_must_fail(self):
        """Test that if two elements in a list have the same key,
        that their relative ordering is not preserved after the
        list is sorted. Selection sort is not a stable sorting algorithm.
        """
        selection_sort(self.list_of_objects)

        # eggs should not come before milk in the list
        products = {}
        for index, obj in enumerate(self.list_of_objects):
            products[obj.name] = index
        self.assertTrue(products["eggs"] > products["milk"])


if __name__ == "__main__":
    unittest.main()
