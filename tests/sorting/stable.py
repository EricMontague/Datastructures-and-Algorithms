"""This module contains a class that is used with helping to test
whether a sorting algorithm is stable or not.
"""


class TestProduct:
    """Dummy class created to test the stability 
    property of sorting algorithms.
    """

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __lt__(self, other):
        return self.quantity < other.quantity

    def __le__(self, other):
        return self.quantity <= other.quantity

    def __eq__(self, other):
        return self.quantity == other.quantity

        