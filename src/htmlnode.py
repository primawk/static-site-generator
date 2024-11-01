class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def to_html(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        print(self)
        if self.value == None:
            raise ValueError("Value can not be empty.")
        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag} href={self.props}>{self.value}</{self.tag}>'
    

        

    


