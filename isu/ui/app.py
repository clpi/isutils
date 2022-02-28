from isu.ui.window import MainWindow
import sys, os
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtGui import QAction, QGuiApplication, QActionEvent, QEnterEvent, QColor, QPen, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox
from PyQt6.QtCore import (
    Qt, QSaveFile, QRunnable, QUuid, QtMsgType, QAbstractItemModel, QAbstractEventDispatcher, QAbstractListModel, QBuffer, QCoreApplication,
    QDirIterator, QDir,  QEvent, QEventLoop, QChildEvent,
    pyqtSignal, QPoint, QFile, QFileInfo, QFileSelector, pyqtSlot
)

class MainApp(QApplication):

    def __init__(self, *args): 
       super().__init__(*args)
       self.window = MainWindow(self, args)

    def open(q: QWidget):
        q.show()

    def run(self):
        self.window.show()
        sys.exit(self.exec())

if __name__ == "__main__":
    MainApp(sys.argv)

    