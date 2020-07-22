"""This module contains an enum for graph traversals."""


from enum import Enum


class Traversal(Enum):
    """Class to represent an enumeration
    for graph traversal algorithms."""

    BREADTH_FIRST_SEARCH = 0
    DEPTH_FIRST_SEARCH = 1

    