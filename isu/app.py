import argparse
from isu.ui.comp.prefs import Prefs
from isu.ui.comp.prog import Progress
from isu.ui.window import AboutDialog, MainWindow
import sys, os
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtGui import QAction, QGuiApplication, QActionEvent, QEnterEvent, QColor, QPen, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox
from PyQt6.QtCore import *
from isu.data import Context
from isu.operation import Op
from isu.models.demo import Demo

__dbg__ = True

class MainApp(QApplication):

    def __init__(self, *args): 
       super().__init__(*args)
       self.ctx = Context()
       self.window = MainWindow(self, args)
       self.window.show()

    def run(self):
        self.window.show()

    @staticmethod
    def open(q: QWidget):
        q.show()

    @pyqtSlot()
    def run_ops(self):
        self.window.show()
        sys.exit(self.exec())

    @pyqtSlot()
    def show_prefs(self):
        prefs = Prefs(parent=self)
        prefs.show()

    @pyqtSlot()
    def show_prog(self):
        prog = Progress(parent=self)
    # @pyqtSlot(QApplication, name="mainApp")
    # def main_app(self):
        

    
if __name__ == "__main__":
    MainApp(sys.argv)

    