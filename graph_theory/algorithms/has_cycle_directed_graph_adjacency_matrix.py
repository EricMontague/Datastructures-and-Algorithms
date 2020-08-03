"""This module contains an algorithm to determine if there is a cycle in
a directed graph.
"""


from enum import Enum


class NodeState(Enum):
    """Class to represent the state of a node during a dfs
    traversal using graph coloring.
    """

    UNVISITED = 0  # never been visited
    VISITING = 1  # currently in dfs tree
    VISITED = 2  # not in dfs tree anymore


def has_cycle(adjacency_matrix):
    states = [NodeState.UNVISITED] * len(adjacency_matrix)
    for node in range(len(adjacency_matrix)):
        if states[node] == NodeState.UNVISITED:
            if has_back_edge(adjacency_matrix, states, node):
                return True
    return False


def has_back_edge(adjacency_matrix, states, node):
    states[node] = NodeState.VISITING
    for neighbor, value in enumerate(adjacency_matrix[node]):
        if value == 1:
            if states[neighbor] == NodeState.UNVISITED:
                if has_back_edge(adjacency_matrix, states, neighbor):
                    return True
            if states[neighbor] == NodeState.VISITING:
                return True
    states[node] = NodeState.VISITED
    return False

