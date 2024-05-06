import unittest

from block_markdown import (
    markdown_to_blocks, block_type_paragraph, block_type_code, block_type_heading, block_type_quote,
    block_type_ordered_list, block_type_unordered_list, block_to_block_type, markdown_to_html_node
)


class TestBlockMarkdown(unittest.TestCase):
    def test_block_markdown(self):
        # formatting the text correctly is a bit tricky
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
"""
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, ["# This is a heading",
                                  "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                                  "* This is a list item\n* This is another list item\n"])

    def test_block_type_heading(self):
        markdown = "## this is a heading"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_heading)

    def test_block_type_not_heading(self):
        markdown = "this isn't a heading\n## block"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_paragraph)

    def test_block_type_code(self):
        markdown = "```this is a code \nblock```"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_code)

    def test_block_type_quote(self):
        markdown = ">this is a quote \n>block"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_quote)

    def test_block_type_not_quote(self):
        markdown = ">this isn't a quote \nblock"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_paragraph)

    def test_block_type_unordered(self):
        markdown = "- this is an unordered \n* list block"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_unordered_list)

    def test_block_type_not_unordered(self):
        markdown = "- this is not an unordered \nlist block"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_paragraph)

    def test_block_type_ordered(self):
        markdown = "1. this is an ordered \n2. list block"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_ordered_list)

    def test_block_type_not_ordered(self):
        markdown = "1. this isn't an ordered \n3. list block"
        result = block_to_block_type(markdown)
        self.assertEqual(result, block_type_paragraph)


def test_paragraph(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
    )


def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )


def test_lists(self):
    md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
    )


def test_headings(self):
    md = """
# this is an h1

this is paragraph text

## this is an h2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
    )


def test_blockquote(self):
    md = """
> This is a
> blockquote block

this is paragraph text

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
    )


if __name__ == "__main__":
    unittest.main()
