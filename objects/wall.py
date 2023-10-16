from drawing.color import Color
from drawing.drawable import Drawable
from drawing.drawer import Drawer


class Wall(Drawable):

    @property
    def x1(self) -> float:
        return self.__x1

    @property
    def y1(self) -> float:
        return self.__y1

    @property
    def x2(self) -> float:
        return self.__x2

    @property
    def y2(self) -> float:
        return self.__y2

    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: Color):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__color = color

    def draw(self, drawer: Drawer):
        drawer.line(self.__color.value, self.__x1, self.__y1, self.__x2, self.__y2)
