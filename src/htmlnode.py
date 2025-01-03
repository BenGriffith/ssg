class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        children = []
        for child in self.children:
            children.append(f"{child.__class__.__name__}({child.tag}, {child.value}, {child.children}, {child.props})")
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {children}, {self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_attributes = []
        for key, value in self.props.items():
            html_attributes.append(f'{key}="{value}"')
        return ' '.join(html_attributes)