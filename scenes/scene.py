from abc import ABC, abstractmethod
from typing import List

from controlling.controllable import Controllable
from drawing.drawable import Drawable


class Scene(Controllable, Drawable, ABC):
    @property
    @abstractmethod
    def drawable(self) -> List[Drawable]:
        pass
