import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):   
        node = HTMLNode("p", "This is a paragraph node")
        node2 = HTMLNode("p", "This is a paragraph node")
        self.assertEqual(node, node2)

    # def test_none(self):
    #     node = HTMLNode("p", "This is a paragraph node")
    #     self.assertIsNone(node)

    def test_noneq(self):
        node = HTMLNode("p", "This is a paragraph node")
        node2 = HTMLNode("h1", "This is a paragraph node")
        self.assertNotEqual(node.tag, node2.tag)

if __name__ == "__main__":
    unittest.main()