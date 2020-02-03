#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""Public settings file"""

import os
from pathlib import Path

from sources.const import Resolution

ROOT_DIR = Path(__file__).parents[1]
OUTPUT_DIR = os.path.join(ROOT_DIR, "generated")
SOURCES_DIR = os.path.join(ROOT_DIR, "sources")

BACKEND_DIR = os.path.join(SOURCES_DIR, "backend")

GUI_DIR = os.path.join(SOURCES_DIR, "gui")
GUI_ENTRY_POINT = os.path.join(GUI_DIR, 'index.html')


GUI_DEFAULT_SIZE = (1280, 920)

# Used to draw horizontal lines on frames
DEFAULT_COLOR = (0, 0, 255)

DEVICES = {
    # Usb id of the left camera
    'left': 2,
    # Usb id of the left camera
    'right': 0,
    # Resolution global variable contain some valid resolutions
    'resolution': Resolution.RESOLUTION_HD,

}
CHESSBOARD = {
    # Rows interesections
    'rows': 5,
    # Columns interesection
    'columns': 7,
    # in cm
    'square_size': 3.19
}
CALIBRATION = {
    'calibration_folder': os.path.join(OUTPUT_DIR, "calibration_data"),
    'pictures_folder': os.path.join(OUTPUT_DIR, "calibration_pictures"),
    'scene_folder': os.path.join(OUTPUT_DIR, "scene"),
    # If you want to display the found chessboard between calibration steps.
    'show_chessboards': False,
    # Number of calibration pictures that should be taken.
    'pictures_count': 50
}
STEREO = {
    'depth_settings_file': os.path.join(OUTPUT_DIR, "depth_map_settings.json"),
}

DEPTH_MAP_DEFAULTS = {
    "blockSize": 5,
    "minDisparity": 2,
    "numDisparities": 128,
    "preFilterCap": 30,
    "preFilterSize": 5,
    "speckleRange": 32,
    "speckleWindowSize": 100,
    "textureThreshold": 100,
    "uniquenessRatio": 10
}

for path in [OUTPUT_DIR,
             CALIBRATION['calibration_folder'],
             CALIBRATION['pictures_folder'],
             CALIBRATION['scene_folder']]:
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except(Exception) as e:
            print(e)
