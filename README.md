# Datastructures-and-Algorithms
On my journey of prepping for technical interviews, I decided to make this repo as a personal study guide for basic data structures and algorithms. This repo contains my implementations of various data structures and algorithms as well as brief descriptions, time complexities of operations, as well as advantages and disadvantages of certain implementations below.

## Data Structures

<details>
<summary>Data Structures</summary>

- ### Union-Find/Disjoint Set
    - #### See implementation [here](../master/data_structures/union_find.py)
    - #### Description: 
        The Union-Find is a data structure that keeps track of a set of elements which are split into one or more subsets that have no elements in common (disjoint sets). Each subset can be visualized as a tree, where each node contains data as well as a pointer to its parent. The parent of a root node is itself.
        <br>
        
        When an element is added to the Union-Find, its parent is itself, and it makes its own set. The two core operations are **find**, and **union**. Find returns the name or id of the set that an element belongs to (the root node) and union merges two sets together by pointing the root of one set to the root of another.
    - #### Implementations And Tradeoffs:
        1. **Without union by rank or path compression**:
            - Union and find operations will both take O(n) time
            - The slowest implementation
        2. **Union by rank without path compression**:
            - Union and find operations will both take O(log n) time
            - You can also do union by size (a.k.a weighted union) or union by height and achieve the same time complexity for both operations
        3. **Union by rank with path compression**:
            - Union and find operations will both take O(alpha(n)) time
            - The combination of these two optimizations makes this the optimal implementation
            - You can also do union by size instead of union by rank along with path compression and get the same time complexity for both operations
            - Rank is the same as the height of the tree if path compression had not been used
        4. **Space complexity**: Linear time in average and worst case for all implementations
    - #### Operations Implemented:
        1. **find()** with path compression -- > Amortized constant time
        2. **union()** by rank -- > Amortized constant time
        3. **is_connected()** -- > Amortized constant time
        4. **get_num_components()** -- > Constant time
    - #### Applications of data structure:
        1. Kruskal's Minimum Spanning Tree algorithm
        2. Detecting a cycle in an undirected graph(DFS is less space efficient but wins out in terms of time complexity due to amortized cost of the union operation.).
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
  
