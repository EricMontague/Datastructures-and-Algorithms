"""This module contains an implementation of depth first search
where the graph is represented as an adjacency list.
"""


# assumes all inputs are valid and that
# the values in the adjacency list are python lists
def dfs(adjacency_list, source):
    visited = {}
    for node in adjacency_list.keys():
        if node not in visited:
            dfs_visit(node, adjacency_list, visited)


def dfs_visit(node, adjacency_list, visited):
    visited.add(node)
    yield node
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            dfs_visit(neighbor, adjacency_list, visited)


def dfs_visit_iterative(node, adjacency_list, visited):
    visited.add(node)
    stack = [node]
    while stack:
        current_node = stack.pop()
        yield node
        for neighbor in adjacency_list[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

