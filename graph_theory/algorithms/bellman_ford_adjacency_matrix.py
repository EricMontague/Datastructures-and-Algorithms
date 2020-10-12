"""This module contains my implementation of the Bellman-Ford algorithm.
The graph is assumed to be represented as an adjacency matrix.
"""


# O(V ^ 3) time complexity
def bellman_ford_adjacency_matrix(source, graph):
    # Setup
    distances = {node: float("inf") for node in range(len(graph))}
    distances[source] = 0
    predecessors = {source: None}

    # Relax v - 1 edges
    for i in range(len(graph) - 1):
        for node in range(len(graph)):
            for neighbor, weight in enumerate(graph[node]):
                if weight != 0:
                    new_distance = distances[node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = node

    # Final relaxation attempt to identify negative cycles
    detect_negative_cycles(graph, distances, predecessors)
    return distances, predecessors


def detect_negative_cycles(graph, distances, predecessors):
    for node in range(len(graph)):
        for neighbor, weight in enumerate(graph[node]):
            if weight != 0:
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:  # negative weight cycle found
                    distances[neighbor] = float("-inf")
                    predecessors[neighbor] = -1


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


# Graph from:
# https://www.geeksforgeeks.org/bellman-ford-algorithm-simple-implementation/
def test_bellman_ford():
    graph = [
        [0, -1, 4, float("inf"), float("inf")],
        [float("inf"), 0, 3, 2, 2],
        [float("inf"), float("inf"), 0, float("inf"), float("inf")],
        [float("inf"), 1, 5, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), -3, 0]
    ]
    start = 0
    end = 3
    distances, predecessors = bellman_ford_adjacency_matrix(start, graph)
    shortest_path = find_shortest_path(predecessors, start, end)

    print("Vertex       Distance from Source")
    for node in distances:
        print(f"{node}                    {distances[node]}")
    print()
    print(f"Shortest path from {start} to {end}: ", shortest_path)


test_bellman_ford()