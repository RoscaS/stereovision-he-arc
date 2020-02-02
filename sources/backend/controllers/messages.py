from os import system

from sources.camera_system.img_utils import check_npy_files_exists


class CLIMessages():
    """
    Sole purpose of this class is to keep things clean by holding
    the messages to display to the user in one place.
    """
    TEMPLATE = lambda key, action: f'- Press "{key}" key to {action}'

    @classmethod
    def gui_strategy(cls, strategy: str):
        print(f"Starting {strategy} loop.")

    @classmethod
    def gui_standby(cls):
        print("Python program is in standby.")

    @classmethod
    def message_for(cls, strategy: str):
        try:
            system('clear')
        except:
            pass
        print(f"{strategy} mode.\n")
        print("Available actions:")
        return {
            'Initialization': cls.initialization_actions,
            'Distortion': cls.distortion_actions,
            'Depth': cls.depth_mode,
        }[strategy]()

    @classmethod
    def global_actions(cls):
        print(cls.TEMPLATE("q", "to exit the program."))
        print(cls.TEMPLATE("1", "to switch to initialization mode."))
        print(cls.TEMPLATE("2", "to switch to calibration mode."))
        if check_npy_files_exists():
            print(cls.TEMPLATE("3", "to distortion mode."))
            print(cls.TEMPLATE("4", "to depth mode"))
        print()

    @classmethod
    def lines_action(cls):
        print(cls.TEMPLATE("l", "draw horizontal lines"))

    @classmethod
    def initialization_actions(cls):
        cls.global_actions()
        cls.lines_action()

    @classmethod
    def distortion_actions(cls):
        cls.global_actions()
        cls.lines_action()
        print(cls.TEMPLATE("d", "turn correction on / off"))

    @classmethod
    def depth_mode(cls):
        cls.global_actions()
        print(cls.TEMPLATE("b", "change between blockmatcher mode"))
        print(cls.TEMPLATE("d", "show raw disparity map"))
        print(cls.TEMPLATE("c", "show fixed and colored disparity map"))
        print(cls.TEMPLATE("w", "show a WLS filtered map"))
        print("In this mode you can double click to get a conversion")
        print("from disparity to distance. (Needs to be setup)")
