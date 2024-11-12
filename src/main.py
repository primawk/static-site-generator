from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

def main():
    # def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #     if (old_nodes[0].text_type != TextType.TEXT):
    #         return old_nodes
    #     elif (delimiter not in old_nodes[0].text):
    #         raise Exception('invalid Markdown syntax')
    #     result = []
    #     for index, text in enumerate(old_nodes[0].text.split(delimiter)):
    #         if index == 1:
    #             result.append(TextNode(text, text_type))
    #         else:
    #             result.append(TextNode(text, TextType.TEXT))
    #     print(result)
    #     return result
            
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    

main()