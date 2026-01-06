import unittest

from htmlnode import HTMLNode

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

childnode = HTMLNode("thing", "this is another value!", [], {"href":"https://www.google.com"})
node = HTMLNode("tag", "this is a value!", [childnode], {"href":"https://www.google.com"})
node2 = HTMLNode("tag", "this is a value!", [childnode], {"href":"https://www.google.com"})
print(node)
print(node2)
if node == node2:
    print("equal!")
else:
    print("not equal.")