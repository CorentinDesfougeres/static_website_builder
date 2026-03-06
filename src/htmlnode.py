


class HTMLNode:
    def __init__(self, tag :str|None =None, value :str|None =None, children :list['HTMLNode']|None =None, props :dict|None =None):
        self.tag = tag
        self.value = value
        self. children = children
        self.props = props
    
    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f'{key}="{value}" '
        return result.strip()
    
    def __repr__(self):
        return f"HTML Node: {self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag :str|None, value :str|None, props :dict|None =None):
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        
        if not self.tag:
            return(self.value)
        
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"HTML Leaf Node: {self.tag}, {self.value}, {self.props}"
