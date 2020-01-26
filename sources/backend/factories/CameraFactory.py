from sources.backend.camera.Camera import Camera


class CameraFactory:

    @classmethod
    def create_camera(cls, id: int):
        return Camera(id)
