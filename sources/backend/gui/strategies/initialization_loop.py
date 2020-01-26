from typing import List

from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.interface import LoopStrategy


class InitializationLoopStrategy(LoopStrategy):
    def loop(self, cameras: CameraPair, store: GUIStore) -> List[str]:
        if store.state.lines:
            return cameras.jpg_lines()

        return cameras.jpg_frame()
