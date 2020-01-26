from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.interface import LoopStrategy


class InitializationLoopStrategy(LoopStrategy):
    def loop(self, cameras: CameraPair, store: GUIStore) -> None:
        if store.state.lines:
            cameras.draw_horizontal_lines()
