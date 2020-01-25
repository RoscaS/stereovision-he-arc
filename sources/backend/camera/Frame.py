import base64
import os
from typing import NamedTuple

import cv2
import numpy as np
from cv2 import VideoCapture
from sources.backend.settings import CALIBRATION
from sources.backend.utils.resolution_utils import Shape


# Needs to be moved at some point
def load_npy_files(type: str) -> dict:
    output = CALIBRATION.calibration_folder
    left = os.path.join(output, f"{type}_map_left.npy")
    right = os.path.join(output, f"{type}_map_right.npy")
    return {'left': np.load(left), 'right': np.load(right)}


class Frame:
    DEFAULT_COLOR = (0, 0, 255)
    CALIBRATION_FOLDER: str = CALIBRATION.calibration_folder
    UNDISTORTION_MATRICES: dict = load_npy_files('undistortion')
    RECTIFICATION_MATRICES: dict = load_npy_files('rectification')
    CORRECTION_OPTIONS: list = [cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0]

    def __init__(self, source: VideoCapture, side: str):
        self.frame: np.ndarray = source.read()[1]
        self.side = side
        self._shape = None

    @property
    def shape(self) -> Shape:
        """Flyweight pattern. Frame is often
        used but shape prop is not used every time."""
        if (self._shape is None):
            width = self.frame.shape[0]
            height = self.frame.shape[1]
            self._shape = Shape(width, height)
        return self._shape

    @property
    def blob(self) -> str:
        jpg = cv2.imencode('.jpg', self.frame)[1]
        return base64.b64encode(jpg).decode('utf-8')

    def apply_correction(self) -> None:
        self.frame = cv2.remap(self.frame,
                               Frame.UNDISTORTION_MATRICES[self.side],
                               Frame.RECTIFICATION_MATRICES[self.side],
                               *Frame.CORRECTION_OPTIONS)

    def draw_horizonal_lines(self, color: tuple = DEFAULT_COLOR) -> None:
        for line in range(0, int(self.shape.width / 20)):
            self.frame[line * 20, :] = color

    def show(self) -> None:
        cv2.imshow(self.side, self.frame)

    @classmethod
    def show_stacked(cls, frames, position: tuple) -> None:
        name = "Stacked"
        cv2.namedWindow(name)
        cv2.moveWindow(name, *position)
        cv2.imshow(name, np.hstack((frames.left.frame, frames.right.frame)))


class Frames(NamedTuple):
    """Namedtuple of two `Frame`."""
    left: Frame
    right: Frame
