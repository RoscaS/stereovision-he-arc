#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of CameraSystem and build to fit a stereovision project
# but could be used for more generic purposes as it abstracts the use
# of cv2's camera and allows to export jpg serialized frames outside
# the program.
#
# CameraSystem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import cv2
import numpy as np

from sources.camera_system.CameraComponent import CameraComponent
from sources.camera_system.img_utils import check_npy_files_exists
from sources.camera_system.img_utils import color_gray
from sources.camera_system.img_utils import draw_horizonal_lines
from sources.camera_system.img_utils import frame_to_jpg
from sources.camera_system.img_utils import load_npy_files


class Camera(CameraComponent):
    """
    A leaf of the composite design pattern build around the camera system.
    This class represents a single cameras that is ment to be used in a
    stereovision system but not exclusively.

    Generic build that only requires to be used inside a loop. It's
    mendatory to use the `clear_frames` method at the end of every
    iteration of the loop.

    Every attribute that is prefixed by _ (underscore) is setup around
    a flyweight design pattern to only allow ressources if needed and
    when needed.

    CORE section methodes are ment to be generic, and are not
    fit for direct use.

    CMD section methodes are a convenient way to see results. Those
    methodes are ment to be used inside Python scripts and will
    play inside cv2's player.

    EXTERNAL section methodes are a serialized version of the results
    spit by CORE section methodes. They are ment to be used by external
    programs or for networking.
     """

    def __init__(self, id: int, side: str, width: int, height: int):
        self.id = id
        self.side = side
        self.width = width
        self.height = height
        self.video = cv2.VideoCapture(id)

        self._frame: np.ndarray = None
        self._lines: np.ndarray = None
        self._gray: np.ndarray = None
        self._corrected: np.ndarray = None
        self._corrected_lines: np.ndarray = None

        self._init_options()

    def __del__(self):
        self.clear_frames()
        self.video.release()
        try:
            cv2.destroyWindow(str(self.id))
        except Exception as e:
            pass

    ############################################################################
    #  COMPONENT INTERFACE IMPLEMENTATION
    ############################################################################

    def clear_frames(self) -> None:
        self._frame = None
        self._lines = None
        self._gray = None
        self._corrected = None
        self._corrected_lines = None

    ######################################
    # CORE
    ######################################

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
        Camera.init_npy_arrays()
        if self._corrected is None:
            self._corrected = self._correct(self.frame())
        return self._corrected

    def frame_corrected_lines(self) -> np.ndarray:
        if self._corrected_lines is None:
            self._corrected_lines = draw_horizonal_lines(self.frame_corrected())
        return self._corrected_lines

    ######################################
    #  CMD
    ######################################

    def show_frame(self) -> None:
        cv2.imshow(str(self.id), self.frame())

    def show_lines(self) -> None:
        cv2.imshow(str(self.id), self.frame_lines())

    def show_gray(self) -> None:
        cv2.imshow(str(self.id), self.frame_gray())

    def show_corrected(self) -> None:
        cv2.imshow(str(self.id), self.frame_corrected())

    def show_corrected_lines(self) -> None:
        cv2.imshow(str(self.id), self.frame_corrected_lines())

    ######################################
    #  EXTERNAL
    ######################################

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

    ############################################################################
    #  INTERNAL
    ############################################################################

    def _correct(self, frame: np.ndarray) -> np.ndarray:
        """Apply undistortion and rectification on `frame`"""
        return cv2.remap(frame,
                         Camera.UNDISTORTION_MATRICES[self.side],
                         Camera.RECTIFICATION_MATRICES[self.side],
                         *Camera.CORRECTION_OPTIONS)

    ############################################################################
    #  SETTINGS
    ############################################################################

    UNDISTORTION_MATRICES: dict = None
    RECTIFICATION_MATRICES: dict = None
    CORRECTION_OPTIONS: list = [cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0]

    def _init_options(self) -> None:
        """Initialize secondary attributes and set camera options"""
        video_codec = cv2.VideoWriter.fourcc(*list("MJPG"))
        self.video.set(cv2.CAP_PROP_FOURCC, video_codec)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    @classmethod
    def init_npy_arrays(cls) -> None:
        """Load calibration data located in external files"""
        err = "\nError: You must calibrate your system first."
        if not cls.UNDISTORTION_MATRICES or not cls.RECTIFICATION_MATRICES:
            if not check_npy_files_exists():
                print(err)
                exit(1)
            cls.UNDISTORTION_MATRICES: dict = load_npy_files('undistortion')
            cls.RECTIFICATION_MATRICES: dict = load_npy_files('rectification')
