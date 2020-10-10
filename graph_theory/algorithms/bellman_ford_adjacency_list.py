"""This module contains my implementation of the Bellman-Ford algorithm.
The graph is assumed to be represented as an adjacency list.
"""

from collections import namedtuple

Node = namedtuple("Node", ["value", "weight"])


# O(VE) time complexity
def bellman_ford_adjacency_list(source, graph):
    # Setup
    distances = {node: float("inf") for node in range(len(graph))}
    distances[source] = 0
    predecessors = {source: None}

    # Relax v - 1 edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                new_distance = distances[node] + neighbor.weight
                if new_distance < distances[neighbor.value]:
                    distances[neighbor.value] = new_distance
                    predecessors[neighbor.value] = node

    # Final relaxation attempt to identify negative cycles
    for node in graph:
        for neighbor in graph[node]:
            new_distance = distances[node] + neighbor.weight
            if new_distance < distances[neighbor.value]:  # negative weight cycle found
                distances[neighbor.value] = float("-inf")
                predecessors.pop(neighbor.value)
    return distances, predecessors


def find_shortest_path(predecessors, source, destination):
    """Given a dictionary of predeccesors that was constructed via
    a shortest paths algorithm, return the vertices in the shortest
    path from source to destination.
    """
    path = []
    current_node = destination
    while current_node is not None:
        predecessor = predecessors[current_node]
        path.append(current_node)
        current_node = predecessor
    path.reverse()
    return path
