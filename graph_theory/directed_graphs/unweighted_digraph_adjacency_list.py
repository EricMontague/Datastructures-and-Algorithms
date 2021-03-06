"""This module contains my implementations of an unweighted directed graph
represented as an adjacency list.
"""

from data_structures.linked_lists.singly_linked_list_no_tail_pointer import (
    SinglyLinkedList,
)


class UnweightedDiGraph:
    """Class to represent an unweighted directed graph using
    an adjacency list.
    """

    def __init__(self):
        self._num_nodes = 0
        self._node_id = 0
        self._adjacency_list = {}

    # O(1)
    def add_node(self):
        """Add a new node to the graph and return the id generated
        for the new node.
        """
        id = self._node_id
        self._adjacency_list[id] = SinglyLinkedList()
        self._node_id += 1
        self._num_nodes += 1
        return id

    # O(V + E)
    def remove_node(self, node_id):
        """Remove the node from the graph with the given id."""
        if not self.has_node(node_id):
            raise ValueError(f"Graph does not have node: {node_id}")
        self._adjacency_list.pop(node_id)
        for node in self._adjacency_list:
            try:
                self._adjacency_list[node].remove(node_id)
            except ValueError:
                pass
        self._num_nodes -= 1

    # O(deg+(V)), # outdegree of V
    def add_edge(self, from_, to):
        """Create an edge between the two given nodes. If either don't exist in
        the graph already, create both nodes before forming the edge.
        """
        if not self.has_node(from_):
            from_ = self.add_node()
        if not self.has_node(to):
            to = self.add_node()
        if self.has_edge(from_, to):
            raise ValueError(f"Edge from {from_} to {to} already exists")
        self._adjacency_list[from_].push_front(to)
        return from_, to

    # O(deg+(V)), # outdegree of V
    def remove_edge(self, from_, to):
        """Remove the edge between the two given nodes."""
        if not self.has_node(from_):
            raise ValueError(f"Graph does not have node: {from_}")
        if not self.has_node(to):
            raise ValueError(f"Graph does not have node: {to}")
        self._adjacency_list[from_].remove(to)

    # O(deg+(V)), # outdegree of V
    def has_edge(self, from_, to):
        """Return True if an edge exists between the two given nodes,
        otherwise return False
        """
        if not self.has_node(from_):
            raise ValueError(f"Graph does not have node: {from_}")
        if not self.has_node(to):
            raise ValueError(f"Graph does not have node: {to}")
        return self._adjacency_list[to].has_node(to)

    # O(1)
    def has_node(self, node_id):
        """Return True if the given node exists in the graph."""
        return node_id in self._adjacency_list
    
    # O(deg+(V)), # outdegree of V
    def get_neighbors(self, node_id):
        """Return a list of neighbors for the given node."""
        if not self.has_node(node_id):
            return []
        return self._adjacency_list[node_id].deep_copy()

    @property
    def num_nodes(self):
        """Return the number of nodes in the graph."""
        return self._num_nodes