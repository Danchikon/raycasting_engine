from pygame.time import Clock

from timing.timer import Timer


class PygameTimer(Timer):
    def __init__(self, clock: Clock):
        self.__clock = clock

    def elapsed(self) -> int:
        return self.__clock.get_time()

    def tick(self, fps: float):
        self.__clock.tick(fps)

    def fps(self) -> float:
        return self.__clock.get_fps()
