"""This module contains tests for my implementation of depth first search."""


import unittest
from graph_theory.algorithms.dfs_adjacency_list import dfs as dfs_adjacency_list
from graph_theory.algorithms.dfs_adjacency_matrix import dfs as dfs_adjacency_matrix

# The iterative version of dfs_visit is not tested here, but given the inputs below,
# it will produce an ordering of [0, 3, 5, 1, 2, 4], which is another correct dfs order
class DFSTestCase(unittest.TestCase):
    """Class to run tests on my dfs implementation."""

    def setUp(self):
        """Create fixtures."""
        self.adjacency_list = {0: [1, 3], 1: [2], 2: [3, 4], 3: [5], 4: [4], 5: [0]}
        self.adjacency_matrix = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
        ]

    def tearDown(self):
        """Delete fixtures."""
        del self.adjacency_list
        del self.adjacency_matrix

    def test_dfs_adjacency_list(self):
        """Test to confirm that the implementation of depth first search
        using an adjacency list produces the vertices in the graph in
        the correct order.
        """
        results = [0, 1, 2, 3, 5, 4]
        self.assertEqual(results, list(dfs_adjacency_list(self.adjacency_list)))

    def test_dfs_adjacency_matrix(self):
        """Test to confirm that the implementation of depth first search
        using an adjacency matrix produces the vertices in the graph in
        the correct order.
        """
        results = [0, 1, 2, 3, 5, 4]
        self.assertEqual(results, list(dfs_adjacency_matrix(self.adjacency_matrix)))


if __name__ == "__main__":
    unittest.main()
