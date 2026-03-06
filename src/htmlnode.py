


class HTMLNode:
    def __init__(self, tag :str|None =None, value :str|None =None, children :list['HTMLNode']|None =None, props :dict|None =None):
        self.tag = tag
        self.value = value
        self. children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f'{key}="{value}" '
        return result.strip()
    
    def __repr__(self):
        return f"HTML Node: {self.tag}, {self.value}"

