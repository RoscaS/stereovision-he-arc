#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of the `strategies` library and build to fit a
# stereovision project. This library is in charge of making the bridge
# between the `CameraSystem` library and `StereovisionGui` library by offering
# a strategy design pattern that conveniently switches between video modes
# in a stereo vision context.
import os

import cv2

from external.stereovision.stereo_cameras import ChessboardFinder
from external.stereovision.ui_utils import calibrate_folder
from external.stereovision.ui_utils import find_files
from public.settings import CALIBRATION
from public.settings import CHESSBOARD
from public.settings import DEVICES
from sources.backend.store import Store
from sources.backend.strategies.interface import LoopStrategy
from sources.camera_system import CameraPair
from sources.containers import Options
from sources.helpers import get_progress_bar


# Should be removed to reduce coupling.
COUNT = CALIBRATION['pictures_count']
DEVICES = DEVICES['left'], DEVICES['right']
SIZE = CHESSBOARD['columns'], CHESSBOARD['rows']
PICTURES = CALIBRATION['pictures_folder']


class CalibrationLoopStrategy(LoopStrategy):
    """
    This strategy interface with the stereovision library. Once the loop
    method called:

    Firstly it will take as many pictures as specified in the settings
    when there is a chessboard visible in each capture. After each capture
    there is (at least) 5 seconds lag before the next capture. All the
    pictures are saved localy in the pictures_folder specified in the
    settings.

    Secondly the calibration process will start and fill up the
    calibration_folder specidied in the settings.

    Lastly, once everything is done, it will switch back on the calling
    controller and switch into Distortion strategy.
    """

    def loop(self, cameras: CameraPair, store: Store) -> any:

        progress = get_progress_bar(CALIBRATION['pictures_count'])
        progress.start()

        print("Calibration process 1/2: Chessboard finder.")
        print("Please show your chessboard to the cameras.")
        print("Note that you can't exit gracefully before the end.")

        with ChessboardFinder(DEVICES) as pair:
            for i in range(COUNT):
                frames = pair.get_chessboard(*SIZE, True)
                for side, frame in zip(("left", "right"), frames):
                    number = str(i + 1).zfill(len(str(COUNT)))
                    filename = f"{side}_{number}.ppm"
                    path = os.path.join(PICTURES, filename)
                    cv2.imwrite(path, frame)

                progress.update(progress.maxval - (COUNT - i))

                for i in range(10):
                    pair.show_frames(1)

        progress.finish()

        print("Calibration process 2/2: Calibration")

        if CALIBRATION['pictures_folder']:
            calibrate_folder(
                Options(find_files(PICTURES),
                        *SIZE,
                        CHESSBOARD['square_size'],
                        CALIBRATION['calibration_folder'],
                        CALIBRATION['show_chessboards']))

        print("Calibration done.")
