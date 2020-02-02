#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
from sources.containers import Shape


class Resolution(Shape):
    """
    Basic static helper class that contains standard 16/9 resolutions
    """
    RESOLUTION_LOW = Shape(width=640, height=480)
    RESOLUTION_HD = Shape(width=1280, height=720)
    RESOLUTION_FHD = Shape(width=1920, height=1080)
