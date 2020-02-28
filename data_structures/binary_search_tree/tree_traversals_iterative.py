"""This module contains implementations of several tree traversal algorithms.
They are implemented as generators to make them easier to test. All methods
are implemented iteratively.
"""
from collections import deque


def level_order_traveral(root):
    """Given the root node of a BST, return
    all nodes in the BST in level order.
    """
    if root is None:
        return root
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        yield node.data
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def preorder_traversal(root):
    """Given the root of a BST, perform a preorder
    traversal of the tree.
    """
    pass


def postorder_traversal(root):
    """Given the root of a BST, perform a postorder
    traversal of the tree.
    """
    pass


def inorder_traversal(root):
    """Given the root of a BST, perform an inorder
    traversal of the tree.
    """
    pass

