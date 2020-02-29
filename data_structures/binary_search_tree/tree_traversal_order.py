"""This module contains an enum to be used for the traversal
method of a Binary Search Tree.
"""


from enum import Enum


class TreeTraversalOrder(Enum):
    """Enum class for Binary Tree traversals."""
    
    PRE_ORDER = 1
    IN_ORDER = 2
    POST_ORDER = 3
    LEVEL_ORDER = 4
