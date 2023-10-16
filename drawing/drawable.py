from abc import ABC, abstractmethod

from drawing.drawer import Drawer


class Drawable(ABC):
    @abstractmethod
    def draw(self, drawer: Drawer):
        pass
