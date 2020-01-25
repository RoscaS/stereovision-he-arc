from typing import NamedTuple

class Shape(NamedTuple):
    """Namedtuple that represents the size of a rectangle"""
    width: int
    height: int

class Resolution(Shape):
    RESOLUTION_LOW = Shape(width=640, height=480)
    RESOLUTION_HD = Shape(width=1280, height=720)
    RESOLUTION_FHD = Shape(width=1920, height=1080)

