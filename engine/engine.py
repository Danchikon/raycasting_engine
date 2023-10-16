import time
from math import cos, sin
from typing import List

from caster import rays, intersection

from controlling.controllable import Controllable
from controlling.controller import Controller
from display.display import Display
from drawing.color import Color
from drawing.drawable import Drawable
from drawing.drawer import Drawer
from objects.circle import Circle
from objects.wall import Wall
from player.player import Player
from timing.timer import Timer


class Engine:
    def __init__(
            self,
            player: Player,
            walls: List[Wall],
            circles: List[Circle],
            display: Display,
            drawer: Drawer,
            controller: Controller,
            timer: Timer,
            fps: float
    ):
        self.__fps = fps
        self.__player = player
        self.__walls = walls
        self.__display = display
        self.__drawer = drawer
        self.__controller = controller
        self.__timer = timer
        self.__controllable: List[Controllable] = [player]
        self.__drawable: List[Drawable] = [player]
        self.__drawable.extend(walls)
        self.__drawable.extend(circles)
        self.__lines = []
        self.__circles = []

        for wall in walls:
            self.__lines.append((wall.x1, wall.y1, wall.x2, wall.y2))

        for circle in circles:
            self.__circles.append((circle.x, circle.y, circle.radius))

    def update(self):
        elapsed = self.__timer.elapsed()
        self.__timer.tick(self.__fps)

        self.__controller.update()
        self.__controller.set_mouse_pos(640, 320)

        for controllable in self.__controllable:
            controllable.control(self.__controller, elapsed)

        self.__display.fill(Color.BLACK)

        for drawable in self.__drawable:
            drawable.draw(self.__drawer)

        rays_list = rays(
            self.__player.angle,
            self.__player.fov,
            400,
            self.__player.x,
            self.__player.y,
            self.__player.rov,
            self.__lines,
            self.__circles,
            0.01
        )

        for ray in rays_list:
            if ray.intersection is None:
                x = cos(ray.angle) * self.__player.rov + self.__player.x
                y = sin(ray.angle) * self.__player.rov + self.__player.y
                self.__drawer.line((200, 200, 200), self.__player.x, self.__player.y, x, y, 1)
            else:
                self.__drawer.line((255, 255, 0), self.__player.x, self.__player.y, ray.intersection.x, ray.intersection.y, 1)

        self.__display.update()

        print(self.__timer.fps())
