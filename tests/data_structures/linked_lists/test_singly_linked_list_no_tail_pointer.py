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

    def test_reverse_on_empty_list(self):
        """Test that when the reverse method is called on an empty list,
        the head node is still None.
        """
        self.assertIsNone(self.empty_list.head)
        self.empty_list.reverse()
        self.assertIsNone(self.empty_list.head)

    def test_reverse_on_non_empty_list(self):
        """Test that when the reverse method is called on a non empty list,
        that the list is properly reversed.
        """
        #the head of the fixture is 0 and the tail is 6
        self.assertEqual(0, self.non_empty_list.head.data)
        self.assertEqual(6, self.non_empty_list.peek_back())

        #reverse list
        self.non_empty_list.reverse()

        #check that head and tail are flipped
        self.assertEqual(6, self.non_empty_list.head.data)
        self.assertEqual(0, self.non_empty_list.peek_back())

        #check that the list is completely reversed
        value = 6
        for node in self.non_empty_list:
            self.assertEqual(value, node)
            value -= 1
    
    def test_insert_at_index_out_of_range_raises_error(self):
        """Test that when the insert method is called with an
        index that is out of range for the list, that an IndexError
        is raised.
        """
        with self.assertRaises(IndexError):
            self.empty_list.insert(0, 234)

        #fixture list indices go from 0 to 6
        with self.assertRaises(IndexError):
            self.non_empty_list.insert(8, 67)

        #negative indicies aren't allowed
        with self.assertRaises(IndexError):
            self.non_empty_list.insert(-1, 67)

    def test_insert_at_head(self):
        """Test that the insert method inserts at the head
        of the list when an index of 0 is passed in.
        """
        data = 798
        #fixture list indices go from 0 to 6
        self.assertEqual(7, self.non_empty_list.size)
        
        #insert at the head
        index = 0
        self.assertEqual(0, self.non_empty_list.head.data)
        self.non_empty_list.insert(index, data)
        self.assertEqual(data, self.non_empty_list.head.data)
        self.assertEqual(8, self.non_empty_list.size)

    def test_insert_not_at_head(self):
        """Test that a new node is correctly inserted at the
        given index if it is not the head.
        """
        index = 5
        data = 798
        self.assertEqual(5, self.non_empty_list.value_at(index))
        self.non_empty_list.insert(index, data)
        self.assertEqual(8, self.non_empty_list.size)
        self.assertEqual(data, self.non_empty_list.value_at(index))

    def test_remove_at_index_on_empty_list(self):
        """Test that if the remove at index method is called on
        an empty list, that an index error is raised.
        """
        with self.assertRaises(IndexError):
            self.empty_list.remove_at_index(4)

    def test_remove_at_index_out_of_range(self):
        """Test that when the remove at index method is called
        with an index that is out of range, an IndexError is raised.
        """
        #fixture list indices go from 0 to 6
        with self.assertRaises(IndexError):
            self.empty_list.remove_at_index(8)
        
        #negative indices aren't valid
        with self.assertRaises(IndexError):
            self.empty_list.remove_at_index(-1)

    def test_remove_at_index_head_node(self):
        """Test that when the remove at index method
        is called and the index is 0, that the head node
        is removed.
        """
        #fixture list indices go from 0 to 6 and
        #the values at each index is the same as the index itself
        self.assertEqual(7, self.non_empty_list.size)
        self.assertEqual(0, self.non_empty_list.head.data)

        #remove from head
        self.non_empty_list.remove_at_index(0)
        self.assertEqual(6, self.non_empty_list.size)
        self.assertEqual(1, self.non_empty_list.head.data)

    def test_remove_at_index_within_range(self):
        """Test that when the remove at index method
        is called on a list with an index that is in range,
        that the appropriate node is removed.
        """
        #fixture list indices go from 0 to 6 and
        #the values at each index is the same as the index itself
        
        #remove 5 from index 5
        self.assertEqual(5, self.non_empty_list.value_at(5))
        self.non_empty_list.remove_at_index(5)
        self.assertEqual(6, self.non_empty_list.size)

        #confirm that 5 is still not in the list
        self.assertFalse(5 in self.non_empty_list)

    def test_remove_value_from_empty_list_raises_error(self):
        """Test that trying to remove a value from an empty
        list raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.empty_list.remove_value(9)

    def test_remove_value_not_in_list_raises_error(self):
        """Test the trying to remove a value that doesn't exist
        in the list raises and error.
        """
        #fixture contains values from 0 to 6
        with self.assertRaises(ValueError):
            self.non_empty_list.remove_value(100)

    def test_remove_value_from_head_of_list(self):
        """Test that when the value to be removed exists at the head
        of the list, it is properly removed.
        """
        #fixture list indices go from 0 to 6 and
        #the values at each index is the same as the index itself
        self.assertEqual(0, self.non_empty_list.head.data)
        self.assertEqual(7, self.non_empty_list.size)
        
        #remove value
        self.non_empty_list.remove_value(0)
        self.assertEqual(6, self.non_empty_list.size)

        #head should now be 1
        self.assertEqual(1, self.non_empty_list.head.data)

        #confirm that 0 is not in the list anymore
        self.assertFalse(0 in self.non_empty_list)

    def test_remove_value_not_from_head_of_list(self):
        """Test that when the value to be removed is not at the head of
        the list, that it is propertly removed.
        """
        #fixture list indices go from 0 to 6 and
        #the values at each index is the same as the index itself
        self.assertEqual(7, self.non_empty_list.size)

        #remove value
        self.non_empty_list.remove_value(5)
        self.assertEqual(6, self.non_empty_list.size)

        #confirm that 5 is not in the list anymore
        self.assertFalse(5 in self.non_empty_list)

    def test_remove_value_removes_first_occurrence(self):
        """Test that if a value appears more that once in a list,
        that only the first occurrence of that value is removed.
        """
        #fixture list indices go from 0 to 6 and
        #the values at each index is the same as the index itself
        self.assertEqual(7, self.non_empty_list.size)

        #insert duplicate valuesinto list
        self.non_empty_list.insert(2, 4)
        self.assertEqual(8, self.non_empty_list.size)
        
        #now there should be a four at indices 2 and 5
        self.assertEqual(4, self.non_empty_list.value_at(2))
        self.assertEqual(4, self.non_empty_list.value_at(5))

        #remove value
        #the value at index 2 should be the one to be removed
        self.non_empty_list.remove_value(4)
        self.assertEqual(7, self.non_empty_list.size)

        #confirm that at least one 4 still exists in the list
        self.assertTrue(4 in self.non_empty_list)
        self.assertTrue(1, self.non_empty_list.count(4))

        #the 4 at index five should now be at index 4
        self.assertEqual(4, self.non_empty_list.value_at(4))
    
    def test_len_magic_method_on_empty_list(self):
        """Test that if the len magic method is invoked on an empty
        list, that 0 is returned.
        """
        self.assertEqual(0, len(self.empty_list))

    def test_len_magic_method_on_non_empty_list(self):
        """Test that if the len magic method is invoked on a non-empty
        list, that the correct length of the list is returned.
        """
        #length of the fixture is 7
        self.assertEqual(7, len(self.non_empty_list))

        #remove node
        self.non_empty_list.pop_front()

        #check length again
        self.assertEqual(6, len(self.non_empty_list))

    def test_contains_magic_method_on_empty_list(self):
        """Test that if the contains magic method is invoked
        on an empty list, that it always returns False.
        """
        self.assertFalse(0 in self.empty_list)
        self.assertFalse(100 in self.empty_list)
        self.assertFalse(3 in self.empty_list)

    def test_contains_magic_method_on_non_empty_list_value_not_in_list(self):
        """Test that if the contains magic method is invoked on
        a non-empty list that doesn't contain the value, that
        it returns False.
        """
        #fixture contains nodes that have values from 0 to 6 in that order
        self.assertFalse(50 in self.non_empty_list)
        self.assertFalse(100 in self.non_empty_list)
        self.assertFalse(30 in self.non_empty_list)

    def test_contains_magic_methods_on_non_empty_list_value_in_list(self):
        """Test that if the contains magic method is invoked on
        a non-empty list that does contain the value, that
        it returns True.
        """
        #fixture contains nodes that have values from 0 to 6 in that order
        self.assertTrue(5 in self.non_empty_list)
        self.assertTrue(0 in self.non_empty_list)
        self.assertTrue(3 in self.non_empty_list)


    def test_loop_through_empty_list(self):
        """Test that if an attempt is made to loop through an empty list,
        that the loop doesn't execute.
        """
        nodes = [node for node in self.empty_list]
        self.assertEqual([], nodes)

    def test_loop_through_non_empty_list(self):
        """Test that if an attempt is made to loop through a non-empty list,
        that the nodes' values are returned in the proper order.
        """
        #fixture contains nodes that have values from 0 to 6 in that order
        value = 0
        for node in self.non_empty_list:
            self.assertEqual(value, node)
            value += 1


if __name__ == "__main__":
    unittest.main()
