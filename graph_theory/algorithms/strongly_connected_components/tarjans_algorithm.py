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
- Tarjan's algorithm is based on keeping track of the start time of each node in the DFS as well
as the earliest start time of all nodes reachable from a given node including itself.
- The "earliest start time" is referred to as a node's low-link value
- Low link value: The low-link value of a node is the earliest start time of a node reachable from that 
node when doing a DFS (including itself)


Overview:

Step 1: Mark the id of each node as unvisited

Step 2: Start DFS. Upon visiting a node, record its start time. At this point a node's start time
and low-link value are the same. Also, push the node onto the 'seen' stack and corresponding set.

Step 3: On DFS callback, if the previous node is on the stack then min the current node's 
low-link value with the last node's low-link value. This allows low-link values to 
propagate throughout cycles

Step 4: After visiting all neighbors, if the current node started a connected component, then
pop nodes off of the stack that are in that component. You know that a node started a 
connected component if its start time equals its low-link value
"""

_UNVISITED = -1
visited_time = 0

# time complexity: O(V + E), where 'V' is the number of vertices and 'E' is the number of edges
# space complexity: O(V)

# the graph is assumed to be an adjacency list
def tarjans_algorithm(graph):


    visited_times = [_UNVISITED] * len(graph)
    low_link_values = [_UNVISITED] * len(graph)

    # Initialize stack to hold nodes during dfs and a set to
    # check whether a given node is in the stack
    stack = []
    in_stack = [False] * len(graph)

    # Iterate over all nodes since the graph may not be fully connected
    for node in range(len(graph)):
        # Only perform DFS from a node that has not yet been visited
        if visited_times[node] == _UNVISITED:
            find_strongly_connected_components(
                node, graph, visited_times, low_link_values, stack, in_stack
            )
    return low_link_values


def find_strongly_connected_components(
    current_node, graph, visited_times, low_link_values, stack, in_stack
):
    global visited_time
    # Assign the node's visited time and low link value to be the current value of the counter
    visited_times[current_node] = visited_time
    low_link_values[current_node] = visited_time

    # Increment visited_time
    visited_time += 1

    # Push node onto the stack and mark it as being in the stack
    stack.append(current_node)
    in_stack[current_node] = True

    # Iterate over adjacenct neighbors
    for neighbor in graph[current_node]:
        # Check if adjacent node has been visited
        if visited_times[neighbor] == _UNVISITED:
            find_strongly_connected_components(
                neighbor,
                graph,
                visited_times,
                low_link_values,
                stack,
                in_stack
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
    # during the DFS traversal and will be equal to its visited time
    if visited_times[current_node] == low_link_values[current_node]:
        # If you wanted to count the number of SCC, here is where you would
        # increment your counter for that purpose

        # Remove all nodes that are a part of this SCC from the stack
        # And marked them as removed
        while stack and low_link_values[stack[-1]] == visited_times[current_node]:
            top_node = stack.pop()
            in_stack[top_node] = False


# Test case taken from here±
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

    strongly_connected_components = tarjans_algorithm(graph)
    for node in range(len(strongly_connected_components)):
        print(f"Node: {node} in component {strongly_connected_components[node]}")

    # Expected results:
    # Node: 0 in component 0
    # Node: 1 in component 0
    # Node: 2 in component 0
    # Node: 3 in component 3
    # Node: 4 in component 4
    # Node: 5 in component 4
    # Node: 6 in component 4
    # Node: 7 in component 3
    # Node: 8 in component 8
    # Node: 9 in component 8
    # Node: 10 in component 8

test_tarjans_algorithm()
