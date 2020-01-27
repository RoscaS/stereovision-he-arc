#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of the `strategies` library and build to fit a
# stereovision project. This library is in charge of making the bridge
# between the `CameraSystem` library and `StereovisionGui` library by offering
# a strategy design pattern that conveniently switches between video modes
# in a stereo vision context.

from abc import ABC
from abc import abstractmethod
from typing import List

from sources.backend.store import Store
from sources.libraries.camera_system.CameraPair import CameraPair


class LoopStrategy(ABC):
    """
    Interface used by the modules of the `strategy` library that links
    the StereovisionGui library to the CameraSystem library.
    """

    @abstractmethod
    def loop(self, cameras: CameraPair, store: Store) -> List[str]:
        pass
