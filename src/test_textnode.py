import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("https://example.com", TextType.LINK, "https://example.com")
        node2 = TextNode("https://example.com", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_url_diff(self):
        node = TextNode("https://example.com", TextType.LINK, "https://example.com")
        node2 = TextNode("https://example.org", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()