"""This module contains an algorithm to determine if there is a cycle in
a directed graph.
"""


from enum import Enum


class NodeState(Enum):
    """Class to represent the state of a node during a dfs
    traversal using graph coloring.
    """
    UNVISITED = 0 # never been visited
    VISITING = 1 # currently in dfs tree
    VISITED = 2 # not in dfs tree anymore


def has_cycle(adjacency_list):
    states = [NodeState.UNVISITED] * len(adjacency_list)
    for node in adjacency_list:
        if states[node] == NodeState.UNVISITED:
            if has_back_edge(adjacency_list, states, node):
                return True
    return False


def has_back_edge(adjacency_list, states, node):
    states[node] = NodeState.VISITING
    for neighbor in adjacency_list[node]:
        if states[neighbor] == NodeState.UNVISITED:
            if has_back_edge(adjacency_list, states, neighbor):
                return True
        if states[neighbor] == NodeState.VISITING:
            return True
    states[node] = NodeState.VISITED
    return False
    

    