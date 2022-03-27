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
       super(QApplication, self).__init__(*args)
       self.ctx = Context()
       self.window: MainWindow = MainWindow(parent=self)
       self.window.show()

    @Slot()
    def quit_app(self):
        self.quit()

    def instance(self) -> QApplication:
        return self.instance()

    def run(self):
        self.window.show()

    @staticmethod
    def open(q: QWidget):
        q.show()

    @Slot()
    def run_ops(self):
        self.window.show()
        sys.exit(self.exec())

    @Slot()
    def show_prefs(self):
        prefs = Prefs(parent=self.window)
        prefs.show()

    @Slot()
    def show_prog(self):
        prog = Progress(parent=self.window)
    # @pyqtSlot(QApplication, name="mainApp")
    # def main_app(self):
        

    
if __name__ == "__main__":
    MainApp(sys.argv)

    
