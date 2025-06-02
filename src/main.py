from textnode import TextNode, TextType


print("hello world")

def main():
    test_object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev)")
    text_to_print = test_object.__repr__()
    print(text_to_print)

main()
