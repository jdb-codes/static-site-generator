import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "URL here")
        node2 = TextNode("This is a text node", TextType.BOLD, "URL here")
        self.assertEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "URL here")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_url_both(self):
        node = TextNode("This is a text node", TextType.BOLD, "URL here")
        node2 = TextNode("This is a text node", TextType.BOLD, "different URL here")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
