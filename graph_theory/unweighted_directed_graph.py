"""This module contains my implementations of an unweighted directed graph."""


from collections import defaultdict


class UnweightedDiGraph1:
    """Class to represent an unweighted directed graph.
    This class uses an adjacency map to represent the graph.
    """

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency_map = defaultdict(list)

    def add_vertex(self, data):
        pass

    def remove_vertex(self, data):
        pass

    def add_edge(self, from_, to):
        pass

    def remove_edge(self, from_, to):
        pass

    def traverse(self, algorithm):
        pass

    def _dfs(self):
        pass

    def _dfs_visit(self, source, visited):
        pass

    def _bfs(self, source):
        pass
