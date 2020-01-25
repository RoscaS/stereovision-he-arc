from dataclasses import dataclass

@dataclass()
class State:
    streaming = False
    distorded = False
    lines = False
    current_tab = "Initialization"


class GuiStore:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call static method instance()')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance



class GuiStoree:
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GuiStoree, cls).__new__(cls)
        return cls._instance



x = GuiStore.instance()
