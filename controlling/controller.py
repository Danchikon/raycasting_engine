from abc import ABC, abstractmethod

from controlling.key import Key


class Controller(ABC):
    @abstractmethod
    def pressed_keys(self) -> dict[Key, bool]:
        pass

    @abstractmethod
    def get_mouse_movement(self) -> (float, float):
        pass

    @abstractmethod
    def set_mouse_pos(self, x: float, y: float):
        pass

    @abstractmethod
    def update(self):
        pass
