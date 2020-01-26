from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.initialization_loop import \
    InitializationLoopStrategy


class DistortionLoopStrategy(InitializationLoopStrategy):
    def loop(self, cameras: CameraPair, store: GUIStore) -> None:
        if store.state.distorded:
            cameras.apply_corrections()

        super().loop(cameras, store)
