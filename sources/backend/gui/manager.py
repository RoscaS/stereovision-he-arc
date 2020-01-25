import os

import eel

from sources.backend.camera.CameraFactory import CameraFactory
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.distortion import DistortionLoopStrategy
from sources.backend.gui.strategies.initialization import \
    InitializationLoopStrategy
from sources.backend.gui.strategies.initialization import LoopStrategy
from sources.backend.settings import ROOT_DIR
from sources.backend.utils.camera_utils import JPGs
from sources.backend.utils.resolution_utils import Resolution


class GUIManager:

    def __init__(self, strategy: LoopStrategy):
        self._strategy = strategy
        self.store = GUIStore()
        self.state = self.store.state

    @property
    def strategy(self) -> LoopStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: LoopStrategy) -> None:
        self._strategy = strategy

    def _choose_strategy(self, frames) -> JPGs:
        jpgs = self._strategy.loop(frames, self.store)
        return jpgs

    def main_loop(self):
        frames = self.cameras.frames
        jpgs = self._strategy.loop(frames, self.store)
        eel.updateImageLeft(jpgs.left)()
        eel.updateImageRight(jpgs.right)()

    def reset_state(self):
        self.state.reset_state()

    def init_frontend_connection(self):
        frontend_path = os.path.join(ROOT_DIR, 'sources', 'frontend')
        frontend_entry_point = 'index.html'
        eel.init(frontend_path)
        eel.start(frontend_entry_point, size=Resolution.RESOLUTION_HD)

    def start_loop(self):
        self.state.streaming = True
        self.cameras = CameraFactory.create_camera_pair()
        print(f"Starting {self.state.current_tab} loop.")
        while self.state.streaming:
            self.main_loop()

        del self.cameras
        print("Python program is in standby.")

    def stop_loop(self):
        self.reset_state()

    # OPTIONS
    def toggle_lines(self):
        self.state.lines = not self.state.lines

    def toggle_distortion(self):
        self.state.distorded = not self.state.distorded

    def set_tab(self, tab):
        self.state.current_tab = tab
        if (self.state.current_tab == "Initialization"):
            self.strategy = InitializationLoopStrategy()
        elif (self.state.current_tab == "Calibration"):
            pass
        elif (self.state.current_tab == "Distortion"):
            self.strategy = DistortionLoopStrategy()
        print(f"{tab} loop loaded.")
