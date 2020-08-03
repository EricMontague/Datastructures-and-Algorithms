"""This module contains an algorithm to find the different
components in a graph represented as an adjacency list.
"""


def find_components(adjacency_list):
    visited = set()
    components = []
    for node in adjacency_list:
        if node not in visited:
            component = []
            build_component(adjacency_list, visited, node, component)
            components.append(component)
    return components


def build_component(adjacency_list, visited, node, component):
    visited.add(node)
    component.append(node)
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            build_component(adjacency_list, visited, neighbor, component)


adj_list = {0: [1], 1: [], 2: [3], 3: [], 4: [5], 5: [6], 6: []}

print(find_components(adj_list))
