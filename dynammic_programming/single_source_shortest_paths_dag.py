"""This file contains an algorithm for computing single source shortest paths
using dynamic programming.


- This algorithm runs in O(|V| + |E|) time for DAGs, but is infinite for
graphs with cycles
- This algorithm (memoized) is essentially doing a DFS, to do a topological sort, to
perform one round of the Belmman-Ford single source shortest paths algorithm
- The second line of the reccurrence relation looks just like the relaxation step
in a generic single source shortest paths problem

Recurrence Relation
--------------------
sp(s ,v) = 0, if s == v
sp(s, v) = min(sp(s, u)) + w(u, v), if s != v

- 's' is the source vertex, 'v' is the destination vertex,
'u' is some vertex on the shortest path from the source to the destination,
and w(u, v) is the weight of the edge from vertex 'u' to vertex 'v'
- In plain English, this says: "The shortest path from some vertex 's', to
another vertex 'v' is the minimum of the shortest path from 's' to another vertex
'u', plus the weight of the edge from 'u' to 'v'
- Here 'u' forms an incoming edge with 'v'
"""

from collections import namedtuple


Vertex = namedtuple("Vertex", ["value", "weight"])


class ShortestPathResult:
    def __init__(self, num_vertices):
        self._distances = {}
        self._predecessors = {}

    def get_distance(self, vertex):
        return self._distances.get(vertex)

    def set_distance(self, vertex, distance):
        self._distances[vertex] = distance

    def get_predecessor(self, vertex):
        return self._predecessors.get(vertex)

    def set_predecessor(self, vertex, predecessor):
        self._predecessors[vertex] = predecessor

    def build_path(self, destination):
        """Return a list containing the shortest path
        from the source vertex to the destination vertex.
        """
        if destination not in self._distances:
            raise ValueError(f"Vertex {destination} not in graph")
        if self._distances[destination] == float("inf"):
            return []
        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = self.get_predecessor(current)
        path.reverse()
        return path


# graph is given as an adjacency list
# Returns the lengths of the shortest path from some source vertex
# to all other vertices in the graph
def single_source_shortest_paths(source, graph):
    result = ShortestPathResult(len(graph))
    inverted_adjacency_list = invert_adjacency_list(graph)
    for vertex in range(len(graph)):
        compute_shortest_paths(source, vertex, inverted_adjacency_list, result)
    return result


def invert_adjacency_list(adjacency_list):
    inverted_adjacency_list = {}
    for vertex in adjacency_list:
        for neighbor in adjacency_list[vertex]:
            if neighbor.value not in inverted_adjacency_list:
                inverted_adjacency_list[neighbor.value] = []
            inverted_adjacency_list[neighbor.value].append(
                Vertex(vertex, neighbor.weight)
            )
    return inverted_adjacency_list


def compute_shortest_paths(source, current_vertex, inverted_adjacency_list, result):
    if result.get_distance(current_vertex) is not None:
        return result.get_distance(current_vertex)
    elif source == current_vertex:
        current_distance = 0
        predecessor = None
    else:
        current_distance = float("inf")
        predecessor = -1
        for incoming_neighbor in inverted_adjacency_list[current_vertex]:
            path_cost = compute_shortest_paths(
                source, incoming_neighbor.value, inverted_adjacency_list, result
            )
            new_distance = path_cost + incoming_neighbor.weight

            if new_distance < current_distance:
                current_distance = new_distance
                predecessor = incoming_neighbor.value
    result.set_distance(current_vertex, current_distance)
    result.set_predecessor(current_vertex, predecessor)
    return result.get_distance(current_vertex)


# informal test
def test_shortest_path():
    # adjacency_list = {
    #     0: [Vertex(1, 1), Vertex(2, 2)],
    #     1: [Vertex(4, 2)],
    #     2: [Vertex(3, 3), Vertex(5, 6)],
    #     3: [Vertex(6, 5)],
    #     4: [Vertex(7, 7)],
    #     5: [Vertex(7, 10)],
    #     6: [Vertex(7, 1)],
    #     7: [],
    # }
    adjacency_list = {0: [Vertex(1, 5)], 1: [Vertex(2, 6)], 2: [Vertex(0, 7)]}
    source = 0
    shortest_path_result = single_source_shortest_paths(source, adjacency_list)
    print()
    print(f"Shortest path from 0 to 1: {shortest_path_result.build_path(1)}")
    print(f"Shortest path from 0 to 2: {shortest_path_result.build_path(2)}")
    # print(f"Shortest path from 0 to 7: {shortest_path_result.build_path(7)}")
    # print(f"Shortest path from 0 to 6: {shortest_path_result.build_path(6)}")
    # print(f"Shortest path from 0 to 5: {shortest_path_result.build_path(5)}")


test_shortest_path()


# Alternative way to compute single source shortest paths that utilizes
# and algorithm to compute single target shortest paths
# Unfortunately it runs in O(V^2 + VE) time
# def single_source_shortest_paths(source, graph):
#     final_distances = {}
#     for vertex in range(len(graph)):
#         temp_distances = {}
#         compute_shortest_path(source, vertex, graph, temp_distances)
#         final_distances[vertex] = temp_distances[source]
#     return final_distances


# def compute_shortest_path(source, destination, graph, distances):
#     # Base case
#     if source == destination:
#         distances[source] = 0
#     elif source in distances:
#         return distances[source]
#     else:
#         # Recursive Case
#         shortest_path_length = float("inf")
#         for neighbor in graph[source]:
#             path_length = compute_shortest_path(
#                 neighbor.value, destination, graph, distances
#             )
#             shortest_path_length = min(
#                 shortest_path_length, path_length + neighbor.weight
#             )
#         distances[source] = shortest_path_length
#     return distances[source]
