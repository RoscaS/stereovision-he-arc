import cv2

from sources.backend.camera.Camera import Camera
from sources.backend.gui.api import GUI_MANAGER
from sources.backend.utils.resolution_utils import Resolution


if __name__ == '__main__':
    GUI_MANAGER.init_frontend_connection()
    GUI_MANAGER.main_loop()
