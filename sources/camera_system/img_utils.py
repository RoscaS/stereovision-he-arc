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

"""
Module level helper functions.
"""

import base64
import os
from typing import Dict

import cv2
import numpy as np

from public.settings import CALIBRATION
from public.settings import DEFAULT_COLOR
from public.settings import DEPTH_MAP_DEFAULTS


def color_gray(frame: np.ndarray) -> np.ndarray:
    """
    Convenience function that produce a gray scale frame.

    @param frame: source frame
    @return: a new frame that is a gray scale copy of `frame`.
    """
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def draw_horizonal_lines(frame: np.ndarray,
                         color: tuple = DEFAULT_COLOR) -> np.ndarray:
    """
    Draw horizontal lines on a frame.

    @param frame: source frame
    @param color: color of the lines
    @return: a new frame that is a copy of `frame` with lines drawn on top.
    """
    new_frame = frame.copy()
    for line in range(0, int(new_frame.shape[0] / 20)):
        new_frame[line * 20, :] = color
    return new_frame


def frame_to_jpg(frame: np.ndarray) -> str:
    """
    Convenience function that convert a frame to JPG
    and serialize it. Can be used to export frames out of the software.

    @param frame: frame to be serialized
    @return: serialized jpg
     """
    jpg = cv2.imencode('.jpg', frame)[1]
    return base64.b64encode(jpg).decode('utf-8')


def load_npy_files(type: str) -> Dict[str, np.ndarray]:
    """
    Convenience function to load content of external (npy) files.

    @param type: a str that specifies the type of file to load. Value can be
    'undistortion' or 'rectification'
    @return: a dict that has as keys the side ('left' or 'right') and the
    content of the file loaded in numpy format.
    """
    output = CALIBRATION['calibration_folder']
    left = os.path.join(output, f"{type}_map_left.npy")
    right = os.path.join(output, f"{type}_map_right.npy")
    return {'left': np.load(left), 'right': np.load(right)}


def check_npy_files_exists() -> bool:
    """
    Make sure that calibration data exists.
    """
    output = CALIBRATION['calibration_folder']
    left = lambda type: os.path.join(output, f"{type}_map_left.npy")
    right = lambda type: os.path.join(output, f"{type}_map_right.npy")
    check = [os.path.exists(left(t)) and os.path.exists(right(t))
             for t in ['rectification', 'undistortion']]
    return not (False in check)


def init_sbm() -> cv2.StereoMatcher:
    """
    Convenience function to setup a fast stereo block matcher.

    @return: fast stereo block matcher
    """
    # todo CHANGE THOSE TERRIBLE HARD CODED VALUES BEFORE RELEASE !
    window_size = 5  # temp
    sbm = cv2.StereoBM_create(blockSize=window_size)
    sbm.setMinDisparity(2)
    sbm.setNumDisparities(128)
    sbm.setPreFilterCap(30)
    sbm.setPreFilterSize(5)
    sbm.setSpeckleRange(15)
    sbm.setSpeckleWindowSize(32)
    sbm.setTextureThreshold(100)
    sbm.setUniquenessRatio(10)
    return sbm


def init_sgbm(settings: Dict = None) -> cv2.StereoMatcher:
    """
    Convenience function to setup a stereo block matcher that is better
    in most cases but slower than the simple stereo block matcher.

    @return: strong stereo block matcher
    """
    window_size = 3  # temp
    values = settings if settings != None else DEPTH_MAP_DEFAULTS
    return cv2.StereoSGBM_create(blockSize=window_size,
                                 minDisparity=values['minDisparity'],
                                 numDisparities=values['numDisparities'],
                                 uniquenessRatio=values['uniquenessRatio'],
                                 speckleRange=values['speckleRange'],
                                 speckleWindowSize=values[
                                     'speckleWindowSize'],
                                 disp12MaxDiff=5,
                                 P1=8 * 3 * window_size ** 2,
                                 P2=32 * 3 * window_size ** 2)


def init_right_matcher(bm: cv2.StereoMatcher) -> cv2.StereoMatcher:
    """
    Convenience function to setup the matcher for computing the right-view
    disparity map that is required for WLS filtering.

    @param bm: Main block matcher instance that will be used with the filter.
    @return: right-view disparity map
    """
    return cv2.ximgproc.createRightMatcher(bm)


def init_wls_filter(bm: cv2.StereoMatcher,
                    lambdaa: int = 8000,
                    sigma: float = .8) -> cv2.ximgproc_DisparityWLSFilter:
    """
    Convenience factory function that creates an instance of
    `cv2.ximgproc_DisparityWLSFilter` and sets up all the relevant filter
    parameters automatically based on the matcher instance `bm`.

    @param bm: The main block matcher instance that is used with the filter
    @param lambda: Smoothness strength parameter for solver
    @param sigma: Similar to spatial space sigma in cv2.bilateralFilter.
    @return instance of DisparityWLSFilter
    """
    wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=bm)
    wls_filter.setLambda(lambdaa)
    wls_filter.setSigmaColor(sigma)
    return wls_filter


def closing_transformation(frame: np.ndarray,
                           kernel_size: int = 3) -> np.ndarray:
    """
    Apply a closing morphologic transform on `frame`

    @param frame: target of the transform
    @param kernel_size: size of the side of the square used
    @return: closed frame
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    closed = (closing - closing.min()) * 255
    return closed.astype(np.uint8)


def fix_disparity(map: np.ndarray) -> np.ndarray:
    """Bring furthest points in image to 0 disp"""
    min_disp = DEPTH_MAP_DEFAULTS['minDisparity']
    num_disp = DEPTH_MAP_DEFAULTS['numDisparities']
    return ((map.astype(np.float32) / 16) - min_disp) / num_disp


def mouse_callback(event, x, y, flags, param):
    """
    EXPERIMENTAL !
    Returns distance in metters @ mouse click position.
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        disparity = average_disparity_at_position(x, y, param)
        d = compute_distance_from_disparity(disparity)
        print(f'Distance: {d} m')

def average_disparity_at_position(x, y, disparity_map) -> float:
    average = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            average += disparity_map[y + j, x + i]

    return average

def compute_distance_from_disparity(disparity: float) -> float:
    """
    EXPERIMENTAL !
    Convert disparity to distance. Polynomial regression was used
    to find the values.
    y = ax^3 + bx^2 + cx + d
    """
    disparity = disparity / 9
    a = -593.97 * disparity**3
    b = 1506.8 * disparity**2
    c = -1373.1 * disparity
    d = 522.06
    distance = a + b + c + d
    return np.around(distance * 0.01, decimals=2)




