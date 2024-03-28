class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, compare_node):
        if self.text == compare_node.text:
            if self.text_type == compare_node.text_type:
                if self.url == compare_node.url:
                    return True

        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
