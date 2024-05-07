import unittest
from textnode import (
    TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link
)
from inline_markdown import (
    split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link,
    text_to_textnodes
)


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
        self.assertEqual(result, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/"
                                            "course_assets/zjjcJKZ.png"),
                                  ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets"
                                              "/course_assets/dfsdkjfd.png")])

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
                         )


if __name__ == "__main__":
    unittest.main()
