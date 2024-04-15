import unittest
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code
from inline_markdown import split_nodes_delimiter


class TestInlineMarkdown(unittest.TestCase):

    def test_split(self):
        node = TextNode("This is text with a `code block` word", "text")
        result = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(result, [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text)
        ])

    def test_invalid_split(self):
        node = TextNode("This is text with a code block` word", "text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", "code")

    def test_split_multi(self):
        node = TextNode("This is text with `two` `code block` words", "text")
        result = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(result, [
            TextNode("This is text with ", text_type_text),
            TextNode("two", text_type_code),
            TextNode(" ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" words", text_type_text)
        ])


if __name__ == "__main__":
    unittest.main()
