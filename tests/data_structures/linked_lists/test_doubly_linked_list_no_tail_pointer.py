"""This module contains tests for the doubly linked list implementation 
without a tail pointer.
"""


import unittest
from data_structures.linked_lists.doubly_linked_list_no_tail_pointer import DoublyLinkedList


class DoublyLinkedListTestCase(unittest.TestCase):
    """Class for running tests on the doubly linked list implementation 
    without a tail pointer.
    """

    def setUp(self):
        """Create different linked list fixtures."""
        self.empty_list = DoublyLinkedList()
        self.non_empty_list = DoublyLinkedList()
        #6 should be the head of the list
        for data in range(7):
            self.non_empty_list.push_front(data)

    def tearDown(self):
        """Delete linked list fixtures."""
        del self.empty_list
        del self.non_empty_list

    def test_peek_front_empty_list(self):
        """Test that the peek front method returns None when the
        linked list is empty.
        """
        self.assertIsNone(self.empty_list.peek_front())

    def test_peek_front_non_empty_list(self):
        """Test that the peek front method returns the data of the
        head node when the list isn't empty.
        """
        self.assertEqual(6, self.non_empty_list.head.data)
        self.assertEqual(
            self.non_empty_list.head.data, self.non_empty_list.peek_front()
        )

    def test_peek_back_empty_list(self):
        """Test that the peek back method returns None when the
        linked list is empty.
        """
        self.assertIsNone(self.empty_list.peek_back())

    def test_peek_back_non_empty_list(self):
        """Test that the peek back method returns the data of the
        last node when the list isn't empty.
        """
        self.assertEqual(0, self.non_empty_list.peek_back())

    def test_push_front(self):
        """Test that the push front method makes a node the head
        node of the list.
        """
        new_data = 19

        #test empty list
        self.assertIsNone(self.empty_list.head)
        self.assertEqual(0, self.empty_list.size)
        self.empty_list.push_front(new_data)
        self.assertIsNotNone(self.empty_list.head)
        self.assertEqual(1, self.empty_list.size)
        self.assertEqual(new_data, self.empty_list.head.data)
        self.assertIsNone(self.empty_list.head.next)
        
        #test non-empty list
        self.assertEqual(7, self.non_empty_list.size)
        self.non_empty_list.push_front(new_data)
        self.assertEqual(new_data, self.non_empty_list.head.data)
        self.assertEqual(8, self.non_empty_list.size)

    def test_pop_front_on_empty_list_raises_error(self):
        """Test that an IndexError is raised when the pop front
        method is called on an empty list.
        """
        with self.assertRaises(IndexError):
            self.empty_list.pop_front()

    def test_pop_front_on_non_empty_list(self):
        """Test that the head node is returned when
        pop front is called on a non-empty list.
        """
        #test first pop
        self.assertEqual(7, self.non_empty_list.size)
        self.assertEqual(6, self.non_empty_list.head.data)
        self.assertEqual(6, self.non_empty_list.pop_front())

        #test another pop 
        self.assertEqual(6, self.non_empty_list.size)
        self.assertEqual(5, self.non_empty_list.head.data)
        self.assertEqual(5, self.non_empty_list.pop_front())
        self.assertEqual(5, self.non_empty_list.size)

    def test_pop_front_on_list_with_one_node(self):
        """Test that a linked list is empty after the
        last node is removed using a pop front operation.
        """
        #insert data
        new_data = 1
        self.empty_list.push_front(new_data)
        self.assertEqual(1, self.empty_list.size)
        self.assertIsNotNone(self.empty_list.head)

        #remove node
        self.assertEqual(new_data, self.empty_list.pop_front())
        self.assertIsNone(self.empty_list.head)
        self.assertEqual(0, self.empty_list.size)
        



if __name__ == "__main__":
    unittest.main()
