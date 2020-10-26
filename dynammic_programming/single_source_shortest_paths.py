"""This file contains an algorithm for computing single source shortest paths
using dynamic programming.


- This algorithm runs in O(|V| + |E|) for DAGs, but is infinite for
graphs with cycles
- This algorithm (memoized) is essentially doing a DFS, to do a topological sort, to
perform one round of the Belmman-Ford single source shortest paths algorithm
- The second line of the reccurrence relation looks just like the relaxation step
in a generic single source shortest paths problem

Recurrence Relation
--------------------
sp(s ,v) = 0, if s == v
sp(s, v) = min(sp(s, u)) + w(u, v), if s != v

- 's' is the source vertex, 'v' is the destination vertex,
'u' is some vertex on the shortest path from the source to the destination,
and w(u, v) is the weight of the edge from vertex 'u' to vertex 'v'
- In plain Enlish, this says: "The shortest path from some vertex 's', to
another vertex 'v' is the minimum of the shortest path from 's' to another vertex
'u', plus the weight of the edge from 'u' to 'v'

"""

from collections import namedtuple


Node = namedtuple("Node", ["value", "weight"])


# graph is given as an adjacency list
# Returns the lengths of the shortest path from some source vertex
# to all other vertices in the graph
def single_source_shortest_paths(source, graph):
    memo = [float("inf") for vertex in len(graph)]
    inverted_adjacency_list = invert_adjacency_list(graph)
    for vertex in range(len(graph)):
        compute_shortest_paths(source, vertex, inverted_adjacency_list, memo)
    return memo


def invert_adjacency_list(adjacency_list):
    invert_adjacency_list = {}
    for vertex in adjacency_list:
        for neighbor in adjacency_list[vertex]:
            if neighbor not in invert_adjacency_list:
                invert_adjacency_list[neighbor.value] = []
            invert_adjacency_list[neighbor.value].append(Node(vertex, neighbor.weight))
    return invert_adjacency_list


def compute_shortest_paths(source, destination, inverted_adjacency_list, memo):
    if memo[destination] != float("inf"):
        return memo[destination]
    if source == destination:
        shortest_path_cost = 0
    else:
        shortest_path_cost = float("inf")
        for neighbor in inverted_adjacency_list[source]:
            path_cost = compute_shortest_paths(
                source, neighbor.value, invert_adjacency_list, memo
            )
            shortest_path_cost = min(shortest_path_cost, path_cost + neighbor.weight)
    memo[destination] = shortest_path_cost
    return shortest_path_cost
