from adapter.printer.adapters import InkJetAdapter, LaserAdapter
from adapter.printer.app import PrinterApp
from adapter.printer.printers import InkJetPrinter, LaserPrinter

def test_app_ink_jet():
    app = PrinterApp()
    ink_jet_printer = InkJetPrinter()
    ink_jet_adapter = InkJetAdapter(ink_jet_printer)
    app.print(ink_jet_adapter)

def test_app_laser():
    app = PrinterApp()
    laser_printer = LaserPrinter()
    laser_adapter = LaserAdapter(laser_printer)
    app.print(laser_adapter)