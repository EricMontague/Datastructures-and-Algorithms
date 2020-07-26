"""This module contains tests for my implementation of an unweighted,
directed graph represented as an adjacency list. All inputs to the graph
are positive integers.
"""


import unittest
from graph_theory.directed_graphs.unweighted_digraph_adjacency_list import UnweightedDiGraph


class UnweightedDiGraphTestCase(unittest.TestCase):
    """Class to run tests on the unweighted, directed 
    graph implementation that is represented as an adjacency list.
    """

    def setUp(self):
        """Create fixtures."""
        self.empty_graph = UnweightedDiGraph(0)
        self.non_empty_graph = UnweightedDiGraph(6)
        self.non_empty_graph.set_edge(0, 1)
        self.non_empty_graph.set_edge(0, 2)
        self.non_empty_graph.set_edge(0, 5)
        self.non_empty_graph.set_edge(2, 3)
        self.non_empty_graph.set_edge(3, 1)
        self.non_empty_graph.set_edge(4, 0)
        self.non_empty_graph.set_edge(5, 5)

        # pretty-printed graph
        # {
        #     0: {1, 2, 5},
        #     1: {},
        #     2: {3},
        #     3: {1},
        #     4: {0},
        #     5: {5}
        # }

    def tearDown(self):
        """Delete fixtures."""
        del self.empty_graph
        del self.non_empty_graph

    def test_instantiate_graph_with_value_less_than_zero_raises_error(self):
        """Test that if the graph is instantiated with a value less than
        zero that an error is raised.
        """
        with self.assertRaises(ValueError):
            graph = UnweightedDiGraph(-1)

        with self.assertRaises(ValueError):
            graph = UnweightedDiGraph(-10)

    def test_add_vertex_less_than_zero_raises_error(self):
        """Test that trying to add a vertex that is less than zero
        raises an error.
        """
        with self.assertRaises(ValueError):
            self.empty_graph.add_vertex(-2)

        with self.assertRaises(ValueError):
            self.empty_graph.add_vertex(-22)

    def test_add_duplicate_vertex(self):
        """Test that a duplicate vertex cannot be added to the graph."""
        # graph has vertices numbered 0 through 5
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)

        # confirm that adding another vertex doesn't increase the number
        # of vertices or edges
        self.non_empty_graph.add_vertex(1)
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)

        # second confirmation
        self.non_empty_graph.add_vertex(5)
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)

    def test_add_vertex_successful(self):
        """Test that a vertex can be successfully added to the graph
        when correct input is given.
        """
        # graph has vertices numbered 0 through 5
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)

        # add new vertex
        self.non_empty_graph.add_vertex(6)
        self.assertTrue(self.non_empty_graph.has_vertex(6))
        self.assertEqual(
            self.non_empty_graph.num_vertices, 7
        )  # vertices should increase by 1
        self.assertEqual(self.non_empty_graph.num_edges, 7)  # edges should be the same
        self.assertEqual(
            len(self.non_empty_graph.get_neighbors(6)), 0
        )  # should have no neighbors

        # add another new vertex
        self.non_empty_graph.add_vertex(7)
        self.assertTrue(self.non_empty_graph.has_vertex(7))
        self.assertEqual(
            self.non_empty_graph.num_vertices, 8
        )  # vertices should increase by 1
        self.assertEqual(self.non_empty_graph.num_edges, 7)  # edges should be the same
        self.assertEqual(
            len(self.non_empty_graph.get_neighbors(7)), 0
        )  # should have no neighbors

    def test_remove_vertex_not_in_graph_raises_error(self):
        """Test that when an attempt is made to remove a vertex that
        is not in the graph, that an error is thrown.
        """
        with self.assertRaises(ValueError):
            self.non_empty_graph.remove_vertex(12)

        with self.assertRaises(ValueError):
            self.empty_graph.remove_vertex(200)

    def test_remove_vertex_successful(self):
        """Test that a vertex can be successfully removed from the graph
        when correct input is given.
        """
        # graph has vertices numbered 0 through 5
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)

        # remove vertex
        self.non_empty_graph.remove_vertex(1)

        # confirm removal
        self.assertEqual(self.non_empty_graph.num_vertices, 5)
        self.assertEqual(self.non_empty_graph.num_edges, 5)
        self.assertFalse(self.non_empty_graph.has_vertex(1))
        self.assertEqual(self.non_empty_graph.get_neighbors(1), [])

        # 2nd removal
        self.assertEqual(self.non_empty_graph.get_neighbors(4), [0])
        self.non_empty_graph.remove_vertex(4)

        # confirm 2nd removal
        self.assertEqual(self.non_empty_graph.num_vertices, 4)
        self.assertEqual(self.non_empty_graph.num_edges, 4)
        self.assertFalse(self.non_empty_graph.has_vertex(4))
        self.assertEqual(self.non_empty_graph.get_neighbors(4), [])

    def test_set_edge_when_both_vertices_dont_exist(self):
        """Test that an edge can be created even when both vertices
        don't exist in the graph.
        """
        # check that both vertices don't exist
        self.assertEqual(self.empty_graph.num_vertices, 0)
        self.assertEqual(self.empty_graph.num_edges, 0)
        self.assertFalse(self.empty_graph.has_vertex(10))
        self.assertFalse(self.empty_graph.has_vertex(11))
        self.assertFalse(self.empty_graph.has_edge(10, 11))

        # add edge from 10 -> 11
        self.empty_graph.set_edge(10, 11)

        # confirm
        self.assertEqual(self.empty_graph.num_vertices, 2)
        self.assertEqual(self.empty_graph.num_edges, 1)
        self.assertTrue(self.empty_graph.has_vertex(10))
        self.assertTrue(self.empty_graph.has_vertex(11))
        self.assertTrue(self.empty_graph.has_edge(10, 11))
        self.assertEqual(self.empty_graph.get_neighbors(10), [11])

    def test_set_edge_when_one_vertex_exists(self):
        """Test that an edge can be created even when only one vertex
        exists in the graph.
        """
        # check some things beforehand
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)
        self.assertTrue(self.non_empty_graph.has_vertex(4))
        self.assertFalse(self.non_empty_graph.has_vertex(20))
        self.assertFalse(self.non_empty_graph.has_edge(4, 20))
        self.assertEqual(self.non_empty_graph.get_neighbors(4), [0])

        # set edge
        self.non_empty_graph.set_edge(4, 20)

        # confirm success
        self.assertEqual(self.non_empty_graph.num_vertices, 7)
        self.assertEqual(self.non_empty_graph.num_edges, 8)
        self.assertTrue(self.non_empty_graph.has_vertex(20))
        self.assertTrue(self.non_empty_graph.has_edge(4, 20))
        self.assertTrue(0 in self.non_empty_graph.get_neighbors(4))
        self.assertTrue(20 in self.non_empty_graph.get_neighbors(4))

    def test_set_edge_when_both_vertices_exist_but_no_edge(self):
        """Test that an edge can be created when both vertices exist
        in the graph, but there is no edge from the source
        the to destination vertex.s
        """
        # check some things beforehand
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)
        self.assertTrue(self.non_empty_graph.has_vertex(4))
        self.assertTrue(self.non_empty_graph.has_vertex(2))
        self.assertFalse(self.non_empty_graph.has_edge(4, 2))
        self.assertEqual(self.non_empty_graph.get_neighbors(4), [0])

        # set edge
        self.non_empty_graph.set_edge(4, 2)

        # confirm success
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 8)
        self.assertTrue(self.non_empty_graph.has_edge(4, 2))
        self.assertTrue(0 in self.non_empty_graph.get_neighbors(4))
        self.assertTrue(2 in self.non_empty_graph.get_neighbors(4))

    def test_set_edge_when_both_vertices_exist_with_existing_edge(self):
        """Test that an edge can be created when both vertices exist
        in the graph, and there is already an edge from the source
        the to destination vertex.
        """
        # check some things beforehand
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)
        self.assertTrue(self.non_empty_graph.has_vertex(0))
        self.assertTrue(self.non_empty_graph.has_vertex(5))
        self.assertTrue(self.non_empty_graph.has_edge(0, 5))
        self.assertTrue(1 in self.non_empty_graph.get_neighbors(0))
        self.assertTrue(2 in self.non_empty_graph.get_neighbors(0))
        self.assertTrue(5 in self.non_empty_graph.get_neighbors(0))
        

        # set edge
        self.non_empty_graph.set_edge(0, 5)

        # confirm that nothing changed
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.non_empty_graph.num_edges, 7)
        self.assertTrue(1 in self.non_empty_graph.get_neighbors(0))
        self.assertTrue(2 in self.non_empty_graph.get_neighbors(0))
        self.assertTrue(5 in self.non_empty_graph.get_neighbors(0))

    def test_remove_edge_when_both_vertices_dont_exist_raises_error(self):
        """Test that if an attempt is made to remove an edge from the graph
        and both vertices don't exist, that an error is thrown.
        """
        with self.assertRaises(ValueError):
            self.empty_graph.remove_edge(18, 99)

    def test_remove_edge_when_one_vertex_doesnt_exist_raises_error(self):
        """Test that if an attempt is made to remove an edge from the graph
        and one of the vertices doesn't exist, that an error is thrown.
        """
        with self.assertRaises(ValueError):
            self.non_empty_graph.remove_edge(1, 99)

        with self.assertRaises(ValueError):
            self.non_empty_graph.remove_edge(99, 1)

    def test_has_vertex(self):
        """Test that the has_vertex method returns the correct result whether
        the vertex exists or not.
        """
        self.assertTrue(self.non_empty_graph.has_vertex(0))
        self.assertTrue(self.non_empty_graph.has_vertex(3))
        self.assertFalse(self.empty_graph.has_vertex(0))
        self.assertFalse(self.empty_graph.has_vertex(3))

    def test_has_edge(self):
        """Test that the has_edge method returns the correct result regardless
        of input given
        """
        self.assertTrue(self.non_empty_graph.has_edge(0, 1))
        self.assertTrue(self.non_empty_graph.has_edge(0, 2))
        self.assertFalse(self.empty_graph.has_edge(0, 1))
        self.assertFalse(self.empty_graph.has_edge(0, 5))

    def test_get_neighbors(self):
        """Test that the has_neighbors method returns the correct result regardless
        of input given
        """
        self.assertEqual(self.non_empty_graph.get_neighbors(5), [5])
        self.assertEqual(self.non_empty_graph.get_neighbors(3), [1])
        self.assertEqual(self.non_empty_graph.get_neighbors(1), [])
        self.assertEqual(self.empty_graph.get_neighbors(2), [])

    def test_num_vertices_getter(self):
        """Test that the num_vertices property returns the correct value."""
        self.assertEqual(self.non_empty_graph.num_vertices, 6)
        self.assertEqual(self.empty_graph.num_vertices, 0)

    def test_num_vertices_setter_raises_error(self):
        """Test that if an attempt is made to set the num_vertices property, that
        an error is raised.
        """
        with self.assertRaises(AttributeError):
            self.empty_graph.num_vertices = 19

        with self.assertRaises(AttributeError):
            self.non_empty_graph.num_vertices = 15

    def test_num_edges_getter(self):
        """Test that the num_edges property returns the correct value."""
        self.assertEqual(self.non_empty_graph.num_edges, 7)
        self.assertEqual(self.empty_graph.num_edges, 0)

    def test_num_edges_setter_raises_error(self):
        """Test that if an attempt is made to set the num_edges property, that
        an error is raised.
        """
        with self.assertRaises(AttributeError):
            self.empty_graph.num_edges = 1200

        with self.assertRaises(AttributeError):
            self.non_empty_graph.num_edges = 120


if __name__ == "__main__":
    unittest.main()

