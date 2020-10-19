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
    detect_negative_cycles(graph, distances, predecessors)

    return distances, predecessors


def detect_negative_cycles(graph, distances, predecessors):
    for node in graph:
        for neighbor in graph[node]:
            new_distance = distances[node] + neighbor.weight
            if new_distance < distances[neighbor.value]:  # negative weight cycle found
                distances[neighbor.value] = float("-inf")
                predecessors[neighbor.value] = -1


def find_shortest_path(predecessors, source, destination):
    """Given a dictionary of predeccesors that was constructed via
    the Bellman-Ford algorithm, return the vertices in the shortest
    path from source to destination.
    """
    path = []
    # destination vertex not reachable from source
    if destination not in predecessors:
        return path

    current_node = destination
    while current_node is not None:
        predecessor = predecessors[current_node]
        if predecessor == -1:  # vertex is part of a negative weight cycle
            return None
        path.append(current_node)
        current_node = predecessor
    path.reverse()
    return path


# Graph from here: https://www.geeksforgeeks.org/bellman-ford-algorithm-simple-implementation/
def test_bellman_ford():
    graph = {
        0: [Node(1, -1), Node(2, 4)],
        1: [Node(2, 3), Node(3, 2), Node(4, 2)],
        2: [],
        3: [Node(2, 5), Node(1, 1)],
        4: [Node(3, -3)]
    }
    start = 0
    end = 3
    distances, predecessors = bellman_ford_adjacency_list(start, graph)
    shortest_path = find_shortest_path(predecessors, start, end)

    print("Vertex       Distance from Source")
    for node in distances:
        print(f"{node}                    {distances[node]}")
    print()
    print(f"Shortest path from {start} to {end}: ", shortest_path)


test_bellman_ford()