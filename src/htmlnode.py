class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props = self.props.copy()
        props_html = ""
        for prop in props:
            props_html += f' {prop}="{props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode:\ntag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value.")
        if self.tag == None:
            return self.value
        if self.props == None:
            html = f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_string = self.props_to_html()
            html = f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
        return html

    def __repr__(self):
        return f"LeafNode:\ntag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have a children value")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        html = f"<{self.tag}>{children_html}</{self.tag}>"
        return html

    def __repr__(self):
        return f"ParentNode:\ntag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}"
