from abc import ABC, abstractmethod

from adapter.printer.printers import InkJetPrinter

class Printer(ABC):
    def print(self):
        pass

class InkJetAdapter(Printer):
    def __init__(self, printer):
        self._printer = printer

    def print(self):
        return self._printer.print_via_ink_jet()
    
class LaserAdapter(Printer):
    def __init__(self, printer):
        self._printer = printer

    def print(self):
        return self._printer.print_via_laser()
