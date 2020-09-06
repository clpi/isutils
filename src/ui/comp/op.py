"""
TODO: Split off each ops params view into own separate QWidget?
TODO: Consider having op type selection be before view is created?
TODO: Consider having op-type params be non-str
TODO: Make default op view be blank, only show params view when one is selected
"""
import sys, os
from typing import Optional, List, Dict
from PyQt5 import uic
from PyQt5.QtCore import (Qt, QObject, pyqtSlot, pyqtSignal)
from PyQt5.QtWidgets import (QWidget, QDialog, QListWidget, QPushButton,
    QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, 
    QApplication, QLineEdit, QSpinBox, QStackedWidget)
from models.operation import OP_TYPES, Op, ShellOp, InsertOp, SectionOp, AudioOp, CropOp, get_op

class OpWidget(QWidget):

    def __init__(self, op: str = "shell", parent: Optional[QWidget] = None):
        """Initializes """
        super().__init__(parent)
        path = os.path.join(os.path.dirname(__file__), "op.ui")
        uic.loadUi(path, self)
        self.op = self.set_op(op)

    def load_tabs(self):
        self.opsParamsStack: QStackedWidget
        self.shellTab: QWidget
        self.insertTab: QWidget
        self.sectionTab: QWidget
        self.audioTab: QWidget
        self.cropTab: QWidget

    def load_data(self):
        self.demoTargetCombo: QComboBox
        self.opCombo: QComboBox
        # Shell ------------------->
        self.shellBrowseImgBtn: QPushButton
        self.shellFgX: QSpinBox
        self.shellFgY: QSpinBox
        self.shellFgW: QSpinBox
        self.shellFgH: QSpinBox
        # Insert ----------------->
        self.insertBrowseImgBtn: QPushButton
        self.insertFgX: QSpinBox
        self.insertFgY: QSpinBox
        self.insertFgW: QSpinBox
        self.insertFgH: QSpinBox
        # Audio ----------------->
        # Crop ------------------>
        # Section --------------->

    def get_op_params(self):
        pass

    def set_demo(self):
        pass

    def set_op(self, op_idx: int):
        self.op = get_op(op_idx)()
        self.opsParamsStack.setCurrentIndex(op_idx)


    def set_op_kind(self, op: str):

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

class OpContext:

    def __init__(self, op: Op):
        self.op = op

