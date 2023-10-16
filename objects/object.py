from abc import ABC, abstractmethod
from typing import List


class Object(ABC):
    @property
    @abstractmethod
    def vectors(self) -> List[(float, float, float, float)]:
        pass