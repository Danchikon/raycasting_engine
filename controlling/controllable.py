from abc import ABC, abstractmethod

from controlling.controller import Controller


class Controllable(ABC):
    @abstractmethod
    def control(self, controller: Controller, elapsed: float):
        pass
