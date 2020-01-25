"""
API exposed to the JS frontend. Simple wrapper around
mathodes of GUIController class that is in charge
of the business.
"""

import eel

from sources.backend.gui.manager import GUIController


GUI_MANAGER = GUIController()


@eel.expose
def toggle_lines():
    GUI_MANAGER.toggle_lines()


@eel.expose
def toggle_distortion():
    GUI_MANAGER.toggle_distortion()


@eel.expose
def set_looping_strategy(tab):
    GUI_MANAGER.set_looping_strategy(tab)


@eel.expose
def stop_loop():
    GUI_MANAGER.stop_loop()


@eel.expose
def start_loop():
    GUI_MANAGER.main_loop()
