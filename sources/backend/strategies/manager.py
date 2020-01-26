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


class LoopStrategyManager:
    """
    Context of the looping strategies of the `strategies` library. Ment
    to be used as an entry point by the StereovisionGui controller.
    """
    """Context of the looping strategies."""

    def __init__(self, strategy: LoopStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> LoopStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: LoopStrategy) -> None:
        self._strategy = strategy

    def run_loop(self, cameras: CameraPair, store: GUIStore) -> List[str]:
        return self._strategy.loop(cameras, store)
