"""This module contains tests for my circular deque implementation."""


import unittest
from data_structures.queues.circular_deque import CircularDeque


class CircularDequeTestCase(unittest.TestCase):
    """Class to run tests on the circular deque implementation."""

    def setUp(self):
        """Create fixtures."""
        self.full_deque = CircularDeque(5)
        for num in range(5):
            self.full_deque.push_back(num)
        self.empty_deque = CircularDeque(5)

    def tearDown(self):
        """Delete fixtures."""
        del self.full_deque
        del self.empty_deque

    def test_max_capacity_less_than_one_throws_error(self):
        """Test that if the circular deque is initialized
        with a max capacity of less than 1, that it throws
        and error.
        """
        with self.assertRaises(ValueError):
            deque = CircularDeque(0)

        with self.assertRaises(ValueError):
            deque = CircularDeque(-1)

    def test_peek_front_on_empty_deque(self):
        """Test that if peek_front() is called on an empty deque
        that it returns None.
        """
        self.assertEqual(self.empty_deque.size, 0)
        self.assertIsNone(self.empty_deque.peek_front())

    def test_peek_front_on_non_empty_deque(self):
        """Test that if peek_front() is called on a non empty deque
        that it returns the correct value.
        """
        self.assertEqual(self.full_deque.size, 5)
        self.assertEqual(self.full_deque.peek_front(), 0)

    def test_peek_back_on_empty_deque(self):
        """Test that if peek_back() is called on an empty deque
        that it returns None.
        """
        self.assertEqual(self.empty_deque.size, 0)
        self.assertIsNone(self.empty_deque.peek_back())

    def test_peek_back_on_non_empty_deque(self):
        """Test that if peek_back() is called on a non empty deque
        that it returns the correct value.
        """
        self.assertEqual(self.full_deque.size, 5)
        self.assertEqual(self.full_deque.peek_back(), 4)

    def test_deque_with_one_item(self):
        """Test that if a deque has only one item, that
        peek_front() and peek_back() return the
        same item.
        """
        self.assertEqual(self.full_deque.size, 5)
        # Remove all items except one
        for num in range(4):
            self.full_deque.pop_front()
        self.assertEqual(self.full_deque.size, 1)
        self.assertEqual(
            self.full_deque.peek_front(), 
            self.full_deque.peek_back()
        )

    def test_is_empty_method(self):
        """Test that is_empty() returns the correct value for
        both empty and non-empty deques.
        """
        self.assertTrue(self.empty_deque.is_empty())
        self.assertFalse(self.full_deque.is_empty())

    def test_is_full_method(self):
        """Test that is_full() returns the correct value for
        both empty and non-empty deques.
        """
        self.assertTrue(self.full_deque.is_full())
        self.assertFalse(self.empty_deque.is_full())

    def test_insert_into_full_deque_raises_error(self):
        """Test that calling push_front() or push_back() on a 
        full deque raises an error.
        """
        with self.assertRaises(ValueError):
            self.full_deque.push_front(6)

        with self.assertRaises(ValueError):
            self.full_deque.push_back(8)

    def test_push_front_on_non_full_deque(self):
        """Test that calling push_front() on a non-full
        deque is successful.
        """
        self.assertEqual(self.empty_deque.size, 0)
        self.empty_deque.push_front(10)
        self.assertEqual(self.empty_deque.size, 1)
        self.assertEqual(
            self.empty_deque.peek_front(), 
            self.empty_deque.peek_back()
        )
        self.assertEqual(self.empty_deque.peek_front(), 10)

        # add another number
        self.empty_deque.push_front(20)
        self.assertEqual(self.empty_deque.size, 2)
        self.assertEqual(self.empty_deque.peek_front(), 20)

    def test_push_back_on_non_full_deque(self):
        """Test that calling push_back() on a non-full
        deque is successful.
        """
        self.assertEqual(self.empty_deque.size, 0)
        self.empty_deque.push_back(10)
        self.assertEqual(self.empty_deque.size, 1)
        self.assertEqual(
            self.empty_deque.peek_front(), 
            self.empty_deque.peek_back()
        )
        self.assertEqual(self.empty_deque.peek_back(), 10)

        # add another number
        self.empty_deque.push_back(20)
        self.assertEqual(self.empty_deque.size, 2)
        self.assertEqual(self.empty_deque.peek_back(), 20)

    def test_remove_from_empty_deque(self):
        """Test that calling pop_front() or pop_back() on
        an empty deque returns None.
        """
        self.assertIsNone(self.empty_deque.pop_back())
        self.assertIsNone(self.empty_deque.pop_front())

    def test_pop_front_on_non_empty_deque(self):
        """Test that calling pop_front() on a non-empty
        deque returns the correct value.
        """
        self.assertEqual(self.full_deque.size, 5)
        self.assertEqual(self.full_deque.pop_front(), 0)
        self.assertEqual(self.full_deque.size, 4)
        self.assertEqual(self.full_deque.peek_front(), 1)

        # remove a second number
        self.assertEqual(self.full_deque.pop_front(), 1)
        self.assertEqual(self.full_deque.size, 3)
        self.assertEqual(self.full_deque.peek_front(), 2)

    def test_pop_back_on_non_empty_deque(self):
        """Test that calling pop_back() on a non-empty
        deque returns the correct value.
        """
        self.assertEqual(self.full_deque.size, 5)
        self.assertEqual(self.full_deque.pop_back(), 4)
        self.assertEqual(self.full_deque.size, 4)
        self.assertEqual(self.full_deque.peek_back(), 3)

        # remove a second number
        self.assertEqual(self.full_deque.pop_back(), 3)
        self.assertEqual(self.full_deque.size, 3)
        self.assertEqual(self.full_deque.peek_back(), 2)

    def test_get_size(self):
        """Test that the size property returns the correct
        value for different sized deques.
        """
        self.assertEqual(self.full_deque.size, 5)
        self.assertEqual(self.empty_deque.size, 0)


if __name__ == "__main__":
    unittest.main()
