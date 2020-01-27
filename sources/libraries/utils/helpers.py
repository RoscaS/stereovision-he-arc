from progressbar import Bar
from progressbar import Percentage
from progressbar import ProgressBar


def get_progress_bar(max_val: int):
    """
    Cli progress bar
    """
    bar = Bar("=", "[", "]")
    widgets = [bar, " ", Percentage()]
    return ProgressBar(maxval=max_val, widgets=widgets)
