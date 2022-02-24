import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QPushButton, QComboBox, QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication, QLineEdit, QSpinBox, QStackedWidget, QFileDialog, QCheckBox,
    QVBoxLayout, QHBoxLayout, QProgressBar, QProgressDialog, QLabel, QButtonGroup, 
)

class Progress(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.lbl = QLabel("Progress ")
        self.pbar = QProgressBar()
        self.setWindowTitle("isutils: Executing op (1/1)...")
        self.resize(400, 250)
        layout.addWidget(self.lbl)
        layout.addWidget(self.pbar)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    progress = Progress()
    progress.show()
    app.exec()