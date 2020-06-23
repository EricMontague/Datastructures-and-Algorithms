"""This module contains my implementation of a circular queue."""


import unittest
from data_structures.queues.circular_queue import CircularQueue


class CircularQueueTestCase(unittest.TestCase):
    """Class to run tests on my circular queue implementation."""

    def setUp(self):
        """Create fixtures."""
        self.full_queue = CircularQueue(5)
        for num in range(5):
            self.full_queue.enqueue(num)
        self.empty_queue = CircularQueue(5)

    def tearDown(self):
        """Delete fixtures."""
        del self.full_queue
        del self.empty_queue

    def test_max_capacity_less_than_one_must_raise_error(self):
        """Test that if the queue is instantiated with a max capacity that is
        less than one, that an error is raised.
        """
        with self.assertRaises(ValueError):
            queue = CircularQueue(0)

        with self.assertRaises(ValueError):
            queue = CircularQueue(-1)

    def test_insert_into_full_queue_raises_error(self):
        """Test that if the queue is full and an insertion is made,
        that an error is raised.
        """
        with self.assertRaises(ValueError):
            self.full_queue.enqueue(9)

    def test_insert_into_non_full_queue_succeeds(self):
        """Test that if the queue is not full and an insertion is made,
        that the operation happens successfully.
        """
        self.assertEqual(self.empty_queue.size, 0)
        self.empty_queue.enqueue(5)
        self.assertEqual(self.empty_queue.size, 1)
        self.assertEqual(self.empty_queue.peek(), 5)

    def test_remove_from_empty_queue(self):
        """Test that if an attempt to remove an item from an empty
        queue is made, that None is returned.
        """
        self.assertEqual(self.empty_queue.size, 0)
        self.assertIsNone(self.empty_queue.dequeue())

    def test_remove_from_non_empty_queue(self):
        """Test that is an attempt to remove from a non-empty queue
        is made, that a value is returned.
        """
        # 0 is at the front of the queue
        self.assertEqual(self.full_queue.size, 5)
        self.assertEqual(self.full_queue.dequeue(), 0)
        self.assertEqual(self.full_queue.size, 4)

        # 1 is at the front of the queue
        self.assertEqual(self.full_queue.dequeue(), 1)
        self.assertEqual(self.full_queue.size, 3)

    def test_queue_is_full_method(self):
        """Test that the is_full() method behaves correctly
        when called on a queue that is not full and on a full queue.
        """
        self.assertTrue(self.full_queue.is_full())
        self.assertFalse(self.empty_queue.is_full())

    def test_queue_is_empty_method(self):
        """Test that the is_empty() method behaves correctly when called
        on an empty queue an a non-empty queue.
        """
        self.assertTrue(self.empty_queue.is_empty())
        self.assertFalse(self.full_queue.is_empty())

    def test_peek_on_empty_queue(self):
        """Test that the peek method returns None when called on
        an empty queue.
        """
        self.assertIsNone(self.empty_queue.peek())

    def test_peek_on_non_empty_queue(self):
        """Test that the peek method returns a value when called on
        a non-empty queue.
        """
        # 0 is the first number in the queue
        self.assertEqual(self.full_queue.size, 5)
        self.assertEqual(self.full_queue.peek(), 0)

    def test_get_size(self):
        """Test that the size property returns the correct
        number of items in the queue.
        """
        self.assertEqual(self.empty_queue.size, 0)
        self.assertEqual(self.full_queue.size, 5)

    
if __name__ == "__main__":
    unittest.main()

