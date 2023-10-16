from abc import abstractmethod, ABC


class Timer(ABC):

    @abstractmethod
    def elapsed(self) -> int:
        pass

    @abstractmethod
    def tick(self, fps: float):
        pass

    @abstractmethod
    def fps(self) -> float:
        pass
