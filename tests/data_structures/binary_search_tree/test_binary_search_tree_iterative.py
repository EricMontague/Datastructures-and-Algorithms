"""This module contains tests for the iterative implementation of the Binary Search Tree."""
import unittest
from data_structures.binary_search_tree.tree_traversal_order import TreeTraversalOrder
from data_structures.binary_search_tree.binary_search_tree_iterative import TreeNode, BinarySearchTree


class BinarySearchTreeTestCase(unittest.TestCase):
    """Class to run tests on the iterative BST implementation."""

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

    def test_delete_node(self):
        """Test the delete method of the BST."""
        pass

    def test_invalid_traversal(self):
        """Test to ensure that the traverse method
        returns an empty generator.
        """
        #Tree should look like this
        #        23
        #     12     34
        #   9   15      45
        #                 56

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)

        #add level 1
        bst.insert(23)
        
        #add level 2
        bst.insert(12)
        bst.insert(34)
        
        #add level 3
        bst.insert(9)
        bst.insert(15)
        bst.insert(45)
        
        #add level 4
        bst.insert(56)

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
