#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Rosca Sol <sol.rosca@gmail.com>

"""
CLI entry point.
"""

from sources.backend.controllers.cli_controller import CLIController


CLI_CONTROLLER = CLIController()

if __name__ == '__main__':
    CLI_CONTROLLER.main_loop()
