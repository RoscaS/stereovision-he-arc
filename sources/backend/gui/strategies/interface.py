from abc import ABC
from abc import abstractmethod

from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.utils.camera_utils import JPGs


class LoopStrategy(ABC):
    @abstractmethod
    def loop(self, cameras: CameraPair, store: GUIStore) -> None:
        pass
