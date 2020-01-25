from sources.backend.camera.CameraPair import CameraPair
from sources.backend.settings import DEVICES
from sources.backend.utils.camera_utils import Sides


class CameraFactory:

    @classmethod
    def create_camera_pair(cls):
        ids = Sides(DEVICES.left, DEVICES.right)
        return CameraPair(ids, DEVICES.resolution)
