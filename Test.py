import unittest
from Node import *


class TestLca(unittest.TestCase):

    def testEmptyTree(self):
        root = Node(1)
        self.assertEqual(-1, findLCA(root, 0, 0))

    def testOneRootNode(self):
        root = Node(1)
        self.assertEqual(1, findLCA(root, 1, 1))

    def testNodesMissing(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(-1, findLCA(root, 4, 5))   # both missing
        self.assertEqual(-1, findLCA(root, 4, 1))   # first one missing
        self.assertEqual(-1, findLCA(root, 4, 5))   # second one missing

    def testSameNode(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(1, findLCA(root, 1, 1))
        self.assertEqual(2, findLCA(root, 2, 2))
        self.assertEqual(3, findLCA(root, 3, 3))

    def testSameBranchOneLevel(self):
        root = Node(1)
        root.left = Node(3)
        self.assertEqual(1, findLCA(root, 1, 3))

    def testSameBranchMultipleLevels(self):
        root = Node(1)
        root.left = Node(3)
        root.left.right = Node(4)
        root.left.right.left = Node(5)
        root.left.right.left.right = Node(6)
        self.assertEqual(3, findLCA(root, 3, 6))

    def testDifferentBranchOneLevel(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(1, findLCA(root, 2, 3))

    def testDifferentBranchMultipleLevels(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.right = Node(3)
        root.right.right = Node(5)
        root.right.right.right = Node(6)
        self.assertEqual(1, findLCA(root, 4, 5))
        self.assertEqual(1, findLCA(root, 4, 6))

    def testFullTree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(2, findLCA(root, 4, 5))
        self.assertEqual(1, findLCA(root, 4, 6))

    def testNoChildNode(self):
        node = Node(1)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def testOneChildNode(self):
        node = Node(1)
        node.left = Node(2)
        self.assertIsNone(node.right)
        self.assertEqual(2, node.left.key)
        self.assertIsNone(node.left.right)
        self.assertIsNone(node.left.left)

    def testTwoChildNone(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertEqual(1, node.key)
        self.assertEqual(2, node.left.key)
        self.assertEqual(3, node.right.key)
        self.assertIsNone(node.left.right)
        self.assertIsNone(node.left.left)
        self.assertIsNone(node.right.right)
        self.assertIsNone(node.right.left)

    def testMultiLayerNode(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.right = Node(5)
        node.right.left = Node(6)
        node.right.right = Node(7)
        self.assertEqual(1, node.key)
        self.assertEqual(2, node.left.key)
        self.assertEqual(3, node.right.key)
        self.assertEqual(4, node.left.left.key)
        self.assertEqual(5, node.left.right.key)
        self.assertEqual(6, node.right.left.key)
        self.assertEqual(7, node.right.right.key)
        self.assertIsNone(node.left.left.left)
        self.assertIsNone(node.left.left.right)
        self.assertIsNone(node.left.right.left)
        self.assertIsNone(node.left.left.right)
        self.assertIsNone(node.right.left.left)
        self.assertIsNone(node.right.left.right)
        self.assertIsNone(node.right.right.left)
        self.assertIsNone(node.right.left.right)

    def testDAG1(self):
        graph = DAG()
        graph.addNode(1)

        graph.addNode(2)
        graph.addNode(3)
        graph.addNode(4)
        graph.addNode(5)
        graph.addNode(6)
        graph.addNode(7)

        graph.addEdge(1, 2)
        graph.addEdge(1, 3)
        graph.addEdge(1, 4)

        graph.addEdge(2, 5)
        graph.addEdge(2, 6)
        graph.addEdge(3, 5)
        graph.addEdge(3, 6)
        graph.addEdge(4, 5)
        graph.addEdge(4, 6)

        graph.addEdge(6, 7)
        graph.addEdge(6, 7)