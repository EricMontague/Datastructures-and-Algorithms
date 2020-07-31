"""This module contains tests for my implementation of breadth first search."""


import unittest
from graph_theory.algorithms.bfs_adjacency_list import bfs as bfs_adjacency_list
from graph_theory.algorithms.bfs_adjacency_matrix import bfs as bfs_adjacency_matrix


class BFSTestCase(unittest.TestCase):
    """Class to run tests on my bfs implementation."""

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

    def test_bfs_adjacency_list(self):
        """Test to confirm that the implementation of breadth first search
        using an adjacency list produces the vertices in the graph in
        the correct order.
        """
        results_one = [0, 1, 3, 2, 5, 4]
        results_two = [5, 0, 1, 3, 2, 4]
        results_three = [2, 3, 4, 5, 0, 1]
        self.assertEqual(results_one, list(bfs_adjacency_list(self.adjacency_list, 0)))
        self.assertEqual(results_two, list(bfs_adjacency_list(self.adjacency_list, 5)))
        self.assertEqual(
            results_three, list(bfs_adjacency_list(self.adjacency_list, 2))
        )

    def test_bfs_adjacency_matrix(self):
        """Test to confirm that the implementation of breadth first search
        using an adjacency matrix produces the vertices in the graph in
        the correct order.
        """
        results_one = [0, 1, 3, 2, 5, 4]
        results_two = [5, 0, 1, 3, 2, 4]
        results_three = [2, 3, 4, 5, 0, 1]
        self.assertEqual(
            results_one, list(bfs_adjacency_matrix(self.adjacency_matrix, 0))
        )
        self.assertEqual(
            results_two, list(bfs_adjacency_matrix(self.adjacency_matrix, 5))
        )
        self.assertEqual(
            results_three, list(bfs_adjacency_matrix(self.adjacency_matrix, 2))
        )


if __name__ == "__main__":
    unittest.main()
