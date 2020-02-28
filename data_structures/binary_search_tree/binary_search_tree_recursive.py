"""This module contains an implementation of a Binary Search Tree.
All operations are implemented recursively.
"""
class TreeNode:
    """Class to represent a node in a binary search tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class to represent a Binary Search Tree. All methods
    implemented are recursive.
    """
    
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        """Insert the a node with the given data into the BST."""
        self.root = self._insert(self.root, data)
        self.size += 1

    def _insert(self, root, data):
        """Recursive helper method to insert a node with the given data into the BST."""
        if root is None:
            return TreeNode(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root
        
    def search(self, data):
        """Return a node in the tree, that contains the given data."""
        return self._search(self.root, data)

    def _search(self, root, data):
        """Recursive helper method to return a node in the tree that contains the
        given data.
        """
        if root is None:
            return root
        if data == root.data:
            return root
        if data < root.data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

    def delete_node(self, data):
        """Delete and return the first node with the given value from the 
        tree.
        """
        node = self._delete(self.root, data)
        if node is not None:
            self.size -= 1
        return node

    def _delete(self, root, data):
        """Recursive elper method to delete and return the first node with the given value from the 
        tree.
        """
        #cover edge case
        if root is None:
            return root
        if data < root.data: #node is in the left subtree
            root.left = self._delete(root.left, data) 
        elif data > root.data: #node is in right subtree
            root.right = self._delete(root.right, data) 
        else: #value is equal to the root, node has been found
            #Case 1: No children
            if root.left is None and root.right is None:
                root = None
            #Case 2: Has one child
            elif root.left is None: #has only a right child
                root = root.right
            elif root.right is None: #has only a left child
                root = root.left
            #Case 3: Two children
            else:
                #get minimum value from right subtree
                min_node = self._get_min(root.right)
                root.data = min_node.data
                #delete the node we just found from the right subtree
                root.right = self._delete(root.right, min_node.data)
        return root #the root may change after the deletion
    
    def _get_min(self, root):
        """Recursive helper method to return the node with the minimum value in the tree or subtree."""
        if root is None:
            return root
        if root.left is None:
            return root
        return self._get_min(root.left)