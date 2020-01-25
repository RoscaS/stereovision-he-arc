import cv2, base64
from cv2 import VideoCapture
from numpy import ndarray
import numpy as np

from sources.utils.resolution_utils import Shape

class Frame:
    DEFAULT_COLOR = (0, 0, 255)

    def __init__(self, source: VideoCapture or ndarray, name: str='nc'):
        is_videCapture = type(source) == cv2.VideoCapture
        self.name = name
        self.frame: ndarray = source.read()[1] if is_videCapture else source
        self.shape = Shape(width=self.frame.shape[0],
                           height=self.frame.shape[1])

    def __str__(self):
        return f"Frame from Camera {self.name}"

    def get_blob(self) -> str:
        jpg = cv2.imencode('.jpg', self.frame)[1]
        return base64.b64encode(jpg).decode('utf-8')

    def draw_horizonal_lines(self, color: tuple=DEFAULT_COLOR) -> None:
        for line in range(0, int(self.shape.width / 20)):
            self.frame[line * 20, :] = color

    def show(self) -> None:
        cv2.imshow(self.name, self.frame)

    @classmethod
    def show_stacked(cls, frames, position: tuple) -> None:
        name = "Stacked"
        cv2.namedWindow(name)
        cv2.moveWindow(name, *position)
        cv2.imshow(name, np.hstack((frames.left.frame, frames.right.frame)))


