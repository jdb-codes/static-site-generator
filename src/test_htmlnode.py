from test import test_print
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html()
            , ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="a", value="b", children="c", props="d")
        self.assertEqual(repr(node), 'HTMLNode:\ntag=a\nvalue=b\nchildren=c\nprops=d')

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")
