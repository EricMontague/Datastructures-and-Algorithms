"""This module contains my implementation of an AVL Tree."""


class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.balance_factor = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        self._update_balance_factors(self.root)
        self.root = self._rebalance_tree(self.root)

    def _insert(self, current_node, data):
        if not current_node:
            return AVLTreeNode(data)
        if data < current_node.data:
            current_node.left = self._insert(current_node.left, data)
        else:
            current_node.right = self._insert(current_node.right, data)
        return current_node

    def delete(self, data):
        self.root = self._delete(self.root, data)
        self._update_balance_factors(self.root)
        self._rebalance_tree(self.root)

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
                max_node = self._find_max(current_node.left)
                current_node.val = max_node.val
                current_node.left = self._delete(current_node.left, max_node.val)
        return current_node

    def _find_max(self, root):
        if not root:
            return None
        if not root.right:
            return root
        return self._find_max(root.right)

    def _update_balance_factors(self, current_node):
        if not current_node:
            return -1
        left_subtree_height = self._update_balance_factors(current_node.left)
        right_subtree_height = self._update_balance_factors(current_node.right)
        current_node.balance_factor = right_subtree_height - left_subtree_height
        return max(left_subtree_height, right_subtree_height) + 1

    def _rebalance_tree(self, root):
        new_root = root
        # right heavy
        if root.balance_factor == 2:
            if self._should_rotate_twice(root):
                root.right = self._rotate_right(root.right)
            new_root = self._rotate_left(root)
        # left heavy
        elif root.balance_factor == -2:
            if self._should_rotate_twice(root):
                root.left = self._rotate_left(root.left)
            new_root = self._rotate_right(root)
        return new_root

    def _should_rotate_twice(self, root):
        # root has a left child. but not a right child
        if root.left and not root.right:
            # left child has no left child, but has a right child
            if not root.left.left and root.left.right:
                return True

        # root has a right child, but not a left child
        if root.right and not root.left:
            # right child ha not right child, but has a left child
            if not root.right.right and root.right.left:
                return True
        return False

    def _rotate_left(self, root):
        right_child = root.right
        right_child_left_subtree = right_child.left
        right_child.left = root
        root.right = right_child_left_subtree
        return right_child

    def _rotate_right(self, root):
        left_child = root.left
        left_child_right_subtree = left_child.right
        left_child.right = root
        root.left = left_child_right_subtree
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
