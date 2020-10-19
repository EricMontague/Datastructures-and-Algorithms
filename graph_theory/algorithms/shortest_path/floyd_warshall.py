"""This module contains an implementation of the Floyd-Warshal algorithm.
This algorithm finds the shortest path between all pairs of vertices in
a graph even if the graph has negative edges. It also has the ability
to report negative-weight cycles.
"""


def floyd_warshall(graph):
    num_nodes = len(graph)
    # distances is used for memoization during the algorithm
    # next_ is used to reconstruct shortest paths after the algorithm runs
    # next_[source][destination] is the next node in the shortest path from
    # the source to the destination node
    distances, next_ = initialize_distances_and_next_tables(graph, num_nodes)

    # find all pairs shortest paths
    for intermediary in range(num_nodes):
        for source in range(num_nodes):
            for destination in range(num_nodes):
                new_distance = (
                    distances[source][intermediary]
                    + distances[intermediary][destination]
                )
                if new_distance < distances[source][destination]:
                    distances[source][destination] = new_distance
                    next_[source][destination] = next_[source][intermediary]

    # final relaxtion attempt to identify negative cycles
    detect_negative_cycles(distances, next_, num_nodes)
    return distances, next_


def initialize_distances_and_next_tables(graph, num_nodes):
    """Create distances and next tables."""
    distances = []
    next_ = []
    for source in range(num_nodes):
        distances_row = []
        next_row = []
        for destination in range(num_nodes):
            distances_row.append(graph[source][destination])
            if graph[source][destination] != float("inf"):
                next_row.append(destination)
            else:
                next_row.append(None)
        distances.append(distances_row)
        next_.append(next_row)
    return distances, next_


def detect_negative_cycles(distances, next_, num_nodes):
    """Run Floyd-Warshall one more time in an attempt to find negative
    weight cycles. If you can relax an edge one more time, this means that
    it is a part of a negative weight cycle and you cannot reliably determine
    the shortest path from the source node to the destination node
    """
    for intermediary in range(num_nodes):
        for source in range(num_nodes):
            for destination in range(num_nodes):
                new_distance = (
                    distances[source][intermediary]
                    + distances[intermediary][destination]
                )
                if (
                    new_distance < distances[source][destination]
                ):  # negative weight cycle found
                    distances[source][destination] = float("-inf")
                    next_[source][destination] = -1


def find_shortest_path(next_, source, destination):
    """Given a matrix next_, where next_[source][destination] represents the 
    next node along the shortest path from source to destination
    return the shortest path from the destination vertex
    to the source.
    """
    path = []
    # The destination node is not reachable from the source node at all
    if next_[source][destination] is None:
        return path
    current_node = source
    while current_node != destination:
        path.append(current_node)
        next_node = next_[current_node][destination]
        # No next node along the path. Negative cycle was detected
        if next_node == -1:
            return None
        current_node = next_node

    # one last check for a negative self-cycle from the destination node to itself
    if next_[current_node][destination] == -1:
        return None
    path.append(destination)
    return path


def test_floyd_warshal():
    graph = [
        [0, -1, 4, float("inf"), float("inf")],
        [float("inf"), 0, 3, 2, 2],
        [float("inf"), float("inf"), 0, float("inf"), float("inf")],
        [float("inf"), 1, 5, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), -3, 0],
    ]

    distances, next_ = floyd_warshall(graph)

    print(distances)

    source = 0
    destination = 3
    path = find_shortest_path(next_, source, destination)
    print()
    print(f"Shortest path from {source} to {destination}: ")
    print(path)


test_floyd_warshal()

