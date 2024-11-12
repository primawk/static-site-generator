from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    

main()