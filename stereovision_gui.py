#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
GUI entry point.
"""
from sources.backend.api import GUI_CONTROLLER


if __name__ == '__main__':
    GUI_CONTROLLER.init_frontend_connection()
    GUI_CONTROLLER.main_loop()
