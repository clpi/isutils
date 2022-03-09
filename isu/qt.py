from PyQt6 import sip
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
# from PyQt6.QtGui import *
from isu.app import MainApp, MainWindow

def findQapp() -> QCoreApplication | MainApp:
    app: QCoreApplication = QApplication.instance()
    return app

