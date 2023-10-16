from abc import ABC, abstractmethod

from drawing.color import Color


class Display(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def fill(self, color: Color):
        pass
