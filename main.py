﻿#! /usr/bin/env python3
"""
@file main.py
@author Chris P <clp@clp.is>
"""
from typing import NoReturn
from isu.ui.window import MainWindow
from isu.app import MainApp
import os, sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication
from PySide6 import QtUiTools
# from PySide6 import QUiLoader

def run():
    app = MainApp([])
    app.window.show()
    sys.exit(app.exec())

    # app = QApplication()


if __name__ == "__main__":
    run()
