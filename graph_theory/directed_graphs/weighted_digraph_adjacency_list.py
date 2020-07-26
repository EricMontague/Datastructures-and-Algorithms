"""This module contains my implementations of a weighted directed graph
represented as an adjacency list. I assume that all of the vertices (inputs) 
are positive integers and edges can be either positive or negative integers.
"""


class WeightedDiGraph:
    """Class to represent a weighted directed graph using
    an adjacency list.
    """

    def __init__(self, num_vertices):
        if num_vertices < 0:
            raise ValueError("num_vertices cannot be less than 0")
        self._num_vertices = num_vertices
        self._adjacency_list = {vertex: [] for vertex in range(num_vertices)}

    def add_vertex(self, vertex):
        """Add a new vertex to the graph."""
        if vertex < 0:
            raise ValueError("A vertex can't be less than 0")
        if not self.has_vertex(vertex):
            self._adjacency_list[vertex] = []
            self._num_vertices += 1

    def remove_vertex(self, vertex):
        """Remove a vertex from the graph, along with its
        outgoing and incoming edges.
        """
        if not self.has_vertex(vertex):
            raise ValueError("The given vertex doesn't exist within the graph")
        self._adjacency_list.pop(vertex)
        self._num_vertices -= 1
        for source in self._adjacency_list:
            self._adjacency_list[source] = {
                (neighbor, weight) 
                for neighbor, weight in self._adjacency_list[source] 
                if neighbor!= vertex
            }
            
    def set_edge(self, source, destination, weight):
        """Add an edge to the graph. If either of the vertices don't exist, they
        will be created and then the edge with be formed. If the edge already exists,
        its weight will be updated.
        """
        # purposefully incomplete edge
        edge = (destination, weight)
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
        self._adjacency_list[source] = {
            (neighbor, weight)
            for neighbor, weight in self._adjacency_list[source]
            if neighbor != destination
        }
        self._adjacency_list[source].add(edge)

    def remove_edge(self, source, destination):
        """Remove an edge from the graph."""
        if not self.has_vertex(source):
            raise ValueError(f"Vertex {source} doesn't exist in the graph")
        if not self.has_vertex(destination):
            raise ValueError(f"Vertex {destination} doesn't exist in the graph")
        neighbors = self._adjacency_list[source]
        for neighbor, weight in enumerate(neighbors):
            if neighbor == destination:
                neighbors.remove((neighbor, weight))

    def has_vertex(self, vertex):
        """Return True if the given vertex exists in the graph."""
        return vertex in self._adjacency_list

    def has_edge(self, source, destination):
        """Return True if an edge exists from the source vertex
        to the destination vertex.
        """
        if self._adjacency_list.get(source) is not None:
            for neighbor, weight in self._adjacency_list[source]:
                if neighbor == destination:
                    return True
        return False

    def get_neighbors(self, vertex):
        """Return the neighboring vertices of the given vertex as a list."""
        if not self.has_vertex(vertex):
            return []
        return list(self._adjacency_list[vertex])

    @property
    def num_vertices(self):
        """Return the number of vertices in the graph."""
        return self._num_vertices

    @property
    def num_edges(self):
        """Return the number of edges in the graph."""
        edges = 0
        for neighbors in self._adjacency_list.values():
            edges += len(neighbors)
        return edges

