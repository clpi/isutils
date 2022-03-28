import os, sys
from pathlib import WindowsPath, Path
from isu.ui import UiLoad
from typing import Optional, Any
from PIL import Image
from PySide6.QtCore import (
    QFile, QMetaObject, QObject, QPoint, QRect,  QDir,
    QSize, QTime, QUrl, Qt, QCoreApplication
)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform
)
from PySide6.QtWidgets import (
    QApplication, QSizePolicy, QWidget, QLabel, QFormLayout, QHBoxLayout,
    QVBoxLayout, QLineEdit, QLayout, QPushButton, QCheckBox, QComboBox, 
    QSpinBox, QStackedLayout, QStackedWidget, QFileDialog
    )
from isu.operation import Audio
from isu.ui.ops.ops import OpUi
from isu.ui import UiLoad

class AudioOp(OpUi, QWidget):
    uifile = QDir(os.path.dirname(os.path.realpath(__file__)))

    def __init__(self, parent: QWidget | None) -> None:
        QWidget.__init__(self, parent)
        UiLoad().loadUi("audio.ui", self, parent)
        self.load_ui()
        self.load_widgets()

    def op(self) -> Audio:
        return Audio()

    def load_ui(self):
        pass

    def load_widgets(self):
        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        pass

    @staticmethod
    def cbidx() -> int:
        return 3

