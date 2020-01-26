from abc import ABC
from abc import abstractmethod
from typing import List

from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore


class LoopStrategy(ABC):
    @abstractmethod
    def loop(self, cameras: CameraPair, store: GUIStore) -> List[str]:
        pass
