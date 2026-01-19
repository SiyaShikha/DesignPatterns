class DocumentationPrototype:
    def __init__(self, header, footer, margin):
        self.header = header
        self.footer = footer
        self.margin = margin

    def set_content(self, content):
        self.content = content

    def clone(self):
        return DocumentationPrototype(self.header, self.footer, self.margin)