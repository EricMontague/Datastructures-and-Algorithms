"""This module contains my implementations of an unweighted directed graph. I assume
that all of the vertices (inputs) are positive integers.
"""



class UnweightedDiGraph1:
    """Class to represent an unweighted directed graph using
    an adjacency map.
    """

    def __init__(self):
        self._num_vertices = 0
        self._adjacency_map = {}

    def add_vertex(self, vertex):
        """Add a new vertex to the graph."""
        if vertex < 0:
            raise ValueError("A vertex can't be less than 0")
        if not self.has_vertex(vertex):
            self._adjacency_map[vertex] = set()
            self._num_vertices += 1

    def remove_vertex(self, vertex):
        """Remove a vertex from the graph, along with its
        outgoing and incoming edges.
        """
        if self.has_vertex(vertex):
            self._adjacency_map.pop(vertex)
            self._num_vertices -= 1
            for neighbors in self._adjacency_map.values():
                if vertex in neighbors:
                    neighbors.remove(vertex)

    def add_edge(self, source, destination):
        """Add an edge to the graph."""
        # Add both vertices to graph first if they don't exist
        if not self.has_vertex(source) and not self.has_vertex(destination):
            self.add_vertex(source)
            self.add_vertex(destination)    
        # Add destination vertex to graph first if it doesn't exist
        elif self.has_vertex(source) and not self.has_vertex(destination):
            self.add_vertex(destination)
        # Add source vertex to graph first if it doesn't exists
        elif not self.has_vertex(source) and self.has_vertex(destination):
            self.add_vertex(source)
        self._adjacency_map[source].add(destination)

    def remove_edge(self, source, destination):
        """Remove an edge from the graph."""
        if self.has_vertex(source):
            neighbors = self._adjacency_map[source]
            if destination in neighbors:
                neighbors.remove(destination)

    def has_vertex(self, vertex):
        """Return True if the given vertex exists in the graph."""
        return vertex in self._adjacency_map

    def has_edge(self, source, destination):
        """Return True if an edge exists from the source vertex
        to the destination vertex.
        """
        if self._adjacency_map.get(source) is not None:
            return destination in self._adjacency_map[source]
        return False

    @property
    def num_vertices(self):
        """Return the number of vertices in the graph."""
        return self._num_vertices

    @property
    def num_edges(self):
        """Return the number of edges in the graph."""
        edges = 0
        for neighbors in self._adjacency_map.values():
            edges += len(neighbors)
        return edges

    def traverse(self, algorithm):
        pass

    def _dfs(self):
        pass

    def _dfs_visit(self, source, visited):
        pass

    def _bfs(self, source):
        pass



class UnWeightedDiGraph2:
    """Class to represent an unweighted, directed graph
    using an adjacency matrix."""

    def __init__(self, num_vertices):
        if num_vertices < 1:
            raise ValueError("num_vertices cannot be less than 1")
        self._num_vertices = num_vertices
        self._adjacency_matrix = [[0] * num_vertices for vertex in range(num_vertices)]
    
    def add_vertex(self, vertex):
        """Add the given vertex to the graph."""
        if vertex < self._num_vertices:
            raise ValueError(f"Vertex must be greater than {self._num_vertices - 1}")
        if not self.has_vertex(vertex):
            self._num_vertices += 1
            for index, row in enumerate(self._adjacency_matrix):
                row.append(0)
            self._adjacency_matrix.append([0] * self._num_vertices)

    def remove_vertex(self, data):
        pass

    def add_edge(self, source, destination):
        pass

    def remove_edge(self, source, destination):
        pass

    def traverse(self, algorithm):
        pass

    @property
    def num_vertices(self):
        """Return the number of vertices in the graph."""
        pass

    @property
    def num_edges(self):
        """Return the number of vertices in the graph."""
        pass

    def has_vertex(self, vertex):
        """Return True if the graph contains the given vertex."""
        pass

    def has_edge(self, source, destination):
        """Return True if the graph contains an edge from the source
        vertex to the destination vertex.
        """
        pass

    def _dfs(self):
        pass

    def _dfs_visit(self, source, visited):
        pass

    def _bfs(self, source):
        pass


