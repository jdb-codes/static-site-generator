from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = node.text.split(delimiter)
        if len(split_nodes) % 2 == 0:
            raise Exception(f"Incorrect markdown: no closing {delimiter}")
        for i in range(len(split_nodes)):
            if split_nodes[i] == "":
                continue
            if i % 2 == 0:
                new_text_node = TextNode(split_nodes[i], TextType.TEXT)
            else:
                new_text_node = TextNode(split_nodes[i], text_type)
            new_nodes.append(new_text_node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
