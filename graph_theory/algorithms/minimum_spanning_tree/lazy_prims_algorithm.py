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
from pprint import pprint
from collections import namedtuple


class Edge:
    """Class to represent an edge in a graph."""

    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return "Edge(source=%r, desintation=%r, cost=%r)" % (
            self.source,
            self.destination,
            self.cost,
        )

    def __lt__(self, other_edge):
        return self.cost < other_edge.cost


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


# Informal test
# graph taken from here: https://www.youtube.com/watch?v=JZBQLXgSGfs
# Vertex 0 is A, vertex 1 is B, vertex 2 is C and so on
def test_lazy_prims_algorithm():
    source = 7
    graph = {
        0: [Node(1, 5), Node(4, 1)],
        1: [Node(0, 5), Node(3, 4), Node(2, 4), Node(3, 2),],
        3: [Node(1, 4), Node(1, 2), Node(4, 2), Node(7, 2), Node(5, 5), Node(6, 11),],
        4: [Node(0, 1), Node(3, 2), Node(5, 1)],
        2: [Node(1, 4), Node(7, 4), Node(9, 2), Node(8, 1),],
        7: [Node(2, 4), Node(3, 2), Node(6, 1), Node(8, 6),],
        9: [Node(2, 2), Node(8, 0)],
        8: [Node(2, 1), Node(6, 4), Node(7, 6), Node(9, 0),],
        5: [Node(3, 5), Node(4, 1), Node(6, 7)],
        6: [Node(3, 11), Node(5, 7), Node(7, 1), Node(8, 4),],
    }

    minimum_spanning_tree, total_tree_cost = lazy_prims_algorithm(source, graph)
    print(f"Minimum Spanning Tree Cost: {total_tree_cost}\n")
    pprint(minimum_spanning_tree)


test_lazy_prims_algorithm()

