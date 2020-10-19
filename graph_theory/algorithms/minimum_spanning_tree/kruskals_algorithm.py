"""This file contains an implementatino of Kruskal's Minimum Spanning Tree Algorithm.
A minimum spanning tree is a subset of edges in the graph which connect all vertices (no cycles)
in the graph with the minimal total edge cost . This algorithm only applies to weighted,
undirected graphs

Algorithm Steps:

1. Sort edges by ascending edge weight

2. Walk through the sorted edge list and look at the two nodes the edge belongs to.
If the two nodes are already unified (in the minimum spanning tree) we don't include this edge.
Otherwise we add the edge to the minimum spanning tree by calling the UnionFind's union method,
which will unify the two sets that each node belongs to. You don't want to unify nodes that
are in the same set in the UnionFind, because that would create a cycle in the minimum spanning tree.


3. The algorithm terminates when every edge has been processed or all of the 
nodes have been unified
"""

import sys
import os
from pathlib import Path
import pprint


# takes care of this package not being in the PYTHON PATH
def setup_imports(levels_up=1):
    current_filepath = os.path.abspath(__file__)
    parent_directory = Path(current_filepath).parents[levels_up]

    if str(parent_directory) not in sys.path:
        sys.path.insert(0, str(parent_directory))


setup_imports(levels_up=3)

from collections import namedtuple
from pprint import pprint
from data_structures.union_find.union_find import UnionFind


Edge = namedtuple("Edge", ["vertex_one", "vertex_two", "weight"])


# time complexity (simple): O(ElogE), where 'E' is the number of edges in the graph

# time complexity (tighter bound): O(ElogV), where 'E' is the number of edges and 'V'
# is the number of vertices

# Explanation: In a dense graph, 'E' can be on the order of V^2, so the first time complexity
# can be expressed as ElogV^2. logV^2 can further be broken down to be 2logV. Then, after getting
# rid of the constant, we're left with logV. So finally, the time complexity becomes ElogV
def kruskals_algorithm(num_vertices, edge_list):

    # initialize UnionFind
    union_find = UnionFind(num_vertices)

    # Sort edges by ascending edge weight
    edge_list.sort(key=lambda e: e.weight)

    # final list of edges contained within the minimum spanning tree
    minimum_spanning_tree = []
    total_tree_weight = 0

    # Walk through list of edges unifying nodes which don't belong to the same set
    # within the union find
    for edge in edge_list:
        if union_find.find(edge.vertex_one) != union_find.find(edge.vertex_two):
            minimum_spanning_tree.append(edge)
            total_tree_weight += edge.weight
            union_find.union(edge.vertex_one, edge.vertex_two)
        # you can terminate early if there is only one set left in the union find
        if union_find.get_num_components() == 1:
            break

    #  The graph contains multiple connected components and thus we cannot find a minimum spanning tree
    if union_find.get_num_components() > 1:
        return [], 0
    return minimum_spanning_tree, total_tree_weight


# Informal test
# graph taken from here: https://www.youtube.com/watch?v=JZBQLXgSGfs
# Vertex 0 is A, vertex 1 is B, vertex 2 is C and so on
def test_kruskals_algorithm():
    num_vertices = 10
    # An edge from 0 -> 1 also means that there is an edge from 1 -> 0
    edge_list = [
        Edge(0, 1, 5),
        Edge(1, 3, 4),
        Edge(0, 4, 1),
        Edge(1, 2, 4),
        Edge(1, 3, 2),
        Edge(2, 7, 4),
        Edge(2, 9, 2),
        Edge(2, 8, 1),
        Edge(3, 4, 2),
        Edge(3, 7, 2),
        Edge(3, 5, 5),
        Edge(3, 6, 11),
        Edge(4, 5, 1),
        Edge(5, 6, 7),
        Edge(6, 7, 1),
        Edge(6, 8, 4),
        Edge(7, 8, 6),
        Edge(8, 9, 0),
    ]
    minimum_spanning_tree, total_tree_weight = kruskals_algorithm(
        num_vertices, edge_list
    )
    print(f"Total Minimum Spanning Tree Weight: {total_tree_weight}\n")
    pprint(minimum_spanning_tree)


test_kruskals_algorithm()
