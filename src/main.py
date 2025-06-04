from textnode import TextNode, TextType
from htmlnode import HTMLNode


print("hello world")

def main():
    test_object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev)")
    node = HTMLNode(props={})
    print(node)
    print(node.props_to_html())

main()
