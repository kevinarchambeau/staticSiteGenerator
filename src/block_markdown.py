import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    regex = r"(?:\r?\n){2,}"

    blocks = re.split(regex, markdown)
    return blocks


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
