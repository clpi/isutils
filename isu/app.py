from isu.ui.comp.prefs import Prefs
from isu.ui.comp.prog import Progress
from isu.ui.window import MainWindow
import sys, os, argparse
from typing import TypeVar
from PySide6 import QtGui, QtWidgets, QtCore, QtUiTools
from PySide6.QtGui import QAction, QGuiApplication, QActionEvent, QEnterEvent, QColor, QPen, QFont
from PySide6.QtWidgets import QApplication, QWidget, QComboBox
from PySide6.QtCore import Slot, Signal, QEnum, QFlag, QObject, QMetaObject, QSignalMapper
from enum import Enum, Flag, auto
from isu.data import Context
from isu.operation import Op
from isu.models.demo import Demo

__dbg__ = True

_MainApp = TypeVar("_MainApp", bound="MainApp")


class MainApp(QApplication):

    def __init__(self, *args): 
       QApplication.__init__(self)
       self.ctx = Context()
       self.main_window: MainWindow = MainWindow(parent=self)
       self.run()

    @Slot()
    def quit_app(self):
        self.quit()

    @Slot()
    def instance(self) -> QApplication:
        match QApplication.instance():
            case None: return self
            case a: return MainApp(a)

    def run(self):
        self.main_window.ui.show()

    @staticmethod
    def open(q: QWidget):
        q.show()

    @Slot()
    def run_ops(self):
        sys.exit(self.exec())


    # @pyqtSlot(QApplication, name="mainApp")
    # def main_app(self):
        

    
if __name__ == "__main__":
    MainApp(sys.argv)

    
