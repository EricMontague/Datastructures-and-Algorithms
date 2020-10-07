"""This module contains my implementation of an AVL Tree."""


class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.balance_factor = 0
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if data is None:
            raise ValueError("Node value cannot be None")
        self.root = self._insert(self.root, data)

    def _insert(self, current_node, data):
        if not current_node:
            return AVLTreeNode(data)
        if data < current_node.data:
            current_node.left = self._insert(current_node.left, data)
        else:
            current_node.right = self._insert(current_node.right, data)
        self._update_balance_factor_and_height(current_node)
        return self._rebalance(current_node)

    def delete(self, data):
        if data is None:
            raise ValueError("Node value cannot be None")
        self.root = self._delete(self.root, data)

    def _delete(self, current_node, data):
        if not current_node:
            return current_node
        if data < current_node.data:
            current_node.left = self._delete(current_node.left, data)
        elif data > current_node.data:
            current_node.right = self._delete(current_node.right, data)
        else:
            if not current_node.left and not current_node.right:
                current_node = None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                # small optimization to prevent unecessary rebalancing
                if current_node.left.height > current_node.right.height:
                    max_node = self._find_max(current_node.left)
                    current_node.data = max_node.data
                    current_node.left = self._delete(
                        current_node.left, current_node.data
                    )
                else:
                    min_node = self._find_min(current_node.right)
                    current_node.data = min_node.data
                    current_node.right = self._delete(
                        current_node.right, current_node.data
                    )

        self._update_balance_factor_and_height(current_node)
        return self._rebalance(current_node)

    def _find_max(self, current_node):
        if not current_node:
            return None
        if not current_node.right:
            return current_node
        return self._find_max(current_node.right)

    def _find_min(self, current_node):
        if not current_node:
            return None
        if not current_node.left:
            return current_node
        return self._find_min(current_node.left)

    def _update_balance_factor_and_height(self, current_node):
        if not current_node:
            return
        left_subtree_height = -1
        right_subtree_height = -1
        if current_node.left:
            left_subtree_height = current_node.left.height
        if current_node.right:
            right_subtree_height = current_node.right.height
        current_node.height = max(left_subtree_height, right_subtree_height) + 1
        current_node.balance_factor = right_subtree_height - left_subtree_height

    def _rebalance(self, node):
        if not node:
            return None
        new_node = node
        # right heavy
        if node.balance_factor == 2:
            if node.right.balance_factor < 0:  # zig-zag, need two rotations
                node.right = self._rotate_right(node.right)
            new_node = self._rotate_left(node)
        # left heavy
        elif node.balance_factor == -2:
            if node.left.balance_factor > 0:  # zig-zag, need two rotations
                node.left = self._rotate_left(node.left)
            new_node = self._rotate_right(node)
        return new_node

    def _rotate_left(self, node):
        right_child = node.right
        right_child_left_subtree = right_child.left
        right_child.left = node
        node.right = right_child_left_subtree
        self._update_balance_factor_and_height(right_child)
        self._update_balance_factor_and_height(node)
        return right_child

    def _rotate_right(self, node):
        left_child = node.left
        left_child_right_subtree = left_child.right
        left_child.right = node
        node.left = left_child_right_subtree
        self._update_balance_factor_and_height(left_child)
        self._update_balance_factor_and_height(node)
        return left_child

    def __str__(self):
        node_values = []

        def preorder_traversal(root):
            if not root:
                node_values.append("#")
            else:
                node_values.append(str(root.data))
                preorder_traversal(root.left)
                preorder_traversal(root.right)

        preorder_traversal(self.root)
        return "".join(node_values)


# Small informal test. Will make an official test later
balanced = True


def is_balanced(root):
    global balanced
    if not root:
        return -1
    left_subtree_height = is_balanced(root.left)
    right_subtree_height = is_balanced(root.right)
    balanced = abs(right_subtree_height - left_subtree_height) <= 1
    return max(left_subtree_height, right_subtree_height) + 1


# test insertions
avl_tree = AVLTree()
for value in range(5):
    print(value)
    avl_tree.insert(value)
is_balanced(avl_tree.root)
print(balanced)
print(avl_tree, "\n")


# test deletions
avl_tree.delete(1)
is_balanced(avl_tree.root)
print(balanced)
print(avl_tree, "\n")

# second deletion
avl_tree.delete(3)
is_balanced(avl_tree.root)
print(balanced)
print(avl_tree, "\n")

# not in tree
avl_tree.delete(15)
is_balanced(avl_tree.root)
print(balanced)
print(avl_tree, "\n")
