"""This module contains algorithms for finding the shortest
distance between two nodes in a wegithed, directed acyclic graph that
is represented as an adjacency list.
"""


from collections import namedtuple


Node = namedtuple("Node", ["value", "weight"])


def single_target_shortest_path(adjacency_list, source, destination):
    # Handle edge case
    if source == destination:
        return [], float("inf")

    # Get topological ordering of nodes
    sorted_nodes = topological_sort(adjacency_list)

    # initialize distances and predecessors dictionaries
    distances = {node: float("inf") for node in adjacency_list}
    distances[source] = 0
    predecessors = {source: None}

    # Optimization - Find the index of the source node in the list
    # so we can start relaxing edges from there. All nodes before this
    # index will be unreachable from the source, so if we encounter
    # the destination node before the source, we can return early
    source_index = 0
    while sorted_nodes[source_index] != source:
        if sorted_nodes[source_index] == destination:
            return [], float("inf")
        source_index += 1

    for index in range(source_index, len(sorted_nodes)):
        node = sorted_nodes[index]
        if node == destination:
            return (
                build_shortest_path(source, destination, predecessors),
                distances[destination],
            )
        relax_edges(adjacency_list, node, distances, predecessors)


def topological_sort(adjacency_list):
    visited = set()
    sorted_nodes = []
    for node in adjacency_list:
        if node not in visited:
            dfs(adjacency_list, visited, node, sorted_nodes)
    sorted_nodes.reverse()
    return sorted_nodes


def dfs(adjacency_list, visited, node, sorted_nodes):
    visited.add(node)
    for neighbor in adjacency_list[node]:
        if neighbor.value not in visited:
            dfs(adjacency_list, visited, neighbor.value, sorted_nodes)
    sorted_nodes.append(node)


def relax_edges(adjacency_list, node, distances, predecessors):
    for neighbor in adjacency_list[node]:
        new_distance = distances[node] + neighbor.weight
        if new_distance < distances[neighbor.value]:
            distances[neighbor.value] = new_distance
            predecessors[neighbor.value] = node


def build_shortest_path(source, destination, predecessors):
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path

