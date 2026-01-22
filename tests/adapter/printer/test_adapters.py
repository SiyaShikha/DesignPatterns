from adapter.printer.adapters import InkJetAdapter
from adapter.printer.printers import InkJetPrinter


def test_ink_jet_adapter():
    ink_jet_printer = InkJetPrinter()
    ink_jet_adapter = InkJetAdapter(ink_jet_printer)
    assert ink_jet_adapter.print() == "ink jet"
