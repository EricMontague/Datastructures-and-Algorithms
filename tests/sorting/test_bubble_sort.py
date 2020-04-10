"""This module contains tests for my bubble sort implementation."""


import unittest
from sorting.bubble_sort import bubble_sort


class TestProduct:
    """Dummy class created to test the stability property of bubble sort."""

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __lt__(self, other):
        return self.quantity < other.quantity


class BubbleSortTestCase(unittest.TestCase):
    """Class to run tests on my bubble sort implementation."""

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
        """Test that when bubble sort is passed an empty list,
        that nothing happens."""
        bubble_sort(self.empty_list)
        self.assertEqual(self.empty_list, [])

    def test_sort_unsorted_list_of_integers(self):
        """Test that when bubble sort is passed an unsorted list
        of integers that the list is properly sorted.
        """
        bubble_sort(self.unsorted_list_of_integers)
        self.assertEqual([-7, -2, -1, 0, 1, 4, 10], self.unsorted_list_of_integers)

    def test_sort_sorted_list_of_integers(self):
        """Test that when bubble sort is passed a sorted list
        of integers that the list remains sorted.
        """
        bubble_sort(self.sorted_list_of_integers)
        self.assertEqual([0, 1, 2, 3, 4, 5], self.sorted_list_of_integers)

    def test_sort_is_stable(self):
        """Test that if two elements in a list have the same key,
        that their relative ordering is still preserved after the
        list is sorted.
        """
        bubble_sort(self.list_of_objects)

        # eggs should still come before milk in the list
        products = {}
        for index, obj in enumerate(self.list_of_objects):
            products[obj.name] = index
        self.assertTrue(products["eggs"] < products["milk"])

