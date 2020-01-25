from sources.camera.CameraPair import CameraPair
from sources.camera.Frame import Frame
from sources.utils.camera_utils import Frames
from sources.utils.stereo_vision_utils import *

undistortionR, undistortionL = load_npy_files("undistortion")
rectificationR, rectificationL = load_npy_files("rectification")


def distortion_loop(frames, lines, distorded):

    if distorded:
        pair = frames
    else:
        rectifiedR = rectify_frame(frames.right.frame, undistortionR, rectificationR)
        rectifiedL = rectify_frame(frames.left.frame, undistortionL, rectificationL)
        pair = Frames(Frame(source=rectifiedL), Frame(source=rectifiedR))

    if lines:
        CameraPair.draw_horizontal_lines(pair)

    jpgs = CameraPair.make_blobs_from(pair)


    return jpgs




