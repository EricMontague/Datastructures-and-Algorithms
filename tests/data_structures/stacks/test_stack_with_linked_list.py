"""This module contains the test case for my implementation of a stack
using a singly linked list.
"""


import unittest
from data_structures.stacks.stack_using_linked_list import Stack


class StackTestCase(unittest.TestCase):
    """Class to run tests on a stack implementation 
    based on a singly linked list.
    """

    def setUp(self):
        """Create stack fixtures."""
        self.empty_stack = Stack()
        self.non_empty_stack = Stack()
        for num in range(5):
            self.non_empty_stack.push(num)

    def tearDown(self):
        """Cleanup fixtures."""
        del self.empty_stack
        del self.non_empty_stack

    def test_push_onto_empty_stack(self):
        """Test the push method on an empty stack."""

        # first round of operations
        self.assertEqual(self.empty_stack.size, 0)
        self.empty_stack.push(10)
        self.assertEqual(self.empty_stack.size, 1)
        self.assertEqual(self.empty_stack.peek(), 10)

        # second round
        self.empty_stack.push(18)
        self.assertEqual(self.empty_stack.size, 2)
        self.assertEqual(self.empty_stack.peek(), 18)

    def test_push_onto_non_empty_stack(self):
        """Test the push method on a non-empty stack."""

        # first round of operations
        self.assertEqual(self.non_empty_stack.size, 5)
        self.non_empty_stack.push(10)
        self.assertEqual(self.non_empty_stack.size, 6)
        self.assertEqual(self.non_empty_stack.peek(), 10)

        # second round
        self.non_empty_stack.push(18)
        self.assertEqual(self.non_empty_stack.size, 7)
        self.assertEqual(self.non_empty_stack.peek(), 18)

    def test_pop_from_empty_stack_raises_error(self):
        """Test the calling the pop method on an empty stack
        raises an error.
        """
        with self.assertRaises(IndexError):
            self.empty_stack.pop()

    def test_pop_from_non_empty_stack_succeeds(self):
        """Test that calling the pop method on a non-empty
        stack successfully removes the item that is on top
        of the stack.
        """
        # confirm size
        self.assertEqual(self.non_empty_stack.size, 5)

        # first pop and reconfirm size
        self.assertEqual(self.non_empty_stack.pop(), 4)
        self.assertEqual(self.non_empty_stack.size, 4)

        # second pop and reconfirm size
        self.assertEqual(self.non_empty_stack.pop(), 3)
        self.assertEqual(self.non_empty_stack.size, 3)

    def test_is_empty_on_empty_stack(self):
        """Test that the is_empty() method returns True when called
        on an empty stack.
        """
        self.assertTrue(self.empty_stack.is_empty())

    def test_is_empty_on_non_empty_stack(self):
        """Test that the is_empty() method returns False
        when called on a non-empty stack."""
        self.assertFalse(self.non_empty_stack.is_empty())

    def test_peek_on_empty_stack(self):
        """Test that the peek method returns None when called
        on an empty stack.
        """
        self.assertIsNone(self.empty_stack.peek())

    def test_peek_on_non_empty_stack(self):
        """Test that the peek method returns the item on top
        of a non-empty stack.
        """
        self.assertEqual(self.non_empty_stack.peek(), 4)

