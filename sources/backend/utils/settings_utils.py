"""
Immutable containers used in the settings files.
Dataclasses are more convenient than dictionaries.
"""

from dataclasses import dataclass

from sources.backend.utils.resolution_utils import Resolution


@dataclass(frozen=True)
class Devices:
    left: int
    right: int
    resolution: Resolution


@dataclass(frozen=True)
class Chessboard:
    rows: int
    columns: int
    square_size: float


@dataclass(frozen=True)
class Calibration:
    scene_folder: str
    calibration_folder: str
    pictures_folder: str
    pictures_count: int
    show_chessboards: bool


@dataclass(frozen=True)
class Stereo:
    sgbm: bool
    depth_map_color: str
    depth_settings_file: str
    depth_map_default: dict
