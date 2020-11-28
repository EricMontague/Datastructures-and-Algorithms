"""This module contains my implementation of topological sort
of a graph represented as an adjacency list.
"""


class NodeState:
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


# assumes that the graph's edges don't have weights
def topological_sort(adjacency_list):
    node_states = [NodeState.UNVISITED for node in adjacency_list]
    sorted_nodes = []
    for node in adjacency_list:
        if node_states[node] == NodeState.UNVISITED:
            # if not dfs_recursive(adjacency_list, node_states, sorted_nodes, node):
            #     return []  # cycle detected in graph
            if not dfs_iterative(adjacency_list, node_states, sorted_nodes, node):
                return []  # cycle detected in graph
    sorted_nodes.reverse()
    return sorted_nodes


def dfs_recursive(adjacency_list, node_states, sorted_nodes, node):
    node_states[node] = NodeState.VISITING
    for neighbor in adjacency_list[node]:
        if node_states[neighbor] == NodeState.UNVISITED:
            if not dfs_recursive(adjacency_list, node_states, sorted_nodes, neighbor):
                return False
        elif node_states[neighbor] == NodeState.VISITING:
            return False  # cycle deteced
    sorted_nodes.append(node)
    node_states[node] = NodeState.VISITED
    return True


def dfs_iterative(adjacency_list, node_states, sorted_nodes, source):
    node_states[source] = NodeState.VISITING
    stack = [(source, NodeState.VISITING)]
    while stack:
        node, state = stack.pop()
        if state == NodeState.VISITED:
            sorted_nodes.append(node)
            node_states[node] = state
        else:
            stack.append((node, NodeState.VISITED))
            for neighbor in adjacency_list[node]:
                if node_states[neighbor] == NodeState.UNVISITED:
                    node_states[neighbor] = NodeState.VISITING
                    stack.append((neighbor, NodeState.VISITING))
                elif node_states[neighbor] == NodeState.VISITING:  # cycle deteced
                    return False
    return True


def run_topological_sort():
    graph = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
    expected = [5, 4, 2, 3, 1, 0]
    sorted_nodes = topological_sort(graph)
    print(expected == sorted_nodes)
    print(sorted_nodes)


run_topological_sort()
