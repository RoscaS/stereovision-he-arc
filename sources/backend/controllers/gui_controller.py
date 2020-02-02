#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
from pathlib import Path
from typing import List
from typing import Tuple

import eel

from sources.backend.controllers.base_controller import BaseController
from sources.backend.controllers.messages import CLIMessages
from sources.backend.models.CameraPairFactory import CameraPairFactory
from sources.backend.strategies.depth_loop import DepthLoopStrategy
from sources.backend.strategies.distortion_loop import \
    DistortionLoopStrategy
from sources.backend.strategies.initialization_loop import \
    InitializationLoopStrategy


class GUIController(BaseController):
    """
    Entry point of the GUI backend. This class setup the connexion with the
    GUI frontend trough the awesome and lightweight
    [eel](https://github.com/samuelhwilliams/Eel) library.

    This class is in charge of starting the main loop that will react to
    changes made in the frontend.

    It also inject pictures captured and computed by the `CameraSystem` library
    into the frontend on every call of `_update_frontend_images` trough IoC
    made available once again by eel.

    The methodes under the OPTIONS section are the API exposed to eel's
    listeners that are them selves exposed to the frontend. Those watchers are
    defined inside the sources/backend/gui/api file.
    """

    def __init__(self, entrypoint: str, gui_size: Tuple):
        super().__init__()
        self.entrypoint = entrypoint
        self.gui_size = gui_size
        self.state.ui = 'gui'


    def init_frontend_connection(self) -> None:
        entrypoint_dir = str(Path(self.entrypoint).parent)
        entrypoint_file = str(Path(self.entrypoint).name)
        eel.init(entrypoint_dir)
        eel.start(entrypoint_file, size=self.gui_size)

    ############################################################################
    #  MAIN LOOP + FRONTEND UPDATE
    ############################################################################

    def main_loop(self) -> None:
        self.state.streaming = True
        self.cameras = CameraPairFactory.create_camera_pair()
        self.display_current_strategy()

        while self.state.streaming:

            jpgs = self.loop_manager.run_loop(self.cameras, self.store)
            self._update_frontend_images(jpgs)
            self.cameras.clear_frames()

        self.cameras.__del__()
        CLIMessages.gui_standby()

    def _update_frontend_images(self, jpgs: List[str]) -> None:
        eel.updateImageLeft(jpgs[0])()
        if (self.state.looping_strategy not in ['Depth', 'Calibration']):
            eel.updateImageRight(jpgs[1])()

    def display_current_strategy(self):
        CLIMessages.gui_strategy(self.state.looping_strategy)

    ############################################################################
    # OPTIONS: (backend of the API exposed in api.py file)
    ############################################################################

    def set_looping_strategy(self, strategy_name: str) -> None:
        self.state.looping_strategy = strategy_name
        self.display_current_strategy()
        self.loop_manager.strategy = {
            'Initialization': InitializationLoopStrategy,
            'Calibration': None,
            'Distortion': DistortionLoopStrategy,
            'Depth': DepthLoopStrategy,
        }[strategy_name]()

    def switch_depth_mode(self, mode: str) -> None:
        self.state.depth_mode = mode
