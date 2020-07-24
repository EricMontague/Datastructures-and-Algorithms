"""This module contains my implementations of an unweighted directed graph
represented as an adjacency matrix. I assume that all of the vertices (inputs) 
are positive integers.
"""


class UnWeightedDiGraph2:
    """Class to represent an unweighted, directed graph
    using an adjacency matrix."""

    def __init__(self, num_vertices):
        if num_vertices < 1:
            raise ValueError("num_vertices cannot be less than 1")
        self._num_vertices = num_vertices
        self._adjacency_matrix = [[0] * num_vertices for vertex in range(num_vertices)]

    def add_vertex(self):
        """Add a new vertex to the graph."""
        self._num_vertices += 1
        for row in self._adjacency_matrix:
            row.append(0)
        self._adjacency_matrix.append([0] * self._num_vertices)

    def remove_vertex(self, vertex):
        """Remove the given vertex from the graph."""
        if not self.has_vertex(vertex):
            raise ValueError("Vertex does not exist in the graph")
        # Shift all rows after the vertex (index) that you are trying to remove back one
        for row in range(vertex + 1, self._num_vertices):
            self._adjacency_matrix[row - 1] = self._adjacency_matrix[row]
        self._adjacency_matrix[-1].pop()  # remove last row as it is now a duplicate

        # Shift all columns after the vertex (index) that you are trying to remove back one
        for row in range(self._num_vertices):
            for col in range(vertex + 1, self._num_vertices):
                self._adjacency_matrix[row][col - 1] = self._adjacency_matrix[row][col]
            self._adjacency_matrix[row].pop()
        self._num_vertices -= 1

    def set_edge(self, source, destination):
        """Add an edge to the graph. If either of the vertices don't exist, they
        will be created and then the edge with be formed.
        """
        if self.has_vertex(source) and self.has_vertex(destination):
            self._adjacency_matrix[source][destination] = 1
        elif not self.has_vertex(source) and not self.has_vertex(destination):
            self.add_vertex()  # add source
            self.add_vertex()  # add destintation
            self._adjacency_matrix[-2][-1] = 1
        elif self.has_vertex(source) and not self.has_vertex(destination):
            self.add_vertex()
            self._adjacency_matrix[source][-1] = 1
        elif not self.has_vertex(source) and self.has_vertex(destination):
            self.add_vertex()
            self._adjacency_matrix[-1][destination] = 1

    def remove_edge(self, source, destination):
        """Remove an edge from the graph."""
        if not self.has_vertex(source):
            raise ValueError(f"Vertex {source} not in graph")
        if not self.has_vertex(destination):
            raise ValueError(f"Vertex {destination} not in graph")
        self._adjacency_matrix[source][destination] = 0

    @property
    def num_vertices(self):
        """Return the number of vertices in the graph."""
        return self._num_vertices

    @property
    def num_edges(self):
        """Return the number of vertices in the graph."""
        edges = 0
        for row in range(self._num_vertices):
            for col in range(self._num_vertices):
                if self._adjacency_matrix[row][col] == 1:
                    edges += 1
        return edges

    def has_vertex(self, vertex):
        """Return True if the graph contains the given vertex."""
        try:
            return self._adjacency_matrix[vertex] is not None
        except IndexError:
            return False

    def has_edge(self, source, destination):
        """Return True if the graph contains an edge from the source
        vertex to the destination vertex.
        """
        try:
            return self._adjacency_matrix[source][destination] == 1
        except IndexError:
            return False

    def get_neighbors(self, vertex):
        """Return the neighboring vertices of the given vertex as a list."""
        if not self.has_vertex(vertex):
            return []
        neighbors = [
            index
            for index, value in enumerate(self._adjacency_matrix[vertex])
            if value == 1
        ]
        return neighbors

