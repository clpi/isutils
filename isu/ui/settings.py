from pathlib import Path, PurePath, PureWindowsPath
import sys, os
import ffmpeg as ff
import moviepy.editor as mp
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QWidget, QMainWindow, QPushButton, QApplication, QCheckBox, QLabel, QLayout,
    QLineEdit, QSpinBox, QSplashScreen, QProgressBar, QMessageBox, QFileDialog,
    QHBoxLayout, QHeaderView, QVBoxLayout, QTableWidget, QTableView, QListView, QListWidget,
    QComboBox,
)
from PyQt6.QtGui import (
    QAction, QColor, QCloseEvent, QCursor, QDropEvent, QGuiApplication, QIcon,
    QPen, QColorConstants, QPainter
)
from PyQt6.QtCore import (
    QBuffer, QXmlStreamAttributes, QItemSelection, QXmlStreamReader, QXmlStreamWriter,
    QTimer, QUrl, QFile, QDir, 
    # pyqtSignal, pyqtPickleProtocol, pyqtSlot, QUrl, Qt, QObject
)
from PyQt6.QtQuick import QQuickView, QQuickPaintedItem

class Settings(QWidget):

    def __init__(self) -> None:
        super().__init__()
        uic.load_ui("settings.ui", self)
        self.setWindowTitle("Settings - isutils")
        self.setGeometry(500, 500, 500, 500)
        self.setFixedHeight(500)
        self.initUi()
        self.show()

    def initUi(self) -> None:
        hbox = QHBoxLayout()
        hbox.addChildLayout(self.initLeftUi())
        hbox.addChildLayout(self.initRightUi())
        self.setLayout(hbox)

    def initLeftUi(self) -> QVBoxLayout:
        vbox = QVBoxLayout()

        self.btn = QPushButton("Button", self)
        self.btn.setIcon(QIcon("football.png"))
        self.btn.move(100, 100)

        self.lab = QLabel("label", self)
        self.lab.move(100,220)

        self.btn.clicked.connect(self.clickedBtn)

        vbox.addWidget(self.btn)
        vbox.addWidget(self.lab)
        return vbox
        
    def initRightUi(self) -> QVBoxLayout:
        vbox = QVBoxLayout()

        self.cb = QComboBox(self)
        self.cb.addItems(["mp4", "avi", "mkv"])

        vbox.addWidget(self.cb)
        return vbox

    def clickedBtn(self):
        self.lab.setText("Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sett = Settings()
    sys.exit(app.exec())