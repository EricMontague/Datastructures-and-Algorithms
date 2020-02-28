"""This module contains implementations of several tree traversal algorithms.
They are implemented as generators to make them easier to test. All methods
are implemented recursively.
"""
from collections import deque


def preorder_traversal(root):
    """Given the root of a BST, perform a preorder
    traversal of the tree.
    """
    if root is not None:
        yield root.data
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    """Given the root of a BST, perform a postorder
    traversal of the tree.
    """
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        yield root.data


def inorder_traversal(root):
    """Given the root of a BST, perform an inorder
    traversal of the tree.
    """
    if root is not None:
        inorder_traversal(root.left)
        yield root.data
        inorder_traversal(root.right)

