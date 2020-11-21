"""This module contains algorithms for computing single source
shortest paths in a graph with cycles.

Source: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec19.pdf
"""


from collections import namedtuple

Vertex = namedtuple("Vertex", ("value", "weight"))


class ShortestPathResult:
    def __init__(self):
        self._distances = {}
        self._predecessors = {}

    def get_distance(self, k, vertex):
        return self._distances[(k, vertex)]

    def set_distance(self, k, vertex, distance):
        self._distances[(k, vertex)] = distance

    def get_predecessor(self, k, vertex):
        return self._predecessors[(k, vertex)]

    def set_predecessor(self, k, vertex, predecessor):
        self._predecessors[(k, vertex)] = predecessor

    def build_path(self, source, destination):
        pass


# graph is assumed to be an adjacency list
def single_source_shortest_paths_cyclic(source, graph):
    num_vertices = len(graph)
    result = ShortestPathResult()
    inverted_adjacency_list = invert_adjacency_list(graph)

    # Set the distance and predecessor
    # For each vertex in all |V| levels of the graph
    # To 0 and None respectively
    for i in range(num_vertices):
        result.set_distance(i, source, 0)
        result.set_predecessor(i, source, None)

    # Set the distance for each vertex that is not the source
    # in the first level of the graph to infinity
    for vertex in range(num_vertices):
        if vertex != source:
            result.set_distance(0, vertex, float("inf"))

    # Copmute shortest paths
    for vertex in range(num_vertices):
        compute_shortest_path(inverted_adjacency_list, num_vertices - 1, vertex, result)

    distances = {}
    predecessors = {}
    for vertex in range(num_vertices):
        distances[vertex] = result.get_distance(num_vertices - 1, vertex)
        predecessors[vertex] = result.get_predecessor(num_vertices - 1, vertex)
    return distances, predecessors


def invert_adjacency_list(graph):
    inverted_adjacency_list = {}
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor.value not in inverted_adjacency_list:
                inverted_adjacency_list[neighbor.value] = []
            inverted_adjacency_list[neighbor.value].append(
                Vertex(vertex, neighbor.weight)
            )
    return inverted_adjacency_list


def compute_shortest_path(inverted_adjacency_list, k, current_vertex, result):
    """ Recursion on finding the shortest path to current_vertex with no more than k edges
    on a graph with cycles. 'k' is the kth level subproblem, i.e. finding paths
    with no more than k edges.
    """
    if result.get_distance(k, current_vertex) is not None:
        return result.get_distance(k, current_vertex)
    current_distance = float("inf")
    predecessor = -1
    for incoming_neighbor in inverted_adjacency_list[current_vertex]:
        new_distance = incoming_neighbor.weight + compute_shortest_path(
            inverted_adjacency_list, k - 1, incoming_neighbor.value, result
        )
        if new_distance < current_distance:
            current_distance = new_distance
            predecessor = incoming_neighbor.value
    result.set_distance(k, current_vertex, current_distance)
    result.set_predecessor(k, current_vertex, predecessor)
    return current_distance


# informal test
def test_single_source_shortest_paths_cyclic():
    adjacency_list = {0: [Vertex(1, 5)], 1: [Vertex(2, 6)], 2: [Vertex(0, 7)]}
    source = 0
    distances, predecessors = single_source_shortest_paths_cyclic(
        source, adjacency_list
    )
    print(distances)
    print(predecessors)
    # print(f"Shortest path from 0 to 1: {shortest_path_result.build_path(1)}")
    # print(f"Shortest path from 0 to 2: {shortest_path_result.build_path(2)}")


test_single_source_shortest_paths_cyclic()


# class ShortestPathResult:
#     def __init__(self, num_vertices):
#         self._distances = []
#         self._predecessors = []
#         for vertex in range(num_vertices):
#             distance_row = [float("inf")] * num_vertices
#             predecessor_row = [-1] * num_vertices
#             self._distances.append(distance_row)
#             self._predecessors.append(predecessor_row)

#     def get_distance(self, k, vertex):
#         return self._distances[k][vertex]

#     def set_distance(self, k, vertex, distance):
#         self._distances[k][vertex] = distance

#     def get_predecessor(self, k, vertex):
#         return self._predecessors[k][vertex]

#     def set_predecessor(self, k, vertex, predecessor):
#         self._predecessors[k][vertex] = predecessor

#     def build_path(self, source, destination):
#         pass


# # graph is assumed to be an adjacency list
# def single_source_shortest_paths_cyclic(source, graph):
#     result = ShortestPathResult(len(graph))
#     inverted_adjacency_list = invert_adjacency_list(graph)
#     for k in range(len(graph)):
#         for vertex in range(len(graph)):
#             compute_shortest_path(k, source, vertex, inverted_adjacency_list, result)
#     return result


# def invert_adjacency_list(graph):
#     inverted_adjacency_list = {}
#     for vertex in graph:
#         for neighbor in graph[vertex]:
#             if neighbor.value not in inverted_adjacency_list:
#                 inverted_adjacency_list[neighbor.value] = []
#             inverted_adjacency_list[neighbor.value].append(
#                 Vertex(vertex, neighbor.weight)
#             )
#     return inverted_adjacency_list


# def compute_shortest_path(k, source, destination, inverted_adjacency_list, result):
#     if result.get_distance(k, destination) != float("inf"):
#         return result.get_distance(k, destination)
#     elif source == destination:
#         current_distance = 0
#         predecessor = None
#     else:
#         current_distance = float("inf")
#         predecessor = -1
#         for incoming_neighbor in inverted_adjacency_list[destination]:
#             path_distance = compute_shortest_path(
#                 k, source, incoming_neighbor.value, inverted_adjacency_list, result
#             )
#             new_distance = path_distance + incoming_neighbor.weight
#             if new_distance < current_distance:
#                 current_distance = new_distance
#                 predecessor = incoming_neighbor.value
#     result.set_distance(k, destination, current_distance)
#     result.set_predecessor(k, destination, predecessor)
#     return result.get_distance(k, destination)


# # informal test
# def test_single_source_shortest_paths_cyclic():
#     adjacency_list = {0: [Vertex(1, 5)], 1: [Vertex(2, 6)], 2: [Vertex(0, 7)]}
#     source = 0
#     shortest_path_result = single_source_shortest_paths_cyclic(source, adjacency_list)
#     print(shortest_path_result._distances)
#     print(shortest_path_result._predecessors)
#     # print(f"Shortest path from 0 to 1: {shortest_path_result.build_path(1)}")
#     # print(f"Shortest path from 0 to 2: {shortest_path_result.build_path(2)}")


# test_single_source_shortest_paths_cyclic()
