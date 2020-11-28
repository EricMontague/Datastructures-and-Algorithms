"""This file contains an implementation of Kahn's algorithm
for creating a topologically sorted list of nodes in a graph.
The graph is assumed to be an adjacency matrix.
"""


from collections import deque

# time complexity: O(V ^ 2)
# space complexity: O(V)
def kahns_algorithm(graph):
    indegrees, num_edges = build_indegrees(graph)
    queue = build_queue(indegrees)
    return sort_nodes(indegrees, graph, queue, num_edges)


def build_indegrees(graph):
    num_edges = 0
    indegrees = [0 for node in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1:
                indegrees[neighbor] += 1
                num_edges += 1
    return indegrees, num_edges


def build_queue(indegrees):
    queue = deque([i for i in range(len(indegrees)) if indegrees[i] == 0])
    return queue


def sort_nodes(indegrees, graph, queue, num_edges):
    sorted_nodes = []
    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)
        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1:
                indegrees[neighbor] -= 1
                num_edges -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
    if num_edges > 0:
        return []  # cycle detected
    return sorted_nodes


# informal test
def run_kahns_algorithm():
    graph = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
    ]
    expected = [4, 5, 0, 2, 3, 1]
    sorted_nodes = kahns_algorithm(graph)
    print(expected == sorted_nodes)
    print(sorted_nodes)


run_kahns_algorithm()
