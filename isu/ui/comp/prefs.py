import sys, os
from typing import Optional, List, Dict
from PyQt6 import uic
from PyQt6.QtCore import (Qt, QObject, pyqtSlot, pyqtSignal)
from PyQt6.QtWidgets import (QWidget, QDialog, QListWidget, QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication)


class Prefs(QDialog):


    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        path = os.path.join(os.path.dirname(__file__), "prefs.ui")
        uic.loadUi(path, self)

    def load_ui(self):
        pass

    @pyqtSlot()
    def open(self, parent: None) -> None:
        self.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    prefs = Prefs()
    prefs.show()
    app.exec()
