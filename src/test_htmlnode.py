import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html.props_to_html(), 'href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        html = LeafNode(value = "weee")
        self.assertEqual(html.to_html(), 'weee')

    def test_to_html_no_props(self):
        html = LeafNode(value = "weee", tag = "p")
        self.assertEqual(html.to_html(), "<p>weee</p>")

    def test_to_html_with_props(self):
        html = LeafNode(value = "weee", tag = "a", props = {"href": "https://www.google.com"})
        self.assertEqual(html.to_html(), '<a href="https://www.google.com">weee</a>')

if __name__ == '__main__':
    unittest.main()
