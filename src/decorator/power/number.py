from abc import ABC, abstractmethod


class NumberComponent(ABC):
    @abstractmethod
    def get_value(self):
        pass

class Number(NumberComponent):
    def __init__(self, num):
        self._num = num

    def get_value(self):
        return self._num