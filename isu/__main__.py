
#/usr/bin/env python3
"""
@file main.py
@author Chris P <clp@clp.is>
"""
from typing import NoReturn
from isu.ui.window import MainWindow
from isu.app import MainApp
import os, sys

def run():
    app = MainApp(sys.argv).run()


if __name__ == "__main__":
    run()
