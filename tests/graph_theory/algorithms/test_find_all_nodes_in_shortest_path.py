"""This module contains tests for my implementation of an algorithm to
find all of the nodes in the shortest path between two nodes in an
UNWEIGHTED graph.
"""

import unittest
from graph_theory.algorithms.find_all_nodes_in_shortest_path_unweighted_graph import (
    find_shortest_path_adj_list,
    find_shortest_path_adj_matrix,
)


class ShortestPathTestCase(unittest.TestCase):
    """Class to run tests on my implementation of an algorithm to
    find all of the nodes in the shortest path between two nodes in an
    UNWEIGHTED graph.
    """

    def setUp(self):
        """Create fixtures."""
        self.adjacency_list = {
            0: [1, 2],
            1: [5],
            2: [1, 3],
            3: [4],
            4: [7],
            5: [3, 4, 6],
            6: [7],
            7: [],
        }
        self.adjacency_matrix = [
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def tearDown(self):
        """Clean up fixtures."""
        del self.adjacency_list
        del self.adjacency_matrix

    def test_vertex_not_in_graph(self):
        """Test that an empty list is returned if either or both of the 
        vertices are not in the graph.
        """
        # empty graphs
        self.assertEqual(find_shortest_path_adj_list({}, 0, 2), [])
        self.assertEqual(find_shortest_path_adj_matrix([[]], 3, 1), [])

        # one vertex not in graph
        self.assertEqual(find_shortest_path_adj_list(self.adjacency_list, 1, 10), [])
        self.assertEqual(
            find_shortest_path_adj_matrix(self.adjacency_matrix, 1, 10), []
        )

        # both vertices not in graph
        self.assertEqual(find_shortest_path_adj_list(self.adjacency_list, 14, 10), [])
        self.assertEqual(
            find_shortest_path_adj_matrix(self.adjacency_matrix, 14, 10), []
        )

    def test_shortest_path_adjacency_list(self):
        """Test that the shortest path implementation for an adjacency list
        returns the correct vertices given particular inputs.
        """
        results_one = [0, 2, 3]
        results_two = [1, 5, 4]
        results_three = [2, 3, 4, 7]
        self.assertEqual(
            find_shortest_path_adj_list(self.adjacency_list, 0, 3), results_one
        )
        self.assertEqual(
            find_shortest_path_adj_list(self.adjacency_list, 1, 4), results_two
        )
        self.assertEqual(
            find_shortest_path_adj_list(self.adjacency_list, 2, 7), results_three
        )

    def test_shortest_path_adjacency_matrix(self):
        """Test that the shortest path implementation for an adjacency matrix
        returns the correct vertices given particular inputs.
        """
        results_one = [0, 2, 3]
        results_two = [1, 5, 4]
        results_three = [2, 3, 4, 7]
        self.assertEqual(
            find_shortest_path_adj_matrix(self.adjacency_matrix, 0, 3), results_one
        )
        self.assertEqual(
            find_shortest_path_adj_matrix(self.adjacency_matrix, 1, 4), results_two
        )
        self.assertEqual(
            find_shortest_path_adj_matrix(self.adjacency_matrix, 2, 7), results_three
        )


if __name__ == "__main__":
    unittest.main()

