import unittest
from search.binary_search.binary_search import (
    binary_search_iterative,
    binary_search_recursive,
)


class BinarySearchIterativeTestCase(unittest.TestCase):
    """Class to test the iterative implementation of 
    binary search.
    """
    def test_target_not_in_list(self):
        """Test to ensure that the algorithm
        returns -1 when the target number is not
        in the list.
        """
        target = 12
        input_list = [1, 2, 3, 4, 5]
        index = binary_search_iterative(input_list, target)
        self.assertEqual(index, -1)

        target = -12
        index = binary_search_iterative(input_list, target)
        self.assertEqual(index, -1)

    def test_target_in_list(self):
        """Test to ensure that the correct
        index is returned when the target number is
        in the list.
        """
        target = 3
        input_list = [1, 2, 3, 4, 5]
        index = binary_search_iterative(input_list, target)
        self.assertEqual(index, 2)

        target = -2
        input_list = [-5, -4, -3, -2, -1]
        index = binary_search_iterative(input_list, target)
        self.assertEqual(index, 3)

    def test_multiple_occurrences(self):
        """Test to ensure that the algorithm
        returns the correct index even if there are 
        multiple occurrences of that number in the list.
        """
        target = 3
        input_list = [1, 2, 3, 3, 3, 4, 5]
        index = binary_search_iterative(input_list, target)
        self.assertEqual(index, 3)

        input_list = [3, 3, 3, 3]
        index = binary_search_iterative(input_list, target)
        self.assertEqual(index, 1)

        target = -2
        input_list = [-5, -4, -3, -2, -2, -1]
        index = binary_search_iterative(input_list, target)
        self.assertEqual(index, 4)


class BinarySearchRecursiveTestCase(unittest.TestCase):
    """Class to test the recursive implementation of
    binary search.
    """
    def test_target_not_in_list(self):
        """Test to ensure that the algorithm
        returns -1 when the target number is not
        in the list.
        """
        target = 12
        input_list = [1, 2, 3, 4, 5]
        low = 0
        high = len(input_list) - 1

        index = binary_search_recursive(input_list, target, low, high)
        self.assertEqual(index, -1)

        target = -12
        index = binary_search_recursive(input_list, target, low, high)
        self.assertEqual(index, -1)

    def test_target_in_list(self):
        """Test to ensure that the correct
        index is returned when the target number is
        in the list.
        """
        target = 3
        input_list = [1, 2, 3, 4, 5]
        low = 0
        high = len(input_list) - 1
        index = binary_search_recursive(input_list, target, low, high)
        self.assertEqual(index, 2)

        target = -2
        input_list = [-5, -4, -3, -2, -1]
        index = binary_search_recursive(input_list, target, low, high)
        self.assertEqual(index, 3)

    def test_multiple_occurrences(self):
        """Test to ensure that the algorithm
        returns the correct index of a number
        even if there are multiple occurrences
        of that number in the list.
        """
        target = 3
        input_list = [1, 2, 3, 3, 3, 4, 5]
        low = 0
        high = len(input_list) - 1
        index = binary_search_recursive(input_list, target, low, high)
        self.assertEqual(index, 3)

        input_list = [3, 3, 3, 3]
        high = len(input_list) - 1
        index = binary_search_recursive(input_list, target, low, high)
        self.assertEqual(index, 1)

        target = -2
        input_list = [-5, -4, -3, -2, -2, -1]
        high = len(input_list) - 1
        index = binary_search_recursive(input_list, target, low, high)
        self.assertEqual(index, 4)

