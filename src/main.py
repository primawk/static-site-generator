from textnode import TextNode

def main():
    dummy = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    dummy_2 = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(dummy == dummy_2)

main()