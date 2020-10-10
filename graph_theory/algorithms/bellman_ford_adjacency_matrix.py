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
    for _ in range(len(graph) - 1):
        for node in range(len(graph)):
            for neighbor, weight in enumerate(graph[node]):
                if weight != 0:
                    new_distance = distances[node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = node

    # Final relaxation attempt to identify negative cycles
    for node in range(len(graph)):
        for neighbor, weight in enumerate(graph[node]):
            if weight != 0:
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:  # negative weight cycle found
                    distances[neighbor] = float("-inf")
                    predecessors.pop(neighbor)
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
