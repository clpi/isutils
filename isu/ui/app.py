from window import MainWindow
import sys, os
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtGui import QAction, QGuiApplication, QActionEvent, QEnterEvent, QColor, QPen, QFont
from PySide6.QtWidgets import QApplication, QWidget, QComboBox
from PySide6.QtCore import (
    Qt, QSaveFile, QRunnable, QUuid, QtMsgType, QAbstractItemModel, QAbstractEventDispatcher, QAbstractListModel, QBuffer, QCoreApplication,
    QDirIterator, QDir, QEnum, QEvent, QEventLoop, QChildEvent,
    Signal, QPoint, QFile, QFileInfo, QFileSelector, Slot
)

class MainApp(QApplication):

   def __init__(self, *args): 
       super().__init__(*args)
       window = MainWindow(args)
       sys.exit(self.exec())

if __name__ == "__main__":
    MainApp(sys.argv)

    