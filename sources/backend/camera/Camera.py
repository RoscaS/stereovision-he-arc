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

        self.video.set(cv2.CAP_PROP_FOURCC, Camera.CODEC)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, resolution.width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution.height)

    def __del__(self):
        self.video.release()

    @property
    def frame(self) -> Frame:
        """A new frame is required at every call"""
        return Frame(source=self.video, side=self.side)

    @classmethod
    def get_blob_from(cls, frame: Frame) -> str:
        return frame.blob
