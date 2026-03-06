import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    # Testing props_to_html
    def test_props_to_html_empty(self):
        node = HTMLNode("<a>", "A link", [], None)
        expected_string = ''
        self.assertEqual(node.props_to_html(), expected_string)
    
    def test_props_to_html_one_attribute(self):
        node = HTMLNode("<a>", "A link", [], {"href": "https://www.google.com"})
        expected_string = 'href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected_string)
    
    def test_props_to_html_two_attributes(self):
        node = HTMLNode("<a>", "A link", [], {"href": "https://www.google.com", "target": "_blank"})
        expected_string = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_string)