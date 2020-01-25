import eel

from sources.loops.distortion import distortion_loop
from sources.loops.initialization import initialization_loop
from sources.camera.CameraFactory import CameraFactory
from sources.utils.resolution_utils import Resolution

streaming = False
distorded = False
lines = False
current_tab = "Initialization"

def reset_options():
    global distorded, lines, streaming
    streaming = False
    distorded = False
    lines = False

@eel.expose
def toggle_lines():
    global lines
    lines = not lines

@eel.expose
def toggle_distortion():
    global distorded
    distorded = not distorded

@eel.expose
def set_tab(tab):
    global current_tab
    current_tab = tab
    print(f"{current_tab} loop loaded.")

@eel.expose
def stop_loop():
    reset_options()

@eel.expose
def start_loop():
    global streaming
    streaming = True
    cameras = CameraFactory.create_camera_pair()
    print(f"Starting {current_tab} loop.")
    while streaming:
        main_loop(cameras)

    del cameras
    print("Python program is in standby.")

def main_loop(cameras):
    frames = cameras.frames

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
