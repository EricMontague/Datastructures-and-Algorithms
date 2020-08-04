"""This module contains my implementation of topological sort
of a graph represented as an adjacency matrix.
"""


def topological_sort(adjacency_matrix):
    visited = set()
    nodes = []
    for node in range(len(adjacency_matrix)):
        if node not in visited:
            dfs(adjacency_matrix, visited, nodes, node)
    nodes.reverse()
    return nodes


def dfs(adjacency_matrix, visited, nodes, node):
    visited.add(node)
    for neighbor, value in enumerate(adjacency_matrix[node]):
        if value == 1 and neighbor not in visited:
            dfs(adjacency_matrix, visited, nodes, neighbor)
    nodes.append(node)

