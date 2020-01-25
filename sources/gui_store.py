from dataclasses import dataclass

@dataclass()
class State:
    streaming: bool = False
    distorded: bool = False
    lines: bool = False
    current_tab: str = "Initialization"

@dataclass()
class GUIStore:
    state: State = State()


gui_store = GUIStore()
