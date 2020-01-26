import cv2

from sources.backend.camera.Frame import Frame
from sources.backend.settings import DEVICES
from sources.backend.utils.resolution_utils import Resolution


class Camera:
    CODEC = cv2.VideoWriter.fourcc(*list("MJPG"))

    def __init__(self, id: int, resolution: Resolution):
        self.side = 'left' if DEVICES['left'] == id else 'right'
        self.video = cv2.VideoCapture(id)
        self.resolution = resolution
        self.id = id

        self._frame = None

        self.video.set(cv2.CAP_PROP_FOURCC, Camera.CODEC)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, resolution.width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution.height)

    def __del__(self):
        self.video.release()
        self.clear_frame()

    def clear_frame(self):
        self._frame = None

    @property
    def frame(self) -> Frame:
        """A new frame is required at every call"""
        # return Frame(self.video, self.side)
        if (self._frame is None):
            self._frame = Frame(source=self.video, side=self.side)
        return  self._frame

    @property
    def blob(self) -> str:
        return self.frame.blob

    def apply_correction(self):
        self.frame.apply_correction()
