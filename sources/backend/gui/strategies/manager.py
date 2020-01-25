from sources.backend.camera.Frame import Frames
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.interface import LoopStrategy
from sources.backend.utils.camera_utils import JPGs


class LoopStrategyManager:
    """Context of the looping strategies."""

    def __init__(self, strategy: LoopStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> LoopStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: LoopStrategy) -> None:
        self._strategy = strategy

    def run_loop(self, frames: Frames, store: GUIStore) -> JPGs:
        return self._strategy.loop(frames, store)
