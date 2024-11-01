from textnode import TextNode
from htmlnode import LeafNode


def main():
    LeafNode("p", "This is a paragraph of text.").to_html()

main()