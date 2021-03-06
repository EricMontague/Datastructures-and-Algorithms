"""This module contains my implementations of Dijkstra's algorithm
where the graph is represented as an adjacency matrix
"""


################
# Adjacency Matrix
################
# O(V^2) time complexity
def dijkstra_adjacency_matrix(source, graph):
    """Finds the shortest paths from some node in the graph to all other nodes.
    Returns a dictionary containing the shortest distances of
    all nodes from the source as well as another dictionary containing
    the predeccesor relationshops during the algorithm's exploration. 
    Assumes the graph is represented as an adjacency list
    """
    predecessors = {source: None}
    visited = set()
    distances, node_list = initialize_distances_and_node_list(source, graph)

    while len(visited) != len(graph):
        node = get_smallest_node_by_distance(visited, distances, node_list)
        visited.add(node)
        for neighbor, weight in enumerate(graph[node]):
            if weight != float("inf") and neighbor not in visited:
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = node
    return distances, predecessors


def initialize_distances_and_node_list(source, graph):
    distances = {}
    node_list = []
    for node in range(len(graph)):
        if node == source:
            initial_distance = 0
        else:
            initial_distance = float("inf")
        distances[node] = initial_distance
        node_list.append(node)
    return distances, node_list


def get_smallest_node_by_distance(visited, distances, node_list):
    """Return the node in the list that is the shortest distance
    from the source and has not yet been visited
    """
    smallest_node = None
    for node in node_list:
        if node not in visited:
            if smallest_node is None:
                smallest_node = node
            elif distances[node] < distances[smallest_node]:
                smallest_node = node
    return smallest_node


def find_shortest_path(predecessors, source, destination):
    """Given a dictionary of predeccesors that was constructed via
    a shortest paths algorithm, return the vertices in the shortest
    path from source to destination.
    """
    path = []
    # destination not reachable from source
    if destination not in predecessors:
        return path
    current_node = destination
    while current_node is not None:
        predecessor = predecessors[current_node]
        path.append(current_node)
        current_node = predecessor
    path.reverse()
    return path


# Informal tests. WIll create formal tests later

# Graph from
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/


def test_dijkstra_adjacency_matrix():
    # create graph - same as the adjacency list one
    graph = [
        [float("inf"), 4, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 8, float("inf")],
        [4, float("inf"), 8, float("inf"), float("inf"), float("inf"), float("inf"), 11, float("inf")],
        [float("inf"), 8, float("inf"), 7, float("inf"), 4, float("inf"), float("inf"), 2],
        [float("inf"), float("inf"), 7, float("inf"), 9, 14, float("inf"), float("inf"), float("inf")],
        [float("inf"), float("inf"), float("inf"), 9, float("inf"), 10, float("inf"), float("inf"), float("inf")],
        [float("inf"), float("inf"), 4, 14, 10, float("inf"), 2, float("inf"), float("inf")],
        [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2, float("inf"), 1, 6],
        [8, 11, float("inf"), float("inf"), float("inf"), float("inf"), 1, float("inf"), 7],
        [float("inf"), float("inf"), 2, float("inf"), float("inf"), float("inf"), 6, 7, float("inf")],
        [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],
    ]
    start = 0
    end = 5
    distances, predecessors = dijkstra_adjacency_matrix(start, graph)
    shortest_path = find_shortest_path(predecessors, start, end)
    print("Vertex       Distance from Source")
    for node in distances:
        print(f"{node}                    {distances[node]}")
    print()
    print(f"Shortest path from {start} to {end}: ", shortest_path)


test_dijkstra_adjacency_matrix()
