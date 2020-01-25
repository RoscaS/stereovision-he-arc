from sources.backend.camera.Camera import Camera
from sources.backend.camera.Frame import Frame
from sources.backend.camera.Frame import Frames
from sources.backend.utils.camera_utils import JPGs
from sources.backend.utils.camera_utils import Sides
from sources.backend.utils.resolution_utils import Resolution


class CameraPair:
    DEFAULT_POSITION = (0, 0)

    def __init__(self, ids: Sides, resolution: Resolution):
        self.left = Camera(ids.left, resolution)
        self.right = Camera(ids.right, resolution)

    def __del__(self):
        del self.left
        del self.right

    @property
    def frames(self) -> Frames:
        return Frames(self.left.frame, self.right.frame)

    @classmethod
    def make_blobs_from(cls, frames: Frames) -> JPGs:
        return JPGs(frames.left.blob, frames.right.blob)

    @classmethod
    def draw_horizontal_lines(cls, frames: Frames) -> None:
        for frame in frames:
            frame.draw_horizonal_lines()

    @classmethod
    def apply_corrections(cls, frames: Frames) -> None:
        """Apply undistortion and rectification on a pair of frames"""
        for frame in frames:
            frame.apply_correction()

    @classmethod
    def show(cls, frames: Frames, stacked=False, position=DEFAULT_POSITION):
        if stacked:
            Frame.show_stacked(frames, position)
        else:
            for frame in frames:
                frame.show()
