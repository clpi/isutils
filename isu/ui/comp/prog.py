import sys
from typing import Callable
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt, QBasicTimer, QTimerEvent
from PyQt6.QtGui import QTabletEvent

from PyQt6.QtWidgets import (
    QPushButton, QComboBox, QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication, QLineEdit, QSpinBox, QStackedWidget, QFileDialog, QCheckBox,
    QVBoxLayout, QHBoxLayout, QProgressBar, QProgressDialog, QLabel, QButtonGroup, 
)

class Progress(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.step = 0

    def setupUi(self):
        layout = QVBoxLayout()
        self.timer = QBasicTimer()
        self.lbl = QLabel("Progress ")
        self.pbar = QProgressBar(self)
        self.setWindowTitle("isutils: Executing op (1/1)...")
        self.resize(400, 250)
        layout.addWidget(self.lbl)
        layout.addWidget(self.pbar)
        self.setLayout(layout)


    def timerEvent(self, e: QTimerEvent):
        if self.timer.isActive() or self.step >= 100:
            self.timer.stop()
            self.lbl.setText("finished")
            return
        self.step += 1
        self.set(self.step)

    def start(self):
        self.timer.start(100, self)

    def set(self, amt: int | float):
        self.pbar.setValue(int(amt))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    progress = Progress()
    progress.show()
    app.exec()