"""This module contains tests for the recursive implementation of the Binary Search Tree."""
import unittest
from data_structures.binary_search_tree.tree_traversal_order import TreeTraversalOrder
from data_structures.binary_search_tree.binary_search_tree_recursive import BinarySearchTree


class BinarySearchTreeTestCase(unittest.TestCase):
    """Class to run tests on the recursive BST implementation."""

    def test_is_empty(self):
        """Test to ensure that the tree is recorded
        as empty when initialized.
        """
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())

    def test_size(self):
        """Test to ensure that the BST is recording the
        correct number of nodes.
        """
        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        bst.insert(1)
        self.assertEqual(bst.size, 1)

    def test_height(self):
        """Test to ensure the BST reports the correct height."""
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56

        bst = BinarySearchTree()

        #empty BST should have a height of -1
        self.assertEqual(bst.get_height(), -1)

        #add level 1
        bst.insert(23)
        self.assertEqual(bst.get_height(), 0)

        #add level 2
        bst.insert(12)
        bst.insert(34)
        self.assertEqual(bst.get_height(), 1)

        #add level 3
        bst.insert(9)
        bst.insert(15)
        bst.insert(45)
        self.assertEqual(bst.get_height(), 2)

        #add level 4
        bst.insert(56)
        self.assertEqual(bst.get_height(), 3)

    def test_search(self):
        """Test that the search method returns the correct
        nodes.
        """
        bst = BinarySearchTree()
        bst.insert(12)
        bst.insert(9)
        bst.insert(22)

        #look for an element that doesn't exist
        node = bst.search(200)
        self.assertIsNone(node)

        #look for an element that does exist
        node = bst.search(12)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 12)

        #look for the root's left child
        node = bst.search(9)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 9)
        
        #look for the root's right child
        node = bst.search(22)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 22)

    def test_insert(self):
        """Test that the insert operation works properly."""
        bst = BinarySearchTree()
        #add unique elements
        self.assertTrue(bst.insert(5))
        self.assertTrue(bst.insert(15))
        self.assertTrue(bst.insert(3))

        #add duplicate element
        self.assertFalse(bst.insert(3))

    def test_delete_node_from_empty_tree(self):
        """Test to ensure the delete method returns False
        when attemptign to delete from an empty tree.
        """
        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)
        self.assertFalse(bst.delete_node(12))

    def test_delete_node_not_in_tree(self):
        """Test that the delete method returns False when trying
        to delete a node that doesn't exist.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = [23, 12, 34, 9, 15, 45, 56]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))
        self.assertEqual(bst.size, 7)
        self.assertEqual(bst.get_height(), 3)

        #try deleting a node that doesn't exist
        self.assertEqual(bst.get_height(), 3)
        self.assertFalse(bst.delete_node(145))
        self.assertEqual(bst.size, 7)
        self.assertEqual(bst.get_height(), 3)

    def test_delete_leaf_node(self):
        """Test that the delete method functions correctly
        when deleting a leaf node.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = [23, 12, 34, 9, 15, 45, 56]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))
        self.assertEqual(bst.size, 7)
        self.assertEqual(bst.get_height(), 3)

        #Case 1: Deleting a leaf node
        self.assertTrue(bst.delete_node(56))
        self.assertEqual(bst.size, 6)
        self.assertEqual(bst.get_height(), 2)
        self.assertIsNone(bst.search(7))

    def test_delete_root_as_leaf(self):
        """Test to ensure that the delete method works properly
        when the root is the only node in the tree.
        """
        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        bst.insert(12)
        self.assertEqual(bst.size, 1)
        self.assertEqual(bst.get_height(), 0)

        root = bst.search(12)
        self.assertEqual(root.data, 12)

        self.assertTrue(bst.delete_node(12))
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)
        self.assertIsNone(bst.root)

    def test_delete_node_one_child(self):
        """Test to delete a node that has only one child."""
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        # 8                56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)
        nodes = [23, 12, 34, 9, 15, 45, 56, 8]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))
        self.assertEqual(bst.size, 8)
        self.assertEqual(bst.get_height(), 3)

        #delete node that just has a left child
        self.assertTrue(bst.delete_node(9))
        self.assertEqual(bst.size, 7)
        self.assertEqual(bst.get_height(), 3)
        self.assertIsNone(bst.search(9))

        #delete node that just has a right child
        self.assertTrue(bst.delete_node(45))
        self.assertEqual(bst.size, 6)
        self.assertEqual(bst.get_height(), 2)
        self.assertIsNone(bst.search(45))

    def test_delete_root_node_right_child(self):
        """Test to delete a root node with only one child
        that is the right child.
        """
        #Tree should look like this
        #        23
        #          34
        #            45
        #              56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = [23, 34, 45, 56]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))
        self.assertEqual(bst.size, 4)
        self.assertEqual(bst.get_height(), 3)

        #root has only a right child
        self.assertTrue(bst.delete_node(23))
        self.assertEqual(bst.size, 3)
        self.assertEqual(bst.get_height(), 2)
        self.assertIsNone(bst.search(23))
        self.assertEqual(bst.root.data, 34)

    def test_delete_root_node_left_child(self):
        """Test to delete a root node with only one child
        that is the left child.
        """
        #Tree should look like this
        #           56
        #          45
        #         34
        #       23

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = [56, 45, 34, 23]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))
        self.assertEqual(bst.size, 4)
        self.assertEqual(bst.get_height(), 3)

        #root has only a right child
        self.assertTrue(bst.delete_node(56))
        self.assertEqual(bst.size, 3)
        self.assertEqual(bst.get_height(), 2)
        self.assertIsNone(bst.search(56))
        self.assertEqual(bst.root.data, 45)

    def test_delete_node_two_children(self):
        """Test to delete a node with two children."""
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        # 8                56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = [23, 12, 34, 9, 15, 45, 56, 8]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))
        self.assertEqual(bst.size, 8)
        self.assertEqual(bst.get_height(), 3)

        self.assertTrue(bst.delete_node(12))
        self.assertEqual(bst.size, 7)
        self.assertEqual(bst.get_height(), 3)
        self.assertIsNone(bst.search(12))

    def test_delete_root_node_two_children(self):
        """Test to ensure the delete method correctly
        deletes a root node that has two children.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        # 8                56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = [23, 12, 34, 9, 15, 45, 56, 8]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))
        self.assertEqual(bst.size, 8)
        self.assertEqual(bst.get_height(), 3)

        self.assertTrue(bst.delete_node(23))
        self.assertEqual(bst.size, 7)
        self.assertEqual(bst.get_height(), 3)
        self.assertIsNone(bst.search(23))
        self.assertEqual(bst.root.data, 34)

    def test_invalid_traversal(self):
        """Test to ensure that the traverse method
        raises an error if an invalid traversal order
        is passed in as an arguement.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)

        nodes = [23, 12, 34, 9, 15, 45, 56]
        #add nodes
        for node in nodes:
            self.assertTrue(bst.insert(node))

        self.assertEqual(bst.size, 7)

        nodes = bst.traverse(5)
        for node in nodes:
            self.assertIsNone(node)

    def test_preorder_traversal(self):
        """Test that a preorder traversal returns the nodes
        in the BST in the correct order.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = bst.traverse(TreeTraversalOrder.PRE_ORDER)
        for node in nodes:
            self.assertIsNone(node)

        nodes = [23, 12, 34, 9, 15, 45, 56]
        #add nodes
        for node in nodes:
            bst.insert(node)
        self.assertEqual(bst.get_height(), 3)
        self.assertEqual(bst.size, 7)

        #order should be 23, 12 9, 15, 34, 45, 56
        i = 0
        preorder = [23, 12, 9, 15, 34, 45, 56]
        for node in bst.traverse(TreeTraversalOrder.PRE_ORDER):
            self.assertEqual(preorder[i], node.data)
            i += 1

    def test_inorder_traversal(self):
        """Test that a inorder traversal returns the nodes
        in the BST in the correct order.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = bst.traverse(TreeTraversalOrder.IN_ORDER)
        for node in nodes:
            self.assertIsNone(node)

        nodes = [23, 12, 34, 9, 15, 45, 56]
        #add nodes
        for node in nodes:
            bst.insert(node)
        self.assertEqual(bst.get_height(), 3)
        self.assertEqual(bst.size, 7)
        
        #this is the expected order
        i = 0
        inorder = [9, 12, 15, 23, 34, 45, 56]
        for node in bst.traverse(TreeTraversalOrder.IN_ORDER):
            self.assertEqual(inorder[i], node.data)
            i += 1

    def test_postorder_traversal(self):
        """Test that a postorder traversal returns the nodes
        in the BST in the correct order.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56
        
        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = bst.traverse(TreeTraversalOrder.IN_ORDER)
        for node in nodes:
            self.assertIsNone(node)

        nodes = [23, 12, 34, 9, 15, 45, 56]
        #add nodes
        for node in nodes:
            bst.insert(node)
        self.assertEqual(bst.get_height(), 3)
        self.assertEqual(bst.size, 7)
        
        #this is the expected order
        i = 0
        postorder = [9, 15, 12, 56, 45, 34, 23]
        for node in bst.traverse(TreeTraversalOrder.POST_ORDER):
            self.assertEqual(postorder[i], node.data)
            i += 1

    def test_level_order_traversal(self):
        """Test that a levelorder traversal returns the nodes
        in the BST in the correct order.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56
        
        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.get_height(), -1)

        nodes = bst.traverse(TreeTraversalOrder.IN_ORDER)
        for node in nodes:
            self.assertIsNone(node)

        nodes = [23, 12, 34, 9, 15, 45, 56]
        #add nodes
        for node in nodes:
            bst.insert(node)
        self.assertEqual(bst.get_height(), 3)
        self.assertEqual(bst.size, 7)
        
        #this is the expected order
        i = 0
        level_order = [23, 12, 34, 9, 15, 45, 56]
        for node in bst.traverse(TreeTraversalOrder.LEVEL_ORDER):
            self.assertEqual(level_order[i], node.data)
            i += 1


if __name__ == "__main__":
    unittest.main()
