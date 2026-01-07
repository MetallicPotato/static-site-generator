import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span></div>")

    def test_single_child(self):
        child_node = LeafNode("span", "single")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>single</span></div>")

