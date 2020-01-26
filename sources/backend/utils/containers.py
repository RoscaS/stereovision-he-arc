#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
Simple convenience classes and namedtuples
"""

from typing import NamedTuple


class Shape(NamedTuple):
    """
    Namedtuple that represents the size of a rectangle
    """
    width: int
    height: int


class Resolution(Shape):
    """
    Basic helper class that contains standard 16/9 resolutions
    """
    RESOLUTION_LOW = Shape(width=640, height=480)
    RESOLUTION_HD = Shape(width=1280, height=720)
    RESOLUTION_FHD = Shape(width=1920, height=1080)
