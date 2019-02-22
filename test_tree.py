import unittest
from tree import BinaryTree


class TestTreeClass(unittest.TestCase):

    def test_init_tree(self):
        tree = BinaryTree('a')
        self.assertEqual(tree.value, 'a')
        self.assertEqual(tree.left_child, None)
        self.assertEqual(tree.right_child, None)

    def test_add_left_child(self):
        tree = BinaryTree('a')
        tree.insert_left('b')
        self.assertEqual(tree.left_child.value, 'b')

    def test_add_right_child(self):
        tree = BinaryTree('a')
        tree.insert_left('b')
        tree.insert_right('c')
        self.assertEqual(tree.right_child.value, 'c')

    def test_add_right_child_when_left_child_empty(self):
        tree = BinaryTree('a')
        tree.insert_right('c')
        self.assertEqual(tree.left_child.value, 'c')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTreeClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
