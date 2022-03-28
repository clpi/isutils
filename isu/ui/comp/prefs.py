import sys, os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Dict, Any
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (Qt, QObject, Slot, Signal, QFile, QDir)
from PySide6.QtWidgets import (QMainWindow, QWidget, QDialog, QListWidget, QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication)
from isu.ui import UiLoad

@dataclass
class Prefs(QDialog):

    def __init__(self, parent: Any | None = None):
        QDialog.__init__(self, parent)
        UiLoad().loadUi("prefs.ui", self, parent)
        self.load_ui()

    def load_ui(self):
        pass

    @Slot()
    def show(self):
        self.show()

    @Slot()
    def close(self):
        self.close()