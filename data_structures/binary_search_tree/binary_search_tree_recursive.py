"""This module contains an implementation of a Binary Search Tree.
All of the common BST methods, except the level order traversal are
recursive.
"""
from .tree_traversal_order import TreeTraversalOrder
from collections import deque


class TreeNode:
    """Class to represent a node in a binary search tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class to represent a Binary Search Tree. All methods
    except for the level order traversal are implemented recursively.
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        """Insert the a node with the given data into the tree."""
        # check if node exists in the tree already
        if self.search(data) is None:
            self.root = self._insert(self.root, data)
            self.size += 1

    def _insert(self, root, data):
        """Helper method to insert a node with the given data into the BST."""
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
        """Helper method to return a node in the tree that contains the
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

    def delete(self, data):
        """Delete the first node with the given value from the tree."""
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        """Helper method to delete and return the first node with the given value from the 
        tree.
        """
        if root is None:
            return root
        if data < root.data:  # node is in the left subtree
            root.left = self._delete(root.left, data)
        elif data > root.data:  # node is in right subtree
            root.right = self._delete(root.right, data)
        else:  # value is equal to the root, node has been found
            # Case 1: No children
            if root.left is None and root.right is None:
                root = None
                self.size -= 1
            # Case 2: Has one child
            elif root.left is None:  # has only a right child
                root = root.right
                self.size -= 1
            elif root.right is None:  # has only a left child
                root = root.left
                self.size -= 1
            # Case 3: Two children
            else:
                # get minimum value from right subtree
                min_node = self._find_min(root.right)
                root.data = min_node.data
                # delete the node we just found from the right subtree
                root.right = self._delete(root.right, min_node.data)

                # if you wanted to, you could find the maximum value from the left subtree instead
                # max_node = self._find_max(root.left)
                # root.data = max_node.data
                # root.left = self._delete(root.left, max_node.data)

        return root  # the root might change, so you need to return it

    def get_height(self):
        """Return the height of the BST. A height of -1, means that
        the BST is empty.
        """
        return self._get_height(self.root)

    def _get_height(self, root):
        """Helper method to find the height of the tree."""
        if root is None:
            return -1
        return 1 + max(self._get_height(root.left), self._get_height(root.right))

    def is_empty(self):
        """Return True if the BST has no nodes."""
        return self.size == 0

    def _find_min(self, root):
        """Helper method to return the node with the minimum value in the tree or subtree."""
        if root.left is None:
            return root
        return self._find_min(root.left)

    def _find_max(self, root):
        """Helper method to return the node with the maximum
        value in the tree or subtree.
        """
        if root.right is None:
            return root
        return self._find_max(root.right)

    def traverse(self, traversal_order):
        """Return an iterator for a given traversal order.
        The four different traversals are level order, preorder,
        postorder, and inorder. Returns an empty iterator if
        there are no nodes in the tree.
        """
        node_list = []
        if traversal_order == TreeTraversalOrder.PRE_ORDER:
            self._preorder_traversal(node_list, self.root)
        elif traversal_order == TreeTraversalOrder.IN_ORDER:
            self._inorder_traversal(node_list, self.root)
        elif traversal_order == TreeTraversalOrder.POST_ORDER:
            self._postorder_traversal(node_list, self.root)
        elif traversal_order == TreeTraversalOrder.LEVEL_ORDER:
            self._level_order_traveral(node_list, self.root)
        for node in node_list:
            yield node

    def _preorder_traversal(self, node_list, root):
        """Append the nodes in the tree in preorder to node_list."""
        if root is not None:
            node_list.append(root)
            self._preorder_traversal(node_list, root.left)
            self._preorder_traversal(node_list, root.right)

    def _inorder_traversal(self, node_list, root):
        """Append the nodes in the tree in inorder to node_list."""
        if root is not None:
            self._inorder_traversal(node_list, root.left)
            node_list.append(root)
            self._inorder_traversal(node_list, root.right)

    def _postorder_traversal(self, node_list, root):
        """Append the nodes in the tree in postorder to node_list."""
        if root is not None:
            self._postorder_traversal(node_list, root.left)
            self._postorder_traversal(node_list, root.right)
            node_list.append(root)

    def _level_order_traveral(self, node_list, root):
        """Return an iterator to traverse the tree in level order."""
        if root is not None:
            queue = deque()
            queue.append(root)
            while queue:
                node = queue.popleft()
                node_list.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

