import eel

from sources.gui_store import gui_store
from sources.loops.distortion import distortion_loop
from sources.loops.initialization import initialization_loop
from sources.camera.CameraFactory import CameraFactory
from sources.utils.resolution_utils import Resolution

state = gui_store.state

def reset_options():
    state.streaming = False
    state.distorded = False
    state.lines = False

@eel.expose
def toggle_lines():
    state.lines = not state.lines
@eel.expose
def toggle_distortion():
    state.distorded = not state.distorded


@eel.expose
def set_tab(tab):
    state.current_tab = tab
    print(f"{tab} loop loaded.")

@eel.expose
def stop_loop():
    reset_options()

@eel.expose
def start_loop():
    state.streaming = True
    cameras = CameraFactory.create_camera_pair()
    print(f"Starting {state.current_tab} loop.")
    while state.streaming:
        main_loop(cameras)

    del cameras
    print("Python program is in standby.")

def main_loop(cameras):
    frames = cameras.frames
    current_tab = state.current_tab
    distorded = state.distorded
    lines = state.lines

    jpgs = None

    if (current_tab == "Initialization"):
        jpgs = initialization_loop(frames, lines)
    elif (current_tab == "Calibration"):
        pass
    elif (current_tab == "Distortion"):
        jpgs = distortion_loop(frames, lines, distorded)

    eel.updateImageLeft(jpgs.left)()
    eel.updateImageRight(jpgs.right)()

if __name__ == '__main__':
    eel.init('gui')
    eel.start('index.html', size=Resolution.RESOLUTION_HD)
