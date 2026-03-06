import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_default(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_type_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_not_equal(self):
        node = TextNode("This is a text node", TextType.IMAGE, "An url")
        node2 = TextNode("This is a text node", TextType.IMAGE, "A different url")
        self.assertNotEqual(node, node2)
    
    def test_url_not_equal_to_none(self):
        node = TextNode("This is a text node", TextType.IMAGE, "An url")
        node2 = TextNode("This is a text node", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()