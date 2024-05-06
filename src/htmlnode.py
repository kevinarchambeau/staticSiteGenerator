class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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

        if not self.props:
            return ""

        for k, v in self.props.items():
            html_list.append(f' {k}="{v}"')
        return "".join(html_list)


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError("No value")

        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def __repr__(self):
        return f"ParentNode(children: {self.children}, tag: {self.tag}, props: {self.props})"

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag")

        if not self.children:
            raise ValueError("No children")

        html = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html
