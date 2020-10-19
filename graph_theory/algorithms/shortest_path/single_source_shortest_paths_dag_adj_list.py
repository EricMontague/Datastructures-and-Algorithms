"""This module contains algorithms for finding the shortest
distance to all nodes in a directed acyclic graph from a single source node.
"""


def single_source_shortest_paths(adjacency_list, source):
    if source not in adjacency_list:
        return None
    distances = {node: float("inf") for node in adjacency_list}
    distances[source] = 0
    nodes = topological_sort(adjacency_list)
    source_found = False
    for node in nodes:
        if node == source:
            source_found = True
        if source_found:
            relax_edges(adjacency_list, node, distances)
    return distances


def topological_sort(adjacency_list):
    visited = set()
    nodes = []
    for node in adjacency_list:
        if node not in visited:
            dfs(adjacency_list, visited, node, nodes)
    nodes.reverse()
    return nodes


def dfs(adjacency_list, visited, node, nodes):
    visited.add(node)
    for neighbor, weight in adjacency_list[node]:
        if neighbor not in visited:
            dfs(adjacency_list, visited, neighbor, nodes)
    nodes.append(node)


def relax_edges(adjacency_list, node, distances):
    for neighbor, weight in adjacency_list[node]:
        new_distance = distances[node] + weight
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance

