import sys

import pygame

from controlling.controller import Controller
from controlling.key import Key


class PygameController(Controller):
    def __init__(self):
        self.__mouse_movement_x: float = 0
        self.__mouse_movement_y: float = 0

    def pressed_keys(self) -> dict[Key, bool]:
        state = {
            Key.W: False,
            Key.S: False,
            Key.A: False,
            Key.D: False,
            Key.N1: False,
            Key.N2: False,
        }

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            state[Key.W] = True
        if keys[pygame.K_s]:
            state[Key.S] = True
        if keys[pygame.K_a]:
            state[Key.A] = True
        if keys[pygame.K_d]:
            state[Key.D] = True
        if keys[pygame.K_1]:
            state[Key.N1] = True
        if keys[pygame.K_2]:
            state[Key.N2] = True

        return state

    def get_mouse_movement(self) -> (float, float):
        return self.__mouse_movement_x, self.__mouse_movement_y

    def set_mouse_pos(self, x: float, y: float):
        pygame.mouse.set_pos((x, y))

    def update(self):
        (mouse_movement_x, mouse_movement_y) = pygame.mouse.get_rel()

        self.__mouse_movement_x = mouse_movement_x
        self.__mouse_movement_y = mouse_movement_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key is pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()



