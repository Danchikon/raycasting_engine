from math import cos, sin

from controlling.controllable import Controllable
from controlling.controller import Controller
from controlling.key import Key
from drawing.color import Color
from drawing.drawable import Drawable
from drawing.drawer import Drawer


class Player(Drawable, Controllable):
    @property
    def angle(self):
        return self.__angle

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def rov(self):
        return self.__ROV

    @property
    def fov(self):
        return self.__FOV

    def __init__(
            self,
            x: int,
            y: int,
            angle: float,
            move_speed: float,
            rotation_speed: float,
            rov: float,
            fov: float,
            color: Color,
            size: int
            ):

        self.__x = x
        self.__y = y
        self.__color = color
        self.__size = size
        self.__angle = angle
        self.__move_speed = move_speed
        self.__rotation_speed = rotation_speed
        self.__ROV = rov
        self.__FOV = fov

    def draw(self, drawer: Drawer):
        drawer.circle(self.__color.value, self.__x, self.__y, self.__size)

    def control(self, controller: Controller, elapsed: float):
        keys = controller.pressed_keys()
        (mouse_movement_x, _) = controller.get_mouse_movement()

        delta_x = cos(self.__angle) * self.__move_speed * elapsed
        delta_y = sin(self.__angle) * self.__move_speed * elapsed

        delta_angle = self.__rotation_speed * mouse_movement_x
        self.__angle += delta_angle

        if keys[Key.W]:
            self.__x += delta_x
            self.__y += delta_y
        if keys[Key.S]:
            self.__x -= delta_x
            self.__y -= delta_y



