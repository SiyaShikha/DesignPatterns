import copy

class DocumentationPrototype:
    def __init__(self, header, footer, margin):
        self.header = header
        self.footer = footer
        self.margin = margin
        self.content = None

    def set_content(self, content):
        self.content = content

    def clone(self):
        state = self.__dict__.copy()
        state["content"] =copy.deepcopy(self.content)
        clone = object.__new__(DocumentationPrototype)
        clone.__dict__ = state
        return clone
    
# prototype = DocumentationPrototype('header','footer','20')
# clone = prototype.clone()
# print(clone.__dict__)
# print(prototype.__dict__)