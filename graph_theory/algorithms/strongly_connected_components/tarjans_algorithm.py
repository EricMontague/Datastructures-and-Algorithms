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


# the graph is assumed to be an adjacency list
def tarjans_algorithm(source, graph):

    # Used to assign ids and intial low link values to nodes
    counter = 0

    # Initialize node ids and low link values lists
    # A value of -1 means that node has not yet been visited
    node_ids = [-1] * len(graph)
    low_link_values = [-1] * len(graph)

    # Initialize stack to hold nodes during dfs and a set to
    # check whether a given node is in the stack
    stack = []
    in_stack = set()

    # Iterate over all nodes since the graph may not be fully connected
    for node in range(len(graph)):
        # Only perform DFS from a node that has not yet been visited
        if node_ids[node] == -1 and low_link_values[node] == -1:
            updated_counter = find_strongly_connected_components(
                node, graph, node_ids, low_link_values, stack, in_stack, counter
            )
            counter = updated_counter
    return low_link_values


def find_strongly_connected_components(
    current_node, graph, node_ids, low_link_values, stack, in_stack, counter
):
    # Assign the node's id and low link value to be the current value of the counter
    node_ids[current_node] = counter
    low_link_values[current_node] = node_ids[current_node]

    # Increment counter
    updated_counter = counter + 1

    # Push node onto the stack and add it to the in_stack set
    stack.append(current_node)
    in_stack.add(current_node)

    # Iterate over adjacenct neighbors
    for neighbor in graph[current_node]:
        # Check if adjacent node has been visited
        if node_ids[neighbor] == -1 and low_link_values[neighbor] == -1:
            updated_counter = find_strongly_connected_components(
                neighbor,
                graph,
                node_ids,
                low_link_values,
                stack,
                in_stack,
                updated_counter,
            )
        # If the neighbor is NOT in the stack, then it must be a part of a different SCC
        # If it is in the stack, then update this current node's low link value
        if neighbor in in_stack:
            low_link_values[current_node] = min(
                low_link_values[current_node], low_link_values[neighbor]
            )

    # Check to see if this current node is the start of a SCC
    # The low link value of a node that is the start of a SCC won't have changed
    # during the DFS traversal and will be equal to its node_id
    if node_ids[current_node] == low_link_values[current_node]:

        # Remove all nodes that are a part of this SCC from the stack
        while stack and low_link_values[stack[-1]] == node_ids[current_node]:
            top_node = stack.pop()
            in_stack.remove(top_node)
    return updated_counter


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
    }
    source = 4
    strongly_connected_components = tarjans_algorithm(source, graph)
    for node in range(len(strongly_connected_components)):
        print(f"Node: {node} in component {strongly_connected_components[node]}")


test_tarjans_algorithm()
