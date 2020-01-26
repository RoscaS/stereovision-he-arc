#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
Entry point of the GUI of the program
"""

from sources.backend.gui.api import GUI_MANAGER


if __name__ == '__main__':
    GUI_MANAGER.init_frontend_connection()
    GUI_MANAGER.main_loop()
