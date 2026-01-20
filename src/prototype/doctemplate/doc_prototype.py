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
        clone = object.__new__(DocumentationPrototype)
        clone.__dict__ = copy.deepcopy(self.__dict__)
        return clone