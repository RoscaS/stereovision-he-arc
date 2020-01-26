import cv2
import eel

from sources.backend.camera.CameraFactory import CameraFactory
from sources.backend.camera.Frame import Frame
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.depth_loop import DepthLoopStrategy
from sources.backend.gui.strategies.distortion_loop import \
    DistortionLoopStrategy
from sources.backend.gui.strategies.initialization_loop import \
    InitializationLoopStrategy
from sources.backend.gui.strategies.manager import LoopStrategyManager
from sources.backend.settings import FRONTEND_DIR
from sources.backend.settings import FRONTEND_ENTRY_POINT
from sources.backend.utils.camera_utils import JPGs
from sources.backend.utils.resolution_utils import Resolution


class GUIController:
    def __init__(self):
        self.loop_manager = LoopStrategyManager(InitializationLoopStrategy())
        self.store = GUIStore()
        self.state = self.store.state
        self.cameras = None

    def init_frontend_connection(self):
        frontend_path = FRONTEND_DIR
        frontend_entry_point = FRONTEND_ENTRY_POINT
        eel.init(frontend_path)
        eel.start(frontend_entry_point, size=Resolution.RESOLUTION_HD)

    def main_loop(self):
        self.state.streaming = True
        self.cameras = CameraFactory.create_camera_pair()
        print(f"Starting {self.state.looping_strategy} loop.")
        while self.state.streaming:
            self.loop_manager.run_loop(self.cameras, self.store)
            self._update_frontend_images(self.cameras.blobs)
            self.cameras.clear_frames()

        del self.cameras
        print("Python program is in standby.")

    def stop_loop(self):
        self.state.reset_state()

    def _update_frontend_images(self, jpgs: JPGs):
        eel.updateImageLeft(jpgs.left)()
        if (self.state.looping_strategy not in ['Depth', 'Calibration']):
            eel.updateImageRight(jpgs.right)()

    # OPTIONS: (backend of the API exposed in api.py file)
    def toggle_lines(self):
        self.state.lines = not self.state.lines

    def toggle_distortion(self):
        self.state.distorded = not self.state.distorded

    def set_looping_strategy(self, strategy_name: str) -> None:
        print(f"Loading {strategy_name} strategy")
        self.state.looping_strategy = strategy_name
        self.loop_manager.strategy = {
            'Initialization': InitializationLoopStrategy,
            'Calibration': None,
            'Distortion': DistortionLoopStrategy,
            'Depth': DepthLoopStrategy,
        }[strategy_name]()
