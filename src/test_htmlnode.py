import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode("tag", "this is a value!", [], {"href":"https://www.google.com"})
        node2 = HTMLNode("tag", "this is a value!", [])
        self.assertNotEqual(node, node2)
    
    def test_equal(self):
        childnode = HTMLNode("thing", "this is another value!", [], {"href":"https://www.google.com"})
        node = HTMLNode("tag", "this is a value!", [childnode], {"href":"https://www.google.com"})
        node2 = HTMLNode("tag", "this is a value!", [childnode], {"href":"https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_props_to_html(self):
        html_text =  ' href=https://www.google.com target=_blank'
        node = HTMLNode("tag", "this is a value!", [], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(html_text, node.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_props_not_equal(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, world!", {"href": "https://www.google.com",})
        self.assertNotEqual(node, node2)

    def test_different_leaves(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Hello, different world!")
        self.assertNotEqual(node, node2)