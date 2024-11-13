from htmlnode import LeafNode
from textnode import TextType 

def text_node_to_html_node(text_node):
        for type in TextType:
            if text_node.text_type == type.value:
                if text_node.text_type == 'text':
                    return LeafNode(None, text_node.text)
                elif text_node.text_type == 'bold':
                    return LeafNode('b', text_node.text)
                elif text_node.text_type == 'italic':
                    return LeafNode('i', text_node.text)
                elif text_node.text_type == 'code':
                    return LeafNode('code', text_node.text)
                elif text_node.text_type == 'link':
                    return LeafNode('a', text_node.text, text_node.url)
                elif text_node.text_type == 'image':
                    return LeafNode('img', '', f'src={text_node.url} alt={text_node.text}')
        raise Exception('Text type does not match')    