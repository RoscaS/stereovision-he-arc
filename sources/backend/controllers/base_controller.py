#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
from abc import ABC
from abc import abstractmethod

from sources.backend.store import Store
from sources.backend.strategies.initialization_loop import \
    InitializationLoopStrategy
from sources.backend.strategies.manager import LoopStrategyManager


class BaseController(ABC):
    """
    Base abstract class for controllers. Contains methodes implementations
    and attributes common to all controllers.
    """

    def __init__(self):
        self.loop_manager = LoopStrategyManager(InitializationLoopStrategy())
        self.store = Store()
        self.state = self.store.state
        self.cameras = None

    ############################################################################
    #  MAIN LOOP
    ############################################################################

    @abstractmethod
    def main_loop(self) -> None:
        pass

    ############################################################################
    # OPTIONS: Base implementation (common to all controllers)
    ############################################################################

    @abstractmethod
    def set_looping_strategy(self, strategy_name: str) -> None:
        pass

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

    @abstractmethod
    def switch_depth_mode(self, mode: str) -> None:
        pass
