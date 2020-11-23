"""This module contains an implementation of an unweighted directed graph
built in an object oriented way.
"""


class UnweightedDiGraphNode:
    """Class to represent a node in an unweighted directed graph."""

    def __init__(self, node_id):
        self._node_id = node_id
        self._neighbors = {}

    @property
    def node_id(self):
        """Return the id for this node."""
        return self._node_id

    @property
    def neighbors(self):
        """Return a list of this node's neighbors."""
        return list(self._neighbors.values())

    def has_neighbor(self, node_id):
        """Return True of the given node is a neighbor of this
        node, otherwise return False.
        """
        return node_id in self._neighbors

    def add_neighbor(self, node):
        """Add the given node as a neighbor for this node."""
        self._neighbors[node.node_id] = node

    def remove_neighbor(self, node_id):
        """Remove the given node from the dictionary of neighbors."""
        if not self.has_neighbor(node_id):
            raise ValueError(f"{node_id} is not a neighbor of {self._node_id}")
        self._neighbors.pop(node_id)


class UnweightedDiGraph:
    def __init__(self):
        self._num_nodes = 0
        self._node_id = 0
        self._nodes = {}

    # O(1)
    def add_node(self):
        """Add a new node to the graph and return the id generated
        for the new node.
        """
        id = self._node_id
        self._nodes[id] = UnweightedDiGraphNode(id)
        self._node_id += 1
        self._num_nodes += 1
        return id

    # O(1)
    def remove_node(self, node_id):
        """Remove the node from the graph with the given id."""
        if not self.has_node(node_id):
            raise ValueError(f"Graph does not have node: {node_id}")
        node_to_remove = self._nodes.pop(node_id)
        for node in self._nodes:
            try:
                self._nodes[node].remove_neighbor(node_id)
            except ValueError:
                pass
        self._num_nodes -= 1

    # O(1)
    def add_edge(self, from_, to):
        """Create an edge between the two given nodes. If either don't exist in
        the graph already, create both nodes before forming the edge.
        """
        if not self.has_node(from_):
            from_ = self.add_node()
        if not self.has_node(to):
            to = self.add_node()
        self._nodes[from_].add_neighbor(to)
        return from_, to

    # O(1)
    def remove_edge(self, from_, to):
        """Remove the edge between the two given nodes."""
        if not self.has_node(from_):
            raise ValueError(f"Graph does not have node: {from_}")
        if not self.has_node(to):
            raise ValueError(f"Graph does not have node: {to}")
        self._nodes[from_].remove_neighbor(to)

    # O(1)
    def has_edge(self, from_, to):
        """Return True if an edge exists between the two given nodes,
        otherwise return False
        """
        if not self.has_node(from_):
            raise ValueError(f"Graph does not have node: {from_}")
        if not self.has_node(to):
            raise ValueError(f"Graph does not have node: {to}")
        self._nodes[from_].has_neighbor(to)

    # O(1)
    def has_node(self, node_id):
        """Return True if the given node exists in the graph."""
        return node_id in self._nodes

    # O(deg+(V)), # outdegree of V
    def get_neighbors(self, node_id):
        """Return a list of neighbors for the given node."""
        if not self.has_node(node_id):
            return []
        return self._nodes[node_id].neighbors

    @property
    def num_nodes(self):
        """Return the number of nodes in the graph."""
        return self._num_nodes
