from sources.backend.camera.CameraPair import CameraPair
from sources.backend.gui.strategies.interface import LoopStrategy


class InitializationLoopStrategy(LoopStrategy):
    def loop(self, frames, store):
        if store.state.lines:
            CameraPair.draw_horizontal_lines(frames)

        jpgs = CameraPair.make_blobs_from(frames)

        return jpgs
