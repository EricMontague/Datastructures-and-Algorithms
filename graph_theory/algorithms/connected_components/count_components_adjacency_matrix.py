"""This module contains algorithms for counting the
number of components in a graph represented as an adjacency
matrix.
"""


from data_structures.union_find.union_find import UnionFind


def count_components(adjacency_matrix):
    visited = set()
    components = 0
    for node in range(len(adjacency_matrix)):
        if node not in visited:
            components += 1
            dfs(adjacency_matrix, visited, node)
    return components


def dfs(adjacency_matrix, visited, node):
    visited.add(node)
    for neighbor, value in enumerate(adjacency_matrix[node]):
        if value == 1 and neighbor not in visited:
            dfs(adjacency_matrix, visited, neighbor)


def count_components_union_find(adjacency_matrix):
    if not adjacency_matrix:
        return 0
    num_nodes = len(adjacency_matrix)
    union_find = UnionFind(num_nodes)
    for row_index, row in enumerate(adjacency_matrix):
        for col_index, col_value in enumerate(row):
            if col_value == 1:
                union_find.union(row_index, col_index)
    return union_find.num_components

