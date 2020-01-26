import base64
import os

import cv2
import numpy as np

from sources.backend.settings import CALIBRATION


DEFAULT_COLOR = (0, 0, 255)

min_disp = 2
num_disp = 128
uniqueness = 10
speckleWindowSize = 100
speckleRange = 32


def color_gray(frame: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def draw_horizonal_lines(frame: np.ndarray,
                         color: tuple = DEFAULT_COLOR) -> np.ndarray:
    new_frame = frame.copy()
    for line in range(0, int(new_frame.shape[0] / 20)):
        new_frame[line * 20, :] = color
    return new_frame


def frame_to_jpg(frame: np.ndarray) -> str:
    jpg = cv2.imencode('.jpg', frame)[1]
    return base64.b64encode(jpg).decode('utf-8')


def load_npy_files(type: str) -> dict:
    output = CALIBRATION['calibration_folder']
    left = os.path.join(output, f"{type}_map_left.npy")
    right = os.path.join(output, f"{type}_map_right.npy")
    return {'left': np.load(left), 'right': np.load(right)}


def init_sgbm():
    window_size = 3
    return cv2.StereoSGBM_create(minDisparity=min_disp,
                                 numDisparities=num_disp,
                                 blockSize=window_size,
                                 uniquenessRatio=uniqueness,
                                 speckleWindowSize=speckleWindowSize,
                                 speckleRange=speckleRange,
                                 disp12MaxDiff=5,
                                 P1=8 * 3 * window_size ** 2,
                                 P2=32 * 3 * window_size ** 2)


def init_right_matcher(sbm):
    return cv2.ximgproc.createRightMatcher(sbm)


def init_wls_filter(sbm, lam=8000, sig=.8):
    wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=sbm)
    wls_filter.setLambda(lam)
    wls_filter.setSigmaColor(sig)
    return wls_filter


def closing_transformation(image, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    closed = (closing - closing.min()) * 255
    return closed.astype(np.uint8)


def fix_disparity(map):
    # Bring furthest points in image to 0 disp
    return ((map.astype(np.float32) / 16) - min_disp) / num_disp
