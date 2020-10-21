"""This module contains my implementation of Kosaraju's algorithm for finding
strongly connected components in directed graphs.

A strongly connected component is a self-contained cycle within a directed graph
where all nodes in that cycle are reachable from each other. Each SCC is unique,
and a node can only belong to one SCC.

Intuition:
The algorithm can be understood as identifying the SCC that a vertex 'u' belongs to
as the set of vertices which are reachable from 'u' both by backwards and forwards traversal.
(Wikipedia)

Steps:

Step 1 - Perform a depth-first search traversal (postorder) from every node in the graph, being sure
to only visit each node exactly once. After you have visited all paths from a given node,
push that node to the top of a stack. After the DFS is finished, the nodes in the stack will
be ordered by their finishing times. The nodes on the bottom will have finished first, and the ones
on the top will have finished last (essentially in reverse topological order).

Step 2 - Reverse all edges in the graph

Step 3 - Perform a second DFS traversal, this time using the stack you created as the source from
which to pull the nodes, being sure to visit each node exactly once. All nodes that you visit during
a given traversal will belong to the same SCC.
"""



# time complexity: O(V + E), where 'V' is the number of vertices and 'E' is the number of edges
# space complexity: O(V + E)

# the graph is assumed to be an adjacency list
def kosarajus_algorithm(graph):
    # Perform a postorder traversal of the graph and return a list of nodes that are reverse
    # ordered by their finishing times (essentially a reversed topological sort)
    stack = postorder_traversal(graph)

    # Return a new graph with all of the edges reversed
    reversed_graph = reverse_edges(graph)

    # Perform a second DFS traversal, and label each node along the traversal with the
    # root of its SCC. You could also return a 2D list where each list contains all of the nodes
    # in the same SCC
    visited = set()

    # Each index represents a node, and the value at the index is the root of the SCC
    strongly_connected_components = [None] * len(reversed_graph)
    while stack:
        node = stack.pop()
        if node not in visited:
            root = node 
            find_strongly_connected_components(
                node, 
                root, 
                reversed_graph, 
                visited, 
                strongly_connected_components
            )

    return strongly_connected_components


def postorder_traversal(graph):
    """Perform a postorder traversal on the graph and return a list of
    nodes in reverse topological order.
    """
    visited = set()
    stack = []
    for node in range(len(graph)):
        if node not in visited:
            _postorder_traversal(node, graph, visited, stack)
    return stack


def _postorder_traversal(current_node, graph, visited, stack):
    """Perform a postorder traversal on a graph, being sure to add each
    node to a stack after you traversed all paths in the graph from that node.
    """
    # Mark node as visited
    visited.add(current_node)
    for neighbor in graph[current_node]:
        # Check if neighbor has been visited
        if neighbor not in visited:
            _postorder_traversal(neighbor, graph, visited, stack)
    # Append node to end of list after its DFS has finished
    stack.append(current_node)


def reverse_edges(graph):
    """Return a new graph with all of its edges reversed. 
    It is assumed that the graph is represented as an adjacency list.
    """
    reversed_graph = {}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in reversed_graph:
                reversed_graph[neighbor] = []
            reversed_graph[neighbor].append(node)
    return reversed_graph

def find_strongly_connected_components(
    current_node, 
    root, 
    graph, 
    visited, 
    strongly_connected_components
):
    # Mark node as visited
    visited.add(current_node)

    # Mark node as a part of this SCC, identified by root
    strongly_connected_components[current_node] = root
    for neighbor in graph[current_node]:
        # Check if neighbor has been visited
        if neighbor not in visited:
            find_strongly_connected_components(
                neighbor,
                root,
                graph,
                visited,
                strongly_connected_components
            )

# Test case taken from here https://www.youtube.com/watch?v=wUgWX0nc4NY
# with some additional vertices added
def test_kosarajus_algorithm():
    graph = {
        0: [1],
        1: [2],
        2: [0],
        3: [4, 7],
        4: [5],
        5: [0, 6],
        6: [2, 0, 4],
        7: [5, 3],
        8: [9],
        9: [10],
        10: [8],
    }
    strongly_connected_components = kosarajus_algorithm(graph)
    for node in range(len(strongly_connected_components)):
        print(f"Node: {node} in component {strongly_connected_components[node]}")


test_kosarajus_algorithm()

