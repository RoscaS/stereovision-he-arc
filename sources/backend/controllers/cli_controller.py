#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

import cv2

from sources.backend.controllers.messages import CliMessages
from sources.backend.store import Store
from sources.backend.strategies.calibration_loop import CalibrationLoopStrategy
from sources.backend.strategies.depth_loop import DepthLoopStrategy
from sources.backend.strategies.distortion_loop import \
    DistortionLoopStrategy
from sources.backend.strategies.initialization_loop import \
    InitializationLoopStrategy
from sources.backend.strategies.manager import LoopStrategyManager
from sources.libraries.camera_system.factories.CameraPairFactory import \
    CameraPairFactory


class CLIController:
    """
    Entry point of the CLI backend.

    This class is in charge of starting the main loop that will react to
    changes triggered by user input.
    """

    def __init__(self):
        self.loop_manager = LoopStrategyManager(InitializationLoopStrategy())
        self.store = Store()
        self.state = self.store.state
        self.cameras = None
        self.state.mode = 'cli'

    ############################################################################
    #  FRONTEND CONNECTION MAIN LOOP
    ############################################################################

    def main_loop(self) -> None:
        self.cameras = CameraPairFactory.create_camera_pair()

        self.display_current_strategy()

        while True:
            self.loop_manager.run_loop(self.cameras, self.store)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('1'):
                self.set_looping_strategy('Initialization')
            elif key == ord('2'):
                self.set_looping_strategy('Calibration')
            elif key == ord('3'):
                self.set_looping_strategy('Distortion')
            elif key == ord('4'):
                self.set_looping_strategy('Depth')

            if self.state.looping_strategy in ['Initialization', 'Distortion']:
                if key == ord('l'):
                    self.toggle_lines()
                elif key == ord('d'):
                    self.toggle_distortion()

            elif (self.state.looping_strategy == 'Depth'):
                if key == ord('b'):
                    self.switch_blockmatcher_mode()
                if key == ord('d'):
                    self.switch_depth_mode('Disparity')
                elif key == ord('c'):
                    self.switch_depth_mode('Colored')
                elif key == ord('w'):
                    self.switch_depth_mode('WLS')

            if key == ord(' ') or key == ord('q'):
                self.cameras.__del__()
                exit(0)

            self.cameras.clear_frames()

    def reload_camera(self):
        self.cameras.__del__()
        self.cameras = CameraPairFactory.create_camera_pair()

    def display_current_strategy(self):
        CliMessages.message_for(self.state.looping_strategy)

    ############################################################################
    # OPTIONS: triggered by user input
    ############################################################################

    def set_looping_strategy(self, strategy_name: str) -> None:
        if (strategy_name == self.state.looping_strategy): return
        self.state.looping_strategy = strategy_name
        if (strategy_name == 'Calibration'):
            self.start_calibration()
        else:
            self.display_current_strategy()
            self.reload_camera()
            self.loop_manager.strategy = {
                'Initialization': InitializationLoopStrategy,
                'Calibration': CalibrationLoopStrategy,
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
        if (mode == self.state.depth_mode): return
        self.reload_camera()
        self.state.depth_mode = mode

    def start_calibration(self):
        self.cameras.__del__()
        self.loop_manager.strategy = CalibrationLoopStrategy()
        self.loop_manager.strategy.loop(self.cameras, self.store)
        self.set_looping_strategy('Distortion')
