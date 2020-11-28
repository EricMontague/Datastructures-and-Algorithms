"""This file contains an implementation of Kahn's algorithm
for creating a topologically sorted list of nodes in a graph.
The graph is assumed to be an adjacency list.
"""


from collections import deque


# time complexity: O(V + E)
# space complexity: O(V)
def kahns_algorithm(graph):
    indegrees, num_edges = build_indegrees(graph)
    queue = build_queue(indegrees)
    return sort_nodes(queue, indegrees, graph, num_edges)


def build_indegrees(graph):
    num_edges = 0
    indegrees = [0 for node in range(len(graph))]
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1
            num_edges += 1
    return indegrees, num_edges


def build_queue(indegrees):
    queue = deque([i for i in range(len(indegrees)) if indegrees[i] == 0])
    return queue


def sort_nodes(queue, indegrees, graph, num_edges):
    sorted_nodes = []
    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            num_edges -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    if num_edges > 0:  # cycle deteced
        return []
    return sorted_nodes


def run_kahns_algorithm():
    graph = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
    expected = [4, 5, 0, 2, 3, 1]
    sorted_nodes = kahns_algorithm(graph)
    print(expected == sorted_nodes)
    print(sorted_nodes)


run_kahns_algorithm()
