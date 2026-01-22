from adapter.printer.adapters import InkJetAdapter, LaserAdapter
from adapter.printer.printers import InkJetPrinter, LaserPrinter


def test_ink_jet_adapter():
    ink_jet_printer = InkJetPrinter()
    ink_jet_adapter = InkJetAdapter(ink_jet_printer)
    assert ink_jet_adapter.print() == "ink jet"

def test_laser_adapter():
    laser_printer = LaserPrinter()
    laser_adapter = LaserAdapter(laser_printer)
    assert laser_adapter.print() == "laser"
