import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node = LeafNode("p", None, "This is a paragraph of text.")
        expected_string = "All leaf nodes must have a value"
        result = ""
        try :
            result = node.to_html()
        except ValueError as e:
            result = str(e)
        self.assertEqual(result, expected_string)
    
    def test_parent_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        expected_string = "All parent nodes must have children"
        result = ""
        try :
            result = parent_node.to_html()
        except ValueError as e:
            result = str(e)
        self.assertEqual(result, expected_string)
    
    def test_parent_to_html_no_tag(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, [child_node])
        expected_string = "All parent nodes must have a tag"
        result = ""
        try :
            result = parent_node.to_html()
        except ValueError as e:
            result = str(e)
        self.assertEqual(result, expected_string)

    def test_to_html_with_child(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><b>child</b></div>")
    
    def test_to_html_with_children(self):
        child1_node = LeafNode("b", "child1")
        child2_node = LeafNode("i", "child2")
        parent_node = ParentNode("div", [child1_node, child2_node])
        self.assertEqual(parent_node.to_html(), "<div><b>child1</b><i>child2</i></div>")

    def test_to_html_with_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_grandchildren(self):
        grandchild1_node = LeafNode("b", "grandchild1")
        grandchild2_node = LeafNode("i", "grandchild2")
        child_node = ParentNode("span", [grandchild1_node, grandchild2_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i></span></div>",
        )
    
    def test_to_html_full_tree(self):
        greatgrandchild = LeafNode("a", "greatgrandchild")
        grandchild1_node = LeafNode("b", "grandchild1")
        grandchild2_node = LeafNode("i", "grandchild2")
        grandchild3_node = ParentNode("deepspan", [greatgrandchild])
        grandchild4_node = LeafNode("d", "grandchild4")
        child1_node = ParentNode("span", [grandchild1_node, grandchild2_node])
        child2_node = LeafNode("e", "child2")
        child3_node = ParentNode("span3", [grandchild3_node, grandchild4_node])
        parent_node = ParentNode("div", [child1_node, child2_node, child3_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i></span><e>child2</e><span3><deepspan><a>greatgrandchild</a></deepspan><d>grandchild4</d></span3></div>",
        )


