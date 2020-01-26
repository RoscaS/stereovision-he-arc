from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.interface import LoopStrategy


have_filter = False

class DepthLoopStrategy(LoopStrategy):

    def loop(self, cameras: CameraPair, store: GUIStore) -> None:
        pass
