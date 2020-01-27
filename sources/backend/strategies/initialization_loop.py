#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of the `strategies` library and build to fit a
# stereovision project. This library is in charge of making the bridge
# between the `CameraSystem` library and `StereovisionGui` library by offering
# a strategy design pattern that conveniently switches between video modes
# in a stereo vision context.

from typing import List

from sources.backend.strategies.interface import LoopStrategy
from sources.libraries.camera_system import CameraPair
from sources.backend.store import Store


class InitializationLoopStrategy(LoopStrategy):
    """
    Default strategy that spits serialized jpgs of the raw pictures
    captured by CameraPair of the CameraSystem library.
    """

    def loop(self, cameras: CameraPair, store: Store) -> List[str]:
        is_gui = store.state.mode == 'gui'

        if store.state.lines:
            return cameras.jpg_lines() if is_gui else cameras.show_lines()

        return cameras.jpg_frame() if is_gui else cameras.show_frame()
