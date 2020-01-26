from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Component(ABC):

    ######################################
    #  CORE COMPONENT PATTERN
    ######################################

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    ######################################
    #  CAMERA SPECIFIC
    ######################################

    ###################
    #  Core
    ###################

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

    ###################
    #  For cmd
    ###################

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

    ###################
    #  External use
    ###################

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
