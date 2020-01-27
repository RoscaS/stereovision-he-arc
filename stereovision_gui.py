#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
GUI entry point.
"""

from sources.backend.gui.api import GUI_MANAGER


if __name__ == '__main__':
    GUI_MANAGER.init_frontend_connection()
    GUI_MANAGER.main_loop()
