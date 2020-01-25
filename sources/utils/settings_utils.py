from dataclasses import dataclass

from sources.utils.resolution_utils import Resolution

@dataclass()
class Devices:
    left: int
    right: int
    resolution: Resolution

@dataclass()
class Chessboard:
    rows: int
    columns: int
    square_size: float

@dataclass()
class Calibration:
    scene_folder: str
    calibration_folder: str
    pictures_folder: str
    pictures_count: int
    show_chessboards: bool

@dataclass()
class Stereo:
    sgbm: bool
    depth_map_color: str
    depth_map_settings_file: str
    depth_map_default: dict


@dataclass(order=True)
class Settings:
    devices: Devices
    chessboard: Chessboard
    calibration: Calibration
    stereo: Stereo

