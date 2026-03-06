import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Some text.", [], None)
        expected_string = ''
        self.assertEqual(node.props_to_html(), expected_string)
    
    def test_props_to_html_one_attribute(self):
        node = HTMLNode("a", "A link", [], {"href": "https://www.google.com"})
        expected_string = 'href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected_string)
    
    def test_props_to_html_two_attributes(self):
        node = HTMLNode("a", "A link", [], {"href": "https://www.google.com", "target": "_blank"})
        expected_string = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_string)
    
    def test_leaf_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_string = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_string)
    
    def test_leaf_to_html_one_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_string = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_string)
    
    def test_leaf_to_html_two_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        expected_string = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected_string)
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw string.")
        expected_string = 'Raw string.'
        self.assertEqual(node.to_html(), expected_string)
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_string = "<p>This is a paragraph of text.</p>"
        result = ""
        try :
            result = node.to_html()
        except ValueError as e:
            result = e
        self.assertEqual(result, expected_string)

