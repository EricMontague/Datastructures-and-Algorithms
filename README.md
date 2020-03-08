# Datastructures-and-Algorithms
On my journey of prepping for technical interviews, I decided to make this repo as a personal study guide for basic data structures and algorithms. This repo contains my implementations of various data structures and algorithms as well as brief descriptions, time complexities of operations, as well as advantages and disadvantages of certain implementations below. Hopefully it can help others who are in a similar boat.

## Data Structures

<details>
<summary>Data Structures</summary>
    
- ### Binary Search Tree
    - #### See Recurive Implementation [here](../master/data_structures/binary_search_tree/binary_search_tree_recursive.py)
    - #### See Iterative Implementation [here](../master/data_structures/binary_search_tree/binary_search_tree_iterative.py)
    - #### Description: 
        - A Binary Search Tree(BST) is a tree data structure that has the following properties:
            1. At any given node, all nodes in the left subtree contain keys that are less than the node's key
            2. At any given node, all nodes in the right subtree contain keys that are greater than the node's key
            3. Both the left and right subtrees must also be BSTs
            4. Each node has at most two child nodes
        - **Translation**: Given a parent node, the value of the left child node is always less than the value of the parent, and the value of the right child node is always greater than the parent
        - This invariant for a BST allows it to keep its keys in sorted order, so that operations can follow the principle (Divide and Conquer) of binary search. 
        - All nodes in a BST are usually distinct, but you can implement one that accomodates for duplicate keys
        <br>
        
     
    - #### Implementations And Tradeoffs:
        1. **Implementing using all iterative methods**:
            - The optimal way to implement BST methods
            - Sometimes less intuitive to implement (e.g. delete_node() operation) but much more space efficient
            - Time complexities for all operations remain the same between iterative and recursive implementations
        2. **Implementing using all recursive methods**:
            - Intuitive to implement as BSTs are a recursive data structure
            - Uses more space compared to iterative implementations 
                - All recursive operations will take O(h) space, where h is the height of the tree, due to the space being taken up on the implicit call stack
                - In a balanced BST, O(h) = O(logn), which isn't that big of a deal, but if the tree is skewed (looks more like a linked list), then this becomes O(n)
    - ### Types of Binary Trees:
        1. Full Binary Tree: A binary tree where every node has exactly zero or two children
        2. Perfect Binary Tree: A binary tree where all interior nodes have two children and **all** leaf nodes are on the same level
        3. Balanced Binary Tree: A binary tree where the height of the left and right subtrees of any node differ by no more than 1
        4. Complete Binary Tree: A binary tree where every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible
                
    - #### Operations Implemented:
        - Some notes:
            - When I say O(h), h is the height of the BST. This means that for a balanced BST, O(h) is really O(logn), but for a skewed BST, O(h) is O(n). Since a skewed BST is really the actual worst case, you can probably just use O(n), but O(h) is a little more descriptive.
            - Time and space complexities below are for the iterative implementations. The recursive implementations have the same time complexities, but all of their space complexities are O(h)
            - Level order traversal is an exception as I didn't implement it recursively. I will probably add it later.
            
        <br>
        
        1. **insert()** -- > O(h) time, O(1) space
        2. **search()** -- > O(h) time, O(1) space
        3. **delete_node()** -- > O(h) time, O(1) space
        4. **is_empty()** -- > O(1) time, O(1) space
        5. **get_height()** -- > O(n) time, O(n) space
        6. **preorder_traversal()** -- > O(n) time, O(h) space
        7. **inorder_traversal()** -- > O(n) time, O(h) space
        8. **postorder_traversal()** -- > O(n) time, O(h) space
        9. **level_order_traversal()** O(n) time, O(n) space
    - #### Tree Traversals:
        - **Traversal**: The process of visiting each node in the tree exactly once, it some order
        - **Breadth-first search**: Visiting all nodes in the BST level by level
            - Good for finding the shortest path from one node to another
            - Generally requires more memory than a DFS traversal (assuming the tree is not skewed)
            - O(1) space for a skewed BST
            - O(n) space for a balanced BST
            - List of BFS algorithms:
                1. Level Order Traversal: Same as the definition of breadth-first search above
        - **Depth-first search**: Start at a root node and walk down a path in the BST as far as possible before backtracking
            - Generally requires less memory than BFS (assuming the tree is not skewed)
            - O(n) space for a skewed BST
            - O(log n) space for a balanced BST
            - Easy to implement with recursion
            - Will not necessarily find the shortest path between two nodes
            - List of DFS algorithms:
                1. Preorder Traversal: Given any node, this algorithm visits (processes) this node first, then visits all nodes in its left subtree, and finally visits all nodes in its right subtree. This continues recursively until all nodes in the tree or subtree have been visited
                2. Inorder Traversal: Given any node, this algorithm visits (processes) all nodes in its left subtree first, then visits it, and finally visits all nodes in its right subtree. This continues recursively until all nodes in the tree or subtree have been visited
                3. Postorder Traversal: Given any node, this algorithms visits (processes) all nodes in its left subtree first, then visits all nodes in its right subtree, and finally visits the given node. This continues recursively until all nodes in the tree or subtree have been visited
    - #### Applications of data structure:
        1. Sorting elements: An inorder traversal of a BST returns all nodes in sorted order
        2. Useful for when you need a data structure that keeps elements sorted as you insert them, but also allows for fast removals (assuming the BST is a self-balancing tree such as an AVL Tree)
        3. Can be used to implement a priority queue (assuming the BST is a self-balancing tree such as an AVL Tree)
       
    - #### Advantages:
        1. Assuming the tree is balanced, BSTs allow for fast lookups, insertions, and deletions
        2. Good for sorting and keeping elements sorted upon insertion
        3. Easy to find the next greatest node (inorder successor) and the next smallest node (inorder predecessor) in O(h) time
        4. Great for representing hierarchies of things
        
    - #### Disadvantages:
        1. Slower lookups than a hash table

    - #### Further Notes:
        1. The height of a node is the length of the longest path from the given node **down** to some leaf
        2. The depth of a node is the length of the longest path from that node to the root
        
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
        - #### What is a Cache? (a simplistic view)
            - A cache is hardware or software that stores the result of an operation so that future requests return faster.
            - **Example**: Storing the results of a database query in a cache so that you don't have to do the computation again and again. 
            - When a request comes in, you look in the cache to see if the request information is in there.
            - If it is, then you simply return the response to the client. This is called a **cache hit**.
            - If it isn't(**cache miss**), then you query the database, store the result of this query in the cache, and then return the response to the client
        - #### What is LRU?
            - LRU stands for least recently used, and it is a type of **cache policy**
            - A cache policy is the set of rules that determines when you insert and remove data from a cache
            - Under the LRU policy, you create a cache of some predetermined size, where the most recently requested data sits on top of the cache, and the least recently requested data sits on the bottom
            - Whenever a request comes in and you successfully hit the cache, either to retrieve data, or update some data, you move that data to the top of the cache, since it is now the most recently requested item
            - Similarly, when a request comes in and the data isn't in the cache, you hit the database, and insert this new data at the top of the cache, since it is now the most recently requested item
            - Where the cache policy comes into play is if the cache has reached max capacity. In this case, you remove, or evict, the least recently used item in the cache, which should be the item at the very bottom
        <br>
        
     
    - #### Implementations And Tradeoffs:
        - **Requirements** - An LRU Cache must support the following operations in constant time:
            - **get(key)**: Return an item from the cache with the corresponding key and move that item to the top of the cache.
            - **put(key, value)**: Insert a new item into the cache. If an item with the given key already exists, update it and move it to the top of the cache. If the cache is full, remove the least recently used entry.
            
        <br>
        
        - **Thinking through a possible implementation** (skip to the last bullet if you just care about an optimal solution):
            - O(1) time operations usually leads me to think of a hash table, so let's look at that first
            - Hash Table: Has O(1) time lookups, inserts, updates, and deletes, which is perfect. You can make an object that represents an item in the cache, and store each item at some key in the hash table. But, we need something to maintain a kind of ordering of our items with a notion of a head and tail in our data structure. Maybe this can be combined with something else?
            - Hash Table + List: O(1) lookups, O(1) updates, and O(1) removals from the end, all of which are optimal. However, we may need to remove items from the middle when they are requested/ updated and then insert them at the front of the list. Removals from the middle of a list take O(n) time and insertions at the front also take O(n) time which is too slow
            - Hash Table  + BST: With this combination you could maybe have each item maintain a timestamp as to when it was last accessed, and keep an instance variable that holds least recently used item to speed up deletions (nodes will have parents pointers as well). O(1) lookups, O(1) updates, O(1) removals from the end. However, moving items from the interior of the BST due to updates and requests to the top of the BST will take O(log n) time for each operation(deletions included), which is too slow.
            - Hash Table + Heap: Same problems as with a BST. Too slow
            - Hash Table + Singly Linked List with a tail pointer: O(1) lookups, O(1) updates, O(1) for insertions at the head, and O(1) removals from the end. This is much better, but still lacking in one area. Deletions from the middle of the list are O(n). After you update an item or get it from the hash table, you will need to delete this node from the linked list and then insert it at the head. The insertion is O(1) time, but you can't traverse backwards in a singly linked list to reconfigure the pointers necessaru to delink the node. This requires that you traverse the list up until that point to perform a deletion which is O(n) time. Once again, too slow.
            - **Hash Table** + **Doubly Linked List with a tail pointer**: O(1) lookups, O(1) updates, O(1) insertions at the head, O(1) deletions regradless of where they occur. The fact that nodes in a doubly linked list maintain a pointer to their next and previous nodes allows us to overcome the inefficiency of the delete operation using singly linked lists. This is an optimal solution and is the one I have implemented. 
    - #### Operations Implemented(all other methods in the cache are weak internals):
        1. **get()** - > O(1) time, O(1) space
        2. **put()** - > O(1) time, O(1) space
        3. **is_full()** -> O(1) time. Not necessary, but I added it because I wanted the convenience of it.
    - #### Applications of data structure:
        - See the section on What is a Cache? above
    - #### Advantages:
        - All operations are very fast: O(1) time
    - #### Disadvantages:
        - Space heavy. Implementing the LRU cache with a hash table and a doubly linked list takes O(n) space for the hash table, O(n) space for the doubly linked list, plus some extra space for the pointers. This is still O(n) space overall, but it's still two data structures as opposed to one.
    - #### Some Reasons to Use a Cache:
        1. Reducing networks calls to a database. Particularly useful if you are querying for commonly used data
        2. Avoiding computations. This is especially true if the computations are slow
        3. Avoiding load on a database
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
        - Binary search is a divide and conquer algorithm used for quickly finding an element in an array that runs in O(log n) time. One of the preconditions for binary search to work is that the input array must be sorted. This precondition is what allows you to halve your search space at each step of the algorithm and achieve the logarithmic time complexity. 
        - Initially your search space is the entire array. The below three steps are to be performed until you've exhausted your search. At that time, the loop should break:
            - **Step 1** - Search: Look at the element in the middle of your search space. 
            - **Step 2** - Comparisons: 
                - **2a** - Target element found: If the current element equals the target element you are looking for, return the index of the current element (or return True or whatever your algorithm is required to return), else proceed to step 2b or 2c
                - **2b** - Target element > current element: If the current element is less your target element, then your target must lie in the right half of your array. Reset your search space to be the upper half of the array and go back to step 1. If not, proceed to step 2c
                - **2c** - Target element < current element: Since the other two conditions weren't True, this means that the current element is greater than your target element, so your target must lie in the left half of your array. Reset your search space to be the lower half of the array and go back to step 1
            - **Step 3** - Target element not found: If you've looped through the above sequence, and haven't found your target element, it must not exist in the array. Return -1 (or False, or whatever your algorithm is required to return)
    - #### Implementations And Tradeoffs:
        1. **Recursive implementation**:
            - Intuitive to implement
            - Time complexity is O(log n)
            - Space complexity is O(log n)
            - Same time complexity as the iterative implementation, but uses more space (not much more)
        2. **Iterative implementation**:
            - Time complexity is O(log n)
            - Space complexity is O(1)
            - Better in terms of space complexity, but log n is pretty small anyways, so it's not really that huge of a difference
    - #### Applications of Algorithm:
        - Finding if an element exists in a sorted array (you don't care about the position or number of occurences)
        - Finding the number of occurences of an element in a sorted array
        - Finding the first or last occurence of an element in a sorted array
        - Finding out how many times a sorted array is rotated
        - Finding an element in a circular array
    - #### Advantages:
        - Fast runtime, O(log n)
    - #### Disadvantages:
        - Requires that an array be sorted to work
    - #### Further Notes:
        - **Divide and conquer algorithms**: These are a set of algorithms that break a problem into two or more sub-problems at each step in the algorithm, until the problem becomes simple enough to solve directly. Two exampe other than binary search are merge sort and quicksort
        - Normally calculating the middle index for your search space is as simple as mid = (low + high) // 2, but to avoid integer overflow in some languages, it is better to do mid = low + (high - low) // 2
        - The basic implementation of binary search will only tell you if an element exists in the array or return the first index it finds. It does not guarantee that this is either the first or last element in the array
        
       
    <br>
</details>
  
