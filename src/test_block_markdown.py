import unittest

from block_markdown import (
    markdown_to_blocks, block_type_paragraph, block_type_code, block_type_heading, block_type_quote,
    block_type_ordered_list, block_type_unordered_list, block_to_block_type
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


if __name__ == "__main__":
    unittest.main()
