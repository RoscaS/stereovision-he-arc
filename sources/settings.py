#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""Public settings file"""

import os
from pathlib import Path

import cv2

from sources.libraries.utils.containers import Resolution


ROOT_DIR = Path(__file__).parents[1]
OUTPUT_DIR = os.path.join(ROOT_DIR, "generated")
SOURCES_DIR = os.path.join(ROOT_DIR, "sources")

BACKEND_DIR = os.path.join(SOURCES_DIR, "backend")
GUI_DIR = os.path.join(SOURCES_DIR, "gui")
FRONTEND_ENTRY_POINT = 'index.html'


DEFAULT_COLOR = (0, 0, 255)  # used to draw horizontal lines on frames

DEVICES = {
    'left': 0,
    'right': 4,
    'resolution': Resolution.RESOLUTION_HD,
    'video_codec': cv2.VideoWriter.fourcc(*list("MJPG")),
}
CHESSBOARD = {
    'rows': 5,
    'columns': 7,
    'square_size': 3.19
}
CALIBRATION = {
    'calibration_folder': os.path.join(OUTPUT_DIR, "calibration_data"),
    'pictures_folder': os.path.join(OUTPUT_DIR, "calibration_pictures"),
    'scene_folder': os.path.join(OUTPUT_DIR, "scene"),
    'show_chessboards': False,
    'pictures_count': 50
}
STEREO = {
    'depth_settings_file': os.path.join(OUTPUT_DIR, "depth_map_settings.json"),
    'depth_map_color': cv2.COLORMAP_JET,
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

GUI_DEFAULT_SIZE = (1280, 920)

for path in [OUTPUT_DIR,
             CALIBRATION['calibration_folder'],
             CALIBRATION['pictures_folder'],
             CALIBRATION['scene_folder']]:
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except(Exception) as e:
            print(e)
