#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of the `strategies` library and build to fit a
# stereovision project. This library is in charge of making the bridge
# between the `CameraSystem` library and `StereovisionGui` library by offering
# a strategy design pattern that conveniently switches between video modes
# in a stereo vision context.

from typing import List

from sources.backend.camera_system.CameraPair import CameraPair
from sources.backend.gui.stores import GUIStore
from sources.backend.strategies.initialization_loop import \
    InitializationLoopStrategy


class DistortionLoopStrategy(InitializationLoopStrategy):
    """
    Strategy that spits serialized jpgs of the undistorded aswell as the
    raw pictures captured by CameraPair of the CameraSystem library.
    """

    def loop(self, cameras: CameraPair, store: GUIStore) -> List[str]:
        if store.state.distorded:
            if store.state.lines:
                return cameras.jpg_corrected_lines()

            return cameras.jpg_corrected()

        return super().loop(cameras, store)
