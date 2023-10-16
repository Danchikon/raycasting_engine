from drawing.color import Color
from drawing.drawable import Drawable
from drawing.drawer import Drawer


class Circle(Drawable):

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def radius(self) -> float:
        return self.__radius

    def __init__(self, x: float, y: float, radius: float, color: Color):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__color = color

    def draw(self, drawer: Drawer):
        drawer.circle(self.__color.value, self.__x, self.__y, self.__radius, 1)
