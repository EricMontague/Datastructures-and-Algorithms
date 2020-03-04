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
        """Delete the first node with the given value from the 
        tree. Returns True if the node was successfully located and deleted.
        and False if the node does not exist in the tree.
        """
        if self.root is None:
            return False
        if self.root.data == data:
            self.root = self._delete(self.root)
        else:
            parent = self._find_parent(self.root, data)
            #node doesn't exist in the treee
            if parent is None:
                return False
            else:
                #figure out which child needs to be deleted
                if parent.left is not None and parent.left.data == data:
                    parent.left = self._delete(parent.left)
                else:
                    parent.right = self._delete(parent.right)
        self.size -= 1
        return True
    
    def _delete(self, node):
        """Helper method to delete a node from the tree."""
        #Case 1: Deleting a leaf node
        if node.left is None and node.right is None:
            return None
        #Case 2: Has one child
        elif node.left is None: #only has a right child
            return node.right
        elif node.right is None: #only has a left child
            return node.left
        #Case 3: Has two children
        else:
            #find inorder successor and parent of inorder successor
            min_node = self._find_min(node.right)
            parent = self._find_parent(node.right, min_node.data)

            #if the inorder successor is the root of the right subtree,
            #set the node to be deleted's right pointer to None
            if node == parent:
                node.right = None
            else:
                #an inorder successot has at most one child and it can only be a right child
                parent.left = min_node.right
            node.data = min_node.data
            return node

    def _find_parent(self, root, data):
        """Return the parent node of the node with the given data in the tree."""
        #edge case where root is the only node in the tree/subtree
        if root.data == data:
            return root
        parent = None
        current = root
        while current is not None:
            if data == current.data:
                return parent
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
        return current
        
    def _find_min(self, root):
        """Helper method to return the minimum value in the given tree or
        subtree.
        """
        if root is None:
            return root
        current = root
        while current.left is not None:
            current = current.left
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
            return self._preorder_traversal(self.root)
        elif traversal_order == TreeTraversalOrder.IN_ORDER:
            return self._inorder_traversal(self.root)
        elif traversal_order == TreeTraversalOrder.POST_ORDER:
            return self._postorder_traversal(self.root)
        elif traversal_order == TreeTraversalOrder.LEVEL_ORDER:
            return self._level_order_traveral()
        else:
            yield None

    def _preorder_traversal(self, root):
        """Return an iterator to traverse the tree in preorder."""
        if root is None:
            yield root
        stack = [root]
        while stack:            
            node = stack.pop()
            yield node
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    
    def _inorder_traversal(self, root):
        """Return an iterator to traverse the tree in inorder."""
        if root is None:
            yield root
        stack = []

        #loop as long as there are more nodes to process
        #'or root' is necessary for when the method comes back up to the
        #root of the BST before traversing the right subtree. At that time
        #there will be no more nodes in the stack
        while stack or root:
            #go as far left as possible, visiting the left subtree
            while root:
                stack.append(root)
                root = root.left

            #pop the node at the top of the stack
            root = stack.pop()

            #process the node
            yield root

            #move to right subtree
            root = root.right
    
    def _postorder_traversal(self, root):
        """Return an iterator to traverse the tree in postorder."""
        if root is None:
            yield root
        #keep track of previously visited node
        prev = None
        stack = [root]

        while stack:
            current = stack[-1]
            #coming down the tree from a parent node
            if prev is None or (prev.left == current or prev.right == current):
                if current.left is not None:
                    stack.append(current.left)
                elif current.right is not None:
                    stack.append(current.right)
            #coming up the tree from the left, move to right subtree
            elif prev == current.left:
                if current.right is not None:
                    stack.append(current.right)
            #coming up the tree from the right, yield node
            else:
                stack.pop()
                yield current
            prev = current

    #Alternative postorder traversal with two stacks
    #it builds up a reverse postordering of the nodes in the second stack
    #and then you pop each node from the second stack one by one.
    #This is essentially a mirroring of preorder traversal
    def _postorder_traversal2(self, root):
        """Return an iterator to traverse the tree in postorder."""
        if root is None:
            yield root
        stack_one = [root]
        stack_two = []

        #loop while stack one isn't empty
        while stack_one:
            #pop node from stack one and push to stack 2
            node = stack_one.pop()
            stack_two.append(node)

            #push left and right children of
            #removed node to stack one
            if node.left is not None:
                stack_one.append(node.left)
            if node.right is not None:
                stack_one.append(node.right)

        #yield all elements in the second stack
        while stack_two:
            node = stack_two.pop()
            yield node

    def _level_order_traveral(self):
        """Return an iterator to traverse the tree in level order."""
        if self.root is None:
            yield self.root
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
