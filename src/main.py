from htmlnode import LeafNode
from htmlnode import ParentNode

def main():
    node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])

    node.to_html()

main()