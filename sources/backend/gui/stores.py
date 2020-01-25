from dataclasses import dataclass


@dataclass()
class State:
    streaming: bool = False
    distorded: bool = False
    lines: bool = False
    current_tab: str = "Initialization"

    def reset_state(self):
        self.streaming = False
        self.distorded = False
        self.lines = False


@dataclass()
class GUIStore:
    state: State = State()


gui_store = GUIStore()
