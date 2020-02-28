"""This module contains an implementation of a Binary Search Tree.
All operations are implemented iteratively.
"""
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
        """Insert the a node with the given data into the BST."""
        node = TreeNode(data)
        if self.root is None: #bst is empty
            self.root = None
        else:
            current = self.root
            while True:
                if node.data < current.data:
                    if current.left is None: #insert if no left child
                        current.left = node
                        self.size += 1
                        break
                    else:   #walk to the left
                        current = current.left
                else:
                    if current.right is None: #insert if no right child
                        current.right = node
                        self.size += 1
                        break
                    else:   #walk to the right
                        current = current.right
    
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
        tree.
        """
        pass
    
    def _get_min(self, root):
        """Helper method to return the minimum value in the given tree or
        subtree.
        """
        if root is None:
            return root
        current = root
        while current.left is not None:
            current = current.left
        return current