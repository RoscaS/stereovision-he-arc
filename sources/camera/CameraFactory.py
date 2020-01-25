from sources.settings import settings
from sources.camera.CameraPair import CameraPair
from sources.utils.camera_utils import Sides

devices = settings.devices

class CameraFactory:
    @classmethod
    def create_camera_pair(cls):
        ids = Sides(devices.left, devices.right)
        return CameraPair(ids, devices.resolution)
