from typing import List

import cv2
import numpy as np

from sources.backend.camera.Component import Component
from sources.backend.camera.img_utils import closing_transformation
from sources.backend.camera.img_utils import fix_disparity
from sources.backend.camera.img_utils import frame_to_jpg
from sources.backend.camera.img_utils import init_right_matcher
from sources.backend.camera.img_utils import init_sgbm
from sources.backend.camera.img_utils import init_wls_filter
from sources.backend.settings import STEREO


class CameraPair(Component):

    def __init__(self):
        self._children: List[Component] = []

        self._frames: List[np.ndarray] = []
        self._lines: List[np.ndarray] = []
        self._gray: List[np.ndarray] = []
        self._corrected: List[np.ndarray] = []
        self._corrected_lines: List[np.ndarray] = []

        self._disparity_map = None
        self._fixed_disparity_map = None
        self._colored_disparity_map = None
        self._wls_filtered_disparity = None
        self._wls_colored_disparity = None

        self.sbm = init_sgbm()
        self.srm = init_right_matcher(self.sbm)
        self.wls = None

    def __del__(self):
        for child in self._children:
            child.__del__()

        self.video.release()
        self.clear_frames()

    ######################################
    #  COMPONENT INTERFACE IMPLEMENTATION
    ######################################

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def clear_frames(self) -> None:
        self._frames.clear()
        self._lines.clear()
        self._gray.clear()
        self._corrected.clear()
        self._corrected_lines.clear()
        self._disparity_map = None
        self._fixed_disparity_map = None
        self._colored_disparity_map = None
        self._wls_filtered_disparity = None
        self._wls_colored_disparity = None
        for child in self._children:
            child.clear_frames()

    ###################
    #  Core
    ###################

    def frame(self) -> List[np.ndarray]:
        if len(self._frames) == 0:
            self._frames = [c.frame() for c in self._children]
        return self._frames

    def frame_lines(self) -> List[np.ndarray]:
        if len(self._lines) == 0:
            self._lines = [c.frame_lines() for c in self._children]
        return self._lines

    def frame_gray(self) -> List[np.ndarray]:
        if len(self._gray) == 0:
            self._gray = [c.frame_gray() for c in self._children]
        return self._gray

    def frame_corrected(self) -> List[np.ndarray]:
        if len(self._corrected) == 0:
            self._corrected = [c.frame_corrected() for c in self._children]
        return self._corrected

    def frame_corrected_lines(self) -> List[np.ndarray]:
        if len(self._corrected_lines) == 0:
            self._corrected_lines = [c.frame_corrected_lines() for c in
                                     self._children]
        return self._corrected_lines

    ###################
    #  For cmd
    ###################

    def show_frame(self) -> None:
        for child in self._children:
            child.show_frame()

    def show_lines(self) -> None:
        for child in self._children:
            child.show_lines()

    def show_gray(self) -> None:
        for child in self._children:
            child.show_gray()

    def show_corrected(self) -> None:
        for child in self._children:
            child.show_corrected()

    def show_corrected_lines(self) -> None:
        for child in self._children:
            child.show_corrected_lines()

    ###################
    #  External use
    ###################

    def jpg_frame(self) -> List[str]:
        return [c.jpg_frame() for c in self._children]

    def jpg_lines(self) -> List[str]:
        return [c.jpg_lines() for c in self._children]

    def jpg_gray(self) -> List[str]:
        return [c.jpg_gray() for c in self._children]

    def jpg_corrected(self) -> List[str]:
        return [c.jpg_corrected() for c in self._children]

    def jpg_corrected_lines(self) -> List[str]:
        return [c.jpg_corrected_lines() for c in self._children]

    ######################################
    #  DISPARITY & DEPTH
    ######################################

    def disparity_map(self) -> np.ndarray:
        if self._corrected is None:
            self.frame_corrected()
        if self._disparity_map is None:
            self._disparity_map = self.sbm.compute(*self.frame_gray())
        return self._disparity_map

    def fixed_disparity_map(self) -> np.ndarray:
        if self._fixed_disparity_map is None:
            self._fixed_disparity_map = fix_disparity(self.disparity_map())
        return self._fixed_disparity_map

    def colored_disparity_map(self) -> np.ndarray:
        if self._colored_disparity_map is None:
            closed = closing_transformation(self.fixed_disparity_map())
            color = STEREO['depth_map_color']
            self._colored_disparity_map = cv2.applyColorMap(closed, color)
        return self._colored_disparity_map

    def wls_filtered_disparity(self):
        if self._fixed_disparity_map is None:
            self.fixed_disparity_map()
        if self.wls is None:
            self.wls = init_wls_filter(self.sbm)
        if self._wls_filtered_disparity is None:
            self._wls_filtered_disparity = self._compute_wls_filter()
        return self._wls_filtered_disparity

    def wls_colored_disparity(self):
        if self._wls_filtered_disparity is None:
            self.wls_filtered_disparity()
        filtered = self._wls_filtered_disparity
        color = STEREO['depth_map_color']

        if self._wls_colored_disparity is None:
            self._wls_colored_disparity = cv2.applyColorMap(filtered, color)
        return self._wls_colored_disparity

    ###################
    #  For cmd
    ###################

    def show_disparity_map(self) -> None:
        cv2.imshow(str("Disparity map"), self.disparity_map())

    def show_fixed_disparity_map(self) -> None:
        cv2.imshow(str("Disparity map"), self.fixed_disparity_map())

    def show_colored_disparity_map(self) -> None:
        cv2.imshow(str("Colored disparity map"), self.colored_disparity_map())

    def show_wls_filtered_disparity(self) -> None:
        cv2.imshow(str("WLS filtered"), self.wls_filtered_disparity())

    def show_wls_colored_disparity(self) -> None:
        cv2.imshow(str("WLS colored"), self.wls_colored_disparity())

    ###################
    #  External use
    ###################

    def jpg_disparity_map(self) -> str:
        return frame_to_jpg(self.disparity_map())

    def jpg_fixed_disparity_map(self) -> str:
        return frame_to_jpg(self.fixed_disparity_map())

    def jpg_colored_disparity_map(self) -> str:
        return frame_to_jpg(self.colored_disparity_map())

    def jpg_wls_filtered_disparity(self) -> str:
        return frame_to_jpg(self.wls_filtered_disparity())

    def jpg_wls_colored_disparity(self) -> str:
        return frame_to_jpg(self.wls_colored_disparity())

    ######################################
    #  INTERNAL
    ######################################

    def _compute_wls_filter(self):
        grayL, grayR = self.frame_gray()
        disparityR = np.int16(self.srm.compute(grayR, grayL))
        disparityL = np.int16(self._disparity_map)
        filteredImg = self.wls.filter(disparityL, grayL, None, disparityR)
        filteredImg = cv2.normalize(src=filteredImg, dst=filteredImg, beta=0,
                                    alpha=255, norm_type=cv2.NORM_MINMAX)
        return np.uint8(filteredImg)
