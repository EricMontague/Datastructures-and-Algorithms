"""This module contains my implementations of Dijkstra's algorithm."""


import heapq
from collections import namedtuple

Node = namedtuple("Node", ["value", "weight"])
PriorityQueueItem = namedtuple("PriorityQueueItem", ["key", "value"])


############
# Adjacency List
##############

# O(VlogV + ElogV)
def dijkstra_adjacency_list(source, graph):
    """Finds the shortest paths from some node in the graph to all other nodes.
    Returns a dictionary containing the shortest distances of
    all nodes from the source as well as another dictionary containing
    the predeccesor relationshops during the algorithm's exploration. 
    Assumes the graph is represented as an adjacency list
    """
    predecessors = {source: None}
    visited = set()
    distances, priority_queue = initialize_distances_and_queue(source, graph)

    while priority_queue:
        node = heapq.heappop(priority_queue)
        if node.value in visited:
            continue
        visited.add(node.value)
        for neighbor in graph[node.value]:
            if neighbor.value not in visited:
                new_distance = distances[node.value] + neighbor.weight
                if new_distance < distances[neighbor.value]:
                    distances[neighbor.value] = new_distance
                    predecessors[neighbor.value] = node.value
                    node_item = PriorityQueueItem(new_distance, neighbor.value)
                    heapq.heappush(priority_queue, node_item)
    return distances, predecessors
        

def initialize_distances_and_queue(source, graph):
    distances = {}
    priority_queue = []
    for node in range(len(graph)):
        if node == source:
            initial_distance = 0
        else:
            initial_distance = float("inf")
        distances[node] = initial_distance
        node_item = PriorityQueueItem(initial_distance, node)
        priority_queue.append(node_item)
    heapq.heapify(priority_queue)
    return distances, priority_queue            
        


################
# Adjacency Matrix
################
# O(V^2)
def dijkstra_adjacency_matrix(source, graph):
    """Finds the shortest paths from some node in the graph to all other nodes.
    Returns a dictionary containing the shortest distances of
    all nodes from the source as well as another dictionary containing
    the predeccesor relationshops during the algorithm's exploration. 
    Assumes the graph is represented as an adjacency list
    """
    predecessors = {source: None}
    visited = set()
    distances, node_list = initialize_distances_and_node_list(source, graph)

    while len(visited) != len(graph):
        node = get_smallest_node_by_distance(visited, distances, node_list)
        visited.add(node)
        for neighbor, weight in enumerate(graph[node]):
            if weight != 0 and neighbor not in visited:
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = node
    return distances, predecessors


def initialize_distances_and_node_list(source, graph):
    distances = {}
    node_list = []
    for node in range(len(graph)):
        if node == source:
            initial_distance = 0
        else:
            initial_distance = float("inf")
        distances[node] = initial_distance
        node_list.append(node)
    return distances, node_list


def get_smallest_node_by_distance(visited, distances, node_list):
    smallest_node = None
    for node in node_list:
        if node not in visited:
            if smallest_node is None:
                smallest_node = node
            elif distances[node] < distances[smallest_node]:
                smallest_node = node
    return smallest_node


def find_shortest_path(predecessors, source, destination):
    """Given a dictionary of predeccesors that was constructed via
    a shortest paths algorithm, return the vertices in the shortest
    path from source to destination.
    """
    path = []
    current_node = destination
    while current_node is not None:
        predecessor = predecessors[current_node]
        path.append(current_node)
        current_node = predecessor
    path.reverse()
    return path





# Informal tests. WIll create formal tests later

# Graph from
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# Adjacency list
def test_dijkstra_adjacency_list():

    # create graph
    graph = {
        0: [Node(1, 4), Node(7, 8)],
        1: [Node(0, 4), Node(7, 11), Node(2, 8)],
        2: [Node(1, 8), Node(3, 7), Node(8, 2), Node(5, 4)],
        3: [Node(2, 7), Node(5, 14), Node(4, 9)],
        4: [Node(3, 9), Node(5, 10)],
        5: [Node(6, 2), Node(2, 4), Node(3, 14), Node(4, 10)],
        6: [Node(7, 1), Node(8, 6), Node(5, 2)],
        7: [Node(0, 8), Node(1, 11), Node(8, 7), Node(6, 1)],
        8: [Node(2, 2), Node(7, 7), Node(6, 6)]
    }
    start = 0   
    end = 8
    distances, predecessors = dijkstra_adjacency_list(start, graph)

    # print shortest path
   
    shortest_path = find_shortest_path(predecessors, start, end)
    print("Vertex       Distance from Source")
    for node in distances:
        print(f"{node}                    {distances[node]}")
    print()
    print(f"Shortest path from {start} to {end}: ", shortest_path)


def test_dijkstra_adjacency_matrix():
    # create graph - same as the adjacency list one
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
    ]
    start = 0
    end = 8
    distances, predecessors = dijkstra_adjacency_matrix(start, graph)
    shortest_path = find_shortest_path(predecessors, start, end)
    print("Vertex       Distance from Source")
    for node in distances:
        print(f"{node}                    {distances[node]}")
    print()
    print(f"Shortest path from {start} to {end}: ", shortest_path)
    

test_dijkstra_adjacency_list()
test_dijkstra_adjacency_matrix()