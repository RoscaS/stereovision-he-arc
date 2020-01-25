from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.strategies.initialization import \
    InitializationLoopStrategy

class DistortionLoopStrategy(InitializationLoopStrategy):

    def loop(self, frames, store):
        if not store.state.distorded:
            CameraPair.apply_corrections(frames)

        return super().loop(frames, store)

