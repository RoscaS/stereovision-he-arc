import os
import cv2

from sources.utils.settings_utils import *

left_device = 2
right_device = 0
resolution = Resolution.RESOLUTION_HD

chessboard_columns = 5
chessboard_rows = 7
chessboard_square_size = 3.19

generated_root = "generated"
calibration_data = "calibration_data"
calibration_pictures = "calibration_pictures"
scene_folder = "scene"
pictures_count = 50
show_chessboards = False

# Stereo
depth_map_settings_file = "depth_map_settings.json"
depth_map_color = cv2.COLORMAP_JET
sgbm = False


# Initialization
calibration_data = os.path.join(generated_root, calibration_data)
calibration_pictures = os.path.join(generated_root, calibration_pictures)
scene_folder = os.path.join(generated_root, scene_folder)

for path in [calibration_data, calibration_pictures, scene_folder]:
    if not os.path.exists(path):
        os.makedirs(path)


settings = Settings(
    devices=Devices(
        left=left_device,
        right=right_device,
        resolution=resolution
    ),
    chessboard=Chessboard(
        rows=chessboard_rows,
        columns=chessboard_columns,
        square_size=chessboard_square_size
    ),
    calibration=Calibration(
        calibration_folder=calibration_data,
        pictures_folder=calibration_pictures,
        pictures_count=pictures_count,
        show_chessboards=show_chessboards,
        scene_folder=scene_folder
    ),
    stereo=Stereo(
        depth_map_settings_file=depth_map_settings_file,
        sgbm=sgbm,
        depth_map_color=depth_map_color,
        depth_map_default= {
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
    )
)


