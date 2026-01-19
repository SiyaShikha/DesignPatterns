from prototype.doctemplate.doc_prototype import DocumentationPrototype


def test_clone_preserves_layout():
    prototype = DocumentationPrototype("Header", "Footer", 20)

    clone = prototype.clone()
    assert clone.header == prototype.header
    assert clone.footer == prototype.footer
    assert clone.margin == prototype.margin

def test_clone_returns_new_instance_of_same_class():
    prototype = DocumentationPrototype("Header", "Footer", 20)
    clone = prototype.clone()
    assert clone is not prototype
    assert clone.__class__ is prototype.__class__

def test_modifying_clone_does_not_modify_prototype():
    prototype = DocumentationPrototype("Header", "Footer", 20)
    clone = prototype.clone()
    clone.header = "New Header"
    assert prototype.header == "Header"
    assert clone.header == "New Header"