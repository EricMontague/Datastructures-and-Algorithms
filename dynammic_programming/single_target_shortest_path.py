"""This module contains an implementation of an algorithm
to find the shortest path from some starting vertex in a
graph to some other vertex in the graph.


time complexity: O(|V| + |E|), where 
Recurrence Relation
--------------------
sp(s, v) == 0, if s == v
sp(s, v) == min(sp(u, v)) + w(s, u), if s != v

- Here 's' is the source vertex, and 'v' the destination
vertex
- 'u' is a vertex that forms an outgoing edge with 's', meaning
that there is an edge from 's' to 'u'
- w(s, u) is the weight of said edge
- In plain English, this states, that the shortest path from
some source vertex 's' to some destination vertex 'v', is the shortest
of all of the paths from each neighboring vertex of 's' to 'v', plus the
weight of the edge formed by the vertex on that shortest path


"""

from collections import namedtuple


Vertex = namedtuple("Vertex", ["value", "weight"])

# Graph is assumed to be an adjacency list
def single_target_shortest_path(source, destination, graph):
    distances = {}
    compute_shortest_path(source, destination, graph, distances)
    return distances


def compute_shortest_path(source, destination, graph, distances):
    # Base case
    if source == destination:
        distances[source] = 0
    elif source in distances:
        return distances[source]
    else:
        # Recursive Case
        shortest_path_length = float("inf")
        for neighbor in graph[source]:
            path_length = compute_shortest_path(
                neighbor.value, destination, graph, distances
            )
            shortest_path_length = min(
                shortest_path_length, path_length + neighbor.weight
            )
        distances[source] = shortest_path_length
    return distances[source]


# informal test
def test_shortest_path():
    adjacency_list = {
        0: [Vertex(1, 1), Vertex(2, 2)],
        1: [Vertex(4, 2)],
        2: [Vertex(3, 3), Vertex(5, 6)],
        3: [Vertex(6, 5)],
        4: [Vertex(7, 7)],
        5: [Vertex(7, 10)],
        6: [Vertex(7, 1)],
        7: [],
    }
    source = 0
    destination = 7
    distances = single_target_shortest_path(
        source, destination, adjacency_list
    )
    print(
        f"Shortest path length from {source} to {destination}: {distances[source]}"
    )


test_shortest_path()

