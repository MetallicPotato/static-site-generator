class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        properties = ""
        for key in self.props.keys():
            newprop = " " + key + "="
            newprop += self.props[key]
            properties += newprop
        return properties
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def __eq__(self, other):
        if self.children == other.children and self.props == other.props and self.tag == other.tag and self.value == other.value:
            return True
        return False
