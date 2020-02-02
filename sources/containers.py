#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
Simple convenience classes and namedtuples
"""
from dataclasses import dataclass
from typing import List
from typing import NamedTuple


class Shape(NamedTuple):
    """
    Namedtuple that represents the size of a rectangle
    """
    width: int
    height: int


class Color(NamedTuple):
    """
    Namedtuple that represent a rgb color
    """
    red: int
    green: int
    blue: int


@dataclass(order=True)
class Options:
    """
    Data class used to interface with stereovision library
    """
    input_files: List
    rows: int
    columns: int
    square_size: float
    output_folder: str
    show_chessboards: bool



