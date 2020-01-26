from typing import List

from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.interface import LoopStrategy


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

    def run_loop(self, cameras: CameraPair, store: GUIStore) -> List[str]:
        return self._strategy.loop(cameras, store)
