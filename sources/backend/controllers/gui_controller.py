#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

from typing import List

import eel

from sources.backend.store import Store
from sources.backend.strategies.depth_loop import DepthLoopStrategy
from sources.backend.strategies.distortion_loop import \
    DistortionLoopStrategy
from sources.backend.strategies.initialization_loop import \
    InitializationLoopStrategy
from sources.backend.strategies.manager import LoopStrategyManager
from sources.libraries.camera_system.factories.CameraPairFactory import \
    CameraPairFactory
from sources.settings import GUI_DIR
from sources.settings import FRONTEND_ENTRY_POINT
from sources.settings import GUI_DEFAULT_SIZE


class GUIController:
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

    def __init__(self):
        self.loop_manager = LoopStrategyManager(InitializationLoopStrategy())
        self.store = Store()
        self.state = self.store.state
        self.cameras = None

    def init_frontend_connection(self) -> None:
        frontend_path = GUI_DIR
        frontend_entry_point = FRONTEND_ENTRY_POINT
        eel.init(frontend_path)
        eel.start(frontend_entry_point, size=GUI_DEFAULT_SIZE)

    ############################################################################
    #  FRONTEND CONNECTION MAIN LOOP
    ############################################################################

    def main_loop(self) -> None:
        self.state.streaming = True
        self.cameras = CameraPairFactory.create_camera_pair()
        print(f"Starting {self.state.looping_strategy} loop.")

        while self.state.streaming:

            jpgs = self.loop_manager.run_loop(self.cameras, self.store)

            self._update_frontend_images(jpgs)
            self.cameras.clear_frames()

        self.cameras.__del__()
        print("Python program is in standby.")

    def _update_frontend_images(self, jpgs: List[str]) -> None:
        eel.updateImageLeft(jpgs[0])()
        if (self.state.looping_strategy not in ['Depth', 'Calibration']):
            eel.updateImageRight(jpgs[1])()

    ############################################################################
    # OPTIONS: (backend of the API exposed in api.py file)
    ############################################################################

    def set_looping_strategy(self, strategy_name: str) -> None:
        print(f"Loading {strategy_name} strategy")
        self.state.looping_strategy = strategy_name
        self.loop_manager.strategy = {
            'Initialization': InitializationLoopStrategy,
            'Calibration': None,
            'Distortion': DistortionLoopStrategy,
            'Depth': DepthLoopStrategy,
        }[strategy_name]()

    def start_loop(self) -> None:
        self.main_loop()

    def stop_loop(self) -> None:
        self.state.reset_state()

    def toggle_lines(self) -> None:
        self.state.lines = not self.state.lines

    def toggle_distortion(self) -> None:
        self.state.distorded = not self.state.distorded

    def switch_blockmatcher_mode(self) -> None:
        self.state.sgbm = not self.state.sgbm

    def switch_depth_mode(self, mode: str) -> None:
        self.state.depth_mode = mode
