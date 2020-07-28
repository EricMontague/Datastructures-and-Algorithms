"""This module contains an implemntation of breadth first search
where the graph is represented as an adjacency matrix.
"""


from collections import deque


# assumes all inputs are valid
def bfs(adjacency_matrix, source):
    visited = {source}
    queue = deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        yield node
        for neighbor, value in enumerate(adjacency_matrix[node]):
            if value == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

