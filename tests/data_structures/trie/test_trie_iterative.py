"""This module contains tests for the iterative implementation of a Trie."""


import unittest
from data_structures.trie.trie_iterative import Trie


class TrieIterativeTestCase(unittest.TestCase):
    """Class to run tests on the iterative Trie implementation."""

    def setUp(self):
        """Instantiate trie."""
        self.trie = Trie()

    def tearDown(self):
        """Delete trie."""
        del self.trie

    def test_empty_string_input(self):
        """Test to ensure that all methods raise a ValueError when an 
        empty string is passed to them."""
        
        with self.assertRaises(ValueError):
            self.trie.insert("")

        with self.assertRaises(ValueError):
            self.trie.search("")

        with self.assertRaises(ValueError):
            self.trie.starts_with("")

        with self.assertRaises(ValueError):
            self.trie.count_prefix("")
            
        with self.assertRaises(ValueError):
            self.trie.delete("")

    def test_non_string_input(self):
        """Test to ensure that all methods raise a TypeError when an object 
        that isn't a string is passed to them.
        """
               
        with self.assertRaises(TypeError):
            self.trie.insert(self.trie)

        with self.assertRaises(TypeError):
            self.trie.search(int)

        with self.assertRaises(TypeError):
            self.trie.starts_with(False)

        with self.assertRaises(TypeError):
            self.trie.count_prefix(None)
            
        with self.assertRaises(TypeError):
            self.trie.delete(dict)

    def test_insert(self):
        """Test the insert method."""
        word_one = "Software"
        word_two = "Soft"
        self.assertFalse(self.trie.search(word_one))
        self.trie.insert(word_one)
        self.assertTrue(self.trie.search(word_one))

        #insert a second word that shares the same prefix
        self.trie.insert(word_two)
        self.assertTrue(self.trie.search(word_two))

    def test_starts_with(self):
        """Test the starts with method."""
        word = "Software"
        self.trie.insert(word)
        self.assertTrue(self.trie.starts_with("Soft"))
        self.assertFalse(self.trie.starts_with("soft")) #case sensitive
        self.assertFalse(self.trie.starts_with("foo"))

    def test_search(self):
        """Test the search method."""
        word_one = "Software"
        word_two = "Soft"
        self.assertFalse(self.trie.search(word_one))
        self.trie.insert(word_one)
        self.assertTrue(self.trie.search(word_one))

        #insert a second word that shares the same prefix
        self.trie.insert(word_two)
        self.assertTrue(self.trie.search(word_two))

    def test_delete(self):
        """Test the delete method."""
        word = "Software"
        self.trie.insert(word)

        #test words not in the trie
        with self.assertRaises(ValueError):
            self.trie.delete("Google")
        
        with self.assertRaises(ValueError):
            self.trie.delete("software") #case sensitive

        self.assertTrue(self.trie.search(word))
        self.trie.delete(word)
        self.assertFalse(self.trie.search(word))

    def test_count_prefix(self):
        """Test the count prefix method."""
        words = ["apple", "apples", "application", "apply"]
        for word in words:
            self.trie.insert(word)
            self.assertTrue(self.trie.search(word))
        self.assertEqual(self.trie.count_prefix("app"), 4)
        self.assertEqual(self.trie.count_prefix("apple"), 2)
        self.assertEqual(self.trie.count_prefix("bread"), 0)



if __name__ == "__main__":
    unittest.main()
