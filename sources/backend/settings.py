import os
from pathlib import Path

import cv2

from sources.backend.utils.resolution_utils import Resolution


ROOT_DIR = Path(__file__).parents[2]
OUTPUT_DIR = os.path.join(ROOT_DIR, "generated")

DEVICES = {
    'left': 2,
    'right': 0,
    'resolution': Resolution.RESOLUTION_HD
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

DEPTH_MAP_DEFAULT = {
    "SADWindowSize": 5,
    "minDisparity": 0,
    "numberOfDisparities": 128,
    "preFilterCap": 29,
    "preFilterSize": 5,
    "speckleRange": 15,
    "speckleWindowSize": 20,
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
