#!/usr/bin/env python
# -*- coding: utf-8 -*-

from public.settings import DEVICES
# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of CameraSystem and build to fit a stereovision project
# but could be used for more generic purposes as it abstracts the use
# of cv2's camera and allows to export jpg serialized frames outside
# the program.
#
# CameraSystem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from sources.camera_system.Camera import Camera


class CameraFactory:
    """
    Simple Camera factory ment to be extended if needed.
    """

    @classmethod
    def create_camera(cls, id: int):
        side = 'left' if DEVICES['left'] == id else 'right'
        width, height = DEVICES['resolution']
        return Camera(id, side, width, height)
