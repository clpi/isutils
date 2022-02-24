#/usr/bin/env python3
"""
@file main.py
@author Chris P <clp@clp.is>
"""
from typing import NoReturn
from ui.window import MainWindow, run
from ui.app import MainApp
import os, sys
import tkinter as tk

def main():
    app = MainApp(sys.argv)


if __name__ == "__main__":
    main()
