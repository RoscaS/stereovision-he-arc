from sources.backend.camera.CameraPair import CameraPair
from sources.backend.settings import DEVICES
from sources.backend.factories.CameraFactory import CameraFactory


class CameraPairFactory:

    @classmethod
    def create_camera_pair(cls):
        left_id = DEVICES['left']
        right_id = DEVICES['right']

        pair = CameraPair()
        pair.add(CameraFactory.create_camera(left_id))
        pair.add(CameraFactory.create_camera(right_id))

        return pair
