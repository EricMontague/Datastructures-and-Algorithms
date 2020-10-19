"""This module contains algorithms for counting the
number of components in a graph represented as an adjacency
list.
"""


from data_structures.union_find.union_find import UnionFind


def count_components(adjacency_list):
    visited = set()
    components = 0
    for node in adjacency_list:
        if node not in visited:
            components += 1
            dfs(adjacency_list, visited, node)
    return components


def dfs(adjacency_list, visited, node):
    visited.add(node)
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            dfs(adjacency_list, visited, neighbor)


def count_components_union_find(adjacency_list):
    if not adjacency_list:
        return 0
    union_find = UnionFind(len(adjacency_list))
    for node in adjacency_list:
        for neighbor in adjacency_list[node]:
            union_find.union(node, neighbor)
    return union_find.num_components

