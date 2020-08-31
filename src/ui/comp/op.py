import sys, os
from typing import Optional, List, Dict
from PyQt5 import uic
from PyQt5.QtCore import (Qt, QObject, pyqtSlot, pyqtSignal)
from PyQt5.QtWidgets import (QWidget, QDialog, QListWidget, QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication, QLineEdit, QSpinBox)
from models.op import Op, ShellOp, InsertOp, SectionOp, AudioOp, CropOp

class OpWidget(QWidget):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        path = os.path.join(os.path.dirname(__file__), "prefs.ui")
        uic.loadUi(path, self)

    def load_data(self):
        pass

    def get_op_params(self):
        pass

    def set_demo(self):
        pass

    def set_op(self, op: Op):
        pass

    def load_input(self) -> None:
        self.insertImgPath: QLineEdit
        self.shellImgPath: QLineEdit
        self.insertFgX: QSpinBox
        self.insertFgY: QSpinBox
        self.insertFgW: QSpinBox
        self.insertFgH: QSpinBox
        self.shellFgX: QSpinBox
        self.shellFgY: QSpinBox
        self.shellFgW: QSpinBox
        self.shellFgH: QSpinBox
