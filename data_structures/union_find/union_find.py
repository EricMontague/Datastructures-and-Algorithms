"""This module contains an implementation of the Union 
Find data structure. It utilizes union by rank and
path compression, which allow the time complexities
of union and find to be amortized constant time.
"""


class UnionFind:
    """Class to represent the Union Find data structure."""

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be greater than 0.")
        self.parent = [None] * size
        self.rank = [None] * size
        self.num_components = size
        self.size = size

    def _validate(self, element):
        """Raise an exception if the given element is not in
        not within the valid range of elements that can be in
        the UnionFind.
        """
        if element < 0 or element > self.size:
            raise ValueError(
                f"{element} not within the valid range of elements in Union Find."
            )

    def make_set(self, element):
        """Create a new disjoint set with that contains
        only the given element.
        """
        self._validate(element)
        # initially, element points to itself and rank is 0
        self.parent[element] = element
        self.rank[element] = 0

    def find(self, element):
        """Return the name of the set that the given element
        belongs to.
        """
        self._validate(element)
        # traverse up the tree until we hit the root
        root = element
        while root != self.parent[root]:
            root = self.parent[root]

        # path compression
        # traverse up the tree pointing each element
        # to the root, until we hit the root itself

        while element != self.parent[element]:
            parent = self.parent[element]
            self.parent[element] = root
            element = parent
        return root

    # recursive find operation with path compression
    # def find(self, element):
    #     """Return the name of the set that the given
    #     element belongs to.
    #     """
    #     if element != self.parent[element]:
    #         self.parent[element] = self.find(self.parent[element])
    #     return self.parent[element]

    def union(self, element_one, element_two):
        """Merge the two sets that both of the given
        elements belong to.
        """
        root_one = self.find(element_one)
        root_two = self.find(element_two)

        # if both roots are the same, both elements are
        # in the same set, so we don't merge anything

        if root_one != root_two:
            # merge set with lower rank into set with higher rank
            if self.rank[root_one] > self.rank[root_two]:
                self.parent[root_two] = root_one
            elif self.rank[root_one] < self.rank[root_two]:
                self.parent[root_one] = root_two
            else:  # Tied rank. Merge arbitrarily and increase rank
                self.parent[root_one] = root_two
                self.rank[root_two] += 1
            self.num_components -= 1  # decrease num components

    def get_num_components(self):
        """Return the number components in the UnionFind."""
        return self.num_components

    def is_connected(self, element_one, element_two):
        """Return True if both elements are in the same set."""
        return self.find(element_one) == self.find(element_two)
