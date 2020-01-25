import cv2
import os
import numpy as np
from typing import Tuple

from sources.settings import settings

min_disp = 2
num_disp = 128
uniqueness = 10
speckleWindowSize = 100
speckleRange = 32

def coords_mouse_disp(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # print x,y,disp[y,x],filteredImg[y,x]
        average = 0
        for u in range(-1, 2):
            for v in range(-1, 2):
                average += param[y + u, x + v]
        average = average / 9
        Distance = -593.97 * average ** (3) + 1506.8 * average ** (
            2) - 1373.1 * average + 522.06
        Distance = np.around(Distance * 0.01, decimals=2)
        print('Distance: ' + str(Distance) + ' m')

def load_npy_files(type: str) -> Tuple[str, str]:
    # output = f"calibration_data/"
    output = settings.calibration.calibration_folder
    path = lambda side: np.load(os.path.join(output, f"{type}_map_{side}.npy"))
    return path("left"), path("right")


def init_wls_filter(sbm, lam=8000, sig=.8):
    wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=sbm)
    wls_filter.setLambda(lam)
    wls_filter.setSigmaColor(sig)
    return wls_filter

def compute_wls(wls, disparityL, disparityR, grayL):
    filteredImg = wls.filter(disparityL, grayL, None, disparityR)
    filteredImg = cv2.normalize(src=filteredImg, dst=filteredImg, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX)
    return np.uint8(filteredImg)

def wls_filter(disparity, wls, srm, grayL, grayR):
    disparityR = np.int16(srm.compute(grayR, grayL))
    disparityL = np.int16(disparity)
    return compute_wls(wls, disparityL, disparityR, grayL)


def init_sbm():
    default = settings.stereo.depth_map_default

    window_size = 5
    sbm = cv2.StereoBM_create(blockSize=window_size)
    sbm.setMinDisparity(2)
    sbm.setNumDisparities(128)
    sbm.setPreFilterCap(30)
    sbm.setPreFilterSize(5)
    sbm.setSpeckleRange(15)
    sbm.setSpeckleWindowSize(32)
    sbm.setTextureThreshold(100)
    sbm.setUniquenessRatio(10)
    return sbm


def init_sgbm():
    window_size = 3
    return cv2.StereoSGBM_create(minDisparity=min_disp,
                                   numDisparities=num_disp,
                                   blockSize=window_size,
                                   uniquenessRatio=uniqueness,
                                   speckleWindowSize=speckleWindowSize,
                                   speckleRange=speckleRange,
                                   disp12MaxDiff=5,
                                   P1=8 * 3 * window_size ** 2,
                                   P2=32 * 3 * window_size ** 2)


def rectify_frame(frame, undistortion, rectification):
    options = [cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0]
    return cv2.remap(frame, undistortion, rectification, *options)


def fix_disparity(disparity, min_disp, num_disp):
    # Bring furthest points in image to 0 disp
    return ((disparity.astype(np.float32) / 16) - min_disp) / num_disp

def closing_transformation(image, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    closed = (closing - closing.min()) * 255
    return closed.astype(np.uint8)

def print_min_max_disparity(disparity):
    print(f"Min: {disparity.min()}\tMax: {disparity.max()}")


# def get_rectified_pair()
