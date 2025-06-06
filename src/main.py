from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode


print("hello world")

def main():
    test_object = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(test_object)
    print(test_object.props_to_html())

main()
