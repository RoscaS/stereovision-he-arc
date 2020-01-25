import cv2

from sources.camera.Frame import Frame
from sources.utils.resolution_utils import Resolution

class Camera:
    CODEC = cv2.VideoWriter.fourcc(*list("MJPG"))

    def __init__(self, id: int, resolution: Resolution):
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
        return Frame(source=self.video, name=str(self.id))

    @classmethod
    def get_blob_from(cls, frame: Frame) -> str:
        return frame.get_blob()
