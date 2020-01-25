from abc import ABC
from abc import abstractmethod


class LoopStrategy(ABC):

    @abstractmethod
    def loop(self, frames, store):
        pass
