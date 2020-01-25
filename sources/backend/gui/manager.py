import eel

from sources.backend.camera.CameraFactory import CameraFactory
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.distortion_loop import \
    DistortionLoopStrategy
from sources.backend.gui.strategies.initialization_loop import \
    InitializationLoopStrategy
from sources.backend.gui.strategies.manager import LoopStrategyManager
from sources.backend.settings import FRONTEND_DIR
from sources.backend.settings import FRONTEND_ENTRY_POINT
from sources.backend.utils.resolution_utils import Resolution


class GUIController:
    def __init__(self):
        self.loop_manager = LoopStrategyManager(InitializationLoopStrategy())
        self.store = GUIStore()
        self.state = self.store.state

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
            frames = self.cameras.frames
            jpgs = self.loop_manager.run_loop(frames, self.store)
            eel.updateImageLeft(jpgs.left)()
            eel.updateImageRight(jpgs.right)()

        del self.cameras
        print("Python program is in standby.")

    def stop_loop(self):
        self.state.reset_state()

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
        }[strategy_name]()
