#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

import cv2

from sources.backend.controllers.base_controller import BaseController
from sources.backend.controllers.messages import CLIMessages
from sources.backend.models.CameraPairFactory import CameraPairFactory
from sources.backend.strategies.calibration_loop import CalibrationLoopStrategy
from sources.backend.strategies.depth_loop import DepthLoopStrategy
from sources.backend.strategies.distortion_loop import \
    DistortionLoopStrategy
from sources.backend.strategies.initialization_loop import \
    InitializationLoopStrategy
from sources.camera_system.img_utils import check_npy_files_exists


class CLIController(BaseController):
    """
    Entry point of the CLI backend.

    This class is in charge of starting the main loop that will react to
    changes triggered by user input.
    """

    def __init__(self):
        super().__init__()
        self.state.ui = 'cli'

    ############################################################################
    #  MAIN LOOP
    ############################################################################

    def main_loop(self) -> None:
        self.state.streaming = True
        self.cameras = CameraPairFactory.create_camera_pair()
        self._display_current_strategy()

        while True:
            self.loop_manager.run_loop(self.cameras, self.store)
            self._keyboard_handler()
            self.cameras.clear_frames()

    def _reload_camera(self):
        self.cameras.__del__()
        self.cameras = CameraPairFactory.create_camera_pair()

    def _display_current_strategy(self):
        CLIMessages.message_for(self.state.looping_strategy)

    def _keyboard_handler(self):
        key = cv2.waitKey(1) & 0xFF

        self._modes_handler(key)
        self._options_handler(key)

        if key == ord(' ') or key == ord('q'):
            self.cameras.__del__()
            exit(0)

    def _modes_handler(self, key: str):
        if key == ord('1'):
            self.set_looping_strategy('Initialization')
        elif key == ord('2'):
            self.set_looping_strategy('Calibration')
            if check_npy_files_exists():
                if key == ord('3'):
                    self.set_looping_strategy('Distortion')
                elif key == ord('4'):
                    self.set_looping_strategy('Depth')

    def _options_handler(self, key: str):
        if self.state.looping_strategy in ['Initialization', 'Distortion']:
            if key == ord('l'):
                self.toggle_lines()
            elif key == ord('d'):
                self.toggle_distortion()

        elif self.state.looping_strategy == 'Depth':
            if key == ord('b'):
                self.switch_blockmatcher_mode()
            if key == ord('d'):
                self.switch_depth_mode('Disparity')
            elif key == ord('c'):
                self.switch_depth_mode('Colored')
            elif key == ord('w'):
                self.switch_depth_mode('WLS')

    ############################################################################
    # OPTIONS: triggered by user input
    ############################################################################

    def set_looping_strategy(self, strategy_name: str) -> None:
        if strategy_name == self.state.looping_strategy:
            return
        self.state.looping_strategy = strategy_name
        if strategy_name == 'Calibration':
            self.start_calibration()
        else:
            self._display_current_strategy()
            self._reload_camera()
            self.loop_manager.strategy = {
                'Initialization': InitializationLoopStrategy,
                'Calibration': CalibrationLoopStrategy,
                'Distortion': DistortionLoopStrategy,
                'Depth': DepthLoopStrategy,
            }[strategy_name]()

    def switch_depth_mode(self, mode: str) -> None:
        if mode == self.state.depth_mode:
            return
        self._reload_camera()
        self.state.depth_mode = mode

    def start_calibration(self):
        self.cameras.__del__()
        self.loop_manager.strategy = CalibrationLoopStrategy()
        self.loop_manager.strategy.loop(self.cameras, self.store)
        self.set_looping_strategy('Distortion')
