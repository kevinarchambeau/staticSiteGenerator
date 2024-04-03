import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = LeafNode("", "weee")
        self.assertEqual(node.to_html(), 'weee')

    def test_to_html_no_props(self):
        node = LeafNode("p", "weee")
        self.assertEqual(node.to_html(), "<p>weee</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "weee", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">weee</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_no_children(self):
        node = ParentNode("a", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_children_and_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com"}
        )
        self.assertEqual(node.to_html(), '<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_nested_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "nested Bold text"),
                        LeafNode(None, "nested Normal text"),
                        LeafNode("i", "nested italic text"),
                        LeafNode(None, "nested Normal text"),
                    ],
                )
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p>'
                                         '<b>nested Bold text</b>nested Normal text<i>nested italic text'
                                         '</i>nested Normal text</p></p>')

if __name__ == '__main__':
    unittest.main()
