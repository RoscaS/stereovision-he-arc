import base64
import numpy as np
import cv2

from sources.backend.camera.CameraPair import CameraPair
from sources.backend.camera.Frame import Frame
from sources.backend.gui.stores import GUIStore
from sources.backend.gui.strategies.interface import LoopStrategy
from sources.backend.settings import DEPTH_MAP_DEFAULT
from sources.backend.utils.stereo_vision_utils import fix_disparity
from sources.backend.utils.stereo_vision_utils import init_sbm


# print(type(sbm))
# srm = cv2.ximgproc.createRightMatcher(sbm)
# wls = None
from sources.backend.utils.stereo_vision_utils import init_sgbm


have_filter = False


class DepthLoopStrategy(LoopStrategy):
    sbm = init_sgbm()

    def loop(self, cameras: CameraPair, store: GUIStore) -> None:

        frameR = cameras.right.video.read()[1]
        frameL = cameras.left.video.read()[1]

        rectifiedR = cv2.remap(frameR,
                               Frame.UNDISTORTION_MATRICES['right'],
                               Frame.RECTIFICATION_MATRICES['right'],
                               *Frame.CORRECTION_OPTIONS)

        rectifiedL = cv2.remap(frameL,
                               Frame.UNDISTORTION_MATRICES['left'],
                               Frame.RECTIFICATION_MATRICES['left'],
                               *Frame.CORRECTION_OPTIONS)

        grayR = cv2.cvtColor(rectifiedR, cv2.COLOR_BGR2GRAY)
        grayL = cv2.cvtColor(rectifiedL, cv2.COLOR_BGR2GRAY)



        disparity = DepthLoopStrategy.sbm.compute(grayL, grayR)
        fixed = ((disparity.astype(np.float32) / 16) - 0) / 128
        # cv2.imshow('Disparity', disparity)



        # jpg = cv2.imencode('.jpg', fixed)[1]
        # jpg = base64.b64encode(jpg).decode('utf-8')

        # jpgs = JPGs(jpg, "")
        # jpgs = JPGs("", "")
        # return jpgs





# cameras.apply_corrections()
# gray_frames = cameras.gray_frames
# disparity = cameras.disparity_map
# fixed = cameras.fixed_disparity_map

# if (have_filter):
#     # image = wls_filter(disparity, wls, srm, *gray_frames)
#     pass
# else:
#     image = closing_transformation(disparity, 3)
#
# image = cv2.applyColorMap(image, STEREO['depth_map_color'])

# cv2.imshow('img', cameras.frames.left.frame)

# test = cameras.sbm.compute(*cameras.gray_frames)

# d = sbm.compute(*gray_frames)
