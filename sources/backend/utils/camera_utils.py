from typing import NamedTuple


class Sides(NamedTuple):
    """Generic namedtuple used to enhance readability when
    working with camera pairs."""
    left: any
    right: any


class JPGs(NamedTuple):
    """Namedtuple of two `Frame` transformed to allow
    them to pass trough network."""
    left: str
    right: str
