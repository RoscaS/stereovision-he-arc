#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of the `strategies` library and build to fit a
# stereovision project. This library is in charge of making the bridge
# between the `CameraSystem` library and `StereovisionGui` library by offering
# a strategy design pattern that conveniently switches between video modes
# in a stereo vision context.

from typing import List

from sources.backend.store import Store
from sources.backend.strategies.interface import LoopStrategy
from sources.libraries.camera_system.CameraPair import CameraPair

class DepthLoopStrategy(LoopStrategy):
    """
    Strategy that spits a single serialized jpg wrapped in a list that
    represents a disparity map captured and computed by CameraPair of
    the CameraSystem library.
    """
    def loop(self, cameras: CameraPair, store: Store) -> List[str]:
        is_gui = store.state.mode == 'gui'

        if store.state.sgbm and not cameras.is_sgbm:
            cameras.set_sgbm_mode() if is_gui else cameras.set_sgbm_mode()

        if not store.state.sgbm and cameras.is_sgbm:
            cameras.set_sbm_mode() if is_gui else cameras.set_sbm_mode()

        if is_gui:
            mode = self.gui_depth_mode_callback(cameras, store.state.depth_mode)
        else:
            mode = self.cli_depth_mode_callback(cameras, store.state.depth_mode)

        return [mode(), ""]


    def gui_depth_mode_callback(self, cameras: CameraPair, name: str):
        return {
            'Disparity': cameras.jpg_disparity_map,
            'Colored': cameras.jpg_colored_disparity_map,
            'WLS': cameras.jpg_wls_colored_disparity
        }[name]

    def cli_depth_mode_callback(self, cameras: CameraPair, name: str):
        return {
            'Disparity': cameras.show_disparity_map,
            'Colored': cameras.show_colored_disparity_map,
            'WLS': cameras.show_wls_colored_disparity
        }[name]

