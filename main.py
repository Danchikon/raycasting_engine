from math import radians, pi, cos, sin
from typing import List

import pygame
from pygame import QUIT, KEYUP

import caster
from controlling.pygame_controller import PygameController
from display.pygame_display import PygameDisplay
from drawing.color import Color
from drawing.pygame_drawer import PygameDrawer
from engine.engine import Engine
from objects.circle import Circle
from objects.wall import Wall
from player.player import Player
from timing.pygame_timer import PygameTimer


def circle(x: float, y: float, sections: int, radius: float) -> List[Wall]:
    result = []

    prev_angle = 0

    for section in range(sections + 1):
        angle = section / sections * pi * 2

        x1 = cos(prev_angle) * radius + x
        y1 = sin(prev_angle) * radius + y
        x2 = cos(angle) * radius + x
        y2 = sin(angle) * radius + y

        result.append(Wall(x1, y1, x2, y2, Color.OCEAN))

        prev_angle = angle

    return result


caption = 'Raycasting 2D'

res = (1280, 720)

caster.init()

pygame.init()
pygame.display.set_caption(caption)
pygame.event.set_allowed([QUIT, KEYUP])
pygame.mouse.set_visible(False)

surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

display = PygameDisplay(surface)
drawer = PygameDrawer(surface)
controller = PygameController()
timer = PygameTimer(clock)
player = Player(10, 10, radians(45), 0.2, 0.01, 600, radians(60), Color.RED, 10)
walls = [
    Wall(140, 140, 520, 520, Color.GREEN),
    Wall(600, 140, 1220, 100, Color.PURPLE),
    Wall(600, 140, 670, 300, Color.PURPLE),
    Wall(1220, 340, 1240, 800, Color.BROWN),
]
circles = [
    Circle(0, 0, 100, Color.OCEAN),
    Circle(0, 720, 100, Color.OCEAN),
    Circle(1280, 0, 100, Color.OCEAN),
    Circle(1280, 720, 100, Color.OCEAN),
    Circle(1000, 600, 100, Color.OCEAN),
    Circle(640, 360, 400, Color.OCEAN)
]

engine = Engine(player, walls, circles, display, drawer, controller, timer, 2260)


if __name__ == "__main__":
    while True:
        engine.update()
