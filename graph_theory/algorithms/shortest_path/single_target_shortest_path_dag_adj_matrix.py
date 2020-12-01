"""This module contains algorithms for finding the shortest
distance between two nodes in a wegithed, directed acyclic graph that
is represented as an adjacency matrix.
"""


from collections import deque


def single_target_shortest_path(adjacency_matrix, source, destination):
    if source == destination:
        return [], float("inf")
    sorted_nodes = topological_sort(adjacency_matrix)
    distances = {node: float("inf") for node in range(len(adjacency_matrix))}
    distances[source] = 0
    parents = {source: None}
    
    source_index = 0
    while sorted_nodes[source_index] != source:
        if sorted_nodes[source_index] == destination:
            return [], float("inf")
        source_index += 1
    
    for index in range(source_index, len(sorted_nodes)):
        node = sorted_nodes[index]
        if node == destination:
            return (
                build_shortest_path(source, destination, parents),
                distances[destination]
            )   
        relax_edges(node, adjacency_matrix, distances, parents)


def topological_sort(adjacency_matrix):
    indegrees = get_node_indegrees(adjacency_matrix)
    queue = build_queue(indegrees)
    return sort_nodes(adjacency_matrix, indegrees, queue)


def get_node_indegrees(adjacency_matrix):
    indegrees = [0 for node in range(len(adjacency_matrix))]
    for node in range(len(adjacency_matrix)):
        for neighbor in range(len(adjacency_matrix)):
            if adjacency_matrix[node][neighbor] != float("inf"):
                indegrees[neighbor] += 1
    return indegrees


def build_queue(indegrees):
    queue = deque()
    for index in range(len(indegrees)):
        if indegrees[index] == 0:
            queue.append(index)
    return queue


def sort_nodes(adjacency_matrix, indegrees, queue):
    sorted_nodes = []
    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)
        for neighbor in range(len(adjacency_matrix)):
            if adjacency_matrix[node][neighbor] != float("inf"):
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
    return sorted_nodes


def relax_edges(adjacency_matrix, node, distances, parents):
    for neighbor in range(len(adjacency_matrix)):
        if adjacency_matrix[node][neighbor] != float("inf"):
            new_distance = distances[node] + adjacency_matrix[node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = node


def build_shortest_path(source, destination, parents):
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path

