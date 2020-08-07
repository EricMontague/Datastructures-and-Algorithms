"""This module contains algorithms for finding the shortest
distance to all nodes in a directed acyclic graph from a single source node.
"""


def single_source_shortest_paths(adjacency_matrix, source):
    distances = {node: float("inf") for node in range(len(adjacency_matrix))}
    if source not in distances:
        return None
    distances[source] = 0
    nodes = topological_sort(adjacency_matrix)
    source_found = False
    for node in nodes:
        if node == source:
            source_found = True
        if source_found:
            relax_edges(adjacency_matrix, node, distances)


def topological_sort(adjacency_matrix):
    visited = set()
    nodes = []
    for node in range(len(adjacency_matrix)):
        if node not in visited:
            dfs(adjacency_matrix, visited, node, nodes)
    nodes.reverse()
    return nodes


def dfs(adjacency_matrix, visited, node, nodes):
    visited.add(node)
    for neighbor, weight in enumerate(adjacency_matrix[node]):
        if weight != 0 and neighbor not in visited:
            dfs(adjacency_matrix, visited, neighbor, nodes)
    nodes.append(node)


def relax_edges(adjacency_matrix, node, distances):
    for neighbor, weight in enumerate(adjacency_matrix[node]):
        if weight != 0:
            new_distance = distances[node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

