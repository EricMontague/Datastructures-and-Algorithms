"""This module contains one way of finding all nodes that are in the shortest
path between two given nodes in an UNWEIGHTED graph.
"""

# Problem Statement:
# Given an UNWEIGHTED graph, and two vertices within that graph,
# return a list containing all of the vertices in the path from
# the source vertex to the destination vertex.
# Assume that the graph is a valid graph and that source and destionation are positive
# integers, but there is no  guarantee that both vertices are in the graph


from collections import deque

# adjacency matrix implementation
def find_shortest_path_adj_matrix(adjacency_matrix, source, destination):
    num_nodes = len(adjacency_matrix)
    if source < 0 or source >= num_nodes or destination < 0 or destination >= num_nodes:
        return []
    predecessor = {source: None}
    queue = deque()
    queue.append(source)
    found = False
    while queue and not found:
        node = queue.popleft()
        for neighbor, value in enumerate(adjacency_matrix[node]):
            if value == 1 and neighbor not in predecessor:
                if neighbor == destination:
                    predecessor[neighbor] = node
                    found = True
                    break
                else:
                    queue.append(neighbor)
                    predecessor[neighbor] = node
    return build_shortest_path(destination, predecessor)


# adjacency list implementation
def find_shortest_path_adj_list(adjacency_list, source, destination):
    if source not in adjacency_list or destination not in adjacency_list:
        return []
    predecessor = {source: None}
    queue = deque()
    queue.append(source)
    found = False
    while queue and not found:
        node = queue.popleft()
        for neighbor in adjacency_list[node]:
            if neighbor not in predecessor:
                if neighbor == destination:
                    predecessor[neighbor] = node
                    found = True
                    break
                else:
                    queue.append(neighbor)
                    predecessor[neighbor] = node
    return build_shortest_path(destination, predecessor)


def build_shortest_path(destination, predecessor):
    path = []
    current_node = destination
    while current_node is not None:
        path.append(current_node)
        current_node = predecessor[current_node]
    path.reverse()
    return path

