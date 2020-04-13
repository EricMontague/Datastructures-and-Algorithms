"""This module contains tests for my insertion sort implementation."""


import unittest
from sorting.insertion_sort import insertion_sort
from tests.sorting.stable import TestProduct


class InsertionSortTestCase(unittest.TestCase):
    """Class to run tests on my insertion sort implementation."""

    def setUp(self):
        """Create fixtures."""
        self.empty_list = []
        self.sorted_list_of_integers = [-7, -2, -1, 0, 1, 4, 10]
        self.unsorted_list_of_integers = [4, -7, 1, 10, 0, -1, -2]
        self.unsorted_list_of_products = [
            TestProduct("bread", 2),
            TestProduct("eggs", 10),
            TestProduct("milk", 10),
            TestProduct("cereal", 3),
            TestProduct("apples", 0),
            TestProduct("cheese", 1),
        ]
        self.sorted_list_of_products_stable = [
            TestProduct("apples", 0),
            TestProduct("cheese", 1),
            TestProduct("bread", 2),
            TestProduct("cereal", 3),
            TestProduct("eggs", 10),
            TestProduct("milk", 10),
        ]
        self.sorted_list_of_products_unstable = [
            TestProduct("apples", 0),
            TestProduct("cheese", 1),
            TestProduct("bread", 2),
            TestProduct("cereal", 3),
            TestProduct("milk", 10),
            TestProduct("eggs", 10),
        ]

    def tearDown(self):
        """Delete fixtures."""
        del self.empty_list
        del self.sorted_list_of_integers
        del self.unsorted_list_of_integers
        del self.unsorted_list_of_products
        del self.sorted_list_of_products_stable
        del self.sorted_list_of_products_unstable

    def test_sort_empty_list(self):
        """Test that when insertion sort is passed an empty list,
        that nothing happens."""
        insertion_sort(self.empty_list)
        self.assertEqual(self.empty_list, [])

    def test_sort_unsorted_list_of_integers(self):
        """Test that when insertion sort is passed an unsorted list
        of integers that the list is properly sorted.
        """
        insertion_sort(self.unsorted_list_of_integers)
        self.assertEqual(self.unsorted_list_of_integers, self.sorted_list_of_integers)

    def test_sort_sorted_list_of_integers(self):
        """Test that when insertion sort is passed a sorted list
        of integers that the list remains sorted.
        """
        insertion_sort(self.sorted_list_of_integers)
        self.assertEqual(self.sorted_list_of_integers, [-7, -2, -1, 0, 1, 4, 10])

    def test_insertion_sort_is_stable(self):
        """Test that if two elements in a list have the same key,
        that their relative ordering is still preserved after the
        list is sorted.
        """
        insertion_sort(self.unsorted_list_of_products)
        self.assertEqual(
            self.unsorted_list_of_products,self.sorted_list_of_products_stable
        )


if __name__ == "__main__":
    unittest.main()

