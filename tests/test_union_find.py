"""This module holds tests for my implementation
of the Union Find data structure.
"""
import unittest
from data_structures.union_find import UnionFind


class UnionFindTestCase(unittest.TestCase):
    """Class to run tests on the Union Find implementation."""

    def test_invalid_size(self):
        """Test to ensure that an exception is raised
        when the UnionFind is instantiated with a size
        that isn't greater than 0.
        """
        with self.assertRaises(ValueError):
            union_find = UnionFind(0)
        
        with self.assertRaises(ValueError):
            union_find = UnionFind(-1)

        with self.assertRaises(ValueError):
            union_find = UnionFind(-2349)

    def test_initial_rank_zero(self):
        """Test that a set's initial rank is 0
        when created.
        """
        initial_rank = 0
        elements = [0, 1, 2, 3]
        union_find = UnionFind(4)
        for element in elements:
            union_find.make_set(element)
            self.assertEqual(union_find.rank[element], initial_rank)

    def test_element_out_of_range(self):
        """Test to ensure that the find and make set methods
        throw an exception when an element that is out of
        range of the Union Find is passed as an arguement.
        """
        elements = [0, 1, 2, 3]
        union_find = UnionFind(4)
        for element in elements:
            union_find.make_set(element)
        with self.assertRaises(ValueError):
            union_find.find(5)

        with self.assertRaises(ValueError):
            union_find.find(-1)

        with self.assertRaises(ValueError):
            union_find.union(1, 6)

        with self.assertRaises(ValueError):
            union_find.union(-1, 3)

        with self.assertRaises(ValueError):
            union_find.is_connected(1, 78)

        with self.assertRaises(ValueError):
            union_find.is_connected(-10, 3)

    def test_root_points_to_itself(self):
        """Test to ensure that the root of the set
        points to itself when created.
        """
        elements = [0, 1, 2, 3]
        union_find = UnionFind(4)
        for element in elements:
            union_find.make_set(element)
            self.assertEqual(union_find.find(element), element)

    def test_is_connected(self):
        """Test to ensure UnionFind reports that elements
        are in the same set after a union operation
        is performed.
        """
        elements = [0, 1, 2, 3]
        union_find = UnionFind(4)
        for element in elements:
            union_find.make_set(element)
            #element should be connected to itself
            self.assertTrue(union_find.is_connected(element, element))
        
        union_find.union(0, 1)
        self.assertTrue(union_find.is_connected(0, 1))
        self.assertTrue(union_find.is_connected(1, 0))
        self.assertFalse(union_find.is_connected(0, 2))
        self.assertFalse(union_find.is_connected(0, 3))
        self.assertFalse(union_find.is_connected(1, 2))
        self.assertFalse(union_find.is_connected(1, 3))
        self.assertFalse(union_find.is_connected(3, 2))

    def test_num_components(self):
        """Test to ensure UnionFind reports the
        corrent number of components after a union
        operation.
        """
        elements = [0, 1, 2, 3]
        union_find = UnionFind(4)
        for element in elements:
            union_find.make_set(element)
        self.assertEqual(union_find.get_num_components(), 4)

        union_find.union(0, 1)
        self.assertEqual(union_find.get_num_components(), 3)

        union_find.union(2, 3)
        self.assertEqual(union_find.get_num_components(), 2)

        union_find.union(1, 3)
        self.assertEqual(union_find.get_num_components(), 1)

        #since both are now in the same set, the number of
        #components should stay the same
        union_find.union(1, 2)
        self.assertEqual(union_find.get_num_components(), 1)
        

if __name__ == "__main__":
    unittest.main() 
        