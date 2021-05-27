import sys, os
from typing import Optional, List, Dict
from PyQt5 import uic
from PyQt5.QtCore import (Qt, QObject, pyqtSlot, pyqtSignal)
from PyQt5.QtWidgets import (QWidget, QDialog, QListWidget, QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication)


class Prefs(QDialog):


    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        path = os.path.join(os.path.dirname(__file__), "prefs.ui")
        uic.loadUi(path, self)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    prefs = Prefs()
    prefs.show()
    app.exec_()
