import unittest
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


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

    def test_extract_image(self):
        text = ("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/"
                "course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets"
                "/course_assets/dfsdkjfd.png)")
        result = extract_markdown_images(text)
        self.assertEqual(result,[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/"
                "course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets"
              "/course_assets/dfsdkjfd.png")] )

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])


if __name__ == "__main__":
    unittest.main()
