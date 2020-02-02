#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>
# This file is part of CameraSystem and build to fit a stereovision project
# but could be used for more generic purposes as it abstracts the use
# of cv2's camera and allows to export jpg serialized frames outside
# the program.
#
# CameraSystem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class CameraComponent(ABC):
    """
    Component interface of the composite design pattern build around
    the camera system. This abstract class (trough ABC extension) is
    used as an interface between `Camera`, `CameraPair` and a client that
    uses a system based on this module. This system is made with
    stereovision in mind but can easily be extended.

    CORE section methodes are ment to be generic, and are not
    fit for direct use.

    CMD section methodes are a convenient way to see results. Those
    methodes are ment to be used inside Python scripts and will
    play inside cv2's player.

    EXTERNAL section methodes are a serialized version of the results
    spit by CORE section methodes. They are ment to be used by external
    programs or for networking.
     """

    @abstractmethod
    def __del__(self):
        pass

    ############################################################################
    #  CORE COMPONENT PATTERN
    ############################################################################

    @property
    def parent(self) -> CameraComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: CameraComponent):
        self._parent = parent

    def add(self, component: CameraComponent) -> None:
        pass

    def remove(self, component: CameraComponent) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    ############################################################################
    #  CAMERA SPECIFIC
    ############################################################################

    ######################################
    #  CORE
    ######################################

    @abstractmethod
    def clear_frames(self) -> None:
        pass

    @abstractmethod
    def frame(self):
        pass

    @abstractmethod
    def frame_lines(self):
        pass

    @abstractmethod
    def frame_gray(self):
        pass

    @abstractmethod
    def frame_corrected(self):
        pass

    @abstractmethod
    def frame_corrected_lines(self):
        pass

    ######################################
    #  CMD
    ######################################

    @abstractmethod
    def show_frame(self) -> None:
        pass

    @abstractmethod
    def show_lines(self) -> None:
        pass

    @abstractmethod
    def show_gray(self) -> None:
        pass

    @abstractmethod
    def show_corrected(self) -> None:
        pass

    @abstractmethod
    def show_corrected_lines(self) -> None:
        pass

    ######################################
    #  EXTERNAL
    ######################################

    @abstractmethod
    def jpg_frame(self):
        pass

    @abstractmethod
    def jpg_lines(self):
        pass

    @abstractmethod
    def jpg_gray(self):
        pass

    @abstractmethod
    def jpg_corrected(self):
        pass

    @abstractmethod
    def jpg_corrected_lines(self):
        pass




