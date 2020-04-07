"""This module contains tests for the singly linked list implementation 
without a tail pointer.
"""


import unittest
from data_structures.linked_lists.singly_linked_list_no_tail_pointer import SinglyLinkedList


class SinglyLinkedListTestCase(unittest.TestCase):
    """Class for running tests on the singly linked list implementation 
    without a tail pointer.
    """

    def setUp(self):
        """Create different linked list fixtures."""
        self.empty_list = SinglyLinkedList()
        self.non_empty_list = SinglyLinkedList()
        #0 should be the head of the list
        for data in range(6, -1, -1):
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
        #fixture contains values from 0 to 6. The values of the linked list
        #nodes are in this same order.
        self.assertEqual(0, self.non_empty_list.head.data)
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
        #fixture contains values from 0 to 6. The values of the linked list
        #nodes are in this same order.
        self.assertEqual(6, self.non_empty_list.peek_back())

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
        #fixture contains values from 0 to 6. The values of the linked list
        #nodes are in this same order.
        #test first pop
        self.assertEqual(7, self.non_empty_list.size)
        self.assertEqual(0, self.non_empty_list.head.data)
        self.assertEqual(0, self.non_empty_list.pop_front())

        #test another pop 
        self.assertEqual(6, self.non_empty_list.size)
        self.assertEqual(1, self.non_empty_list.head.data)
        self.assertEqual(1, self.non_empty_list.pop_front())
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

    def test_push_back_on_empty_list(self):
        """Test that when the push back operation is performed
        on an empty list, that new node becomes the head node.
        """
        new_data = 1
        self.assertIsNone(self.empty_list.head)
        self.assertEqual(0, self.empty_list.size)
        self.empty_list.push_back(new_data)
        self.assertEqual(new_data, self.empty_list.head.data)
        self.assertEqual(1, self.empty_list.size)

    def test_push_back_on_non_empty_list(self):
        """Test that the push back operation adds a node
        at the tail of a non-empty linked list.
        """
        new_data = 1
        self.assertEqual(7, self.non_empty_list.size)
        self.non_empty_list.push_back(new_data)
        self.assertEqual(8, self.non_empty_list.size)
        self.assertEqual(new_data, self.non_empty_list.peek_back())

    def test_pop_back_on_empty_list_raises_error(self):
        """Test that when the pop back method is called
        on an empty list, an IndexError is raised.
        """
        with self.assertRaises(IndexError):
            self.empty_list.pop_back()

    def test_pop_back_on_list_with_one_node(self):
        """Test that when the pop back operation is performed
        on a list that contains one node, the list becomes empty.
        """
        new_data = 1
        self.assertIsNone(self.empty_list.head)
        self.assertEqual(0, self.empty_list.size)
        self.empty_list.push_back(new_data)
        self.assertEqual(1, self.empty_list.size)

        self.assertEqual(new_data, self.empty_list.pop_back())
        self.assertIsNone(self.empty_list.head)
        self.assertEqual(0, self.empty_list.size)

    def test_pop_back_on_non_empty_list(self):
        """Test that when the pop back method is called
        on a non-empty list, that the last node is returned.
        """
        self.assertEqual(7, self.non_empty_list.size)
        last_node_data = self.non_empty_list.peek_back()
        self.assertEqual(last_node_data, self.non_empty_list.pop_back())
        self.assertEqual(6, self.non_empty_list.size)
    
    def test_count_method_called_on_empty_list(self):
        """Test that when the count method is called on an empty
        list, that the returned value is 0.
        """
        data = 5
        self.assertIsNone(self.empty_list.head)
        self.assertEqual(0, self.empty_list.size)
        self.assertEqual(0, self.empty_list.count(data))

    def test_count_method_value_exists_in_non_empty_list(self):
        """Test that when the count method is called on a non-empty
        list that contains the value, its correct count is returned.
        """
        #fixture contains one occurrence of each number from 0 to 6
        data = 5
        self.assertEqual(1, self.non_empty_list.count(data))

        #insert a duplicate just for extra testing
        self.non_empty_list.push_front(data)
        self.assertEqual(data, self.non_empty_list.head.data)
        self.assertEqual(2, self.non_empty_list.count(data))

    def test_count_method_value_not_in_non_empty_list(self):
        """Test that when the count method is called on a non-empty
        list that doesn't contains the value, that 0 is returned.
        """
        #fixture contains one occurrence of each number from 0 to 6
        self.assertEqual(0, self.non_empty_list.count(124))
    
    def test_value_at_index_on_empty_list_raises_error(self):
        """Test that when the value at method is called on an empty
        list, that it raises an error regardless on what index is
        passed in.
        """
        with self.assertRaises(IndexError):
            self.empty_list.value_at(0)
        
        with self.assertRaises(IndexError):
            self.empty_list.value_at(2)

        with self.assertRaises(IndexError):
            self.empty_list.value_at(5)

        with self.assertRaises(IndexError):
            self.empty_list.value_at(8)

    def test_value_at_index_out_of_range_raises_error(self):
        """Test that when the value at method is called and the
        index passed in is out of range, that an IndexError
        is raised.
        """
        #fixture contains values from 0 to 6. The values of the linked list
        #nodes are in this same order.
        with self.assertRaises(IndexError):
            self.non_empty_list.value_at(7)
        
        with self.assertRaises(IndexError):
            self.non_empty_list.value_at(9)
        
        with self.assertRaises(IndexError):
            self.non_empty_list.value_at(12)

    def test_value_at_index_within_range(self):
        """Test that when the value at method is called and the index
        passed in is within range, the correct value is returned.
        """
        #fixture contains values from 0 to 6. The values of the linked list
        #nodes are in this same order.
        self.assertEqual(0, self.non_empty_list.value_at(0))
        self.assertEqual(3, self.non_empty_list.value_at(3))
        self.assertEqual(4, self.non_empty_list.value_at(4))

    def test_is_empty_on_empty_list(self):
        """Test that when the is empty method is called on an empty
        list, that it returns True.
        """
        self.assertTrue(self.empty_list.is_empty())

    def test_is_empty_on_non_empty_list(self):
        """Test that when the is empty method is called on a non-empty
        list, that it returns False.
        """
        self.assertFalse(self.non_empty_list.is_empty())




if __name__ == "__main__":
    unittest.main()
