import pygame
from pygame import Surface

from display.display import Display
from drawing.color import Color


class PygameDisplay(Display):
    def __init__(self, surface: Surface):
        self.__surface = surface

    def update(self):
        pygame.display.update()

    def fill(self, color: Color):
        self.__surface.fill(color.value)
