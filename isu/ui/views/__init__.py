"""NOTE: the views module represents the third rightmost part of the UI,
intended to give the user a visual sense of what's going on and what's being 
reflectd by their choices made in the middle tab on the data from the left
"""
import os, sys
from pathlib import Path
from typing import Any
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile, QDir, Signal, Slot, QCoreApplication, QObject
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QMainWindow, QDialog, QLayout

class ViewPane(QObject, QWidget):
    ui: QWidget

    def __init__(self, parent: Any):
        self.uifile = QFile(os.path.join(__file_) / Path("views/main.ui"))
        super(ViewPane, self).__init__(parent)
        self.load_ui()

    def load_ui(self):
        ldr = UiLoad("")
        self.ui = 