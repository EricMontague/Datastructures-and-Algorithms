"""This module contains an implementation of the lazy version of Prim's 
Minimum Spanning Tree algorithm. 

MST Definition - A minimum spanning tree is a set of edges
in a weighted, undirected graph that contains all vertices in the graph (no cycles),
and where the total cost of all edges is minimal.

High level description of Prim's algorithm - The algorithm works by building the MST
one vertex at a time from an arbitrary starting vertex. At each step, the algorithm adds 
the cheapest possible connection from the tree to another vertex

"""

import heapq
from collections import namedtuple


class Edge:
    """Class to represent an edge in a graph."""

    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __lt__(self, other_edge):
        return self.cost < other_edge


# Edge = namedtuple("Edge", ["source", "destination", "cost"])
Node = namedtuple("Node", ["value", "cost"])


# time complexity: O(ElogE), where 'E' is the number of edges
# and 'V' is the number of vertices

# space complexity: O(E)
# graph is assumed to be an adjacency list
def lazy_prims_algorithm(source, graph):
    # An MST should have V - 1 edges
    num_edges = len(graph) - 1

    # Track the edges in the MST as well as its total cost
    total_tree_cost = 0
    minimum_spanning_tree = []

    # track which nodes are already in the MST
    visited = set()

    # Priority queue which contains edges not yet in the MST
    priority_queue = []

    # Add initial set of edges to PQ
    add_edges(source, graph, priority_queue, visited)

    # Process edges while PQ is not empty and the MST is not fully formed
    while priority_queue and len(minimum_spanning_tree) != num_edges:
        edge = heapq.heappop(priority_queue)

        # Check for stale edges that connect to nodes already in the MST
        if edge.destination in visited:
            continue

        # Add edge to MST and increment total cost
        minimum_spanning_tree.append(edge)
        total_tree_cost += edge.cost

        # Add outgoing edges from edge.destionation to the PQ
        add_edges(edge.destination, graph, priority_queue, visited)

    # If the tree does not have V - 1 edges, then a MST for this graph cannot be formed
    # because we cannot reach all nodes in the graph
    if len(minimum_spanning_tree) != num_edges:
        return [], 0
    return minimum_spanning_tree, total_tree_cost


def add_edges(source, graph, priority_queue, visited):
    """Add all outgoing edges from the given source node to
    the priority queue if the node on the other end of the edge
    is not yet in the minimum spanning tree.
    """
    visited.add(source)
    for neighbor in graph[source]:
        # Check if neighbor in MST
        if neighbor.value not in visited:
            heapq.heappush(priority_queue, Edge(source, neighbor.value, neighbor.cost))


def test_lazy_prims_algorithm():
    pass

