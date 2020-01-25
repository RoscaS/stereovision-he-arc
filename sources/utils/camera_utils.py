from typing import NamedTuple
from sources.camera.Frame import Frame

class Sides(NamedTuple):
    """Generic namedtuple used to enhance readability when
    working with camera pairs."""
    left: any
    right: any


class Frames(NamedTuple):
    """Namedtuple of two `Frame`."""
    left: Frame
    right: Frame


class JPGs(NamedTuple):
    """Namedtuple of two `Frame` transformed to allow
    them to pass trough network."""
    left: str
    right: str
