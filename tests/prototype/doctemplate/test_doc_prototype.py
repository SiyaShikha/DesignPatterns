def test_clone_preserves_layout():
    prototype = Prototype()
    prototype.header = "Company Header"
    prototype.footer = "Confidential"
    prototype.margin = 20

    clone = prototype.clone()
    assert clone.header == prototype.header
    assert clone.footer == prototype.footer
    assert clone.margin == prototype.margin
