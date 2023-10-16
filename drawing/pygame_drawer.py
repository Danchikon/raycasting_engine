import pygame
from pygame import Surface

from drawing.drawer import Drawer


class PygameDrawer(Drawer):
    def __init__(self, surface: Surface):
        self.__surface = surface

    def rect(
            self,
            color: tuple[int, int, int],
            x: float,
            y: float,
            width: float,
            height: float,
            border: int = 0
    ):
        pygame.draw.rect(self.__surface, color, (x, y, width, height), border)

    def line(
            self,
            color: tuple[int, int, int],
            x1: float,
            y1: float,
            x2: float,
            y2: float,
            width: int = 1
    ):
        pygame.draw.line(self.__surface, color, (x1, y1), (x2, y2), width)

    def circle(
            self,
            color: tuple[int, int, int],
            x: float,
            y: float,
            radius: float,
            border: int = 0
    ):
        pygame.draw.circle(self.__surface, color, (x, y), radius, border)
