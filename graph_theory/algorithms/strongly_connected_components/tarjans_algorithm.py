"""This module contains my implementation of Tarjan's Strongly Connected 
Components algorithm.

A directed graph is strongly connected if you can reach each vertex in the 
graph from all other vertices in the graph. The strongly connected components
of a directed graph form a partition into subgraphs that themselves are strongly 
connected (Wikipedia).

Another way to think of this is that SCCs are self-contained cycles within a directed 
graph where every vertex in a given cycle can reach every other vertex in the same cycle.
For each SCC in a directed graph, there is no way to find a path that leaves the component 
and comes back. Because of this property, we can be sure that each SCC is unique

Concepts for this algorithm:
Low link value: The low-link value of a node is the smallest node id reachable from that 
node when doing a DFS (including itself)


Overview:

Step 1: Mark the id of each node as unvisited

Step 2: Start DFS. Upon visiting a node, assign it an id and a low-link value and
mark it as visited and add it to the 'seen' stack

Step 3: On DFS callback, if the previous node is on the stack then min the current node's 
low-link value with the last node's low-link value. This allows low-link values to 
propagate throughout cycles

Step 4: After visiting all neighbors, if the current node started a connected component, then
pop nodes off of the stack that are in that component. You know that a node started a 
connected component if it's id equals its low link value
"""

_UNVISITED = -1

# the graph is assumed to be an adjacency list
def tarjans_algorithm(source, graph):

    # Used to assign ids and intial low link values to nodes
    node_id = 0

    # Initialize node ids and low link values lists
    # A value of -1 means that node has not yet been visited
    node_ids = [_UNVISITED] * len(graph)
    low_link_values = [_UNVISITED] * len(graph)

    # Initialize stack to hold nodes during dfs and a set to
    # check whether a given node is in the stack
    stack = []
    in_stack = [False] * len(graph)

    # Iterate over all nodes since the graph may not be fully connected
    for node in range(len(graph)):
        # Only perform DFS from a node that has not yet been visited
        if node_ids[node] == _UNVISITED:
            updated_node_id = find_strongly_connected_components(
                node, graph, node_ids, low_link_values, stack, in_stack, node_id
            )
            node_id = updated_node_id
    return low_link_values


def find_strongly_connected_components(
    current_node, graph, node_ids, low_link_values, stack, in_stack, node_id
):
    # Assign the node's id and low link value to be the current value of the counter
    node_ids[current_node] = node_id
    low_link_values[current_node] = node_ids[current_node]

    # Increment node_id
    updated_node_id = node_id + 1

    # Push node onto the stack and mark it as being in the stack
    stack.append(current_node)
    in_stack[current_node] = True

    # Iterate over adjacenct neighbors
    for neighbor in graph[current_node]:
        # Check if adjacent node has been visited
        if node_ids[neighbor] == _UNVISITED:
            updated_node_id = find_strongly_connected_components(
                neighbor,
                graph,
                node_ids,
                low_link_values,
                stack,
                in_stack,
                updated_node_id,
            )
        # If the neighbor is NOT in the stack, then it must be a part of a different SCC
        # If it is in the stack, then update this current node's low link value
        # This is what allows the low link values to propagate throughout the cycles in the graph
        if in_stack[neighbor]:
            low_link_values[current_node] = min(
                low_link_values[current_node], low_link_values[neighbor]
            )

    # Check to see if this current node is the start of a SCC
    # The low link value of a node that is the start of a SCC won't have changed
    # during the DFS traversal and will be equal to its node_id
    if node_ids[current_node] == low_link_values[current_node]:
        # If you wanted to count the number of SCC, here is where you would
        # increment your counter for that purpose

        # Remove all nodes that are a part of this SCC from the stack
        # And marked them as removed
        while stack and low_link_values[stack[-1]] == node_ids[current_node]:
            top_node = stack.pop()
            in_stack[top_node] = False
    return updated_node_id


# Test case taken from here https://www.youtube.com/watch?v=wUgWX0nc4NY
# with some additional vertices added
def test_tarjans_algorithm():
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
    source = 4
    strongly_connected_components = tarjans_algorithm(source, graph)
    for node in range(len(strongly_connected_components)):
        print(f"Node: {node} in component {strongly_connected_components[node]}")


test_tarjans_algorithm()
