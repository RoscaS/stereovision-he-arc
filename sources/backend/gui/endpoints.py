import eel

from sources.backend.gui.manager import GUIManager
from sources.backend.gui.strategies.initialization import InitializationLoopStrategy


GUI_MANAGER = GUIManager(InitializationLoopStrategy())


@eel.expose
def toggle_lines():
    GUI_MANAGER.toggle_lines()


@eel.expose
def toggle_distortion():
    GUI_MANAGER.toggle_distortion()


@eel.expose
def set_tab(tab):
    GUI_MANAGER.set_tab(tab)


@eel.expose
def stop_loop():
    GUI_MANAGER.stop_loop()


@eel.expose
def start_loop():
    GUI_MANAGER.start_loop()
