import cv2
import numpy as np

from sources.backend.camera.Camera import Camera
from sources.backend.camera.Frame import Frame
# from sources.backend.camera.Frame import Frames
from sources.backend.settings import DEPTH_MAP_DEFAULT
from sources.backend.utils.camera_utils import JPGs
from sources.backend.utils.camera_utils import Sides
from sources.backend.utils.resolution_utils import Resolution


# def init_sgbm():
#     window_size = 3
#     defaults = DEPTH_MAP_DEFAULT
#     return cv2.StereoSGBM_create(minDisparity=defaults['minDisparity'],
#                                  numDisparities=defaults['numberOfDisparities'],
#                                  blockSize=window_size,
#                                  uniquenessRatio=defaults['uniquenessRatio'],
#                                  speckleWindowSize=defaults['speckleWindowSize'],
#                                  speckleRange=defaults['speckleRange'],
#                                  disp12MaxDiff=5,
#                                  P1=8 * 3 * window_size ** 2,
#                                  P2=32 * 3 * window_size ** 2)


# sbm = init_sgbm()


class CameraPair:
    DEFAULT_POSITION = (0, 0)

    def __init__(self, ids: Sides, resolution: Resolution):
        self.left = Camera(ids.left, resolution)
        self.right = Camera(ids.right, resolution)
        # self._sbm = init_sgbm()

        self._frames = None
        self._disparity = None
        self._fixed_disparity = None

    def __del__(self):
        del self.left
        del self.right

    def clear_frames(self):
        for camera in [self.left, self.right]:
            camera.clear_frame()
        self._frames = None
        self._disparity = None
        self._fixed_disparity = None

    # @property
    # def frames(self) -> Frames:
    #     if (self._frames is None):
    #         self._frames = Frames(self.left.frame, self.right.frame)
    #     return self._frames
    @property
    def frames(self) -> tuple:
        return self.left.frame, self.right.frame

    # @property
    # def gray_frames(self) -> tuple:
        # return (self.left.frame.gray_frame, self.right.frame.gray_frame)
        # return self.frames.gray_frames()

    # @property
    # def sbm(self) -> cv2.StereoMatcher:
    #     if (self._sbm is None):
    #         self._sbm = init_sgbm()
    #     return self._sbm

    @property
    def disparity_map(self) -> np.ndarray:
        # if (self._disparity is None):
        #     self._disparity = self.sbm.compute(*self.gray_frames)
        # return self._disparity
        return self._sbm.compute(*self.gray_frames)

    @property
    def fixed_disparity_map(self) -> np.ndarray:
        if (self._fixed_disparity is None):
            # ratio = DEPTH_MAP_DEFAULT['minDisparity'] / DEPTH_MAP_DEFAULT['numberOfDisparities']
            self._fixed_disparity = ((self.disparity_map.astype(np.float32) / 16) - 0) / 128
        return self._fixed_disparity
        # return ((disparity_map.astype(np.float32) / 16) - ratio)

    @property
    def blobs(self) -> JPGs:
        return JPGs(self.left.blob, self.right.blob)

    def draw_horizontal_lines(self) -> None:
        for frame in self.frames:
            frame.draw_horizonal_lines()

    def apply_corrections(self) -> None:
        """Apply undistortion and rectification on both cameras"""
        for camera in [self.left, self.right]:
            camera.apply_correction()

        # for frame in self.frames:
        #     frame.apply_correction()

    # @classmethod
    # def show(cls, frames: Frames, stacked=False, position=DEFAULT_POSITION):
    #     if stacked:
    #         Frame.show_stacked(frames, position)
    #     else:
    #         for frame in frames:
    #             frame.show()
