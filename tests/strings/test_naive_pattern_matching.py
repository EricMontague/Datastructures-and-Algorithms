"""This module contains tests for my naive pattern matching
algorithm.
"""

import unittest
from strings.naive_pattern_matching import search


class NaivePatternMatchingTestCase(unittest.TestCase):
    def setUp(self):
        """Setup fixtures."""
        self.string1 = "aaaaab"
        self.pattern1 = "aaab"

        self.string2 = "abcdefghdef"
        self.pattern2 = "def"

        self.string3 = "alsjnhpe"
        self.pattern3 = "jk"

    def tearDown(self):
        """Clean up fixtures."""
        del self.string1
        del self.string2
        del self.string3

        del self.pattern1
        del self.pattern2
        del self.pattern3

    def test_pattern_string_is_empty(self):
        """Test to confirm that if the pattern string is an empty string,
        the search function returns -1.
        """
        self.assertEqual(-1, search("", self.string1))

    def test_large_string_is_empty(self):
        """Test to confirm that if the large string is an empty string,
        the search function returns -1.
        """
        self.assertEqual(-1, search(self.pattern1, ""))

    def test_pattern_string_longer_than_large_string(self):
        """Test to confirm that if the pattern string is longer than the
        large string that the search function returns -1.
        """
        pattern = "a" * 20
        self.assertEqual(-1, search(pattern, self.string1))

    def test_pattern_not_in_string(self):
        """Test to confirm that if the pattern does not exist in the string
        that the search function returns -1.
        """
        self.assertTrue(self.pattern3 not in self.string3)
        self.assertEqual(-1, search(self.pattern3, self.string3))

    def test_pattern_exists_in_string(self):
        """Test to confirm that if the pattern exists in the string, that
        the search function returns the starting index of the pattern.
        """
        self.assertTrue(self.pattern1 in self.string1)
        self.assertEqual(2, search(self.pattern1, self.string1))

    def test_pattern_exists_in_string_and_returns_first_occurrence(self):
        """Test to confirm that if the pattern exists multiple times in the 
        string, that the search function returns the index of the first occurrence
        of the pattern.
        """
        self.assertTrue(self.pattern2 in self.string2)
        self.assertTrue(self.string2.count(self.pattern2) > 1)
        self.assertEqual(3, search(self.pattern2, self.string2))


if __name__ == "__main__":
    unittest.main()
