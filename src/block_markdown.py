import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_block_type(block):
    heading_regex = r"^(#){1,6} "
    code_regex = r"(^`{3}.*`{3}$)"
    quote_regex = r"(^>(.*))"
    unordered_regex = r"(^\*|- )"
    ordered_regex = r"(^\d. )"

    if re.match(code_regex, block, re.S):
        return block_type_code

    lines = block.split("\n")

    is_all_ordered = True
    for i in range(0, len(lines)):
        if i == 0 and re.match(ordered_regex, lines[i]):
            if int(lines[i][0]) != 1:
                is_all_ordered = False
                break
        elif not re.match(ordered_regex, lines[i]):
            is_all_ordered = False
            break
        elif re.match(ordered_regex, lines[i]):
            if not int(lines[i - 1][0]) + 1 == int(lines[i][0]):
                is_all_ordered = False
                break

    if is_all_ordered:
        return block_type_ordered_list

    is_all_header = True
    is_all_quotes = True
    is_all_unordered = True
    for line in lines:
        if not re.match(heading_regex, line):
            is_all_header = False
        if not re.match(quote_regex, line):
            is_all_quotes = False
        if not re.match(unordered_regex, line):
            is_all_unordered = False

    if is_all_header:
        return block_type_heading
    if is_all_quotes:
        return block_type_quote
    if is_all_unordered:
        return block_type_unordered_list

    return block_type_paragraph


# def block_to_block_type(block):
#     lines = block.split("\n")
#
#     if (
#             block.startswith("# ")
#             or block.startswith("## ")
#             or block.startswith("### ")
#             or block.startswith("#### ")
#             or block.startswith("##### ")
#             or block.startswith("###### ")
#     ):
#         return block_type_heading
#     if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
#         return block_type_code
#     if block.startswith(">"):
#         for line in lines:
#             if not line.startswith(">"):
#                 return block_type_paragraph
#         return block_type_quote
#     if block.startswith("* "):
#         for line in lines:
#             if not line.startswith("* "):
#                 return block_type_paragraph
#         return block_type_unordered_list
#     if block.startswith("- "):
#         for line in lines:
#             if not line.startswith("- "):
#                 return block_type_paragraph
#         return block_type_unordered_list
#     if block.startswith("1. "):
#         i = 1
#         for line in lines:
#             if not line.startswith(f"{i}. "):
#                 return block_type_paragraph
#             i += 1
#         return block_type_ordered_list
#     return block_type_paragraph


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case "paragraph":
            return paragraph_to_html_node(block)
        case "heading":
            return heading_to_html_node(block)
        case "code":
            return code_to_html_node(block)
        case "ordered_list":
            return ordered_list_to_html_node(block)
        case "unordered_list":
            return unordered_list_to_html_node(block)
        case "quote":
            return quote_to_html_node(block)
        case _:
            raise ValueError("Invalid block type")


def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
