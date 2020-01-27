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
from sources.backend.strategies.interface import LoopStrategy

class DepthLoopStrategy(LoopStrategy):
    """
    Strategy that spits a single serialized jpg wrapped in a list that
    represents a disparity map captured and computed by CameraPair of
    the CameraSystem library.
    """

    def loop(self, cameras: CameraPair, store: GUIStore) -> List[str]:

        if store.state.sgbm and not cameras.is_sgbm:
            cameras.set_sgbm_mode()

        if not store.state.sgbm and cameras.is_sgbm:
            cameras.set_sbm_mode()

        mode = cameras.get_depth_mode_callback(store.state.depth_mode)()

        return [mode, ""]
