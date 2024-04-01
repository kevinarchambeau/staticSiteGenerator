class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_list = []

        for k, v in self.props.items():
            html_list.append(f'{k}="{v}"')
        return " ".join(html_list)


class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(tag, value, None, props)

        self.value = value
        self.tag = tag
        self.props = props

    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"

    def to_html(self):
        if not self.value:
            raise ValueError

        if not self.tag:
            return self.value

        return f'"{self.tag}"'

