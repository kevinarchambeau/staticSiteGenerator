import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_string_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_string_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "other")
        self.assertNotEqual(node, node2)

    def test_eq_is_true(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertTrue(node.__eq__(node2))

    def test_eq_is_false(self):
        node = TextNode("This is a text node", "something", "other")
        node2 = TextNode("This is a text node", "bold")
        self.assertFalse(node.__eq__(node2))


if __name__ == "__main__":
    unittest.main()
