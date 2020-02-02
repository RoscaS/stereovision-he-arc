#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
API exposed to the JS frontend. Simple wrapper around
mathodes of GUIController class that is in charge
of the business.
"""

import eel

from public.settings import GUI_DEFAULT_SIZE
from public.settings import GUI_ENTRY_POINT
from sources.backend.controllers.gui_controller import GUIController


# GUIController must be declared in the same file as the funcions
# decorated by @eel.expose
GUI_CONTROLLER = GUIController(GUI_ENTRY_POINT, GUI_DEFAULT_SIZE)


############################################################################
#  Javascript -> Python // Ment to be called by javascript code.
############################################################################
@eel.expose
def set_looping_strategy(tabName: str) -> None:
    GUI_CONTROLLER.set_looping_strategy(tabName)


@eel.expose
def start_loop() -> None:
    GUI_CONTROLLER.start_loop()


@eel.expose
def stop_loop() -> None:
    GUI_CONTROLLER.stop_loop()


@eel.expose
def toggle_lines() -> None:
    GUI_CONTROLLER.toggle_lines()


@eel.expose
def toggle_distortion() -> None:
    GUI_CONTROLLER.toggle_distortion()


@eel.expose
def switch_blockmatcher_mode() -> None:
    GUI_CONTROLLER.switch_blockmatcher_mode()


@eel.expose
def switch_depth_mode(modeName: str) -> None:
    GUI_CONTROLLER.switch_depth_mode(modeName)
