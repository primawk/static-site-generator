import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):   
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertIsNone(node)

    def test_noneq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertIsNone(node)



if __name__ == "__main__":
    unittest.main()