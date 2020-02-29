"""This module contains an implementation of a Binary Search Tree.
All operations are implemented iteratively.
"""
from collections import deque
from .tree_traversal_order import TreeTraversalOrder


class TreeNode:
    """Class to represent a node in a binary search tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class to represent a Binary Search Tree. All methods
    implemented are iterative.
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        """Insert the a node with the given data into the tree.
        Returns True if a node was successfully inserted amd False
        if the node already exists in the tree.
        """
        #check to see if there is already a node with this data in the tree.
        if self.search(data) is not None:
            return False
        node = TreeNode(data)
        if self.root is None: #bst is empty
            self.root = node
        else:
            current = self.root
            while True:
                if node.data < current.data:
                    if current.left is None: #insert if no left child
                        current.left = node
                        break
                    else:   #walk to the left
                        current = current.left
                else:
                    if current.right is None: #insert if no right child
                        current.right = node
                        break
                    else:   #walk to the right
                        current = current.right
        self.size += 1
        return True
    
    def search(self, data):
        """Return a node in the tree, that contains the given data."""
        if self.root is None:
            return self.root #bst is empty
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return current

    def delete_node(self, data):
        """Delete and return the first node with the given value from the 
        tree. Returns True if the node was successfully located and deleted.
        and False if the node does not exist in the tree.
        """
        if self.search(data) is None:
            return False
        self.size -= 1
        return True
        
    def __find_min(self, root):
        """Private method to return the minimum value in the given tree or
        subtree.
        """
        if root is None:
            return root
        current = root
        while current.left is not None:
            current = current.left
        return current

    def __find_max(self, root):
        """Private method to return the maximum value in the given tree or
        subtree.
        """
        if root is None:
            return root
        current = root
        while current.right is not None:
            current = current.right
        return current

    def is_empty(self):
        """Return True if the tree has no nodes."""
        return self.size == 0

    #essentially level order traversal
    def get_height(self):
        """Return the height of the tree. If the tree is empty,
        return -1.
        """
        height = -1
        if self.root is None:
            return height
        queue = deque()
        queue.append(self.root)
        while queue:
            num_nodes = len(queue)
            height += 1
            for num in range(num_nodes):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return height

    def traverse(self, traversal_order):
        """Return an iterator for a given traversal order.
        The four different traversals are level order, preorder,
        postorder, and inorder.
        """
        if traversal_order == TreeTraversalOrder.PRE_ORDER:
            return self.__preorder_traversal(self.root)
        elif traversal_order == TreeTraversalOrder.IN_ORDER:
            return self.__inorder_traversal(self.root)
        elif traversal_order == TreeTraversalOrder.POST_ORDER:
            return self.__postorder_traversal(self.root)
        elif traversal_order == TreeTraversalOrder.LEVEL_ORDER:
            return self.__level_order_traveral()
        else:
            yield None

    def __preorder_traversal(self, root):
        """Return an iterator to traverse the tree in preorder.
        Returns None if the root is None instead of an iterator.
        """
        if root is None:
            return root
        stack = [root]
        while stack:            
            node = stack.pop()
            yield node
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    
    def __inorder_traversal(self, root):
        """Return an iterator to traverse the tree in inorder.
        Returns None if the root is None instead of an iterator.
        """
        if root is None:
            return root
        stack = []

        #loop as long as there are more nodes to process
        #'or root' is necessary for when the method comes back up to the
        #root of the BST before traversing the right subtree. At that time
        #there will be no more nodes in the stack
        while stack or root:
            #go as far left as possible
            while root:
                stack.append(root)
                root = root.left

            #pop the node at the top of the stack
            root = stack.pop()

            #process the node
            yield root

            #move to right subtree
            root = root.right

    def __postorder_traversal(self, root):
        """Return an iterator to traverse the tree in postorder.
        Returns None if the root is None instead of an iterator.
        """
        if root is None:
            return root
        stack = []
        
        while stack:
            while root:
                #push root's right child and then root onto the stack
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)

                #set root as root's left child
                root = root.left

            #pop a node from the stack and set it as root
            root = stack.pop()

            #if the popped node has a right child and the right child is not processed yet 
            #(on top of the stack), then make sure the right child is processed before root
            if root.right is not None and (stack[-1] == root.right or stack == []):
                stack.pop()   #Remove right child from stack
                stack.append(root)   #push root back to stack
                root = root.right   #change root so that the right child is processed next
            else:
                #yield root and set root to None
                yield root
                root = None

    #a less space efficient, but simpler way to do postorder traversal using two stacks
    #it builds up a reverse postordering of the nodes in the second stack
    #and then you pop each node from the second stack one by one
    #this is essentially a mirroring of preorder traversal
    # def __postorder_traversal(self, root):
    #     """Return an iterator to traverse the tree in postorder.
    #     Returns None if the root is None instead of an iterator.
    #     """
    #     if root is not None:
    #         return root
    #     stack_one = [root]
    #     stack_two = []

    #     #loop while stack one isn't empty
    #     while stack_one:
    #         #pop node from stack one and push to stack 2
    #         node = stack_one.pop()
    #         stack_two.append(node)

    #         #push left and right children of
    #         #removed item to stack one
    #         if node.left is not None:
    #             stack_one.append(node.left)
    #         if node.right is not None:
    #             stack_one.append(node.right)

    #     #yield all elements in the second stack

    #     while stack_two:
    #         node = stack_two.pop()
    #         yield node

    def __level_order_traveral(self):
        """Return an iterator to traverse the tree in level order."""
        if self.root is None:
            return self.root
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)