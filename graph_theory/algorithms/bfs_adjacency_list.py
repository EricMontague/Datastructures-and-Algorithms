"""This module contains an implementation of breadth first search
where the graph is represented as an adjacency list.
"""


from collections import deque


# assumes all inputs are valid and that
# the values in the adjacency list are python lists
def bfs(adjacency_list, source):
    visited = {source}
    queue = deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        yield node
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

