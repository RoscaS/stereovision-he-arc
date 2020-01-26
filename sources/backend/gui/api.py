#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
API exposed to the JS frontend. Simple wrapper around
mathodes of GUIController class that is in charge
of the business.
"""

import eel

from sources.backend.gui.controller import GUIController


GUI_MANAGER = GUIController()


@eel.expose
def toggle_lines() -> None:
    GUI_MANAGER.toggle_lines()


@eel.expose
def toggle_distortion() -> None:
    GUI_MANAGER.toggle_distortion()


@eel.expose
def set_looping_strategy(tab) -> None:
    GUI_MANAGER.set_looping_strategy(tab)


@eel.expose
def start_loop() -> None:
    GUI_MANAGER.start_loop()


@eel.expose
def stop_loop() -> None:
    GUI_MANAGER.stop_loop()
