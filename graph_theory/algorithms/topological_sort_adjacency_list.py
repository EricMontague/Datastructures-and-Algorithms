"""This module contains my implementation of topological sort
of a graph represented as an adjacency list.
"""


def topological_sort(adjacency_list):
    visited = set()
    nodes = []
    for node in adjacency_list:
        if node not in visited:
            dfs(adjacency_list, visited, nodes, node)
    nodes.reverse()
    return nodes


def dfs(adjacency_list, visited, nodes, node):
    visited.add(node)
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            dfs(adjacency_list, visited, nodes, node)
    nodes.append(node)

