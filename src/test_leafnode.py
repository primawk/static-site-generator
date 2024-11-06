import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):   
        node = LeafNode("p", "This is a paragraph node")
        node2 = LeafNode("p", "This is a paragraph node")
        self.assertEqual(node, node2)

    # def test_none(self):
    #     node = LeafNode("p", "This is a paragraph node")
    #     self.assertIsNone(node)

    def test_noneq(self):
        node = LeafNode("p", "This is a paragraph node")
        node2 = LeafNode("h1", "This is a paragraph node")
        self.assertNotEqual(node.tag, node2.tag)

if __name__ == "__main__":
    unittest.main()