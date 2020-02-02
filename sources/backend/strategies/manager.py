#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of the `strategies` library and build to fit a
# stereovision project. This library is in charge of making the bridge
# between the `CameraSystem` library and a cotroller library by offering
# a strategy design pattern that conveniently switches between video modes.

from typing import List

from sources.backend.store import Store
from sources.backend.strategies.interface import LoopStrategy
from sources.camera_system import CameraPair


class LoopStrategyManager:
    """
    Context of the looping strategies of the `strategies` library. Ment
    to be used as mode swicher tool by a controller.
    """

    def __init__(self, strategy: LoopStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> LoopStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: LoopStrategy) -> None:
        self._strategy = strategy

    def run_loop(self, cameras: CameraPair, store: Store) -> List[str]:
        return self._strategy.loop(cameras, store)
