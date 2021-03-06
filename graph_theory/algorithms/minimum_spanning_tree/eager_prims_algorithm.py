"""This module contains an implementation of the eager version of Prim's 
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
from collections import namedtuple, defaultdict


Edge = namedtuple("Edge", ["vertex_one", "vertex_two", "cost"])
Node = namedtuple("Node", ["value", "cost"])


# time complexity: O(VlogV + ElogV) = O(ElogV), where 'E' is the number of edges
# and 'V' is the number of vertices

# graph is assumed to be an adjacency list
def eager_prims_algorithm(source, graph):
    # The number of edges in a tree should equal V - 1
    num_edges = len(graph) - 1

    # Track the edges in the MST along with there total cost
    total_tree_cost = 0
    minimum_spanning_tree = []

    # Keep a set to tell which nodes are already in the MST
    visited = set()

    # Map nodes to their cheapest incoming edges
    node_edge_mapping = {}

    # Priority Queue based on a min heap that sorts nodes by the cost of their
    # cheapest incoming edge
    priority_queue = []

    # Initialize priority queue with the adjacenct nodes from the source
    relax_edges(graph, source, visited, priority_queue, node_edge_mapping)

    # process nodes
    while priority_queue and len(minimum_spanning_tree) != num_edges:
        edge_cost, destination_node = heapq.heappop(priority_queue)

        # Need this extra check since python doesn't have a built-in Indexed Priority Queue
        # The workaround is to simply insert duplicate nodes into the priority queue and then check
        # for the duplicates after they're removed from the PQ
        if destination_node in visited:
            continue

        # Add edge to MST and update MST total cost
        minimum_spanning_tree.append(node_edge_mapping[destination_node])
        total_tree_cost += edge_cost

        # Relax outgoing edges from the node removed from the PQ
        relax_edges(graph, destination_node, visited, priority_queue, node_edge_mapping)

    # A tree should have V - 1 edges. If the MST doesn't have V - 1 edges,
    # then you know that you can't build an MST because the graph isn't connected
    if len(minimum_spanning_tree) != num_edges:
        return [], 0
    return minimum_spanning_tree, total_tree_cost


def relax_edges(graph, source, visited, priority_queue, node_edge_mapping):
    """Add adjacenct nodes from the given source node to the priority queue if
    they are not yet in the minimum spanning tree. If an adjacenct node is already
    in the priority queue, relax the edge and update the node-to-edge mapping
    if a cheaper connection to that node is found.
    """
    visited.add(source)
    for neighbor in graph[source]:
        # Check if node is already in the MST
        if neighbor.value not in visited:
            # An incoming edge to this node doesn't exist in the PQ
            if neighbor.value not in node_edge_mapping:
                node_edge_mapping[neighbor.value] = Edge(
                    source, neighbor.value, neighbor.cost
                )
                heapq.heappush(priority_queue, (neighbor.cost, neighbor.value))
            # Attempt to relax the incoming edge since another incoming edge is already in the PQ
            elif neighbor.cost < node_edge_mapping[neighbor.value].cost:
                node_edge_mapping[neighbor.value] = Edge(
                    source, neighbor.value, neighbor.cost
                )
                heapq.heappush(priority_queue, (neighbor.cost, neighbor.value))


# Informal test
# graph taken from here: https://www.youtube.com/watch?v=JZBQLXgSGfs
# Vertex 0 is A, vertex 1 is B, vertex 2 is C and so on
def test_eager_prims_algorithm():
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
        6: [Node(3, 11), Node(5, 7), Node(7, 1), Node(8, 4),]
    }

    minimum_spanning_tree, total_tree_cost = eager_prims_algorithm(source, graph)
    print(f"Minimum Spanning Tree Cost: {total_tree_cost}\n")
    pprint(minimum_spanning_tree)


test_eager_prims_algorithm()

