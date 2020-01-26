import cv2
import numpy as np

from sources.backend.camera.Component import Component
from sources.backend.camera.img_utils import color_gray
from sources.backend.camera.img_utils import draw_horizonal_lines
from sources.backend.camera.img_utils import frame_to_jpg
from sources.backend.camera.img_utils import load_npy_files
from sources.backend.settings import DEVICES


class Camera(Component):

    def __init__(self, id: int):
        self.id = id
        self.video = cv2.VideoCapture(id)
        self.width: int = None
        self.height: int = None
        self.side: str = None

        self._frame: np.ndarray = None
        self._lines: np.ndarray = None
        self._gray: np.ndarray = None
        self._corrected: np.ndarray = None
        self._corrected_lines: np.ndarray = None

        self._init_options()

    ######################################
    #  COMPONENT INTERFACE IMPLEMENTATION
    ######################################

    def clear_frames(self) -> None:
        self._frame = None
        self._lines = None
        self._gray = None
        self._corrected = None
        self._corrected_lines = None

    ###################
    #  Core
    ###################

    def frame(self) -> np.ndarray:
        if self._frame is None:
            self._frame = self.video.read()[1]
        return self._frame

    def frame_lines(self) -> np.ndarray:
        if self._lines is None:
            self._lines = draw_horizonal_lines(self.frame())
        return self._lines

    def frame_gray(self) -> np.ndarray:
        if self._gray is None:
            self._gray = color_gray(self.frame())
        return self._gray

    def frame_corrected(self) -> np.ndarray:
        if self._corrected is None:
            self._corrected = self._correct(self.frame())
        return self._corrected

    def frame_corrected_lines(self) -> np.ndarray:
        if self._corrected_lines is None:
            self._corrected_lines = draw_horizonal_lines(self.frame_corrected())
        return self._corrected_lines

    ###################
    #  For cmd
    ###################

    def show_frame(self) -> None:
        cv2.imshow(str(self.id), self.frame())

    def show_lines(self) -> None:
        cv2.imshow(str(self.id), self.frame_lines())

    def show_gray(self) -> None:
        cv2.imshow(f"{self.id} gray", self.frame_gray())

    def show_corrected(self) -> None:
        cv2.imshow(f"{self.id} corrected", self.frame_corrected())

    def show_corrected_lines(self) -> None:
        cv2.imshow(f"{self.id} corrected", self.frame_corrected_lines())

    ###################
    #  External use
    ###################

    def jpg_frame(self) -> str:
        return frame_to_jpg(self.frame())

    def jpg_lines(self) -> str:
        return frame_to_jpg(self.frame_lines())

    def jpg_gray(self) -> str:
        return frame_to_jpg(self.frame_gray())

    def jpg_corrected(self) -> str:
        return frame_to_jpg(self.frame_corrected())

    def jpg_corrected_lines(self) -> str:
        return frame_to_jpg(self.frame_corrected_lines())

    ######################################
    #  INTERNAL
    ######################################

    def _correct(self, frame: np.ndarray) -> np.ndarray:
        return cv2.remap(frame,
                         Camera.UNDISTORTION_MATRICES[self.side],
                         Camera.RECTIFICATION_MATRICES[self.side],
                         *Camera.CORRECTION_OPTIONS)

    ######################################
    #  SETTINGS
    ######################################

    UNDISTORTION_MATRICES: dict = load_npy_files('undistortion')
    RECTIFICATION_MATRICES: dict = load_npy_files('rectification')
    CORRECTION_OPTIONS: list = [cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0]

    def _init_options(self) -> None:
        self.width = DEVICES['resolution'].width
        self.height = DEVICES['resolution'].height
        self.side = 'left' if DEVICES['left'] == self.id else 'right'

        self.video.set(cv2.CAP_PROP_FOURCC, DEVICES['video_codec'])
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
