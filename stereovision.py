#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
CLI entry point.
"""

import cv2

from sources.backend.camera_system.factories.CameraPairFactory import \
    CameraPairFactory


pair = CameraPairFactory.create_camera_pair()

while True:
    # pair.show_frame()
    # pair.show_lines()
    # pair.show_gray()
    # pair.show_corrected()
    # pair.show_corrected_lines()

    # pair.show_disparity_map()
    # pair.show_fixed_disparity_map()
    # pair.show_colored_disparity_map()
    # pair.show_wls_filtered_disparity()
    pair.show_wls_colored_disparity()


    key = cv2.waitKey(1) & 0xFF
    if key == ord(' ') or key == ord('q'):
        break

    pair.clear_frames()
