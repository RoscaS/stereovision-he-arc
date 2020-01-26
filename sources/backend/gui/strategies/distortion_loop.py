from typing import List

from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.initialization_loop import \
    InitializationLoopStrategy


class DistortionLoopStrategy(InitializationLoopStrategy):
    def loop(self, cameras: CameraPair, store: GUIStore) -> List[str]:
        if store.state.distorded:
            if store.state.lines:
                return cameras.jpg_corrected_lines()

            return cameras.jpg_corrected()

        return super().loop(cameras, store)
