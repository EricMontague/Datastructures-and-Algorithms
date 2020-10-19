"""This module contains an implementation of depth first search
where the graph is represented as an adjacency list.
"""


# assumes all inputs are valid and that
# the values in the adjacency list are python lists
def dfs(adjacency_list):
    visited = set()
    for node in adjacency_list:
        if node not in visited:
            yield from dfs_visit(node, adjacency_list, visited)


def dfs_visit(node, adjacency_list, visited):
    visited.add(node)
    yield node
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            yield from dfs_visit(neighbor, adjacency_list, visited)


# iterative implementation of dfs_visit
# will produce a different ordering than the recursive version
def dfs_visit_iterative(node, adjacency_list, visited):
    visited.add(node)
    stack = [node]
    while stack:
        current_node = stack.pop()
        yield current_node
        for neighbor in adjacency_list[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

