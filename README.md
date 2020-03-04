# Datastructures-and-Algorithms
On my journey of prepping for technical interviews, I decided to make this repo as a personal study guide for basic data structures and algorithms. This repo contains my implementations of various data structures and algorithms as well as brief descriptions, time complexities of operations, as well as advantages and disadvantages of certain implementations below. Hopefully it can help others who are in a similar boat.

## Data Structures

<details>
<summary>Data Structures</summary>
    
- ### Binary Search Tree
    - #### See Recurive Implementation [here](../master/data_structures/binary_search_tree/binary_search_tree_recursive.py)
    - #### See Iterative Implementation [here](../master/data_structures/binary_search_tree/binary_search_tree_iterative.py)
    - #### Description: 
        A Binary Search Tree(BST) is a Binary Tree that has the following properties:
            1. At any given node, all nodes in the left subtree contain keys that are less than the node's key
            2. At any given node, all nodes in the right subtree contain keys that are greater than the node's key
            3. Both the left and right subtrees must also be BSTs
        This invariant for a BST allows it to keep its keys in sorted order, so that operations can follow the principle (Divide and Conquer) of binary search.
        <br>
        
     
    - #### Implementations And Tradeoffs:
        1. **Implementing using all iterative methods**:
            - The optimal way to implement BST methods
            - Sometimes less intuitive to implement (e.g. delete_node() operation) but much more space efficient
            - Time complexities for all operations remain the same between iterative and recursive implementations
        2. **Implementing using all recursive methods**:
            - Intuitive to implement as BSTs are a recursive data structure
            - Space inefficient compared to iterative implementations 
                - All recursive operations will take O(h) space, where h is the height of the tree, due to the space being taken up on the implicit call stack
                - In a balanced BST, O(h) = O(logn), which isn't bad, but if the tree is skewed (looks more like a linked list), then this becomes O(n)
                
    - #### Operations Implemented:
        - Some notes:
            - When I say O(h), h is the height of the BST. This means that for a balanced BST, O(h) is really O(logn), but for a skewed BST, O(h) is O(n). Since a skewed BST is really the actual worst case, you can probably just use O(n), but O(h) is a little more descriptive.
            - Time and space complexities below are for the iterative implementations. The recursive implementations have the same time complexities, but all of their space complexities are O(h)
            - Level order traversal is an exception as I didn't implement it recursively. I will probably add it later.
        1. **insert()** -- > O(h) time, O(1) space
        2. **search()** -- > O(h) time, O(1) space
        3. **delete_node()** -- > O(h) time, O(1) space
        4. **is_empty()** -- > O(1) time, O(1) space
        5. **get_height()** -- > O(n) time, O(n) space
        6. **preorder_traversal()** -- > O(n) time, O(h) space
        7. **inorder_traversal()** -- > O(n) time, O(h) space
        8. **postorder_traversal()** -- > O(n) time, O(h) space
        9. **level_order_traversal()** O(n) time, O(n) space
    - #### Applications of data structure:
       
    - #### Advantages:
        
    - #### Disadvantages:

    - ### Further Notes:
        
    <br>

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
        2. **With union by rank without path compression**:
            - Union and find operations will both take O(log n) time
            - You can also do union by size (a.k.a weighted union) or union by height and achieve the same time complexity for both operations
        3. **With union by rank with path compression**:
            - Union and find operations will both take O(alpha(n)) time
            - The combination of these two optimizations makes this the optimal implementation
            - You can also do union by size instead of union by rank along with path compression and get the same time complexity for both operations
            - Rank is the same as the height of the tree if path compression had not been used
        4. **Space complexity**: Linear time in average and worst case for all implementations
    - #### Operations Implemented:
        1. **find()** with path compression -- > Amortized constant time, O(1) space
        2. **union()** by rank -- > Amortized constant time, O(1) space
        3. **is_connected()** -- > Amortized constant time, O(1) space
        4. **get_num_components()** -- > Constant time, O(1) space
    - #### Applications of data structure:
        1. Kruskal's Minimum Spanning Tree algorithm
        2. Detecting a cycle in an undirected graph(DFS is less space efficient but wins out in terms of time complexity due to amortized cost of the union operation.).
        3. Network connectivity: Determining whether two vertices in a graph are connected to each other through a series of edges.
        4. Least Common Ancestor in Trees
    - #### Advantages:
        1. Near constant time complexity for all operations when implemented with union by rank (or size) and path compression.
    - #### Disadvantages:
        1. Depends on what problem you are trying to solve.
    - ### Further Notes:
        1. The Union Find takes O(n) time to construct a set of "n" elements
        2. The size of the Union Find is determined when it is instantiated
        3. There is no "un-union" operation
        4. The number of components is always equal to the number of roots remaining
        5. The number of root nodes never increases
    <br>
    
- ### LRU Cache
    - #### See implementation [here](../master/data_structures/lru_cache/lru_cache.py)
    - #### Description: 
        
        <br>
        
     
    - #### Implementations And Tradeoffs:
  
    - #### Operations Implemented:
      
    - #### Applications of data structure:
       
    - #### Advantages:
        
    - #### Disadvantages:

    - ### Further Notes:
        
    <br>
    
</details>


## Sorting Algorithms
<details>
  <summary>Sorting Algorithms</summary>
</details>

## Searching Algorithms
<details>
  <summary>Searching Algorithms</summary>
  
  - ### Binary Search
    - #### See implementations [here](../master/search/binary_search/binary_search.py)
    - #### Description:
    - #### Implementations And Tradeoffs:
    - #### Applications of Algorithm:
    - #### Advantages:
    - #### Disadvantages:
    - #### Further Notes:
    <br>
</details>
  
