"""This module contains an implementation of depth first search
where the graph is represented as an adjacency matrix.
"""


def dfs(adjacency_matrix):
    visited = set()
    for node in range(len(adjacency_matrix)):
        if node not in visited:
            yield from dfs_visit(node, adjacency_matrix, visited)


def dfs_visit(node, adjacency_matrix, visited):
    visited.add(node)
    yield node
    for neighbor, value in enumerate(adjacency_matrix[node]):
        if value == 1 and neighbor not in visited:
            yield from dfs_visit(neighbor, adjacency_matrix, visited)


# iterative implementation of dfs_visit
# will produce a different ordering than the recursive version
def dfs_visit_iterative(node, adjacency_matrix, visited):
    visited.add(node)
    stack = [node]
    while stack:
        current_node = stack.pop()
        yield current_node
        for neighbor, value in enumerate(adjacency_matrix[current_node]):
            if value == 1 and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

