# Datastructures-and-Algorithms
On my journey of learning CS Fundamentals, I decided to make this repo as a personal study guide for basic data structures and algorithms. This repo contains my implementations of various data structures and algorithms as well as brief descriptions, time complexities of operations, and advantages and disadvantages of certain implementations below.

## Data Structures

<details>
<summary>Data Structures</summary>

- ### Union-Find/Disjoint Set
    - #### Description: 
        The Union Find is a data structure that keeps track of elements which are split into one or more sets that have no elements in common (disjoint sets).
    - #### Highlights:
        1. **Path compression**:
        2. **Union by rank**:
    - #### Operations Implemented:
        1. **find()** with path compression -- > Amortized constant time
        2. **union()** by rank -- > Amortized constant time
        3. **is_connected()** -- > Amortized constant time
        4. **get_num_components()** -- > Constant time
    - #### Applications of data structure:
        1. Kruskal's Minimum Spanning Tree algorithm
        2. Detecting a cycle in an undirected graph
        3. Network connectivity: Determining whether two vertices in a graph are connected to each other through a series of edges.
        4. Least Common Ancestor in Trees
    - #### Advantages:
        1. Near constant time complexity for all operations when implemented with union by rank (or size) and path compression.
    - #### Disadvantages:
        1. None
    - ### Further Notes:
        1. The Union Find takes O(n) time to construct a set of "n" elements
        2. The size of the Union Find is determined when it is instantiated
        3. There is no "un-union" operation
        4. The number of components is always equal to the number of roots remaining
        5. The number of root nodes never increases
    <br>
</details>


## Sorting Algorithms
<details>
  <summary>Sorting Algorithms</summary>
</details>

## Searching Algorithms
<details>
  <summary>Searching Algorithms</summary>
</details>
  
