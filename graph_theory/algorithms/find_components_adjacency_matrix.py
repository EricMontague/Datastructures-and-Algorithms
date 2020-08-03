"""This module contains an algorithm to find the different
components in a graph represented as an adjacency matrix.
"""


def find_components(adjacency_matrix):
    visited = set()
    components = []
    for node in range(len(adjacency_matrix)):
        if node not in visited:
            component = []
            build_component(adjacency_matrix, visited, node, component)
            components.append(component)
    return components


def build_component(adjacency_matrix, visited, node, component):
    visited.add(node)
    component.append(node)
    for neighbor, value in enumerate(adjacency_matrix[node]):
        if value == 1 and neighbor not in visited:
            build_component(adjacency_matrix, visited, neighbor, component)

