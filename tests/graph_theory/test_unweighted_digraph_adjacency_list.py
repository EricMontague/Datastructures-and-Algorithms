"""This module contains tests for my implementation of an unweighted,
directed graph represented as an adjacency list. All inputs to the graph
are positive integers.
"""


import unittest
from graph_theory.unweighted_digraph_adjacency_list import UnweightedDiGraph


class UnweightedDiGraphTestCase(unittest.TestCase):
    """Class to run tests on the unweighted, directed 
    graph implementation that is represented as an adjacency list.
    """

    def setUp(self):
        """Create fixtures."""
        pass

    def tearDown(self):
        """Delete fixtures."""
        pass

    def test_add_vertex_less_than_zero_raises_error(self):
        """Test that trying to add a vertex that is less than zero
        raises an error.
        """
        pass

    def test_add_duplicate_vertex(self):
        """Test that a duplicate vertex cannot be added to the graph."""
        pass

    def test_add_vertex_successful(self):
        """Test that a vertex can be successfully added to the graph
        when correct input is given.
        """
        pass

    def test_remove_vertex_not_in_graph_raises_error(self):
        """Test that when an attempt is made to remove a vertex that
        is not in the graph, that an error is thrown.
        """
        pass

    def test_remove_vertex_successful(self):
        """Test that a vertex can be successfully removed from the graph
        when correct input is given.
        """
        pass

    def test_set_edge_when_both_vertices_dont_exist(self):
        """Test that an edge can be created even when both vertices
        don't exist in the graph.
        """
        pass

    def test_set_edge_when_one_vertex_exists(self):
        """Test that an edge can be created even when only one vertex
        exists in the graph.
        """
        pass

    def test_set_edge_when_both_vertices_exist_but_no_edge(self):
        """Test that an edge can be created when both vertices exist
        in the graph, but there is no edge from the source
        the to destination vertex.s
        """
        pass

    def test_set_edge_when_both_vertices_exist_with_existing_edge(self):
        """Test that an edge can be created when both vertices exist
        in the graph, and there is already an edge from the source
        the to destination vertex.
        """
        pass

    def test_remove_edge_when_both_vertices_dont_exist_raises_error(self):
        """Test that if an attempt is made to remove an edge from the graph
        and both vertices don't exist, that an error is thrown.
        """
        pass

    def test_remove_edge_when_one_vertex_doesnt_exist_raises_error(self):
        """Test that if an attempt is made to remove an edge from the graph
        and one of the vertices doesn't exist, that an error is thrown.
        """
        pass

    def test_has_vertex(self):
        """Test that the has_vertex method returns the correct result whether
        the vertex exists or not.
        """
        pass

    def test_has_edge(self):
        """Test that the has_edge method returns the correct result regardless
        of input given
        """
        pass

    def test_get_neighbors(self):
        """Test that the has_neighbors method returns the correct result regardless
        of input given
        """
        pass

    def test_num_vertices_getter(self):
        """Test that the num_vertices property returns the correct value."""
        pass

    def test_num_vertices_setter_raises_error(self):
        """Test that if an attempt is made to set the num_vertices property, that
        an error is raised.
        """
        pass

    def test_num_edges_getter(self):
        """Test that the num_edges property returns the correct value."""
        pass

    def test_num_edges_setter_raises_error(self):
        """Test that if an attempt is made to set the num_edges property, that
        an error is raised.
        """
        pass
