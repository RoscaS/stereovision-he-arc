#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
State of the application. Based on a flux design pattern to ensure
that a state change is reflected everywhere needed
"""

from dataclasses import dataclass


@dataclass()
class State:
    mode: str = 'gui'
    streaming: bool = False
    distorded: bool = True
    lines: bool = False
    sgbm: bool = True

    looping_strategy: str = "Initialization"
    depth_mode = "WLS"

    def reset_state(self):
        self.mode = 'gui'
        self.streaming = False
        self.distorded = True
        self.lines = False
        self.sgbm = True


@dataclass()
class Store:
    state: State = State()


gui_store = Store()
