from abc import ABC, abstractmethod


class Drawer(ABC):
    @abstractmethod
    def rect(
            self,
            color: tuple[int, int, int],
            x: float,
            y: float,
            width: float,
            height: float,
            border: int = 0
    ):
        pass

    @abstractmethod
    def line(
            self,
            color: tuple[int, int, int],
            x1: float,
            y1: float,
            x2: float,
            y2: float,
            width: int = 1
    ):
        pass

    @abstractmethod
    def circle(
            self,
            color: tuple[int, int, int],
            x: float,
            y: float,
            radius: float,
            border: int = 0
    ):
        pass

