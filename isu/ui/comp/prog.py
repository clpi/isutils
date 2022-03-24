from asyncio.base_futures import _FINISHED
import time
import enum
import sys
from typing import Callable, Type
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QTabletEvent
from PySide6.QtCore import *

from PySide6.QtWidgets import (
    QWidget,
    QPushButton, QComboBox, QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication, QLineEdit, QSpinBox, QStackedWidget, QFileDialog, QCheckBox,
    QVBoxLayout, QHBoxLayout, QProgressBar, QProgressDialog, QLabel, QButtonGroup, 
)

from isu.operation.operation import Op, Status
from isu.ui.data import OpQueue
from isu.operation.shell import Shell


class Progress(QtWidgets.QWidget):
    pbar: QProgressBar
    index: int
    len: int

    def __init__(self, curr_op: Type[Op] = Shell, len: int = 1, ix = 0,parent: QWidget|None=None):
        super().__init__(parent)
        self.index = ix
        self.lblh = self.toplabel()
        self.lblh = QLabel(self)
        self.lblo = self.oplabel()
        self.opmsg = QLabel("", self)
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.len = len
        self.setupUi()

    # @pyqtSlot(Type[Op])
    def upd(self, op_type: Type[Op]) -> None:
        self.curr_op = op_type
        if self.index < self.len:
            self.lblh = self.toplabel()
            self.lblo = self.oplabel()
        else:
            self.lblh.setText(f"All {self.len} operations completed successfully.")
            self.close()

    @Slot(str)
    def set_opmsg(self, msg: str) -> None:
        self.opmsg.setText(msg)

    def toplabel(self) -> QLabel: 
        return QLabel("Running operations... "+str(self.index + 1)+ "of"+ str(self.len + 1)+ ", self", self)

    def oplabel(self) -> QLabel: 
        return QLabel("Operation {str(self.curr_op)} in progress", self)

    def set_optype(self, ot: Type[Op]):
        self.curr_op = ot

    @Slot(int)
    def progress(self, val: int):
        self.pbar.setValue(val)
        self.lblh = self.toplabel()
        self.lblo = self.oplabel()

    @Slot(Status)
    def handle_status(self, st: Status, ): 
        if st == Status.Canceled:
            self.lblh.setText("Canceled")
            self.lblo.setText(f"{self.curr_op} was canceled by the user.")
        elif st == Status.Done:
            self.lblh.setText("Finished")
            self.lblo.setText(f"{self.curr_op} is complete.")
        elif st == Status.Failed:
            self.lblh.setText("Failed")
            self.lblo.setText(f"{self.curr_op} failed.")
        elif st == Status.InProgress:
            self.lblh = self.toplabel()
            self.lblo = self.oplabel()

    def setupUi(self):
        layout = QVBoxLayout()
        self.timer = QBasicTimer()
        self.pbar = QProgressBar(self)
        self.setWindowTitle("isutils: Executing op (1/1)...")
        self.resize(400, 250)
        layout.addWidget(self.lblh)
        layout.addWidget(self.lblo)
        layout.addWidget(self.pbar)
        self.setLayout(layout)

    def timerEvent(self, e: QTimerEvent):
        if self.timer.isActive() or self.pbar.value() >= 100:
            self.timer.stop()
            self.lblh.setText("finished")
            return
        self.index += 1
        self.set(self.index)

    @Slot()
    def start(self):
        self.timer.start(100, self)

    @Slot()
    def finish(self):
        self.lblh.setText("Finished")
        self.lblo.setText(f"{self.curr_op} is complete.")

    def set(self, amt: int | float):
        self.pbar.setValue(int(amt))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    progress = Progress()
    progress.show()
    app.exec()
