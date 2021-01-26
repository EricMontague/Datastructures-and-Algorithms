"""This module contains tests for my hash table implementation that
uses chaining to deal with key collisions.
"""

import unittest
from data_structures.hash_tables.hash_table_with_chaining import HashTable


class HashTableTestCase(unittest.TestCase):
    """Class for running tests on the hash table with chaining
    implementation.
    """

    def setUp(self):
        """Create fixtures."""
        self.empty_table = HashTable()
        self.non_empty_table = HashTable()
        keys = ["Apple", "Orange", "Banana", "Avocado", "Peach"]
        for value in range(5):
            self.non_empty_table.put(keys[value], value)

    def tearDown(self):
        """Cleanup fixtures."""
        del self.empty_table
        del self.non_empty_table

    def test_instantiating_hash_table_with_invalid_arguments_raises_error(self):
        """Test that if the hash table is instantiated with invalid arguments that
        an error is raised.
        """
        with self.assertRaises(ValueError):
            hash_table = HashTable(capacity=-1)

        with self.assertRaises(ValueError):
            hash_table = HashTable(max_load_factor=0)

        with self.assertRaises(ValueError):
            hash_table = HashTable(max_load_factor=2)

        with self.assertRaises(ValueError):
            hash_table = HashTable(min_load_factor=0)

        with self.assertRaises(ValueError):
            hash_table = HashTable(min_load_factor=2)

    def test_get_key_does_not_exist(self):
        """Test that when the get method is called on the hash table and
        the key does NOT exist in the table, that None is returned.
        """
        self.assertIsNone(self.empty_table.get("Bread"))
        self.assertIsNone(self.non_empty_table.get("Bread"))

        self.assertIsNone(self.empty_table["Bread"])
        self.assertIsNone(self.non_empty_table["Bread"])

    def test_get_key_does_exist(self):
        """Test that when the get method is called on the hash table and
        the key exists in the table, that the correct value is returned
        """
        # the numbers correspond to the strings' positions in the list
        # found in the setUp method
        self.assertEqual(0, self.non_empty_table.get("Apple"))
        self.assertEqual(3, self.non_empty_table.get("Avocado"))

        # test __getiem__
        self.assertEqual(0, self.non_empty_table["Apple"])
        self.assertEqual(3, self.non_empty_table["Avocado"])

    def test_insert_new_item_into_table(self):
        """Test that if you are inserting a new key-value pair into the hash
        table, that the insertion is successful.
        """
        # confirm size and that the key doesn't exist
        self.assertEqual(5, self.non_empty_table.num_items)
        self.assertFalse(self.non_empty_table.exists("Grapes"))
        self.assertEqual(8, self.non_empty_table._capacity)

        # insert key-value pair
        self.non_empty_table.put("Grapes", 16)

        # confirm insertion worked
        self.assertEqual(6, self.non_empty_table.num_items)
        self.assertTrue(self.non_empty_table.exists("Grapes"))
        self.assertEqual(16, self.non_empty_table.get("Grapes"))

        # confirm that the table resized itself.
        # The capacity should have grown from 8 to 16
        self.assertEqual(16, self.non_empty_table._capacity)

        # second insertion, this time using the dunder method
        self.non_empty_table["Mango"] = 100

        # confirm again
        self.assertEqual(7, self.non_empty_table.num_items)
        self.assertTrue(self.non_empty_table.exists("Mango"))
        self.assertEqual(100, self.non_empty_table.get("Mango"))

    def test_insert_with_null_key_raises_error(self):
        """Test that if an attempt is made to set a key-value pair
        with the key being None, that an error is raised.
        """
        with self.assertRaises(KeyError):
            self.non_empty_table.put(None, 199)

        with self.assertRaises(KeyError):
            self.non_empty_table[None] = 200

    def test_update_item(self):
        """Test that if you are inserting a key-value pair into the hash table
        and the key already exists in the table, that the value associated
        with that key is updated.
        """
        # confirm size and that the key does exist
        self.assertEqual(5, self.non_empty_table.num_items)
        self.assertTrue(self.non_empty_table.exists("Peach"))
        self.assertEqual(4, self.non_empty_table.get("Peach"))

        # update value
        self.non_empty_table.put("Peach", 1000)

        # confirmation that update worked
        self.assertEqual(
            5, self.non_empty_table.num_items
        )  # num_items should still be the same
        self.assertEqual(1000, self.non_empty_table.get("Peach"))

        # second update to test __setitem__
        self.assertTrue(self.non_empty_table.exists("Avocado"))
        self.assertEqual(3, self.non_empty_table.get("Avocado"))

        self.non_empty_table["Avocado"] = 1500

        self.assertEqual(5, self.non_empty_table.num_items)
        self.assertEqual(1500, self.non_empty_table.get("Avocado"))

    def test_delete_key_does_not_exist_raises_error(self):
        """Test that when the delete method is called on the hash table and
        the key does NOT exist in the hash table, that an error is raised
        """
        with self.assertRaises(KeyError):
            self.empty_table.delete("Bread")

        with self.assertRaises(KeyError):
            self.non_empty_table.delete("Bread")

    def test_delete_key_does_exist(self):
        """Test that when the delete method is called on the hash table and
        the key exists in the hash able, that the correct item is deleted.
        """
        # confirm size and that the key does exist
        self.assertEqual(5, self.non_empty_table.num_items)
        self.assertTrue(self.non_empty_table.exists("Peach"))
        self.assertEqual(4, self.non_empty_table.get("Peach"))
        self.assertEqual(8, self.non_empty_table._capacity)

        # delete key-value pair
        self.non_empty_table.delete("Peach")

        # confirm deletion
        self.assertEqual(4, self.non_empty_table.num_items)
        self.assertFalse(self.non_empty_table.exists("Peach"))
        self.assertIsNone(self.non_empty_table.get("Peach"))

        # second deletion to test __delitem__
        del self.non_empty_table["Apple"]
        self.assertEqual(3, self.non_empty_table.num_items)
        self.assertFalse(self.non_empty_table.exists("Apple"))
        self.assertIsNone(self.non_empty_table.get("Apple"))

        # third deletion to test the resizing of the table.
        # Capacity should be halved from 8 to 4
        del self.non_empty_table["Avocado"]
        self.assertEqual(2, self.non_empty_table.num_items)
        self.assertFalse(self.non_empty_table.exists("Avocado"))
        self.assertIsNone(self.non_empty_table.get("Avocado"))
        self.assertEqual(4, self.non_empty_table._capacity)

    def test_delete_with_null_key_raises_error(self):
        """Test that if an attempt is made to delete a key-value pair
        with the key being None, that an error is raised.
        """
        with self.assertRaises(KeyError):
            self.non_empty_table.delete(None)

        with self.assertRaises(KeyError):
            del self.non_empty_table[None]

    def test_exists_method(self):
        """Test that the exists method returns the correct boolean value
        when a key is in the hash table and when it is not in the table.
        """
        # don't forget to test __contains__
        self.assertFalse(self.empty_table.exists("Bread"))
        self.assertFalse(self.non_empty_table.exists("Bread"))

        # test __contains__
        self.assertFalse("Bread" in self.empty_table)
        self.assertFalse("Bread" in self.non_empty_table)

    def test_is_empty_method(self):
        """Test that the is_empty method returns the correct boolean value
        when a the has table hash items in it, and when it doesn't
        """
        self.assertTrue(self.empty_table.is_empty())
        self.assertFalse(self.non_empty_table.is_empty())

    def test_keys_method(self):
        """Test that the keys method correctly returns a list of all
        of the keys in the hash table.
        """
        self.assertEqual([], self.empty_table.keys())
        keys = ["Apple", "Orange", "Banana", "Avocado", "Peach"]
        results = set(self.non_empty_table.keys())
        for key in keys:
            self.assertTrue(key in results)

    def test_values_method(self):
        """Test that the values method correctly returns a list of all
        of the values in the hash table.
        """
        self.assertEqual([], self.empty_table.values())
        values = [0, 1, 2, 3, 4]
        results = set(self.non_empty_table.values())
        for value in values:
            self.assertTrue(value in results)

    def test_items_method(self):
        """Test that the items method correctly returns a list of all
        of the key-value pairs in the hash table.
        """
        self.assertEqual([], self.empty_table.items())
        items = [
            ("Apple", 0),
            ("Orange", 1),
            ("Banana", 2),
            ("Avocado", 3),
            ("Peach", 4),
        ]
        results = set(self.non_empty_table.items())
        for item in items:
            self.assertTrue(item in results)

    def test_clear_method(self):
        """Test that the clear method clears all items out of the hash table."""

        # confirm contents of table
        self.assertFalse(self.non_empty_table.is_empty())
        self.assertEqual(5, self.non_empty_table.num_items)

        # clear
        self.non_empty_table.clear()

        # confirm that the table is reset
        self.assertTrue(self.non_empty_table.is_empty())
        self.assertEqual(0, self.non_empty_table.num_items)
        self.assertIsNone(self.non_empty_table.get("Apple"))
        self.assertFalse(self.non_empty_table.exists("Orange"))

        with self.assertRaises(KeyError):
            self.non_empty_table.delete("Banana")

    def test_num_items_property_getter(self):
        """Test that the num_items property returns the correct number of
        items in the hash table.
        """
        self.assertEqual(0, self.empty_table.num_items)
        self.assertEqual(5, self.non_empty_table.num_items)

    def test_num_items_no_setter(self):
        """Test that the num_items property is not writable."""
        with self.assertRaises(AttributeError):
            self.non_empty_table.num_items = 100


if __name__ == "__main__":
    unittest.main()
