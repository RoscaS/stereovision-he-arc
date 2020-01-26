#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""Settings file"""

import os
from pathlib import Path

import cv2

from sources.backend.utils.containers import Resolution


ROOT_DIR = Path(__file__).parents[2]
OUTPUT_DIR = os.path.join(ROOT_DIR, "generated")
SOURCES_DIR = os.path.join(ROOT_DIR, "sources")
BACKEND_DIR = os.path.join(SOURCES_DIR, "backend")
FRONTEND_DIR = os.path.join(SOURCES_DIR, "frontend")
FRONTEND_ENTRY_POINT = 'index.html'
DEFAULT_COLOR = (0, 0, 255) # used to draw horizontal lines on frames

DEVICES = {
    'left': 2,
    'right': 0,
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
    'sgbm': False,
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

for path in [OUTPUT_DIR,
             CALIBRATION['calibration_folder'],
             CALIBRATION['pictures_folder'],
             CALIBRATION['scene_folder']]:
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except(Exception) as e:
            print(e)
